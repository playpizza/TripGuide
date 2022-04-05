from django.http import Http404
from django.shortcuts import render
from .models import EventBoard, EventDocument
# from django.core.paginator import Paginator

def event_list(request):
    all_events = EventBoard.objects.all().order_by('-id')
    return render(request, 'event_list.html', {'events': all_events})



def event_detail(request, id):
    try:
        event = EventBoard.objects.get(id=id)
    except EventBoard.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'event_detail.html', {'event': event})