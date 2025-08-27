from django.db import models

# Create your models here.
class Blog(models.Model):
    """ Blog model """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('author.Author',
                            related_name='author_blogs',
                            on_delete=models.PROTECT)
    cover_image = models.OneToOneField('CoverImage',
                                related_name='blog_cover_image', null=True,
                                blank=True,
                                on_delete=models.PROTECT)
    tags = models.ManyToManyField("Tags", related_name='blog_tags', blank=True)
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

class DemoModel(BaseTimeStampModel):
    name = models.CharField(max_length=100)

class CoverImage(BaseTimeStampModel):
    """ Cover Image model """
    image_link = models.URLField()

class Tags(BaseTimeStampModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name