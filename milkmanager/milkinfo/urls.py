from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('fill_milk/', views.fill_milk, name='fill_milk'),
]
