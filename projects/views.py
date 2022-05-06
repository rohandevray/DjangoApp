from email import message
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from numpy import product
from .models import Project  #importing the model name called model from the models


#defining a function
def projects(request):
    projects = Project.objects.all  #gives all the objects in model name(Project) database table
    context={"projects":projects}
    return render(request,"projects/projects.html",context)

def greet(request,id):
    projectObj = Project.objects.get(id=id)
    return render(request,"projects/greet.html",{"project":projectObj})