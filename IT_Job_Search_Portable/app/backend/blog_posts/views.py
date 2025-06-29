from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

def blog_list(request):
    blogs = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    related = BlogPost.objects.exclude(id=blog.id).order_by('-created_at')[:5]
    return render(request, 'blog_detail.html', {'blog': blog, 'related': related})
