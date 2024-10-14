from django.shortcuts import render


def vista_empleados(request):
    listado = ["Carlos", "Juana", "Florencia", "Roberto", "Jose", "Manuela"]
    context = {"categories": listado}
    return render(request, "empleados/vista.html", context)
