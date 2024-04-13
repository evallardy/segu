from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils import timezone

from .models import Cliente
from .forms import ClienteForm
from core.contantes import ESTADOS

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

    def get_queryset(self):
        # Aquí defines tu lógica de filtrado específica
        queryset = Cliente.objects.all()
        return queryset

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/cliente_detail.html'

    def get(self, request, *args, **kwargs):
        cliente = self.get_object()

        # Crear el formulario con la instancia del cliente
        form = ClienteForm(instance=cliente)

        # Iterar sobre los campos del formulario y establecerlos como de solo lectura
        for field_name, field in form.fields.items():
            field.widget.attrs['readonly'] = True

        context = {'form': form, 'object': cliente}
        return render(request, self.template_name, context)

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    def form_valid(self, form):

        # Guarda el objeto cliente
        self.object = form.save()

        # Obtiene el ID del cliente recién creado
        cliente_id = self.object.pk

        # Redirige al usuario a la vista de modificación del cliente
        return redirect('cliente_update', pk=cliente_id)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ventana'] = 'Crea'
        return context


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha_alta'].initial = self.object.fecha_alta
        form.fields['fecha_baja'].initial = self.object.fecha_baja
        return form 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.get_object()
        context['ventana'] = 'Edita'
        context['estatus_actual'] = cliente.estatus
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        # Excluir el campo direccion del formulario
        form = self.get_form(self.form_class)
        form.fields.pop('domicilio', None)

        if form.is_valid():
            # Obtener el estado actual y el nuevo estado del cliente
            estado_actual = request.POST['estatus_actual']
            nuevo_estado = form.cleaned_data['estatus']

            # Si el estado ha cambiado y el nuevo estado es 0 (baja)
            if estado_actual != nuevo_estado:
                if nuevo_estado == 0:
                    # Asignar la fecha actual al campo fecha_baja
                    self.object.fecha_baja = timezone.now().date()
                else:
                    # Eliminar la fecha de baja si el nuevo estado es 1 (activo)
                    self.object.fecha_baja = None

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

    def get(self, request, *args, **kwargs):
        cliente = self.get_object()

        # Crear el formulario con la instancia del cliente
        form = ClienteForm(instance=cliente)

        # Iterar sobre los campos del formulario y establecerlos como de solo lectura
        for field_name, field in form.fields.items():
            field.widget.attrs['readonly'] = True

        context = {'form': form, 'object': cliente}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # Obtener el objeto cliente
        cliente = Cliente.objects.get(pk=pk)

        # Asignar la fecha del día al campo fecha_baja
        cliente.fecha_baja = timezone.now().date()

        # Cambiar el estado a 0 en lugar de eliminar
        cliente.estatus = 0
        cliente.save()

        # Redireccionar a la lista de cliente
        return redirect('cliente_list')

class Domicilio_cliente(TemplateView):
    template_name = 'cliente/domicilio_cliente.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        cliente = Cliente.objects.filter(id=pk).first()
        if cliente.fisica_moral == 0:
            nombre = cliente.paterno + ' ' + cliente.materno + ', ' + cliente.nombre
        else:
            nombre = cliente.razon
        datos = cliente.domicilio
        if datos:
            return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'estados': ESTADOS})
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'estados': ESTADOS})    

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)
        # Crear un diccionario para almacenar los datos de dirección
        direccion = {}

        # Extraer los valores de los campos de formulario y guardarlos en el diccionario
        direccion['calle'] = request.POST.get('calle')
        direccion['colonia'] = request.POST.get('colonia')
        direccion['codigo_postal'] = request.POST.get('codigo_postal')
        direccion['municipio'] = request.POST.get('municipio')
        direccion['estado'] = int(request.POST.get('estado'))

        Cliente.objects.filter(id=pk).update(domicilio=direccion)

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('cliente_update', kwargs={'pk': pk}))        