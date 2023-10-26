from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView

from .models import Post
# Create your views here.


class PostListView(ListView):
    queryset = Post.pushlished.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/index.html'


@require_http_methods(["GET"])
def detail_post(request, year, month, day, post):

    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    contex = {
        'post': post,
    }
    return render(request, 'blog/detail_post.html', contex)

@require_http_methods(["GET"])
def sobre(request):
    return render(request, 'blog/sobre.html')

