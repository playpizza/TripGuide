from django.shortcuts import render
from add.models import AdBoard, AdDocument


def home(request):
    return render(request, 'home.html')
