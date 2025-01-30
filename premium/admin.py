from django.contrib import admin
from .models import License


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('key', 'plan', 'time_limit')
    list_display_links = ('key',)
    search_fields = ('key',)
    list_filter = ('plan', 'time_limit')


admin.site.register(License, LicenseAdmin)
