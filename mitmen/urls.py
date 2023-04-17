from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('contact',views.contact),
    path('ai/',views.ai),
    path('web-development/',views.webDevelopment),
    path('digital-marketing/',views.digitalMarketing),
]
