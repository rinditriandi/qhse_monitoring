from django.urls import path

from .views import index, add, edit, details

app_name = 'locations'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('details/<int:id>/', details, name='details'),
]
