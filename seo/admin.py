from django.contrib import admin
from seo.models import SeoPage

class SeoPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'page',)
    search_fields = ('title','page',)

admin.site.register(SeoPage, SeoPageAdmin)
