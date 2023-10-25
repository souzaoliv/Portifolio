from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Post
# Create your views here.

@require_http_methods(["GET"])
def index(request):
    query_post = Post.objects.all()
    context = {
        'posts': query_post
    }
    return render(request, 'blog/index.html', context)

@require_http_methods(["GET"])
def sobre(request):
    return render(request, 'blog/sobre.html')

@require_http_methods(["GET"])
def detail_post(request):
    return render(request, 'blog/detail_post.html')

