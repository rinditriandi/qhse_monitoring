from django.shortcuts import render

def index(request):
    context = {
        'title': 'Monitoring'
    }

    return render(request, 'monitoring/index.html', context)

def add(request):
    context = {
        'title': 'Tambah Monitoring'
    }

    return render(request, 'monitoring/add.html', context)

def edit(request, id):
    context = {
        'title': 'Edit Monitoring'
    }

    return render(request, 'locations/edit.html', context)

def details(request, id):
    context = {
        'title': 'Detil Monitoring'
    }

    return render(request, 'locations/details.html', context)
