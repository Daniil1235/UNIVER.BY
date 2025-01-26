from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('univeradmin/', admin.site.urls),
    path("", include("main.urls")),
]