from django.contrib import admin
from .models import Book # Import your Book model

# Define a custom ModelAdmin for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fiels to display in the list view of the admin
    list_display = ('title', 'author', 'published_date')
    # Fields to enable search functionality on
    search_fields = ('title', 'author')
    # You can add more customizations here later, e.g., list_filter, fieldsets


# Register the Book models with its custom ModelAdmin
admin.site.register(Book, BookAdmin)