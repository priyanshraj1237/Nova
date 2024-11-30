from .import views
from django.urls import path

urlpatterns = [
    
     path('',views.landpage,name="landpage"),  
     path('register/',views.register,name="register"),
     path('signin/',views.signin,name="signin"),
     path('choice/',views.choice,name="choice"),
     path('learning/',views.learning,name="learning"),
]