from ckeditor.fields import RichTextField
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    content = RichTextField()
    meta_title = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    published = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)