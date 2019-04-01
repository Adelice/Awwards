from django.contrib import admin

from .models import Project,Location,Profile
admin.site.register(Project)
admin.site.register(Profile)

admin.site.register(Location)
