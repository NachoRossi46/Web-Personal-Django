from django.shortcuts import render
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects}) # Se pasa el diccionario con los proyectos a la plantilla portfolio.html
