from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from count.models import CountBoard
from add.models import AdBoard
from event.models import EventBoard
from member.models import User
from board.models import Board, Comment
from django.db.models import Q


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
    context = {
        'labelData': [],
        'numData': [],
        # 통계값
        'user_num': 0,
        'ban_users': 0,
        'today_login': 0,
        # 검색값
        'viewType': 'view_user',
        'startDate': (datetime.today() - timedelta(days=6)).strftime("%Y-%m-%d"),
        'endDate': datetime.today().strftime("%Y-%m-%d"),
        'viewRange': 'view_day',
    }
    # 기본통계
    try:
        context['user_num'] = User.objects.count()
        context['ban_users'] = User.objects.filter(is_banned=1).count()
    except ObjectDoesNotExist:
        pass
    try:
        context['today_login'] = CountBoard.objects.get(reg_date=datetime.today()).login_cnt
    except ObjectDoesNotExist:
        temp = CountBoard()
        temp.save()

    # 차트 조건
    if request.method == 'POST':
        context['viewType'] = request.POST['view_type']
        context['startDate'] = request.POST['start_date']
        context['endDate'] = request.POST['end_date']
        context['viewRange'] = request.POST['view_range']
    viewType = context['viewType']
    startDate = context['startDate']
    endDate = context['endDate']
    viewRange = context['viewRange']

    # 차트 데이터
    context['labelData'] = []
    context['numData'] = []
    checkDate = datetime.strptime(startDate,'%Y-%m-%d')
    lastDate = datetime.strptime(endDate,'%Y-%m-%d')
    if viewType == 'view_user':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(User.objects.filter(
                        date_joined__lt=(checkDate + timedelta(days=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(User.objects.filter(
                        date_joined__lt=(checkDate + relativedelta(months=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(User.objects.filter(
                        date_joined__lt=(checkDate + relativedelta(years=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_login':
        while checkDate <= lastDate:
            checkExist = True
            if viewRange == 'view_day':
                try:
                    context['numData'].append(CountBoard.objects.get(
                        reg_date=checkDate
                        ).login_cnt)
                except ObjectDoesNotExist:
                    context['numData'].append(0)
                context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                try:
                    temp = CountBoard.objects.filter(
                        Q(reg_date__year=checkDate.strftime("%Y")) &
                        Q(reg_date__month=checkDate.strftime("%m"))
                        )
                    tempSum = 0
                    for i in temp:
                        tempSum += i.login_cnt
                    context['numData'].append(tempSum)
                    checkExist = False
                except ObjectDoesNotExist:
                    pass
                context['labelData'].append(checkDate.strftime("%Y-%m"))
                if checkExist:
                    context['numData'].append(0)
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                try:
                    temp = CountBoard.objects.filter(
                        Q(reg_date__year=checkDate.strftime("%Y"))
                        )
                    tempSum = 0
                    for i in temp:
                        tempSum += i.login_cnt
                    context['numData'].append(tempSum)
                    checkExist = False
                except ObjectDoesNotExist:
                    pass
                context['labelData'].append(checkDate.strftime("%Y"))
                if checkExist:
                    context['numData'].append(0)
                checkDate += relativedelta(years=1)

    return render(request, 'm_user_stats.html', context)





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
    context = {
        'labelData': [],
        'numData': [],
        # 통계값
        'all_board': 0,
        'today_board': 0,
        'today_view': 0,
        # 검색값
        'viewType': 'view_board',
        'startDate': (datetime.today() - timedelta(days=6)).strftime("%Y-%m-%d"),
        'endDate': datetime.today().strftime("%Y-%m-%d"),
        'viewRange': 'view_day',
    }
    # 기본통계
    try:
        context['all_board'] = Board.objects.count()
    except ObjectDoesNotExist:
        pass
    try:
        context['today_board'] = CountBoard.objects.get(reg_date=datetime.today()).board_cnt
        context['today_view'] = CountBoard.objects.get(reg_date=datetime.today()).board_view_cnt
    except ObjectDoesNotExist:
        temp = CountBoard()
        temp.save()

    # 차트 조건
    if request.method == 'POST':
        context['viewType'] = request.POST['view_type']
        context['startDate'] = request.POST['start_date']
        context['endDate'] = request.POST['end_date']
        context['viewRange'] = request.POST['view_range']
    viewType = context['viewType']
    startDate = context['startDate']
    endDate = context['endDate']
    viewRange = context['viewRange']

    # 차트 데이터
    context['labelData'] = []
    context['numData'] = []
    checkDate = datetime.strptime(startDate,'%Y-%m-%d')
    lastDate = datetime.strptime(endDate,'%Y-%m-%d')
    if viewType == 'view_board':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(Board.objects.filter(
                        registered_date__lt=(checkDate + timedelta(days=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(Board.objects.filter(
                        registered_date__lt=(checkDate + relativedelta(months=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(Board.objects.filter(
                        registered_date__lt=(checkDate + relativedelta(years=1))
                        ).count())
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_cnt':
        while checkDate <= lastDate:
            checkExist = True
            if viewRange == 'view_day':
                try:
                    context['numData'].append(CountBoard.objects.get(
                        reg_date=checkDate
                        ).board_view_cnt)
                except ObjectDoesNotExist:
                    context['numData'].append(0)
                context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                try:
                    temp = CountBoard.objects.filter(
                        Q(reg_date__year=checkDate.strftime("%Y")) &
                        Q(reg_date__month=checkDate.strftime("%m"))
                        )
                    tempSum = 0
                    for i in temp:
                        tempSum += i.board_view_cnt
                    context['numData'].append(tempSum)
                    checkExist = False
                except ObjectDoesNotExist:
                    pass
                context['labelData'].append(checkDate.strftime("%Y-%m"))
                if checkExist:
                    context['numData'].append(0)
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                try:
                    temp = CountBoard.objects.filter(
                        Q(reg_date__year=checkDate.strftime("%Y"))
                        )
                    tempSum = 0
                    for i in temp:
                        tempSum += i.board_view_cnt
                    context['numData'].append(tempSum)
                    checkExist = False
                except ObjectDoesNotExist:
                    pass
                context['labelData'].append(checkDate.strftime("%Y"))
                if checkExist:
                    context['numData'].append(0)
                checkDate += relativedelta(years=1)

    return render(request, 'm_board_stats.html', context)
    


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

