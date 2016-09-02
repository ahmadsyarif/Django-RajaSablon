from django.shortcuts import render
from django.http import HttpResponse
from .models import category,product
from .form import productForm,categoryForm
# Create your views here.

def index(request):
    context ={
        'page':"home"
    }
    return render(request,'home/main.html',context)

def add_product(request):
    if request.method =="POST":
        form = productForm(request.POST,request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            context = {
                'page':"details",
                'type':"product",
                'product':prod
            }
        else:
            context = {
                'page':"error"
            }
    else:
        form = productForm()
        context = {
            'page':"upload",
            'type':"product",
            'form':form
        }
    return render(request,'home/main.html',context)

def add_category(request):
    if request.method =="POST":
        form = categoryForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.save()
            context = {
                'page':"details",
                'type':"category",
                'category':cate
            }
        else:
            context = {
                'page':"error"
            }
        return render(request,'home/main.html',context)
    else:
        form = categoryForm()
        context = {
            'page':"upload",
            'type':"category",
            'form':form
        }
        return render(request,'home/main.html',context)
    
    