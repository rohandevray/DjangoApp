from distutils.command.upload import upload
import email
from email.policy import default
import imp
import uuid
from pyexpat import model
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, null=True, blank=True) #this create a one to one relationship bewteen django default user model to profile model 
    #one to one means (1 user 1 profile linked) & (1 profile 1 user linked) whenever a new user created in user modeldb then a profile is created from where we can extract the user info to and make our profile model.
    name = models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    username =models.CharField(max_length=200,null=True,blank=True)
    location =models.CharField(max_length=200,null=True,blank=True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio= models.TextField(null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_twitter = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)
    social_quora = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,primary_key=True)
    def __str__(self):
        return str(self.user.username)
    
class Skill(models.Model):
    owner= models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    description= models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,primary_key=True)
    def __str__(self):
        return str(self.name)
