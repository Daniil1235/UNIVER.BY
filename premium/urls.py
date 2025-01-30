from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("", views.premium_index, name="premium"),
                  path("pricing", views.pricing, name="pricing"),
                  path("buy", views.premium_buy, name="premium_buy"),
                  path("activate", views.premium_activate, name="premium_activate"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
