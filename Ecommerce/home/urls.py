from django.urls import path
from home import views

urlpatterns = [
    path('',views.homePage, name = 'home'),
    path('profile',views.user_profile, name = 'profile'),
]