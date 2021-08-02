from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_date']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'visible','featured', 'status', 'created_date']
    list_editable = ['featured','status', 'visible']

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)


class EmailSendAdmin(admin.ModelAdmin):
    list_display = ['sender_user', 'sender', 'subject', 'send_date']

admin.site.register(EmailSend, EmailSendAdmin)