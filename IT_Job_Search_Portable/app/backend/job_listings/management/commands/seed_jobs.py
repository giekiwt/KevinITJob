from django.core.management.base import BaseCommand
from it_job_search.models import ProgrammingLanguage
from company_profiles.models import Company, Location
from job_listings.models import Job
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed jobs, companies, locations, programming languages'

    def handle(self, *args, **kwargs):
        # Xóa location và job cũ để seed lại chuẩn
        Job.objects.all().delete()
        Location.objects.all().delete()

        # Seed locations
        locations = ['Hồ Chí Minh City', 'Hà Nội', 'Đà Nẵng']
        location_objs = {}
        for loc in locations:
            l, _ = Location.objects.get_or_create(name=loc)
            location_objs[loc] = l

        # Seed programming languages
        langs = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'TypeScript', 'Ruby', 'Go', 'Swift', 'Kotlin']
        lang_objs = []
        for lang in langs:
            l, _ = ProgrammingLanguage.objects.get_or_create(name=lang)
            lang_objs.append(l)

        # Seed companies
        companies = [
            'FPT Software', 'VNG Corporation', 'Viettel Group', 'MB Bank', 'Techcombank', 'Momo', 'Tiki', 'Shopee', 'Grab', 'VNPT',
            'CMC Corporation', 'Haravan', 'Axon', 'KMS Technology', 'NashTech', 'TMA Solutions', 'Sendo', 'Be Group', 'Vietcombank', 'ELCA'
        ]
        company_objs = []
        for i, name in enumerate(companies):
            c, _ = Company.objects.get_or_create(name=name, defaults={
                'description': f'Công ty {name} chuyên về công nghệ thông tin.',
                'website': f'https://{name.lower().replace(" ", "")}.com',
                'location': random.choice(list(location_objs.values()))
            })
            company_objs.append(c)

        titles = [
            'Backend Developer', 'Frontend Developer', 'Fullstack Developer', 'Mobile Developer', 'DevOps Engineer',
            'QA Engineer', 'Data Engineer', 'AI Engineer', 'Project Manager', 'Business Analyst'
        ]

        # Seed jobs cho từng location
        jobs_per_location = {
            'Hồ Chí Minh City': 110,
            'Hà Nội': 110,
            'Đà Nẵng': 50
        }
        for loc_name, num_jobs in jobs_per_location.items():
            for _ in range(num_jobs):
                company = random.choice(company_objs)
                title = random.choice(titles)
                salary_min = random.choice([800, 1000, 1200, 1500, 2000])
                salary_max = salary_min + random.choice([500, 800, 1000])
                lang_obj = random.choice(lang_objs)
                job = Job.objects.create(
                    title=f"{random.choice(['Junior', 'Middle', 'Senior'])} {title}",
                    company=company,
                    location=location_objs[loc_name],
                    salary_min=salary_min,
                    salary_max=salary_max,
                    description=f"Mô tả công việc {title} tại {company.name}.",
                    requirements=f"Yêu cầu: {', '.join(random.sample(langs, 3))}.",
                    posted_at=timezone.now()
                )
                other_skills = random.sample([l for l in lang_objs if l != lang_obj], k=random.randint(0, 3))
                job.skills.set([lang_obj] + other_skills)
        self.stdout.write(self.style.SUCCESS('Đã seed dữ liệu mẫu cho jobs, companies, locations, programming languages!')) 