from django.shortcuts import render
from django.http import HttpResponse
from .models import test
# Create your views here.

def index(request):
    return HttpResponse("hello world")