from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tag'] #the lists fields which we wanna see in our form moedel

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({"class":'input'})