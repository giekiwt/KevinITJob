from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from it_job_search.models import ProgrammingLanguage
from company_profiles.models import Company
from blog_posts.models import BlogPost
from job_listings.models import ApplyJob, Job
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime

User = get_user_model()

@csrf_protect
def custom_login(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or '/job-invitation/'
            return redirect(next_url)
        else:
            error = 'Email hoặc mật khẩu không đúng.'
    return render(request, 'login.html', {'error': error})

@csrf_protect
def register(request):
    error = None
    success = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            error = 'Mật khẩu xác nhận không khớp.'
        elif User.objects.filter(email=email).exists():
            error = 'Email đã được sử dụng.'
        else:
            user = User.objects.create_user(email=email, password=password)
            user.save()
            success = 'Đăng ký thành công! Bạn có thể đăng nhập ngay.'
    return render(request, 'register.html', {'error': error, 'success': success})

def home(request):
    languages = ProgrammingLanguage.objects.all()
    top_companies = Company.objects.all()[:6]
    latest_blogs = BlogPost.objects.order_by('-created_at')[:3]
    return render(request, 'home.html', {'languages': languages, 'top_companies': top_companies, 'latest_blogs': latest_blogs})

def job_invitation(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next=/job-invitation/')
    upload_success = False
    company_name = ''
    job_title = ''
    location = ''
    company_slug = request.GET.get('company')
    job_title_param = request.GET.get('job_title')
    location_param = request.GET.get('location')
    if company_slug:
        try:
            company = Company.objects.get(slug=company_slug)
            company_name = company.name
        except Company.DoesNotExist:
            company_name = ''
    if job_title_param:
        job_title = job_title_param
    if location_param:
        location = location_param
    if request.method == 'POST' and request.FILES.get('cv'):
        cv_file = request.FILES['cv']
        company_name = request.POST.get('company', company_name)
        job_title = request.POST.get('job_title', job_title)
        location = request.POST.get('location', location)
        company_obj = Company.objects.filter(name=company_name).first()
        job_obj = Job.objects.filter(title=job_title, company=company_obj).first()
        ApplyJob.objects.create(
            user=request.user,
            company=company_obj,
            job=job_obj,
            job_title=job_title,
            location=location,
            cv_file=cv_file
        )
        upload_success = True
    return render(request, 'job_invitation.html', {'upload_success': upload_success, 'company_name': company_name, 'job_title': job_title, 'location': location})

@csrf_protect
def forgot_password(request):
    success = None
    if request.method == 'POST':
        email = request.POST.get('email')
        # Demo: chỉ hiển thị thông báo, chưa gửi email thực tế
        success = 'Nếu email tồn tại, hướng dẫn đặt lại mật khẩu đã được gửi.'
    return render(request, 'forgot_password.html', {'success': success})

@csrf_protect
@login_required
def change_password(request):
    error = None
    success = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = request.user
        if not user.check_password(old_password):
            error = 'Mật khẩu hiện tại không đúng.'
        elif new_password != confirm_password:
            error = 'Mật khẩu mới xác nhận không khớp.'
        else:
            user.set_password(new_password)
            user.save()
            success = 'Đổi mật khẩu thành công!'
    return render(request, 'change_password.html', {'error': error, 'success': success})

def logout_user(request):
    logout(request)
    return redirect('/')

def cv_templates(request):
    # Danh sách mẫu CV mẫu (tên + ảnh demo)
    templates = [
        {"name": f"CV Template {i+1}", "img": f"/static/cv_templates/cv{i+1}.png"} for i in range(20)
    ]
    return render(request, 'cv_templates.html', {"templates": templates})

def top_companies(request):
    # Nếu chưa có trường phân loại, chia tạm: 15 công ty đầu là large, còn lại là SME
    companies = list(Company.objects.all())
    large_companies = companies[:15]
    sme_companies = companies[15:30]
    return render(request, 'top_companies.html', {
        'large_companies': large_companies,
        'sme_companies': sme_companies,
    })

def applied_jobs(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next=/applied-jobs/')
    applied_list = ApplyJob.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'applied_jobs.html', {'applied_list': applied_list})

@csrf_protect
@login_required
def update_applied_job(request):
    if request.method == 'POST':
        apply_id = request.POST.get('apply_id')
        company = request.POST.get('company', '')
        job_title = request.POST.get('job_title', '')
        location = request.POST.get('location', '')
        apply = ApplyJob.objects.filter(id=apply_id, user=request.user).first()
        if apply:
            company_obj = Company.objects.filter(name=company).first()
            job_obj = Job.objects.filter(title=job_title, company=company_obj).first()
            apply.company = company_obj
            apply.job = job_obj
            apply.job_title = job_title
            apply.location = location
            apply.save()
    return redirect('/applied-jobs/')

@csrf_protect
@login_required
def delete_applied_job(request):
    if request.method == 'POST':
        apply_id = request.POST.get('apply_id')
        apply = ApplyJob.objects.filter(id=apply_id, user=request.user).first()
        if apply:
            # Xóa file vật lý
            if apply.cv_file and os.path.exists(apply.cv_file.path):
                os.remove(apply.cv_file.path)
            apply.delete()
    return redirect('/applied-jobs/') 