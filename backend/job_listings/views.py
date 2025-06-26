from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.core.paginator import Paginator
from .models import Job
from .serializers import JobSerializer
from it_job_search.models import ProgrammingLanguage
from company_profiles.models import Company, Location

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def get_languages():
    return ProgrammingLanguage.objects.all()

def job_list(request):
    """Hiển thị danh sách tất cả việc làm"""
    jobs = Job.objects.select_related('company', 'location').prefetch_related('skills').all().order_by('-posted_at')
    
    # Filter theo ngôn ngữ
    language_id = request.GET.get('language')
    if language_id:
        jobs = jobs.filter(skills__id=language_id)
    
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
        'selected_language': language_id,
        'selected_company': company_id,
        'selected_location': location_id,
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
        'company': company.name,
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
    return render(request, 'job_listings/job_detail.html', {'job': job})
