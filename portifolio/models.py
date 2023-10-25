from django.db import models

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
    imagem = models.ImageField(upload_to='portifolio/projetos', blank=False)

    def __str__(self):
        return self.nome

class ProjetosTags(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.tag

class ProjetosFuncionalidades(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    funcionalidade = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=1000, blank=False)
    def __str__(self):
        return self.funcionalidade


