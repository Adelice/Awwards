from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = models.ImageField(upload_to='picture/', null=True, blank=True)
    description = models.TextField()
    project_url=models.URLField(max_length=250)

# Create your models here.
