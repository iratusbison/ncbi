from django.urls import path
from . import views

urlpatterns = [
    path('mining', views.literature_mining, name='literature_mining'),
]
