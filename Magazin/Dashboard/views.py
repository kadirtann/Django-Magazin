from django.shortcuts import render
from Login.models import * 


# Create your views here.
def writerdashboard(request, slug):
    writer = Writer.objects.get(slug = slug)
    return render(request, 'writer-dashboard.html', {'writer' : writer})

def readerdashboard(request):
    return render(request, 'reader-dashboard.html')

def writer_edit(request, slug):
    writer = Writer.objects.get(slug = slug)
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        biyo = request.POST.get('bio')
        writer.user.first_name = first_name
        writer.user.last_name = last_name
        writer.bio = biyo 
        writer.user.save()
        writer.save()
        return render(request, 'partials/kendini-tanit.html', {'writer' : writer})
    else:
        return render(request, 'partials/edit.html', {'writer' : writer})
 
        


    


