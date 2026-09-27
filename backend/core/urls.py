from django.urls import path
from .views import proj_demo

urlpatterns = [
    path('project-demo/', proj_demo)
]