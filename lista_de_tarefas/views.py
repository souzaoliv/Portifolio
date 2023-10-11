from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Tarefa

# Create your views here.
def index(request):
    return render(request, 'lista_de_tarefas/index.html')


@require_http_methods(["POST", "GET"])
def cadastrar(request):
    if request.method == "GET":
        return render(request, 'lista_de_tarefas/cadastrar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # se usuario ja existe sera redirecionado para a pagina de login
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Usuário "{username}" já existe. Faca login!')
            return redirect('logar')
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('exibir_tarefas')
            except ValueError as e:
                print(e)
                messages.error(request, f'Erro ao criar usuário "{username}" . Tente novamente!')
                return render(request,'lista_de_tarefas/cadastrar.html')

@require_http_methods(["POST", "GET"])
def logar(request):
    if request.method == "GET":
        return render(request, 'lista_de_tarefas/logar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # se usuario nao existe sera redirecionado para a pagina de cadastro
        if user is None:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Senha incorreta para o usuário "{username}" . Tente novamente!')
                return render(request,'lista_de_tarefas/logar.html')
            else:
                messages.error(request, f'Usuário "{username}" não existe. Faça o cadastro!')
                return redirect('cadastrar')
        else:
            try:
                login(request, user)
                return redirect('exibir_tarefas')
            except ValueError as e:
                print(e)
                messages.error(request, f'Erro ao logar usuário "{username}" . Tente novamente!')
                return render(request, 'lista_de_tarefas/logar.html')

def deslogar(request):
    ...

def exibir_tarefas(request):
    ...

def criar_tarefa(request):
    ...
def editar_tarefa(request, pk):
    ...
def excluir_tarefa(request, pk):
    ...



