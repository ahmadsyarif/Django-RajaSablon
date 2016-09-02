from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^add/product',views.add_product),
    url(r'^add/category',views.add_category)
]

