from django.contrib import admin
from content_app.models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    search_fields = ('title',)
    ordering = ('-created',)

    class Media:
        js = ('content_admin.js',)    
        css = {
             'all': ('content_admin.css',)
        }

admin.site.register(News, NewsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    search_fields = ('title', 'author',)
    ordering = ('-created',)

admin.site.register(Post, PostAdmin)
