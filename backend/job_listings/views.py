from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.core.paginator import Paginator
from .models import Job
from .serializers import JobSerializer
from it_job_search.models import ProgrammingLanguage
from company_profiles.models import Company, Location
import random
from django.db.models import Q

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def get_languages():
    return ProgrammingLanguage.objects.all()

def job_list(request):
    """Hiển thị danh sách tất cả việc làm"""
    jobs = Job.objects.select_related('company', 'location').prefetch_related('skills').all().order_by('-posted_at')
    q = request.GET.get('q')
    if q:
        jobs = jobs.filter(
            Q(title__icontains=q) |
            Q(company__name__icontains=q) |
            Q(skills__name__icontains=q)
        ).distinct()
    # Filter theo ngôn ngữ
    language_slug = request.GET.get('language')
    if language_slug:
        try:
            language_obj = ProgrammingLanguage.objects.get(slug=language_slug)
            jobs = jobs.filter(skills=language_obj)
        except ProgrammingLanguage.DoesNotExist:
            jobs = jobs.none()
    # Filter theo công ty
    company_id = request.GET.get('company')
    if company_id:
        jobs = jobs.filter(company__id=company_id)
    # Filter theo khu vực
    location_id = request.GET.get('location')
    if location_id:
        jobs = jobs.filter(location__id=location_id)
    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Context data
    context = {
        'page_obj': page_obj,
        'languages': get_languages(),
        'companies': Company.objects.all(),
        'locations': Location.objects.all(),
        'selected_language': language_slug,
        'selected_company': company_id,
        'selected_location': location_id,
        'q': q,
    }
    return render(request, 'job_listings/job_list.html', context)

def job_list_by_language(request, language_slug):
    """Hiển thị danh sách việc làm theo ngôn ngữ cụ thể"""
    language = get_object_or_404(ProgrammingLanguage, slug=language_slug)
    jobs = Job.objects.select_related('company', 'location').prefetch_related('skills').filter(skills=language).order_by('-posted_at')
    
    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'language': language,
        'page_obj': page_obj,
        'languages': get_languages(),
        'companies': Company.objects.all(),
        'locations': Location.objects.all(),
    }
    
    return render(request, 'job_listings/job_list_by_language.html', context)

def job_list_by_company(request, company_slug):
    company = get_object_or_404(Company, slug=company_slug)
    jobs = Job.objects.select_related('company', 'location').prefetch_related('skills').filter(company=company).order_by('-posted_at')
    context = {
        'company': company,
        'jobs': jobs,
        'companies': Company.objects.all(),
        'languages': ProgrammingLanguage.objects.all(),
        'locations': Location.objects.all(),
    }
    return render(request, 'job_listings/job_list_by_company.html', context)

def job_list_by_location(request, location_slug):
    location = get_object_or_404(Location, slug=location_slug)
    jobs = Job.objects.select_related('company', 'location').prefetch_related('skills').filter(location=location).order_by('-posted_at')
    context = {
        'location': location.name,
        'jobs': jobs,
        'companies': Company.objects.all(),
        'languages': ProgrammingLanguage.objects.all(),
        'locations': Location.objects.all(),
    }
    return render(request, 'job_listings/job_list_by_location.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    # Danh sách đánh giá mẫu
    sample_reviews = [
        {
            'name': 'Nguyễn Văn A', 'avatar': 'https://randomuser.me/api/portraits/men/32.jpg', 'rating': 5, 'content': 'Môi trường làm việc năng động, đồng nghiệp thân thiện.',
        },
        {
            'name': 'Trần Thị B', 'avatar': 'https://randomuser.me/api/portraits/women/44.jpg', 'rating': 4, 'content': 'Công ty có nhiều cơ hội phát triển bản thân.',
        },
        {
            'name': 'Lê Văn C', 'avatar': 'https://randomuser.me/api/portraits/men/65.jpg', 'rating': 4, 'content': 'Chính sách phúc lợi tốt, lương thưởng rõ ràng.',
        },
        {
            'name': 'Phạm Thị D', 'avatar': 'https://randomuser.me/api/portraits/women/12.jpg', 'rating': 5, 'content': 'Sếp tâm lý, hỗ trợ nhân viên hết mình.',
        },
        {
            'name': 'Hoàng Văn E', 'avatar': 'https://randomuser.me/api/portraits/men/23.jpg', 'rating': 3, 'content': 'Công việc đôi khi áp lực nhưng học hỏi được nhiều.',
        },
        {
            'name': 'Đỗ Thị F', 'avatar': 'https://randomuser.me/api/portraits/women/55.jpg', 'rating': 5, 'content': 'Văn phòng đẹp, trang thiết bị hiện đại.',
        },
        {
            'name': 'Ngô Văn G', 'avatar': 'https://randomuser.me/api/portraits/men/77.jpg', 'rating': 4, 'content': 'Được tham gia nhiều dự án lớn, đồng nghiệp giỏi.',
        },
        {
            'name': 'Vũ Thị H', 'avatar': 'https://randomuser.me/api/portraits/women/36.jpg', 'rating': 5, 'content': 'Thời gian làm việc linh hoạt, work-life balance tốt.',
        },
        {
            'name': 'Phan Văn I', 'avatar': 'https://randomuser.me/api/portraits/men/41.jpg', 'rating': 4, 'content': 'Được đào tạo bài bản, có mentor hướng dẫn.',
        },
        {
            'name': 'Bùi Thị K', 'avatar': 'https://randomuser.me/api/portraits/women/28.jpg', 'rating': 5, 'content': 'Đồng nghiệp vui vẻ, teamwork tốt.',
        },
    ]
    reviews = random.sample(sample_reviews, k=random.randint(5, 10))
    # More jobs for you: cùng công ty hoặc cùng kỹ năng, loại trừ job hiện tại
    related_jobs = Job.objects.filter(company=job.company).exclude(id=job.id)
    if related_jobs.count() < 4:
        # Bổ sung thêm job cùng kỹ năng nếu chưa đủ
        skill_ids = job.skills.values_list('id', flat=True)
        more_by_skill = Job.objects.filter(skills__in=skill_ids).exclude(id__in=[job.id]+list(related_jobs.values_list('id', flat=True)))
        related_jobs = list(related_jobs) + list(more_by_skill)
    # Loại trùng và lấy tối đa 6 job
    seen = set()
    more_jobs = []
    for j in related_jobs:
        if j.id not in seen and len(more_jobs) < 6:
            more_jobs.append(j)
            seen.add(j.id)
    return render(request, 'job_listings/job_detail.html', {'job': job, 'reviews': reviews, 'more_jobs': more_jobs})
