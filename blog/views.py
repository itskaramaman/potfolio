from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'allblogs': allblogs})


def detailed_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detailed_blog.html', {'blog': blog})
