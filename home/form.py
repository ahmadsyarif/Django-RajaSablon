from django import forms
from .models import *

class productForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    #discount = forms.FloatField()
    #date_created = forms.DateTimeField(auto_now_add=True)
    #date_last_modified = forms.DateTimeField(auto_now=True)
    #created_by = forms.CharField(max_length=200)
    #TODO to create image field and its callable function to upload image in external repository
    #image = forms.URLField(default='empty')
    #available = forms.IntegerField(default=0)