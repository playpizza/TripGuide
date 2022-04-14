from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from .models import EventBoard, EventDocument
from home.views import getAd
from count.models import CountBoard
from django.core.exceptions import ObjectDoesNotExist
# from django.core.paginator import Paginator

def event_list(request):
    context = {}
    all_events = EventBoard.objects.all().order_by('-id')
    context['events'] = all_events
    context['ad'] = getAd()
    context['now'] = 'event'
    return render(request, 'event_list.html', context)



def event_detail(request, id):
    context = {}
    try:
        event = EventBoard.objects.get(id=id)

        event.view_cnt += 1
        event.save()

        try:
            today_view = CountBoard.objects.get(reg_date=datetime.today())
        except ObjectDoesNotExist:
            today_view = CountBoard()
        today_view.event_view_cnt += 1
        today_view.save()

    except EventBoard.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    
    context['event'] = event
    context['ad'] = getAd()
    context['now'] = 'event'

    return render(request, 'event_detail.html', context)