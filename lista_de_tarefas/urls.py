from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_lista_de_tarefas'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('logar/', views.logar, name='logar'),
    path('deslogar/', views.deslogar, name='deslogar'),
    path('exibir_tarefas/', views.exibir_tarefas, name='exibir_tarefas'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('editar_tarefa/<int:pk>/', views.editar_tarefa, name='editar_tarefa'),
    path('excluir_tarefa/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
]
