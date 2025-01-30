from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('univeradminby/', admin.site.urls, name='admin'),
    path("", include("main.urls")),
    path("premium/", include("premium.urls")),
]