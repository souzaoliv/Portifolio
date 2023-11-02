from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Formulario(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    mensagem = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.nome



class Projetos(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=1000, blank=False)
    imagem = models.FileField(upload_to='portifolio/projetos', validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg'])])
    link = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome
class Tags(models.Model):
    tag = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.tag

class Funcionalidades(models.Model):
    funcionalidade = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=1000, blank=False)
    def __str__(self):
        return self.funcionalidade

class ProjetosTags(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.tag


class ProjetosFuncionalidades(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    funcionalidade = models.ForeignKey(Funcionalidades, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionalidade.funcionalidade




