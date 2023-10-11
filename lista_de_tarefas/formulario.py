from django import forms
from .models import Tarefa

class FormularioTarefas(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao']
        labels = {'nome': 'Nome da tarefa', 'descricao': 'Descrição da tarefa'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
