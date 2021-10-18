from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('info/', views.info, name='info'),
    path('videos/', views.videos, name='videos'),
    path('results/', views.results, name='results'),
    path('author/', views.author, name='author'),
    path('', views.home, name='home'),
]
