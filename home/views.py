from django.shortcuts import render
# from add.models import AdBoard, AdDocument
from add.models import AdBoard
import random


def home(request):
    adAll = AdBoard.objects.all()
    ad = random.choice(adAll)
    return render(request, 'home.html', {'ad': ad})
