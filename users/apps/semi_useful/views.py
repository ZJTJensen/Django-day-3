# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

from django.core.urlresolvers import reverse

def index(request):
    context = {
        "users": users.objects.all()
    }
    return render(request, "semi_useful/index.html", context)

def new(request):
    return render(request, "semi_useful/new_user.html")

def edit(request, id):
    return render(request, "semi_useful/edit_user.html")

def show(request, id):
    context={
    "q":users.objects.get(id=id)
    }
    return render(request, "semi_useful/user.html", context)

def create(request):
    users.objects.create(first_name= request.POST['first_name'],last_name=request.POST['last_name'],email= request.POST['email'])
    
    id=users.objects.last().id
    return redirect("/users/{}".format(id))

def destroy(request, id):

    users.objects.get(id=id).delete()

    return redirect("/")

def update(request, id):
    c=users.objects.get(id=id)
    c.first_name= request.POST['first_name']
    c.last_name=request.POST['last_name']
    c.email= request.POST['email']
    c.save()
    
    return redirect("/users/{}".format(id))



# Create your views here.
