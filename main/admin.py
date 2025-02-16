from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Type


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "user_type", "is_staff", "licensed")
    list_filter = ("is_staff", "is_active", "groups", "user_type", "licensed")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name", "email", "photo", "user_type")}),
        ("Лицензия", {"fields": ("licensed", "license_key")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Type)