from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Formulario, Projetos, ProjetosTags, ProjetosFuncionalidades
from . formulario import FormularioCadastro
# Create your views here.
def index(request):
    queryset_projetos = Projetos.objects.all()
    projetos_detalhados = []
    if queryset_projetos.exists():
        for projeto in queryset_projetos:
            tags = ProjetosTags.objects.filter(projeto=projeto)
            funcionalidades = ProjetosFuncionalidades.objects.filter(projeto=projeto)
            projetos_detalhados.append(
                {'projeto': projeto, 'projetos_tags': tags, 'projetos_funcionalidades': funcionalidades})

            context = {
                'projetos_detalhados': projetos_detalhados
            }
    else:
        context = {}
    if request.method == "GET":
        return render(request, 'portifolio/index.html', context)
    if request.method == "POST":
        formulario = FormularioCadastro(request.POST)
        if formulario.is_valid():
            formulario.save()
            sucesso = "Seus dados foram enviados com sucesso."
            return render(request, 'portifolio/index.html', {'sucesso': sucesso})
        else:
            erro = "Não foi possivel enviar o formulario, Retorne e reenvie por favor."
        return render(request, 'portifolio/index.html', {'erro': erro})
    else:
        return render(request, 'portifolio/index.html', context)







