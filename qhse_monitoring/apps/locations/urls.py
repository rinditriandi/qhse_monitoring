from django.urls import path

from .views import index

app_name = 'locations'

urlpatterns = [
    path('', index, name='locations'),
]
