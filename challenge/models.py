from django.db import models
from django.utils import timezone

# Create your models here.

class Application(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=128)
    short_text = models.TextField()
    detail_text = models.TextField()
    submitted_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
