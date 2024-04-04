from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class ArmaDeleteView(DeleteView):
    model = Armamento
    template_name = 'armamento/arma_confirm_delete.html'
    success_url = reverse_lazy('arma_list')

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar
        self.object.estatus = 0
        self.object.save()
        return super().delete(request, *args, **kwargs)