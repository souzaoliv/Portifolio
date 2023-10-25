from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_blog'),
    path('sobre/', views.sobre, name='sobre'),
    path('detail_post/', views.detail_post, name='detail_post'),
]