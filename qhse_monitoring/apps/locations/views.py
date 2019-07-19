from django.shortcuts import render

def index(request):
    context = {
        'title': 'Lokasi'
    }

    return render(request, 'locations/index.html', context)

def add(request):
    context = {
        'title': 'Tambah Lokasi'
    }

    return render(request, 'locations/add.html', context)

def edit(request, id):
    context = {
        'title': 'Edit Lokasi'
    }

    return render(request, 'locations/edit.html', context)
