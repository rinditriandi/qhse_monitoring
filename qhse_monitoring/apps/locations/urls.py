from django.urls import path

from .views import index, add, edit

app_name = 'locations'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
]
