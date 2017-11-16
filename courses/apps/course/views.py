# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from django.shortcuts import render, redirect

def index(request):
    context = {
        "description": description.objects.all()
    }
    return render(request, 'course/index.html', context)

def add(request):
    description.objects.create(name= request.POST['name'],description=request.POST['description'])

    return redirect('/')

def remove(request, id):
    context={
        "Q":description.objects.get(id=id)
    }
    return render(request, 'course/remove.html', context)

def delete(request, id):
    description.objects.get(id=id).delete()
    return redirect('/')

def returns(request):

    return redirect('/')

# Create your views here.
