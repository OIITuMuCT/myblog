from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # demo_field = models.TextField(default='demo')
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)

    def get_author_email(self):
        return f'{self.email}'

    def get_short_bio(self):
        return f'{self.bio[:200]}...'

    def __str__(self):
        return self.name

class BlogAuthor(Author):
    class Meta:
        proxy = True

    def perform_something(self):
        pass
