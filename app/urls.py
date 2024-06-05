from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('<str:short_code>/', views.redirect_to_original, name='redirect'),
]
