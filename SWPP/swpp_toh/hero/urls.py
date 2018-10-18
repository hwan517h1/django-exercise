from django.urls import path
from .views import hero_list, hero_detail

urlpatterns = [
    path('hero/', hero_list),
    path('hero/<int:hero_id>/', hero_detail),
]
