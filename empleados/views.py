from django.shortcuts import render


def vista_empleados(request):
    return render(request, "empleados/vista.html")
