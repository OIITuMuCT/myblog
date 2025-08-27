from django.core.management.base import BaseCommand
from blog.models import Blog

class Command(BaseCommand):
    help = 'Return total number of blogs'

    def handle(self, *args, **kwargs):
        total_blogs = Blog.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Total blogs: "{total_blogs}"'))