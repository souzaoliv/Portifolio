from django import forms

from portifolio.models import Formulario

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ('nome', 'email', 'mensagem')