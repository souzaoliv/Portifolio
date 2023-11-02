from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, blank=False)
    summary = RichTextField(config_name='awesome_ckeditor',max_length=1000, blank=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField(config_name='awesome_ckeditor')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)




    objects = models.Manager()
    pushlished = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['slug', 'publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_post', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_tags(self):
        return self.posttags_set.all()

class Tags(models.Model):
    tag = models.CharField(max_length=250, blank=False)
    def __str__(self):
        return self.tag

class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag
class Categorias (models.Model):
    categoria = models.CharField(max_length=250, blank=False)
    def __str__(self):
        return self.categoria
class PostCategorias(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    def __str__(self):
        return self.categoria