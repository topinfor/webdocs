from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Sector(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(max_length=150, unique=True)
    tags = models.CharField(max_length=65)
    is_published = models.BooleanField(default=False)
    content = models.TextField()
    content_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='blog/covers/%Y/%m/%d', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.author and 'user' in kwargs:
            self.author = kwargs.pop('user')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title