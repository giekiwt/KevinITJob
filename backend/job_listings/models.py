from django.db import models
from company_profiles.models import Company

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)
