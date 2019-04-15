from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add =  True)
    last_modified = models.DateTimeField(auto_now = True)
    is_draft = models.BooleanField(default = True)
    slug = models.SlugField(max_length = 100)

    def __str__(self):
        return self.title
    @property
    def days_since_creation(self):
        diff = timezone.now() - self.date_created
        return diff.days
