from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # External
    path('users/', views.index, name="index"),
    path('users/add/', views.add, name='add'),
    path('users/<int:id>/details/', views.details, name='detail'),
    path('users/<int:id>/edit/', views.edit, name='edit'),
    path('users/<int:id>/delete/', views.delete, name='delete'),
    path('users/<int:id>/reset-password/', views.reset_password, name='reset_password')
]