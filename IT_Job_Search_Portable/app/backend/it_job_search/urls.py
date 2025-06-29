"""
URL configuration for it_job_search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import home, job_invitation, custom_login, register, forgot_password, change_password, logout_user, cv_templates, top_companies, applied_jobs, update_applied_job, delete_applied_job
from blog_posts.views import blog_list, blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('job-invitation/', job_invitation, name='job_invitation'),
    path('login/', custom_login, name='custom_login'),
    path('register/', register, name='register'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('change-password/', change_password, name='change_password'),
    path('logout/', logout_user, name='logout_user'),
    path('cv-templates/', cv_templates, name='cv_templates'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('user_management.urls')),
    path('api/jobs/', include('job_listings.urls')),
    path('api/companies/', include('company_profiles.urls')),
    path('api/blog/', include('blog_posts.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('companies/', top_companies, name='top_companies'),
    path('user_management/', include('user_management.urls')),
    path('applied-jobs/', applied_jobs, name='applied_jobs'),
    path('update-applied-job/', update_applied_job, name='update_applied_job'),
    path('delete-applied-job/', delete_applied_job, name='delete_applied_job'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
