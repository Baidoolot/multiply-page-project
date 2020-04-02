from django.urls import path
from . import views
from .views import ImagesView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('images/', ImagesView.as_view(), name='images'),
]