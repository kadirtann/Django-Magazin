from django.shortcuts import render

# Create your views here.
def writerdashboard(request):
    return render(request, 'writer-dashboard.html')

def readerdashboard(request):
    return render(request, 'reader-dashboard.html')