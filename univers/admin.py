from django.contrib import admin
from .models import Univer, Country, Subject, Direction


class UniverAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website', 'bysite')
    list_display_links = ('name', )
    search_fields = ('name', 'description', 'website')
    list_editable = ('bysite',)
    list_filter = ('country', 'subjects', 'directions')
    filter_horizontal = ('subjects', 'directions')
    fieldsets = (
        (None, {"fields": ("name", "description")}),
        ("Основная информация", {"fields": ("country", "address", "number", "email", "website")}),
        ("Предметы и направления", {"fields": ("subjects", "directions")}),
        (
            "Социальные сети",
            {
                "fields": (
                    "twitter",
                    "facebook",
                    "linkedin",
                    "instagram",
                    "youtube",
                    "telegram"
                ),
            },
        ),
        ("Наши программы", {"fields": ("bysite", )}),
    )


admin.site.register(Univer, UniverAdmin)
admin.site.register(Subject)
admin.site.register(Direction)