from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from count.models import CountBoard
from add.models import AdBoard
from event.models import EventBoard
from member.models import User


def manage_home(request):
    context = {
        'today_login': 0,
        'user_num': 0,
        'today_contents_view': 0,
        'activation_contents': 0,
        'today_board': 0,
        'report_board': 0,
        'today_review': 0,
        'report_review': 0,
        'today_comment': 0,
        'report_comment': 0,
        'on_event': 0,
        'today_event_veiw': 0,
        'today_question': 0,
        'undo_question': 0,
        'on_ad': 0,
        'today_ad_view':0, 
    }
    # CountBoard
    try:
        today_count = CountBoard.objects.get(reg_date=datetime.today())
        context['today_login'] = today_count.login_cnt
        context['today_contents_view'] = today_count.trip_view_cnt + today_count.food_view_cnt + today_count.lodging_view_cnt + today_count.festival_view_cnt
        context['today_board'] = today_count.board_cnt
        context['today_review'] = today_count.review_cnt
        context['today_comment'] = today_count.comment_cnt
        context['today_event_veiw'] = today_count.event_view_cnt
        context['today_ad_view'] = today_count.ad_view_cnt
    except ObjectDoesNotExist:
        pass

    # EventBoard
    try:
        context['on_event'] = EventBoard.objects.filter(exp_date__gte = datetime.today()).count()
    except ObjectDoesNotExist:
        pass
    
    # AdBoard
    try:
        context['on_ad'] = AdBoard.objects.filter(exp_date__gte = datetime.today()).count()
    except ObjectDoesNotExist:
        pass

    # User
    try:
        context['user_num'] = User.objects.all().count()
    except ObjectDoesNotExist:
        pass
    



    return render(request, 'm_home.html', context)


def m_user_stats(request):
    # TODO
    pass


def m_user_manage(request):
    # TODO
    pass


def m_user_detail(request, id):
    # TODO
    pass


def m_contents_stats(request):
    # TODO
    pass


def m_contents_manage(request):
    # TODO
    pass


def m_board_stats(request):
    # TODO
    pass


def m_board_manage(request):
    # TODO
    pass


def m_review_stats(request):
    # TODO
    pass


def m_review_manage(request):
    # TODO
    pass


def m_comment_stats(request):
    # TODO
    pass


def m_comment_manage(request):
    # TODO
    pass


def m_event_manage(request):
    # TODO
    pass


def m_event_detail(request, id):
    # TODO
    pass


def m_ad_manage(request):
    # TODO
    pass


def m_ad_detail(request, id):
    # TODO
    pass


def m_question_manage(request):
    # TODO
    pass


def m_question_detail(request, id):
    # TODO
    pass

