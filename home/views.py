from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *
# Create your views here.

def index(request):
    context ={
        'page':"home"
    }
    return render(request,'home/main.html',context)

def upload(request):
    if request.method =="POST":
        form = productForm(request.POST)
        if form.is_valid():
            return HttpResponse("success")
        else:
            return HttpResponse("failed")
    else:
        form = productForm()
        context = {
            'page':"upload",
            'form':form
        }
    return render(request,'home/main.html',context)