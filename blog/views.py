from django.shortcuts import render
from .models import Post
def showblog(request):
	posts = Post.objects
	return render(request, 'blog/blog.html',{'posts': posts})

# Create your views here.
