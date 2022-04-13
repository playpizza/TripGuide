from datetime import datetime, timedelta
import os
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from count.models import CountBoard
from add.models import AdBoard
from event.models import EventBoard
from member.models import User
from board.models import Board, Comment
from reviews.models import *
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator

def manage_home(request):
    context = {
        'today_login': 0,
        'user_num': 0,
        'today_contents_view': 0,
        'activation_contents': 0,   # TODO
        'today_board': 0,
        'today_review': 0,
        'today_comment': 0,
        'on_event': 0,
        'today_event_veiw': 0,
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
        context['today_login'] = User.objects.filter(last_login__startswith=timezone.now().date()).count()
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
    context = {
        'onlyReport': 'off',
        'searchWord': '',
        'userData': [],
    }
    if request.method == 'POST':
        context['onlyReport'] = request.POST.get('onlyReport', 'off')
        context['searchWord'] = request.POST['searchWord'].strip()
        searchWord = context['searchWord']
        if context['onlyReport'] == 'off':
            try:
                all_users = User.objects.filter(
                    Q(username__icontains=searchWord) |
                    Q(name__icontains=searchWord) |
                    Q(nickname__icontains=searchWord)
                ).order_by('-date_joined')
            except ObjectDoesNotExist:
                all_users = []
        else:
            try:
                all_users = User.objects.filter(
                    Q(is_banned=1)
                ) & User.objects.filter(
                    Q(username__icontains=searchWord) |
                    Q(name__icontains=searchWord) |
                    Q(nickname__icontains=searchWord)
                ).order_by('-date_joined')
            except ObjectDoesNotExist:
                all_users = []
    else:
        try:
            all_users = User.objects.all().order_by('-date_joined')
        except ObjectDoesNotExist:
            all_users = []
    
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_users, 20)
    users = paginator.get_page(page)

    context['userData'] = users

    return render(request, 'm_user_manage.html', context)


def m_user_detail(request, id):
    context = {
        'ban_end_date': datetime.today().strftime("%Y-%m-%d"),
    }
    u = User.objects.get(id=id)
    writing = Board.objects.filter(writer__id=id)
    comment = Comment.objects.filter(writer__id=id)

    context['u'] = u
    context['writing'] = writing
    context['comment'] = comment

    if request.method == 'POST':
        if request.POST['ban']:
            if u.is_banned == 0:
                u.is_banned = 1
            else:
                u.is_banned = 0
            u.save()

    
    return render(request, 'm_user_detail.html', context)


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
    context = {
        'onlyReport': 'off',
        'searchWord': '',
        'boardData': [],
        'defaultDelete': 0,
    }
    if request.method == 'POST':
        # 삭제
        if request.POST['deleteId'] != 0:
            try:
                targetBoard = Board.objects.get(id=request.POST['deleteId'])
                if targetBoard.upload_files:
                    os.remove(targetBoard.upload_files.path)
                targetBoard.delete()
            except ObjectDoesNotExist:
                pass


        # 검색
        context['searchWord'] = request.POST['searchWord'].strip()
        searchWord = context['searchWord']
        try:
            all_boards = Board.objects.filter(
                Q(writer__name__icontains=searchWord) |
                Q(title__icontains=searchWord)
            ).order_by('-registered_date')
        except ObjectDoesNotExist:
            all_boards = []
    else:
        try:
            all_boards = Board.objects.all().order_by('-registered_date')
        except ObjectDoesNotExist:
            all_boards = []
    
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 20)
    boards = paginator.get_page(page)

    context['boardData'] = boards


    return render(request, 'm_board_manage.html', context)


