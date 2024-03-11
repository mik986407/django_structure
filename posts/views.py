from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # return HttpResponse("My First Django App.")   
    return render(request, "posts/index.html", {"posts": posts})