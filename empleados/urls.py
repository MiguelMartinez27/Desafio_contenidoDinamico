from django.urls import path
from . import views

urlpatterns = [
    path("vista/", views.vista_empleados, name="vista_empleados"),
]
