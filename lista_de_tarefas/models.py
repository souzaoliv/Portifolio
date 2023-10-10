from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome