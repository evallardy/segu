from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, CreateView, UpdateView, FormView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import json

from .forms import EmpleadoForm, Escolaridadform
from .models import *
from core.contantes import ESTADOS

class ListarEmpleadosView(ListView):
    model = Empleado
    template_name = 'rh/listar_empleados.html'
    context_object_name = 'empleados'

class CrearEmpleadoView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'rh/empleados_form.html'
    success_url = reverse_lazy('listar_empleados')
    def form_valid(self, form):

        # Guarda el objeto Empleado
        self.object = form.save()

        # Obtiene el ID del empleado recién creado
        empleado_id = self.object.pk

        # Redirige al usuario a la vista de modificación del empleado
        return redirect('modificar_empleado', pk=empleado_id)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forma'] = 'Alta de empleado'
        return context

class ModificarEmpleadoView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'rh/empleados_form.html'
    success_url = reverse_lazy('listar_empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forma'] = 'Edita empleado'
        pk = self.kwargs.get('pk',0)
        context['pk'] = pk
        return context

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

class Domicilio_empleado(TemplateView):
    template_name = 'rh/domicilio_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.domicilio:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'estados': ESTADOS})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'estados': ESTADOS})    
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

        empleado_direccion = Generales.objects.filter(empleado=pk).first()

        if empleado_direccion:
            Generales.objects.filter(empleado=pk).update(domicilio=direccion)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = direccion
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Beneficiario_empleado(TemplateView):
    template_name = 'rh/beneficiario_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.beneficiario:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        beneficiarios = []

        # Obtener los datos de los beneficiarios enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            nombre = dato['nombre']
            curp = dato['curp']
            parentezco = dato['parentezco']
            porcentaje = dato['porcentaje']

            # Agregar los datos del beneficiario a la lista
            beneficiario = {
                'nombre': nombre,
                'curp': curp, 
                'parentezco': parentezco,
                'porcentaje': porcentaje,
            }
            beneficiarios.append(beneficiario)
        # Convertir la lista de beneficiarios a JSON
        beneficiarios_json = beneficiarios

        empleado_beneficiario = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_beneficiario:
            Generales.objects.filter(empleado=pk).update(beneficiario=beneficiarios_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.beneficiario = beneficiarios_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Escolaridad_empleado(TemplateView):
    template_name = 'rh/escolaridad_empleado.html'
    form_class = Escolaridadform

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.escolaridad:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 
                    'escolaridad': ESCOLARIDAD, 'si_no': SI_NO})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'escolaridad': ESCOLARIDAD,
                     'si_no': SI_NO})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'escolaridad': ESCOLARIDAD,
                 'si_no': SI_NO})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        escuelas = []

        # Obtener los datos de las escuelas enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            tipo = dato['tipo']
            nombre = dato['nombre']
            fecha_inicial = dato['fecha_inicial']
            fecha_final = dato['fecha_final']
            terminada = dato['terminada']

            # Agregar los datos de la escuela a la lista
            escuela = {
                'tipo': tipo, 
                'nombre': nombre,
                'fecha_inicial': fecha_inicial, 
                'fecha_final': fecha_final,
                'terminada': terminada,
            }
            escuelas.append(escuela)
        # Convertir la lista de escuelas a JSON
        escuelas_json = escuelas

        empleado_escuela = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_escuela:
            Generales.objects.filter(empleado=pk).update(escolaridad=escuelas_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.escolaridad = escuelas_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Experiencia_empleado(TemplateView):
    template_name = 'rh/experiencia_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.experiencia:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        trabajos = []

        # Obtener los datos de los trabajos enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            empresa = dato['empresa']
            puesto = dato['puesto']
            actividades = dato['actividades']
            fecha_inicial = dato['fecha_inicial']
            fecha_final = dato['fecha_final']

            # Agregar los datos del trabajo a la lista
            trabajo = {
                'empresa': empresa, 
                'puesto': puesto,
                'actividades': actividades,
                'fecha_inicial': fecha_inicial, 
                'fecha_final': fecha_final,
            }
            trabajos.append(trabajo)
        # Convertir la lista de trabajos a JSON
        trabajos_json = trabajos

        empleado_trabajos = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_trabajos:
            Generales.objects.filter(empleado=pk).update(experiencia=trabajos_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.experiencia = trabajos_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Familia_empleado(TemplateView):
    template_name = 'rh/familia_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.familia:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR, 'si_no': SI_NO})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR, 'si_no': SI_NO})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'familiar': FAMILIAR, 'si_no': SI_NO})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        familiares = []

        # Obtener los datos de los familiares enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            parentezco = dato['parentezco']
            nombre = dato['nombre']
            edad = dato['edad']
            vive = dato['vive']

            # Agregar los datos del familiar a la lista
            familiar = {
                'parentezco': parentezco,
                'nombre': nombre,
                'edad': edad,
                'vive': vive,
            }
            familiares.append(familiar)
        # Convertir la lista de familiares a JSON
        familiares_json = familiares

        empleado_familiar = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_familiar:
            Generales.objects.filter(empleado=pk).update(familia=familiares_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.familia = familiares_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Idioma_empleado(TemplateView):
    template_name = 'rh/idioma_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.idioma:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'idioma': IDIOMA})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'idioma': IDIOMA})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'idioma': IDIOMA})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        idiomas = []

        # Obtener los datos de los idiomas enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            idioma = dato['idioma']
            leido = dato['leido']
            hablado = dato['hablado']

            # Agregar los datos del idiomas a la lista
            idioma = {
                'idioma': idioma,
                'leido': leido,
                'hablado': hablado, 
            }
            idiomas.append(idioma)
        # Convertir la lista de idiomas a JSON
        idiomas_json = idiomas

        empleado_idioma = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_idioma:
            Generales.objects.filter(empleado=pk).update(idioma=idiomas_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.idioma = idiomas_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))

class Referencia_empleado(TemplateView):
    template_name = 'rh/referencia_empleado.html'

    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET
        pk = self.kwargs.get('pk', 0)
        datos = Generales.objects.filter(empleado=pk).first()
        empleado = Empleado.objects.filter(pk=pk).first()
        nombre = empleado.paterno + ' ' + empleado.materno + ', ' + empleado.nombre
        if datos:
            if datos.referencia:
                return render(request, self.template_name, {'datos': datos, 'pk': pk, 'nombre': nombre, 'tipo_referencia': TIPO_REFERENCIA})
            else:
                return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'tipo_referencia': TIPO_REFERENCIA})    
        else:
            return render(request, self.template_name, {'pk': pk, 'nombre': nombre, 'tipo_referencia': TIPO_REFERENCIA})

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        pk = self.kwargs.get('pk', 0)

        # Crear un diccionario para almacenar los datos de dirección
        referencias = []

        # Obtener los datos de las referencias enviados desde el formulario
        datosTabla = json.loads(self.request.POST.get('datosTabla'))
        for dato in datosTabla:
            tipo = dato['tipo']
            nombre = dato['nombre']
            fecha = dato['fecha']

            # Agregar los datos de la referencia a la lista
            referencia = {
                'tipo': tipo,
                'nombre': nombre, 
                'fecha': fecha,
            }
            referencias.append(referencia)
        # Convertir la lista de referencias a JSON
        referencias_json = referencias

        empleado_referencia = Generales.objects.filter(empleado=pk).first()

        # Guardar los datos en el modelo Generales
        if empleado_referencia:
            Generales.objects.filter(empleado=pk).update(referencia=referencias_json)
        else:
            # Obtener o crear el objeto Generales asociado al Empleado
            generales = Generales()
            generales.empleado_id = pk
            generales.domicilio = {"calle": "S/N"}
            generales.referencia = referencias_json
            generales.save()

        # Realiza la lógica para procesar los datos POST según sea necesario

        # Después de procesar los datos, puedes redirigir a la misma vista u otra página
        return HttpResponseRedirect(reverse_lazy('modificar_empleado', kwargs={'pk': pk}))        