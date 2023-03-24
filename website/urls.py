from django.contrib import admin
from django.urls import path
from website.views import home_view,about_view,contact_view
urlpatterns = [
    path('',home_view),
    path('about',about_view),
    path('contact',contact_view)
]
