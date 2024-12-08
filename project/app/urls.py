from . import views
from django.urls import path

urlpatterns = [
    path('', views.landpage, name="landpage"),  
    path('register/', views.register, name="register"),
    path('signin/', views.signin, name="signin"),
    path('choice/', views.choice, name="choice"),
    path('learning/', views.learning, name="learning"),
    path('learn/', views.learn, name="learn"),
    path('earn/', views.earn, name="earn"),
    path('learning_video/', views.learning_video, name="learning_video"),
    path('courses/', views.courses, name='courses'),
    path('buisness/', views.buisness, name="buisness"),
]
