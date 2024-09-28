from django.shortcuts import render , get_list_or_404
from blog.models import Post
# Create your views here.

def allpost(request):
    post = Post.objects
    return render(request,'post.html',{'post':post})

def detail(request, blog_id):
    detail = get_list_or_404(Post, pk = blog_id)
    return render(request, 'details.html', {'post' : detail})