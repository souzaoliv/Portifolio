import unittest
from django.test import TestCase, Client

from .models import Tarefa
from django.contrib.auth.models import User
# Create your tests here.
class TestPaginaTemplates(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin', password='correta')
        Tarefa.objects.create(nome='nome', descricao='descricao', usuario=User.objects.get(id=1))
    def test_pagina_inicial(self):
        """ esperado renderizzar template index.html"""
        response = self.client.get('/lista_de_tarefas/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/index.html')

    def test_pagina_cadastrar(self):
        """ esperado renderizzar template cadastrar.html"""
        response = self.client.get('/lista_de_tarefas/cadastrar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/cadastrar.html')
    def test_pagina_logar(self):
        """ esperado renderizzar template logar.html"""
        response = self.client.get('/lista_de_tarefas/logar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/logar.html')

    def test_pagina_exibir_tarefas(self):
        """ esperado renderizzar template exibir_tarefas.html"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/exibir_tarefas.html')

    def test_pagina_criar_tarefa(self):
        """ esperado renderizzar template criar_tarefa.html"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/criar_tarefa/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/criar_tarefa.html')

    def test_pagina_editar_tarefa(self):
        """ esperado renderizzar template editar_tarefa.html"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/editar_tarefa/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/editar_tarefa.html')

    def test_pagina_excluir_tarefa(self):
        """ esperado renderizzar template excluir_tarefa.html"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/excluir_tarefa/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_de_tarefas/excluir_tarefa.html')


class TestFuncionalidades(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin', password='correta')
        Tarefa.objects.create(nome='nome', descricao='descricao', usuario=User.objects.get(id=1))

    def test_cadastrar_usuario(self):
        """ esperado CRIAR usuario cadastrado"""
        self.client.post('/lista_de_tarefas/cadastrar/', {'username': 'novo_usuario', 'password': 'correta'})
        self.assertTrue(User.objects.filter(username='novo_usuario').exists())
    def test_cadastrar_usuario_existente(self):
        """ esperado NEGAR cadastrar usuario existente"""
        self.client.post('/lista_de_tarefas/cadastrar/', {'username': 'admin', 'password': 'correta'})
        self.assertTrue(User.objects.filter(username='admin').count() == 1)

    def test_logar_usuario(self):
        """ esperado LOGAR usuario cadastrado"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logar_usuario_nao_existente(self):
        """ esperado NEGAR logar usuario nao cadastrado"""
        self.client.login(username='nao_cadastrado', password='NaN')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_deslogar_usuario(self):
        """ esperado DESLOGAR usuario cadastrado"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/deslogar/')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_criar_tarefa(self):
        """ esperado CRIAR tarefa"""
        self.client.login(username='admin', password='correta')
        self.client.post('/lista_de_tarefas/criar_tarefa/', {'nome': 'nome', 'descricao': 'descricao'})
        self.assertTrue(Tarefa.objects.filter(nome='nome').exists())
    def test_editar_tarefa(self):
        """ esperado EDITAR tarefa"""
        self.client.login(username='admin', password='correta')
        self.client.post('/lista_de_tarefas/editar_tarefa/1/', {'nome': 'nome_editado', 'descricao': 'descricao_editada'})
        self.assertTrue(Tarefa.objects.filter(nome='nome_editado').exists())
    def test_excluir_tarefa(self):
        """ esperado EXCLUIR tarefa"""
        self.client.login(username='admin', password='correta')
        self.client.post('/lista_de_tarefas/excluir_tarefa/1/')
        self.assertFalse(Tarefa.objects.filter(id=1).exists())

    def test_exibir_tarefas(self):
        """ esperado EXIBIR tarefas"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertTrue(Tarefa.objects.filter(usuario=User.objects.get(username="admin")).exists())

class Test_Autenticacao_A_Privilegios(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin', password='correta')
    def test_acesso_autenticado(self):
        """esperado ACENDER a pagina de previlegios"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertEqual(response.status_code, 200)
    def test_acesso_nao_autenticado(self):
        """esperado NEGAÇÂO a pagina de previlegios"""
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertEqual(response.status_code, 302)
    def test_autenticar_com_usuario_nao_cadastrado(self):
        """esperado NEGAÇÂO a pagina de previlegios"""
        self.client.login(username='nao_cadastrado', password='correta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertEqual(response.status_code, 302)

    def test_autenticar_com_senha_incorreta(self):
        """esperado NEGAÇÂO a pagina de previlegios"""
        self.client.login(username='admin', password='incorreta')
        response = self.client.get('/lista_de_tarefas/exibir_tarefas/')
        self.assertEqual(response.status_code, 302)

class Test_Autenticacao_Rotas(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin', password='correta')
    def test_logar_com_usuario_autenticado(self):
        """Esperado ser MANTIDO na pagina de logar"""
        self.client.login(username='admin', password='correta')
        response = self.client.get('/lista_de_tarefas/logar/')
        self.assertEqual(response.status_code, 200)

    def test_cadastrar_usuario_existente(self):
        """Esperado ser redirecionado para a pagina de login"""
        response = self.client.post('/lista_de_tarefas/cadastrar/', {'username': 'admin', 'password': 'NaN'})
        self.assertEqual(response.status_code, 302)
    def test_logar_usuario_nao_existente(self):
        """Esperado ser redirecionado para a pagina de cadastro"""
        response = self.client.post('/lista_de_tarefas/logar/', {'username': 'nao_cadastrado', 'password': 'NaN'})
        self.assertEqual(response.status_code, 302)
    def test_logar_senha_incorreta(self):
        """Esperado ser MANTIDO na pagina de logar"""
        response = self.client.post('/lista_de_tarefas/logar/', {'username': 'admin', 'password': 'incorreta'})
        self.assertEqual(response.status_code, 200)

