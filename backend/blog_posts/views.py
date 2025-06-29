from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost

# Create your views here.

def blog_list(request):
    blogs_list = BlogPost.objects.order_by('-created_at')
    
    # Phân trang - 6 bài blog mỗi trang
    paginator = Paginator(blogs_list, 6)
    page = request.GET.get('page')
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # Nếu page không phải là số, hiển thị trang đầu tiên
        blogs = paginator.page(1)
    except EmptyPage:
        # Nếu page vượt quá số trang, hiển thị trang cuối
        blogs = paginator.page(paginator.num_pages)
    
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    related = BlogPost.objects.exclude(id=blog.id).order_by('-created_at')[:5]
    return render(request, 'blog_detail.html', {'blog': blog, 'related': related})
