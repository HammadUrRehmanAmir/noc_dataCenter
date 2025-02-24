from django.shortcuts import render

# Create your views here.
from .models import NOC

def noc_list(request):
    nocs = NOC.objects.all()
    return render(request, 'monitoring/noc_list.html', {'nocs', nocs})