#  hello/urls.py
from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('inicio', views.inicio_page_view, name='inicio'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('layout', views.layout_page_view, name='layout')

]