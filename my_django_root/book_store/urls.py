# book_store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]