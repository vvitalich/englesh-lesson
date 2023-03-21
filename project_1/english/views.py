from django.shortcuts import render
from django.views.generic import ListView
from .models import World

class WorldView(ListView):
    model = World
    template_name = 'index.html'

# Create your views here.
