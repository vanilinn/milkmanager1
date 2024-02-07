# urls.py в вашем приложении
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cisterns'),
]
