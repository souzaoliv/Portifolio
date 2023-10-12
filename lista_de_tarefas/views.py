from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods

from django.contrib import messages

from .models import Tarefa
from .formulario import FormularioTarefas
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
                return render(request, 'lista_de_tarefas/cadastrar.html')

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

@require_http_methods(["GET"])
def deslogar(request):
    try:
        logout(request)
        return redirect('index_lista_de_tarefas')
    except ValueError as e:
        print(e)
        messages.error(request, f'Erro ao deslogar usuário. Tente novamente!')
        return redirect('exibir_tarefas')

@require_http_methods(["GET"])
def exibir_tarefas(request):
    if request.user.is_authenticated:
        tarefas = Tarefa.objects.filter(usuario=request.user)
        username = request.user.username
        context = {
            'tarefas': tarefas,
            'username': username,
        }
        return render(request, 'lista_de_tarefas/exibir_tarefas.html', context=context)
    else:
        messages.error(request, f'Usuário não logado. Faça o login!')
        return redirect('logar')

@require_http_methods(["POST", "GET"])
def criar_tarefa(request):
    if request.user.is_authenticated:

        username = request.user.username
        context = {"username": username,}

        if request.method == "GET":
            return render(request, 'lista_de_tarefas/criar_tarefa.html', context)

        else:
            formulario = FormularioTarefas(request.POST)
            if formulario.is_valid():
                try:
                    tarefa = formulario.save(commit=False)
                    tarefa.usuario = request.user  # Associe a tarefa ao usuário logado
                    tarefa.save()
                    return redirect("exibir_tarefas")
                except ValueError as e:
                    print(e)
                    messages.error(request, f'Erro ao salvar tarefa. Tente novamente!')
                    return render(request, 'lista_de_tarefas/criar_tarefa.html', context)
            else:
                messages.error(request, f'Erro ao validar tarefa. Tente novamente!')
                return render(request, 'lista_de_tarefas/criar_tarefa.html', context)


@require_http_methods(["GET", "POST", "PATCH"])
def editar_tarefa(request, pk):
    if request.user.is_authenticated:
        tarefa = Tarefa.objects.get(pk=pk, usuario=request.user)
        form = FormularioTarefas(request.POST or None, instance=tarefa)
        username = request.user.username
        if request.method == "POST" or request.method == "PATCH":
            if form.is_valid():
                try:
                    form.save()
                    return redirect("exibir_tarefas")
                except ValueError as e:
                    print(e)
                    messages.error(request, f'Erro ao salvar tarefa. Tente novamente!')
                    return render(request, 'lista_de_tarefas/editar_tarefa.html', {'form': form, 'username': username})
            else:
                messages.error(request, f'Erro ao validar tarefa. Tente novamente!')
                return render(request, 'lista_de_tarefas/editar_tarefa.html', {'form': form, 'username': username})
        else:
            return render(request, 'lista_de_tarefas/editar_tarefa.html', {'form': form, 'username': username})

    else:
        redirect('logar')

@require_http_methods(["POST", "GET", "DELETE"])
def excluir_tarefa(request, pk):
    if request.user.is_authenticated:
        tarefa = Tarefa.objects.get(pk=pk, usuario=request.user)
        form = FormularioTarefas(request.POST or None, instance=tarefa)
        username = request.user.username
        if request.method == "POST" or request.method == "DELETE":
            try:
                tarefa.delete()
                return redirect("exibir_tarefas")
            except ValueError as e:
                print(e)
                messages.error(request, f'Erro ao excluir tarefa. Tente novamente!')
                return render(request, 'lista_de_tarefas/excluir_tarefa.html', {'form': form, 'username': username})
        else:
            return render(request, 'lista_de_tarefas/excluir_tarefa.html', {'form': form, 'username': username})

    else:
        redirect('logar')





