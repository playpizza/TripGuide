from django.shortcuts import render
# from add.models import AdBoard, AdDocument
from add.models import AdBoard
from django.core.exceptions import ObjectDoesNotExist
from board.models import Board, Comment

import random


def home(request):
    context = {
        'bestContent': [],
        'bestBoard': [],
        'bestReview': [],
        'ad': None,
    }


    # 게시글
    try:
        bestBoard = Board.objects.all().order_by('-like_count')[:5]
        context['bestBoard'] = bestBoard
    except ObjectDoesNotExist:
        pass




    # 광고
    context['ad'] = getAd()

    context['now'] = 'home'
    


    return render(request, 'home.html', context)

def getAd():
    try:
        adAll = AdBoard.objects.all()
        if adAll:
            ad = random.choice(adAll)
        else:
            ad = ""
    except ObjectDoesNotExist:
        ad = ""
    return ad