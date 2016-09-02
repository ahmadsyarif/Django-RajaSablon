from django import forms
from .models import product,category

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','price','unit','description','discount','image_file','available','category']

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name','description']