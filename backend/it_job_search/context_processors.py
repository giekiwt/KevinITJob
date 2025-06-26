from company_profiles.models import Company, Location
from it_job_search.models import ProgrammingLanguage
from user_management.models import Profile

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

def user_profile_context(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
    return {'user_profile': profile} 