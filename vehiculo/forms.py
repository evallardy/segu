from bootstrap_datepicker_plus import DatePickerInput
from django import forms
import datetime

from .models import Vehiculo

class DateInput(forms.DateInput):
    input_type = 'date'

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'fecha_alta': DateInput(),
            'fecha_baja': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    def clean_anio(self):
        # Obtiene el valor del campo 'anio'
        anio = self.cleaned_data.get('anio')

        # Obtiene el año actual
        anio_actual = datetime.datetime.now().year

        # Verifica si el año está en el rango deseado
        anio_menos = anio_actual - 20
        anio_mas = anio_actual + 1

        if anio < anio_menos or anio > anio_mas:
            raise forms.ValidationError("Debe ser entre " + str(anio_menos) + " y " + str(anio_mas) )

        return anio

    def clean(self):
        cleaned_data = super().clean()
        marca = cleaned_data.get('marca')
        otra_marca = cleaned_data.get('otra_marca')

        if marca == 99 and otra_marca is None:
            self.add_error('otra_marca', 'Especifica otra marca')

        tipo_vehiculo = cleaned_data.get('tipo_vehiculo')
        otro_tipo_vehiculo = cleaned_data.get('otro_tipo_vehiculo')

        if tipo_vehiculo == 99 and otro_tipo_vehiculo is None:
            self.add_error('otro_tipo_vehiculo', 'Especifica otro tipo')

        tipo_combustible = cleaned_data.get('tipo_combustible')
        otro_tipo_combustible = cleaned_data.get('otro_tipo_combustible')

        if tipo_combustible == 99 and otro_tipo_combustible is None:
            self.add_error('otro_tipo_combustible', 'Especifica otro tipo')

        return cleaned_data
