from email import message
from multiprocessing import context
import re
from turtle import pos
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from numpy import product
from .models import Project  #importing the model name called model from the models
from .forms import ProjectForm #importing the projectform we created to add project on preform CRUD operations


#defining a function
def projects(request):
    projects = Project.objects.all  #gives all the objects in model name(Project) database table
    context={"projects":projects}
    return render(request,"projects/projects.html",context)

def greet(request,id):
    projectObj = Project.objects.get(id=id)
    return render(request,"projects/greet.html",{"project":projectObj})

def createProject(request):
    form = ProjectForm()  #as projectForm is a class we have to use bracket to indicate we are using right terminology
    
    if request.method == "POST":
        form = ProjectForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context={ 
       "form":form
    }
    return render(request,"projects/project_form.html",context)

    

def updateProject(request,pk):
    project = Project.objects.get(id=pk) #getting the project as when we click the edit button via the pk(primar key) we get that project
    form = ProjectForm(instance=project)  #as projectForm is a class we have to use bracket to indicate we are using right terminology
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES ,instance=project) #instance is the project we want to edit
        if form.is_valid():
            form.save()
            return redirect('projects')

    context={ 
       "form":form
    }
    return render(request,"projects/project_form.html",context)



def deleteProject(request,pk):
    project= Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete() #this gonna delete the database
        return redirect("projects")

    context={"object":project}
    return render(request,"projects/delete_template.html",context)













#notes
#form = ProjectForm(instance=project)  here what is the role of instance = project
# it will match prefill ProjectForm with the datas of the project available
#update PRoject is simple its just taking one step before the createProject step 
#and autofill all the data we already filled there (via instance = project ) and from there we are just able to change it.
#nothing complicated here!!!