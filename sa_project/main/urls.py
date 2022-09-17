from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('favorite', views.favorite),
    path('market', views.market),
    path('orders', views.orders),
    path('sale', views.sale),
    path('login', views.login),
    path('signin', RegisterUser.as_view(), name = 'register'),

]