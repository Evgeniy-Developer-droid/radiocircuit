from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from site_app.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "rang", "is_active", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (("first_name", "last_name",), 
        ("email", "rang",), ("avatar",))}),
        (
            _("Permissions"),
            {
                "fields": (
                    ("is_active", "is_staff", "is_superuser",),
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
