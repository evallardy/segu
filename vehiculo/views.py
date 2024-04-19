from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Vehiculo
from .forms import VehiculoForm, VehiculoConsultaForm

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'

    def get_queryset(self):
        # Aquí defines tu lógica de filtrado específica
        queryset = Vehiculo.objects.exclude(estatus=0)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos_active'] = True
        return context

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')
    def form_valid(self, form):

        # Guarda el objeto Vehículo
        self.object = form.save()

        # Obtiene el ID del empleado recién creado
        vehiculo_id = self.object.pk

        # Redirige al usuario a la vista de modificación del vehiculo
        return redirect('vehiculo_update', pk=vehiculo_id)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos_active'] = True
        return context

class VehiculoDetailView(DetailView):
    model = Vehiculo
    form_class = VehiculoConsultaForm
    template_name = 'vehiculo/vehiculo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Itera sobre los campos del formulario para agregar la clase 'form-control'
        for field_name, field_value in context['object'].__dict__.items():
            if hasattr(field_value, 'field') and hasattr(field_value.field.widget, 'attrs'):
                field_value.field.widget.attrs['class'] = 'form-control'
        context['vehiculos_active'] = True
        return context

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha_alta'].initial = self.object.fecha_alta
        form.fields['fecha_baja'].initial = self.object.fecha_baja
        return form    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos_active'] = True
        return context

class VehiculoBajaView(View):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')

    def get(self, request, *args, **kwargs):
        # Obtener el ID del vehículo de los kwargs
        vehiculo_id = kwargs.get('pk')
        
        # Buscar el vehículo en la base de datos
        try:
            vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
        except Vehiculo.DoesNotExist:
            return HttpResponse("El vehículo no existe", status=404)
        
        # Aquí puedes realizar cualquier otra lógica necesaria antes de renderizar el template
        
        # Definir el contexto con el vehículo
        context = {'object': vehiculo, 'vehiculos_active': True}

        # Renderizar el template con el contexto y devolver la respuesta
        return render(request, 'vehiculo/vehiculo_confirm_delete.html', context)

    def post(self, request, pk):
        # Obtener el objeto Vehiculo
        vehiculo = Vehiculo.objects.get(pk=pk)

        # Cambiar el estado a 0 en lugar de eliminar
        vehiculo.estatus = 0
        vehiculo.save()

        # Redireccionar a la lista de vehículos
        return redirect('vehiculo_list')