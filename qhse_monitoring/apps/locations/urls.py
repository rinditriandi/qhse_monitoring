from django.urls import path

from .views import index, add

app_name = 'locations'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
]
