from django.shortcuts import render
from .models import Moshina

def index(request):
    malumotlar = Moshina.objects.all()
    gol = {
        'malumotlar': malumotlar
    }

    return render(request, 'index.html', gol)
