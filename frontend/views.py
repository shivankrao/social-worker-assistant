from django.shortcuts import render
from django.views.generic.detail import DetailView

from main.models import Main

def index(request):
    return render(request, 'frontend/index.html')

class MainDetailView(DetailView):
    model = Todo
    template_name = 'frontedn/index.html'
