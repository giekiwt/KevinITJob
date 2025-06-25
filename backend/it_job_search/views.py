from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def job_invitation(request):
    return render(request, 'job_invitation.html') 