from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Armamento

class DateInput(forms.DateInput):
    input_type = 'date'

class ArmaForm(forms.ModelForm):
    class Meta:
        model = Armamento
        fields = '__all__'
        widgets = {
            'fecha_alta': DateInput(),
            'fecha_baja': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        tipo_arma = cleaned_data.get('marca')
        otro_tipo_arma = cleaned_data.get('otro_tipo_arma')

        if tipo_arma == 99 and otro_tipo_arma is None:
            self.add_error('otro_tipo_arma', 'Especifica otro tipo')

        marca = cleaned_data.get('marca')
        otra_marca = cleaned_data.get('otra_marca')

        if marca == 99 and otra_marca is None:
            self.add_error('otra_marca', 'Especifica otra marca')

        calibre = cleaned_data.get('calibre')
        otro_calibre = cleaned_data.get('otro_calibre')

        if calibre == 99 and otro_calibre is None:
            self.add_error('otro_calibre', 'Especifica otro calibre')