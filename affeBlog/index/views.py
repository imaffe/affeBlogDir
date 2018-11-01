from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def index_home(request):
    query_set = Post.objects.all()
    instance = get_object_or_404(Post, id=1)
    context = {
        "object_list": query_set,
        "title": instance.title,
    }
    return render(request, "index.html", context)

