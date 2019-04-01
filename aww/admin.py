from django.contrib import admin

from .models import Project,Image,Location,Profile
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Location)
