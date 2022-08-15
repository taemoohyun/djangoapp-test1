from django.urls import path

from accountapp.views import hello_world, hello_world_mvt, test, test2

urlpatterns = [
    path('hello_world/', hello_world),
    path('hello_world_mvt/', hello_world_mvt),
    path('test/',test),
    path('test2/',test2),
]
