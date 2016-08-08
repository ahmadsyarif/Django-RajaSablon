from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello world, rita I love you")

def upload(request):
    context = {
        'page':"upload"
    }
    return render(request,'home/main.html',context)