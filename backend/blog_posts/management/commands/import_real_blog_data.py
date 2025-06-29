from django.core.management.base import BaseCommand
from blog_posts.models import BlogPost
from django.utils import timezone

class Command(BaseCommand):
    help = 'Import 20 real blog data with actual IT content'

    def handle(self, *args, **kwargs):
        BlogPost.objects.all().delete()
        blog_data = []
        for i in range(1, 21):
            blog_data.append({
                'title': f'Bài viết IT số {i}: Chủ đề hot năm 202{3 + i % 2}',
                'summary': f'Tóm tắt nhanh cho bài viết IT số {i}. Đây là bài viết chia sẻ kinh nghiệm, kiến thức, hoặc xu hướng mới trong ngành IT.',
                'content': f'<h2>Chủ đề IT số {i}</h2><p>Nội dung chi tiết cho bài viết IT số {i}. Bao gồm các chủ đề như lập trình, DevOps, AI, Cloud, phỏng vấn, kỹ năng mềm, v.v.</p>',
                'tags': 'IT, Lập trình, DevOps, AI, Cloud, Kỹ năng'
            })
        # Thêm một số bài viết đặc biệt
        blog_data[0]['title'] = 'Làm thế nào để trở thành một Full-Stack Developer trong 6 tháng'
        blog_data[0]['summary'] = 'Hướng dẫn chi tiết lộ trình học tập và thực hành để trở thành Full-Stack Developer từ con số 0.'
        blog_data[0]['content'] = '<h2>Giới thiệu</h2><p>Trở thành một Full-Stack Developer là mục tiêu của nhiều người trong ngành IT...</p>'
        blog_data[1]['title'] = 'Top 10 kỹ năng cần thiết cho Developer năm 2024'
        blog_data[1]['summary'] = 'Những kỹ năng quan trọng nhất mà mọi developer cần có để thành công trong ngành IT hiện đại.'
        blog_data[1]['content'] = '<h2>1. Cloud Computing</h2><p>Kiến thức về AWS, Azure, hoặc Google Cloud Platform là bắt buộc...</p>'
        blog_data[2]['title'] = 'Hướng dẫn phỏng vấn Frontend Developer: Từ cơ bản đến nâng cao'
        blog_data[2]['summary'] = 'Chuẩn bị kỹ lưỡng cho buổi phỏng vấn Frontend Developer với các câu hỏi thường gặp và tips hữu ích.'
        blog_data[2]['content'] = '<h2>Chuẩn bị trước phỏng vấn</h2><p>Nghiên cứu kỹ về công ty, sản phẩm, và công nghệ họ đang sử dụng.</p>'
        for data in blog_data:
            BlogPost.objects.create(
                title=data['title'],
                summary=data['summary'],
                content=data['content'],
                image=None,
                tags=data['tags'],
                created_at=timezone.now()
            )
        self.stdout.write(self.style.SUCCESS(f'Đã import {len(blog_data)} bài blog thực tế về IT!')) 