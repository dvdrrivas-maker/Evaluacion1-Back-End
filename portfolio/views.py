from django.shortcuts import render
import datetime

# Create your views here.

# http://127.0.0.1:800/
def raiz(request):
    hora = datetime.datetime.now().hour
    if hora >= 8 and hora < 12:
        mensaje = "Buenos días"
    elif hora >=12 and hora < 20:
        mensaje = "Buenas tardes"
    else:
        mensaje = "Buenas noches"
    return render(request, 'raiz.html', {"mensaje":mensaje})

# http://127.0.0.1:800/projects
def projects(request):
    proyectos = [
        {"title":"Proyecto A", "description":"Desarrollo web con Django",
        "in_progress":True, "image":"images/django_logo.png"},
        {"title":"Proyecto B", "description":"Aplicación móvil con Flutter",
        "in_progress":False, "image":"images/img1.png"},
        {"title":"Proyecto C","description":"Análisis de datos con Python",
        "in_progress":True, "image":"images/python_logo.png"},
        ]
    en_desarrollo = [
        proyecto for proyecto in proyectos
        if proyecto["in_progress"] 
    ]
    return render(request, 'projects.html', {"proyectos":en_desarrollo})

# http://127.0.0.1:800/contact
def contact(request):
    return render(request, 'contact.html')