from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_date']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'featured', 'created_date']

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)