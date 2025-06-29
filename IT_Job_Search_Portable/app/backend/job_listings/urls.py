from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/language/<slug:language_slug>/', views.job_list_by_language, name='job_list_by_language'),
    path('jobs/company/<slug:company_slug>/', views.job_list_by_company, name='job_list_by_company'),
    path('jobs/location/<slug:location_slug>/', views.job_list_by_location, name='job_list_by_location'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
] 