from django.shortcuts import render

# Create your views here.
from .models import NOC

def noc_list(request):
    # Assuming `nocs` is a list of NOC data you want to pass to the template
    nocs = get_nocs()  # Replace with the logic to fetch your NOCs
    return render(request, 'monitoring/noc_list.html', {'nocs': nocs})

from django.shortcuts import render

def home(request):
    return render(request, 'monitoring/home.html')