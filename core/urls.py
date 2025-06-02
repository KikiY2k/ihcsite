from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('definicao/<int:id>/', views.detail, name='detail'),
    path('sobre/', views.about, name='about'),
    path('definicoes/', views.terms, name='terms'),
    path('referencias/', views.references, name='references'),
]