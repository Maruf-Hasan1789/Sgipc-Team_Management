from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import teamInformation


# Create your views here.


class Standings(ListView):
    template_name='teamranking/standings.html'
    model=teamInformation
    ordering=['-rating']
    context_object_name='all_teams'
    
    


