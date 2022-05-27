#we have created this file 
from django.urls import URLPattern, path
from . import views

# . means from this app or main folder 


urlpatterns = [
    path('',views.profiles, name="profiles"), #root domain (don't give space between the empty bracket)
    path('profile/<str:pk>/',views.userProfile,name="user-profile")
]