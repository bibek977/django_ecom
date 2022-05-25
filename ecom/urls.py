from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about', views.about,name="about"),
    path('contact', views.contact, name="contact"),
    path('product', views.product, name='product'),
    path('tracker', views.tracker, name='tracker'),
    path('search', views.search, name='search'),
    path('cart', views.cart, name='cart'),
]