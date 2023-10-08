from django.shortcuts import render, redirect
from django.http import HttpResponse

from . formulario import FormularioCadastro
# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'portifolio/index.html')
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
        return render(request, 'portifolio/index.html')







