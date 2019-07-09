from django.urls import path, include

from . import views

app_name = 'apps'

urlpatterns = [
    # namspace urls
    path('', include('qhse_monitoring.apps.users.urls', namespace='users')),
    # path('location/', include('qhse_monitoring.apps.locations.urls', namespace='locatios')),
    # path('project/', include('qhse_monitoring.apps.projects.urls', namespace='projects')),
    # path('monitoring/', include('qhse_monitoring.apps.monitoring.urls', namespace='monitoring')),
]