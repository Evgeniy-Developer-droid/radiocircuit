from django.contrib import admin
from seo.models import SeoPage, Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'country', 'isp', 'user', 'created',)
    search_fields = ('ip','country',)

admin.site.register(Visitor, VisitorAdmin)


class SeoPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'page',)
    search_fields = ('title','page',)

admin.site.register(SeoPage, SeoPageAdmin)
