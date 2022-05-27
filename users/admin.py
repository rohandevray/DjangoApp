from django.contrib import admin

# Register your models here.
#now after creating models and after its 2 steps i.e
#makemigrations and migrate

#u have to register model here to see it admin panel

from .models import Profile
from .models import Skill

admin.site.register(Profile)
admin.site.register(Skill)
