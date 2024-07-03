from django.shortcuts import render
from .views import *

# Create your views here.
def base(request):
    return render(request, 'Writer/base.html')