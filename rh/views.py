from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm
from .models import Empleado

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'rh/listar_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'rh/empleados_form.html', {'form': form})

def modificar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'rh/empleados_form.html', {'form': form})

def confirmar_eliminar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'rh/confirmar_eliminar.html', {'empleado': empleado})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if empleado:
        empleado.delete()
        return redirect('listar_empleados')
    return redirect('confirmar_eliminar', pk=pk)

def consulta_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if empleado:
        return render(request, 'rh/consulta_empleado.html', {'empleado': empleado})
    else:
        return redirect('listar_empleados')

    
