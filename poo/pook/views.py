from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.
class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='pook/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name='pook/detail.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': posts})

