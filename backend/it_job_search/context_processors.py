from company_profiles.models import Company, Location
from it_job_search.models import ProgrammingLanguage

def companies_context(request):
    return {
        'companies': Company.objects.all()
    }

def locations_context(request):
    return {
        'locations': Location.objects.all()
    }

def languages_context(request):
    return {
        'languages': ProgrammingLanguage.objects.all()
    } 