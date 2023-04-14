from django import forms
from django.contrib import admin
from content_app.models import *
from ckeditor.widgets import CKEditorWidget

# ==========================================================================

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created',)

admin.site.register(Category, CategoryAdmin)

# ===========================================================================
class NewsContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = NewsContent
        fields = '__all__'

class NewsContentInline(admin.StackedInline):
    model = NewsContent
    form = NewsContentAdminForm
    extra = 1
    fields = [("image", "video", "file",),("youtube", "link",), "content"]    


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created',)
    inlines = [NewsContentInline,]

admin.site.register(News, NewsAdmin)
# ==========================================================================

class PostContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = PostContent
        fields = '__all__'

class PostContentInline(admin.StackedInline):
    model = PostContent
    form = PostContentAdminForm
    extra = 1
    fields = [("image", "video", "file",),("youtube", "link",), "content"]   


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'author',)
    ordering = ('-created',)
    inlines = [PostContentInline,]

admin.site.register(Post, PostAdmin)
# ==========================================================================