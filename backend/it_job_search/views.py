from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from it_job_search.models import ProgrammingLanguage
from company_profiles.models import Company

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
    return render(request, 'home.html', {'languages': languages})

def job_invitation(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next=/job-invitation/')
    # Nếu đã đăng nhập, render form nhập thông tin cá nhân + upload CV
    return render(request, 'job_invitation.html')

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