from django.db import models
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Using RichTextField for the content
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
