from django.urls import path 
from . import views

urlpatterns = [
  path('',views.sellerProfile, name = "sellerProfile"),

]