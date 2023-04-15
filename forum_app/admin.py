from django import forms
from django.contrib import admin
from forum_app.models import *
from ckeditor.widgets import CKEditorWidget


# ==========================================================================


class MessageFileInline(admin.StackedInline):
    model = MessageFile
    extra = 1


class MessageAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Message
        fields = '__all__'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'chapter', 'creator', 'body', 'created')
    search_fields = ('body',)
    ordering = ('-created',)
    form = MessageAdminForm
    inlines = [MessageFileInline]

admin.site.register(Message, MessageAdmin)

# ==========================================================================

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'chapter', 'creator', 'created')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created',)

admin.site.register(Topic, TopicAdmin)

# ==========================================================================

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created',)

admin.site.register(Chapter, ChapterAdmin)

# ===========================================================================
