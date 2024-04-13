from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import json

from .models import Asignacion
from .forms import AsignacionForm
from vehiculo.models import Vehiculo
from rh.models import Empleado

class AsigancionListView(ListView):
    model = Asignacion
    template_name = 'asignacion/asignacion_list.html'

    def get_queryset(self):
        # Aquí defines tu lógica de filtrado específica
        queryset = Asignacion.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos_libres'] = Vehiculo.objects.filter(estatus=2)
        context['empleados_libres'] = Empleado.objects.filter(estatus=2)
        return context

class AsignacionCreateView(CreateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'asignacion/asignacion_form.html'
    success_url = reverse_lazy('asignacion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forma'] = 'Crea'
        context['empleadosSinAsignacion'] = Empleado.objects.filter(estatus=2)
        context['vehiculosSinAsignacion'] = Vehiculo.objects.filter(estatus=2)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)

        # Recuperar los datos del POST
        cliente_id = request.POST.get('cliente')
        servicio = request.POST.get('servicio')
        otro_servicio = request.POST.get('otro_servicio')
        detalle = request.POST.get('detalle')
        cobro = request.POST.get('cobro')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_termina = request.POST.get('fecha_termina')
        estatus = request.POST.get('estatus')
        empleados_asignados_json = request.POST.get('empleados_asignados')
        vehiculos_asignados_json = request.POST.get('vehiculos_asignados')

        # Convertir los datos JSON a objetos Python
        empleados_asignados = json.loads(empleados_asignados_json)
        vehiculos_asignados = json.loads(vehiculos_asignados_json)

        # Crear una nueva instancia de Asignacion
        if fecha_termina:
            asignacion = Asignacion(
                cliente_id=cliente_id,
                servicio=servicio,
                otro_servicio=otro_servicio,
                detalle=detalle,
                cobro=cobro,
                fecha_inicial=fecha_inicial,
                fecha_termina=fecha_termina,
                estatus=estatus
            )
        else:
            asignacion = Asignacion(
                cliente_id=cliente_id,
                servicio=servicio,
                otro_servicio=otro_servicio,
                detalle=detalle,
                cobro=cobro,
                fecha_inicial=fecha_inicial,
                estatus=estatus
            )
            
        # Guardar la nueva asignación en la base de datos
        asignacion.save()

        # Asignar empleados y vehículos a la asignación
        asignacion.empleados.set([empleado['id'] for empleado in empleados_asignados])
        asignacion.vehiculos.set([vehiculo['id'] for vehiculo in vehiculos_asignados])

        # Actualizar el estado de los empleados asociados
        empleados_a_actualizar = Empleado.objects.filter(id__in=[empleado['id'] for empleado in empleados_asignados], estatus=2)
        empleados_a_actualizar.update(estatus=0)

         # Actualizar el estado de los vehículos asociados
        vehiculos_a_actualizar = Vehiculo.objects.filter(id__in=[vehiculo['id'] for vehiculo in vehiculos_asignados], estatus=2)
        vehiculos_a_actualizar.update(estatus=0)

        return HttpResponseRedirect(reverse_lazy('asignacion_update', kwargs={'pk': asignacion.id}))


def asignar_empleado(request):
    if request.method == 'POST' and request.is_ajax():
        empleado_id = request.POST.get('empleado_id')
        asignacion_id = request.POST.get('asignacion_id')  # Si tienes un ID de asignación, obténlo de alguna manera
        try:
            asignacion = Asignacion.objects.get(pk=asignacion_id)
            asignacion.empleados.add(empleado_id)
            asignacion.save()
            return JsonResponse({'success': True})
        except Asignacion.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'La asignación no existe'})
    return JsonResponse({'success': False, 'error': 'Método no permitido o no es una solicitud AJAX'})
    
class AsignacionUpdateView(UpdateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'asignacion/asignacion_form.html'
    success_url = reverse_lazy('asignacion_list')

    def get_object(self, queryset=None):
        # Recuperar la instancia de Asignacion que se está actualizando
        return get_object_or_404(Asignacion, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forma'] = 'actualiza'
        context['empleadosSinAsignacion'] = Empleado.objects.filter(estatus=2)
        context['vehiculosSinAsignacion'] = Vehiculo.objects.filter(estatus=2)
        return context

    def post(self, request, *args, **kwargs):
        # Obtener el ID de la asignación desde el POST
        id_asignacion = self.kwargs['pk']  # Suponiendo que estás usando Django

        # Obtener la asignación correspondiente
        asignacion = Asignacion.objects.get(pk=id_asignacion)

        # Obtener los empleados asociados a esa asignación
        empleados_asignados = asignacion.empleados.all()

        # Iterar sobre los empleados asignados y actualizar su estatus
        for empleado_act in empleados_asignados:
            empleado_act.estatus = 2
            empleado_act.save()

        vehiculos_asignados = asignacion.vehiculos.all()

        # Iterar sobre los empleados asignados y actualizar su estatus
        for vehiculo_act in vehiculos_asignados:
            vehiculo_act.estatus = 2
            vehiculo_act.save()

        # Recuperar los datos del POST
        cliente_id = request.POST.get('cliente')
        servicio = request.POST.get('servicio')
        otro_servicio = request.POST.get('otro_servicio')
        detalle = request.POST.get('detalle')
        cobro = request.POST.get('cobro')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_termina = request.POST.get('fecha_termina')
        estatus = request.POST.get('estatus')
        empleados_asignados_json = request.POST.get('empleados_asignados')
        vehiculos_asignados_json = request.POST.get('vehiculos_asignados')

        # Convertir los datos JSON a objetos Python
        empleados_asignados = json.loads(empleados_asignados_json)
        vehiculos_asignados = json.loads(vehiculos_asignados_json)

        # Crear una nueva instancia de Asignacion
        if fecha_termina:
            Asignacion.objects.filter(id=id_asignacion).update(
                cliente_id=cliente_id,
                servicio=servicio,
                otro_servicio=otro_servicio,
                detalle=detalle,
                cobro=cobro,
                fecha_inicial=fecha_inicial,
                fecha_termina=fecha_termina,
                estatus=estatus
            )
        else:
            Asignacion.objects.filter(id=id_asignacion).update(
                cliente_id=cliente_id,
                servicio=servicio,
                otro_servicio=otro_servicio,
                detalle=detalle,
                cobro=cobro,
                fecha_inicial=fecha_inicial,
                estatus=estatus
            )
            
        # Guardar la nueva asignación en la base de datos
#        asignacion.save()

        # Asignar empleados y vehículos a la asignación
        asignacion.empleados.set([empleado['id'] for empleado in empleados_asignados])
        asignacion.vehiculos.set([vehiculo['id'] for vehiculo in vehiculos_asignados])


        # Actualizar el estado de los empleados asociados
        empleados_a_actualizar = Empleado.objects.filter(id__in=[empleado['id'] for empleado in empleados_asignados], estatus=2)
        empleados_a_actualizar.update(estatus=0)

         # Actualizar el estado de los vehículos asociados
        vehiculos_a_actualizar = Vehiculo.objects.filter(id__in=[vehiculo['id'] for vehiculo in vehiculos_asignados], estatus=2)
        vehiculos_a_actualizar.update(estatus=0)

        return HttpResponseRedirect(reverse_lazy('asignacion_update', kwargs={'pk': asignacion.id}))        

class AsignacionDeleteView(DeleteView):
    model = Asignacion
    template_name = 'asignacion/asignacion_confirm_delete.html'
    success_url = reverse_lazy('asignacion_list')