from django.db import models

# Create your models here.
class Blog(models.Model):
    """ Blog model """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('author.Author',
                            related_name='author_blogs',
                            on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

## Using model inheritance
class BaseTimeStampModel(models.Model):
    """Adding a create and update date time"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Abstract base class"""
        abstract = True


class CoverImage(BaseTimeStampModel):
    """ Cover Image model """
    image_link = models.URLField()
    blog = models.OneToOneField(Blog, related_name='blog_ci', on_delete=models.PROTECT)
