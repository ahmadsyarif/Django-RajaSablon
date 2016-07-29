from django.contrib import admin
from .models import product, category
# Register your models here.

#register product
admin.site.register(product)

#register category
admin.site.register(category)