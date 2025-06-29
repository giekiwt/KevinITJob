from django.core.management.base import BaseCommand
from blog_posts.models import BlogPost
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed 10 blog posts'

    def handle(self, *args, **kwargs):
        BlogPost.objects.all().delete()
        for i in range(1, 11):
            BlogPost.objects.create(
                title=f"Bài blog IT số {i}",
                summary=f"Đây là tóm tắt ngắn gọn cho bài blog IT số {i}. Chia sẻ về kinh nghiệm, kỹ năng, hoặc xu hướng mới trong ngành IT.",
                content=f"<p>Nội dung chi tiết cho bài blog IT số {i}. Đây là nơi bạn có thể viết bài phân tích, hướng dẫn, hoặc chia sẻ kinh nghiệm thực tế về công việc IT, lập trình, phỏng vấn, lương thưởng, v.v.</p>",
                image=None,
                tags="IT, Kinh nghiệm, Lập trình, Blog",
                created_at=timezone.now()
            )
        self.stdout.write(self.style.SUCCESS('Đã seed 10 blog posts mẫu!')) 