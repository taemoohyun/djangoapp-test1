from django.urls import path

from accountapp.views import hello_world, hello_world_mvt

urlpatterns = [
    path('hello_world/', hello_world),
    path('hello_world_mvt/', hello_world_mvt),
]
