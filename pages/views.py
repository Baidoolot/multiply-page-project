from django.shortcuts import render
from django.views.generic import ListView
from .models import Images

def home(request):
    return render(request, 'home/home.html')

def about(request):
    with open('pages/about.txt', 'r') as f:
        data = f.read()
    file_data = data
    return render(request, 'home/about.html', {'about_datas': file_data})

def contacts(request):
    with open('pages/contacts.txt', 'r') as f:
        contacts = f.read()
    return render(request, 'home/contacts.html', {'contacts': contacts})

class ImagesView(ListView):
    model = Images
    template_name = 'home/images.html'
    context_object_name = 'images'
