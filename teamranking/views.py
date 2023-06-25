from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import teamInformation


# Create your views here.

#Current standings of the SGIPC Team using ListView
class Standings(ListView):
    template_name='teamranking/standings.html'
    model=teamInformation
    ordering=['-rating']
    context_object_name='all_teams'
    
    


