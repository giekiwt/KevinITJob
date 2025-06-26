from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.

@login_required
def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_update')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user_management/profile_update.html', {'form': form, 'profile': profile})
