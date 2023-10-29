from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    name_ukr = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    link = models.SlugField(unique=True)
    content_ukr = RichTextField()
    content_eng = RichTextField()

    def __str__(self):
        return self.name_ukr
