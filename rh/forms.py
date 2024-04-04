from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Empleado, Generales
class DateInput(forms.DateInput):
    input_type = 'date'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'  # Todos los campos del modelo Empleado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class Escolaridadform(forms.ModelForm):
    class Meta:
        model = Generales
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_final': DateInput(),
        }
