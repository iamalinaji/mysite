from django.contrib import admin
from django.urls import path
from website.views import home_view,about_view,contact_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home_view),
    path('about',about_view),
    path('contact',contact_view)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
