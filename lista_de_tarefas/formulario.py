from django import forms
from .models import Tarefa

class FormularioTarefas(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao']


