from django.urls import path 
from . import views
urlpatterns = [
  path('login',views.login_page, name = "login"),
  path('register',views.register,name = "register"),
  path('createuser',views.test_user_creation,name = "testing_user"),
]