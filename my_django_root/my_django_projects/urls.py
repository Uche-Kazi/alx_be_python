# my_django_projects/urls.py (the main project's urls.py)
from django.contrib import admin
from django.urls import include, path # Ensure 'include' is imported

urlpatterns = [
    path("books/", include("book_store.urls")), # Add this line
    path("admin/", admin.site.urls),
]