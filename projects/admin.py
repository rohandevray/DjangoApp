from django.contrib import admin

# Register your models here.
#we have to register our models to show it in admin panel
from . models import Project,Review,Tag

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)