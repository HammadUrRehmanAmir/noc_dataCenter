from django.shortcuts import render

# Create your views here.
from .models import NOC

def noc_list(request):
    nocs = NOC.objects.all()
    return render(request, 'monitoring/noc_list.html', {'nocs', nocs})

from django.shortcuts import render

def home(request):
    return render(request, 'monitoring/home.html')