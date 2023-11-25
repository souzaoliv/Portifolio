from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'imobiliaria/index.html')

def cadastrar(request):
    return render(request, 'imobiliaria/cadastrar.html')

def logar(request):
    return render(request, 'imobiliaria/logar.html')