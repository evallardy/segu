from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_alta': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#        self.fields['fecha_alta'].required = False

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        fisica_moral = cleaned_data.get('fisica_moral')
        nombre = cleaned_data.get('nombre')
        paterno = cleaned_data.get('paterno')
        razon = cleaned_data.get('razon')

        if fisica_moral == 0:  # Si el cliente es de tipo "Física"
            if not nombre:  # Si nombre no está informado
                self.add_error('nombre', "Este campo es obligatorio.")
            if not paterno:  # Si paterno no está informado
                self.add_error('paterno', "Este campo es obligatorio.")
        else:
            if not razon:  # Si paterno no está informado
                self.add_error('razon', "Este campo es obligatorio.")
        return cleaned_data            