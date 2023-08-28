# gene_sequence_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('gene', views.retrieve_gene_sequences, name='retrieve_gene_sequences'),
]
