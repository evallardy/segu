from django import forms
from django.forms import NumberInput
from crispy_forms.helper import FormHelper
import datetime, re

from .models import Asignacion
from rh.models import Empleado

class DateInput(forms.DateInput):
    input_type = 'date'

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 4}),
            'fecha_inicial': DateInput(),
            'fecha_termina': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

        self.fields['ubicacion'].required = False
        self.fields['fecha_inicial'].required = False
        self.fields['empleados'].required = False
        self.fields['vehiculos'].required = False

    def clean(self):
        cleaned_data = super().clean()
        empleados = cleaned_data.get('empleados')
        
        
        cliente = cleaned_data.get('cliente')
        if not cliente:
            self.add_error('cliente', "Debe seleccionar el cliente.")

        servicio = cleaned_data.get('servicio')
        if servicio == 99:
            otro_servicio = cleaned_data.get('otro_servicio')
            if not otro_servicio:
                self.add_error('otro_servicio', "Este campo es obigatorio.")

        return cleaned_data  

   