def m_review_stats(request):
    context = {
        'labelData': [],
        'numData': [],
        # 통계값
        'all_review': 0,
        'today_review': 0,
        # 검색값
        'viewType': 'view_all',
        'startDate': (datetime.today() - timedelta(days=6)).strftime("%Y-%m-%d"),
        'endDate': datetime.today().strftime("%Y-%m-%d"),
        'viewRange': 'view_day',
    }
    # 기본통계
    try:
        context['all_review'] = R_review.objects.count() + H_review.objects.count() + F_review.objects.count() + T_review.objects.count()
    except ObjectDoesNotExist:
        pass
    try:
        context['today_review'] = CountBoard.objects.get(reg_date=datetime.today()).review_cnt
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
    if viewType == 'view_all':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count() + 
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count() + 
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count() + 
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count() + 
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count() + 
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count() + 
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count() + 
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count() + 
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count() + 
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_trip':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(
                        T_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_rest':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(
                        H_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_food':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(
                        R_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)
    elif viewType == 'view_fest':
        while checkDate <= lastDate:
            if viewRange == 'view_day':
                try:
                    context['numData'].append(
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + timedelta(days=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
                except ObjectDoesNotExist:
                    pass
                checkDate += timedelta(days=1)
            elif viewRange == 'view_month':
                checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
                try:
                    context['numData'].append(
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(months=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y-%m"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(months=1)
            elif viewRange == 'view_year':
                checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
                try:
                    context['numData'].append(
                        F_review.objects.filter(
                        reg_date__lt=(checkDate + relativedelta(years=1))
                        ).count()
                        )
                    context['labelData'].append(checkDate.strftime("%Y"))
                except ObjectDoesNotExist:
                    pass
                checkDate += relativedelta(years=1)

    return render(request, 'm_review_stats.html', context)


def m_review_manage(request):
    context = {
        'searchWord': '',
        'reviewData': [],
        'viewType': '',
        'defaultDelete': 0,
    }
    if request.method == 'POST':
        context['onlyReport'] = request.POST.get('onlyReport', 'off')
        context['viewType'] = request.POST['viewType']
        context['searchWord'] = request.POST['searchWord'].strip()
        searchWord = context['searchWord']
        viewType = context['viewType']

        # 삭제
        if request.POST['deleteId'] != 0:
            if viewType == 'T':
                try:
                    targetreview = T_review.objects.get(id=request.POST['deleteId'])
                    targetreview.delete()
                except ObjectDoesNotExist:
                    pass
            elif viewType == 'R':
                try:
                    targetreview = R_review.objects.get(id=request.POST['deleteId'])
                    targetreview.delete()
                except ObjectDoesNotExist:
                    pass
            elif viewType == 'H':
                try:
                    targetreview = H_review.objects.get(id=request.POST['deleteId'])
                    targetreview.delete()
                except ObjectDoesNotExist:
                    pass
            elif viewType == 'F':
                try:
                    targetreview = F_review.objects.get(id=request.POST['deleteId'])
                    targetreview.delete()
                except ObjectDoesNotExist:
                    pass

        # 검색
        if viewType == 'T':
            try:
                all_reviews = T_review.objects.filter(
                    title__icontains=searchWord
                ).order_by('-reg_date')
            except ObjectDoesNotExist:
                all_reviews = []
        elif viewType == 'R':
            try:
                all_reviews = R_review.objects.filter(
                    title__icontains=searchWord
                ).order_by('-reg_date')
            except ObjectDoesNotExist:
                all_reviews = []
        elif viewType == 'H':
            try:
                all_reviews = H_review.objects.filter(
                    title__icontains=searchWord
                ).order_by('-reg_date')
            except ObjectDoesNotExist:
                all_reviews = []
        elif viewType == 'F':
            try:
                all_reviews = F_review.objects.filter(
                    title__icontains=searchWord
                ).order_by('-reg_date')
            except ObjectDoesNotExist:
                all_reviews = []
    else:
        context['viewType'] = 'T'
        try:
            all_reviews = T_review.objects.all().order_by('-reg_date')
        except ObjectDoesNotExist:
            all_reviews = []
    
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_reviews, 20)
    reviews = paginator.get_page(page)

    context['reviewData'] = reviews


    return render(request, 'm_review_manage.html', context)


def m_comment_stats(request):
    context = {
        'labelData': [],
        'numData': [],
        # 통계값
        'all_comment': 0,
        'today_comment': 0,
        # 검색값
        'startDate': (datetime.today() - timedelta(days=6)).strftime("%Y-%m-%d"),
        'endDate': datetime.today().strftime("%Y-%m-%d"),
        'viewRange': 'view_day',
    }
    # 기본통계
    try:
        context['all_comment'] = Comment.objects.count()
    except ObjectDoesNotExist:
        pass
    try:
        context['today_comment'] = CountBoard.objects.get(reg_date=datetime.today()).comment_cnt
    except ObjectDoesNotExist:
        temp = CountBoard()
        temp.save()

    # 차트 조건
    if request.method == 'POST':
        context['startDate'] = request.POST['start_date']
        context['endDate'] = request.POST['end_date']
        context['viewRange'] = request.POST['view_range']
    startDate = context['startDate']
    endDate = context['endDate']
    viewRange = context['viewRange']

    # 차트 데이터
    context['labelData'] = []
    context['numData'] = []
    checkDate = datetime.strptime(startDate,'%Y-%m-%d')
    lastDate = datetime.strptime(endDate,'%Y-%m-%d')
    while checkDate <= lastDate:
        if viewRange == 'view_day':
            try:
                context['numData'].append(Comment.objects.filter(
                    created__lt=(checkDate + timedelta(days=1))
                    ).count())
                context['labelData'].append(checkDate.strftime("%Y-%m-%d"))
            except ObjectDoesNotExist:
                pass
            checkDate += timedelta(days=1)
        elif viewRange == 'view_month':
            checkDate = datetime.strptime(checkDate.strftime("%Y-%m"),'%Y-%m')
            try:
                context['numData'].append(Comment.objects.filter(
                    created__lt=(checkDate + relativedelta(months=1))
                    ).count())
                context['labelData'].append(checkDate.strftime("%Y-%m"))
            except ObjectDoesNotExist:
                pass
            checkDate += relativedelta(months=1)
        elif viewRange == 'view_year':
            checkDate = datetime.strptime(checkDate.strftime("%Y"),'%Y')
            try:
                context['numData'].append(Comment.objects.filter(
                    created__lt=(checkDate + relativedelta(years=1))
                    ).count())
                context['labelData'].append(checkDate.strftime("%Y"))
            except ObjectDoesNotExist:
                pass
            checkDate += relativedelta(years=1)

    return render(request, 'm_comment_stats.html', context)


def m_comment_manage(request):
    context = {
        'onlyReport': 'off',
        'searchWord': '',
        'commentData': [],
        'defaultDelete': 0,
        'defaultReport': 0,
    }
    if request.method == 'POST':
        # 삭제
        if request.POST['deleteId'] != 0:
            try:
                targetComment = Comment.objects.get(id=request.POST['deleteId'])
                targetComment.delete()
            except ObjectDoesNotExist:
                pass


        # 검색
        context['searchWord'] = request.POST['searchWord'].strip()
        searchWord = context['searchWord']
        
        try:
            all_comments = Comment.objects.filter(
                Q(nickname__icontains=searchWord) |
                Q(post__title__icontains=searchWord)
            ).order_by('-created')
        except ObjectDoesNotExist:
            all_comments = []
        
    else:
        try:
            all_comments = Comment.objects.all().order_by('-created')
        except ObjectDoesNotExist:
            all_comments = []
    
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_comments, 20)
    comments = paginator.get_page(page)

    context['commentData'] = comments


    return render(request, 'm_comment_manage.html', context)


def m_event_manage(request):
    context = {

    }
    return render(request, 'm_event_manage.html', context)


def m_event_detail(request, id):
    context = {
        
    }
    return render(request, 'm_event_detail.html', context)


def m_ad_manage(request):
    context = {
        
    }
    return render(request, 'm_ad_manage.html', context)


def m_ad_detail(request, id):
    context = {
        
    }
    return render(request, 'm_ad_detail.html', context)




