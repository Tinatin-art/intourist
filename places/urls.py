from django.urls import path, include
from .views import places

urlpatterns = [
    path('', places, name='places-list')
]