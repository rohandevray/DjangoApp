from multiprocessing import context
from django.shortcuts import render
from .models import Profile
# Create your views here.
#after creating the template for this app now we create function based view

def profiles(request):
    profiles=Profile.objects.all() #taking all the profiles in database (as structured as model and pass as context dictionary to the template to render it)
    context={
        "profiles":profiles,
    }
    return render(request,"users/profiles.html",context)




def userProfile(request,pk):
    profile= Profile.objects.get(id=pk) #get method gives a single data depending upon the condition written inside the get () here we want the profile having id = pk i.e grab the profile we selected/clicked upon
    topSkills= profile.skill_set.exclude(description__exact="") # (modelname)_set is the way to access the data of its child models
    otherSkills = profile.skill_set.filter(description="")
    context={
        "profile":profile,
        "topSkills":topSkills,
        "otherSkills":otherSkills
    }
    return render(request,"users/user-profile.html",context)
    #by passsing context(bunch of datas ), it is now available to the template we are sending it
 #and from there we can grab the datas from db.
# users/profiles.html this is the template name we want to render via a function profiles
# after this create a file of url to add a path to the views
