from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^addproduct$', views.addproduct),
    url(r'^productsuccess$', views.productsuccess),
]
