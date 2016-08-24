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
        form = productForm(request.POST,request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.name = "test"
            prod.price = 222
            prod.description = "test lagi"
            prod.discount = 20
            prod.upload_picture(request.FILES["imageFile"])
            prod.save()
            context = {
                'page':"details",
                'product':prod
            }
        else:
            return HttpResponse("{} {}".format(form.errors,form.non_field_errors ))
    else:
        form = productForm()
        context = {
            'page':"upload",
            'form':form
        }
    return render(request,'home/main.html',context)