from django.urls import path

from . import views

urlpatterns = [
    path('<int:hero_id>/', views.hero_id, name = 'hero_id'),
    path('<str:name>/', views.hero_name, name = 'hero_name'),
    path('', views.index, name = 'index') 
]
