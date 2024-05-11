from django.contrib import admin
from .models import Book,Grade,Author
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Grade)
