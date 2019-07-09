from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # External
    path('login/', views.login_view, name="login_view"),
]