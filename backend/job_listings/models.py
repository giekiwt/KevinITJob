from django.db import models
from company_profiles.models import Company, Location
from it_job_search.models import ProgrammingLanguage

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    skills = models.ManyToManyField(ProgrammingLanguage, blank=True)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.company.name}"
