from django.db import models

# Create your models here.
"""
Defenition of class product
"""
class product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    discount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField()
    #TODO to create image field and its callable function to upload image in external repository
    #image = models.ImageField()
    available = models.IntegerField(default=0)

    #manager
    products = models.Manager()

    def __str__(self):
        return '{}'.format(self.name)
"""
Defenition of class Category
"""
class category(models.Model):
    name = models.CharField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField()

    #many to many relationship with product
    products = models.ManyToManyField(product)

    #manager
    categories = models.Manager()