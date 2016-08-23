from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *
# Create your views here.

def index(request):
    return HttpResponse("hello world, rita I love you")

def upload(request):
    form = productForm()
    context = {
        'page':"upload",
        'form':form
    }
    return render(request,'home/main.html',context)