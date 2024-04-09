from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Armamento
from .forms import ArmaForm

class ArmaListView(ListView):
    model = Armamento
    template_name = 'armamento/arma_list.html'

    def get_queryset(self):
        # Aquí defines tu lógica de filtrado específica
        queryset = Armamento.objects.exclude(estatus=0)
        return queryset

class ArmaCreateView(CreateView):
    model = Armamento
    form_class = ArmaForm
    template_name = 'armamento/arma_form.html'
    success_url = reverse_lazy('arma_list')
    def form_valid(self, form):

        # Guarda el objeto Vehículo
        self.object = form.save()

        # Obtiene el ID del empleado recién creado
        arma_id = self.object.pk

        # Redirige al usuario a la vista de modificación del arma
        return redirect('arma_update', pk=arma_id)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['forma'] = 'Alta de empleado'
        return context

class ArmaDetailView(DetailView):
    model = Armamento
    template_name = 'armamento/arma_detail.html'

class ArmaUpdateView(UpdateView):
    model = Armamento
    form_class = ArmaForm
    template_name = 'armamento/arma_form.html'
    success_url = reverse_lazy('arma_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha_alta'].initial = self.object.fecha_alta
        form.fields['fecha_baja'].initial = self.object.fecha_baja
        return form    

class ArmaDeleteView(View):
    model = Armamento
    template_name = 'armamento/arma_confirm_delete.html'
    success_url = reverse_lazy('arma_list')

    def get(self, request, *args, **kwargs):
        # Obtener el ID del arma de los kwargs
        arma_id = kwargs.get('pk')
        
        # Buscar el vehículo en la base de datos
        try:
            arma = Armamento.objects.get(pk=arma_id)
        except Armamento.DoesNotExist:
            return HttpResponse("El arma no existe", status=404)
        
        # Aquí puedes realizar cualquier otra lógica necesaria antes de renderizar el template
        
        # Definir el contexto con el vehículo
        context = {'object': arma}

        # Renderizar el template con el contexto y devolver la respuesta
        return render(request, 'armamento/arma_confirm_delete.html', context)

    def post(self, request, pk):
        # Obtener el objeto Vehiculo
        arma = Armamento.objects.get(pk=pk)

        # Cambiar el estado a 0 en lugar de eliminar
        arma.estatus = 0
        arma.save()

        # Redireccionar a la lista de vehículos
        return redirect('arma_list')