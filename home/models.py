from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
# Create your models here.
"""
Defenition of class product
"""
class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    discount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200)
    imageFile = models.FileField(upload_to='image')
    imageUrl = models.URLField(default='empty')
    available = models.IntegerField(default=0)

    #manager
    products = models.Manager()

    def __str__(self):
        return '{}'.format(self.name)

    def upload_picture(self,file):
        response = cloudinary.uploader.upload(file)
        self.imageUrl = response['secure_url']
        
    def remove_cache_image(self):
        os.remove(self.imageFile.path)
    
    def save(self):
        super(product,self).save()
        try:
            self.remove_cache_image()
        except FileNotFoundError:
            pass
        
"""
Defenition of class Category
"""
class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200)

    #many to many relationship with product
    products = models.ManyToManyField(product)

    #manager
    categories = models.Manager()