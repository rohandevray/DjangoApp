from django.urls import path
from . import views


urlpatterns = [
    path("", views.projects, name="projects"),
    path("greet/<str:id>/",views.greet , name="greet")
]