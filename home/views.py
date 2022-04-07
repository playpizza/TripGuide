from django.shortcuts import render
# from add.models import AdBoard, AdDocument
from add.models import AdBoard
import random


def home(request):
    adAll = AdBoard.objects.all()
    if adAll:
        ad = random.choice(adAll)
    else: 
        ad = None
    return render(request, 'home.html', {'ad': ad})
