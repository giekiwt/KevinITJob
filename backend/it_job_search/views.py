from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

User = get_user_model()

@csrf_protect
def custom_login(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is not None and user.check_password(password):
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
    return render(request, 'home.html')

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