from datetime import datetime
from django.shortcuts import render
from count.models import CountBoard
from .models import AdBoard
from django.core.exceptions import ObjectDoesNotExist

def add(request, id):
    context = {}

    ad = AdBoard.objects.get(id=id)
    ad.view_cnt += 1
    ad.save()

    try:
        today_view = CountBoard.objects.get(reg_date=datetime.today())
    except ObjectDoesNotExist:
        today_view = CountBoard()
    today_view.ad_view_cnt += 1
    today_view.save()

    context['linkUrl'] = ad.link

    return render(request, 'add.html', context)
