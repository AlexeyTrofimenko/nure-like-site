from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Page(models.Model):

    name_ukr = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    link = models.SlugField(unique=True, blank=True)
    content_ukr = RichTextUploadingField()
    content_eng = RichTextUploadingField()

    def __str__(self):
        return self.name_ukr
