from django.shortcuts import render
from .models import Member
from .utilities import get_tenant
# Create your views here.



def home(request):
    tenant = get_tenant(request)
    # ... otras lógicas ...
    return render(request, 'main/home.html', {'tenant': tenant})
