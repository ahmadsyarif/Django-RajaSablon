from django.db import models
import cloudinary.uploader
import os
# Create your models here.
        
"""
Defenition of class Category
"""
class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200)

    #manager
    categories = models.Manager()

    def __str__(self):
        return self.name

"""
Defenition of class product
"""
class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=20   )
    description = models.TextField(blank=True)
    discount = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200)
    image_file = models.FileField(upload_to='image')
    image_url = models.URLField(blank=True)
    available = models.IntegerField(default=0)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    #manager
    products = models.Manager()

    #cloudinary specific field
    image_cloudinary = None
    
    def __str__(self):
        return '{}'.format(self.name)

    def upload_picture(self,file):
        self.image_cloudinary = cloudinary.uploader.upload(file)
        self.image_url = self.image_cloudinary['secure_url']
        
    def remove_cache_image(self):
        os.remove(self.image_file.path)
    
    def save(self):
        super(product,self).save()
        try:
            self.upload_picture(self.image_file.path)
            self.remove_cache_image()
            super(product,self).save()
        except FileNotFoundError:
            pass


