from django.shortcuts import render
from .models import EventBoard, EventDocument
# from django.core.paginator import Paginator

def event_list(request):
    all_events = EventBoard.objects.all().order_by('-id')



    return render(request, 'event_list.html', {'events': all_events})



def event_detail(request, id):
    return render(request, 'event_detail.html')