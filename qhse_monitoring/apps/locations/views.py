from django.shortcuts import render

def index(request):
    context = {
        'title': 'Lokasi'
    }

    return render(request, 'locations/index.html', context)
