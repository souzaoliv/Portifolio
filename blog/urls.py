from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index_blog'),
    path('sobre/', views.sobre, name='sobre'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.detail_post, name='detail_post'),
]