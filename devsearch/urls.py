
import imp
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include("projects.urls")), #empty string that triggers the root domain
    path('',include("users.urls")) #anything that starts with users go to this users.urls file
    #and the user app (urls.py) takes care of routing from there
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)