from asyncio.windows_events import NULL
import os
import json
from django.urls import reverse_lazy
from .models import Board
from .models import Comment
from count.models import CountBoard
from home.views import getAd
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.conf import settings

class BoardListView(ListView):
    model = Board
    paginate_by = 10
    template_name = './list.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        board_list = Board.objects.order_by('-id') 
        
        if search_keyword :
            if len(search_keyword) > 1 :
                if search_type == 'all':
                    search_board_list = board_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword) | Q (nickname__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_board_list = board_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
                elif search_type == 'title':
                    search_board_list = board_list.filter(title__icontains=search_keyword)    
                elif search_type == 'content':
                    search_board_list = board_list.filter(content__icontains=search_keyword)    
                elif search_type == 'nickname':
                    search_board_list = board_list.filter(nickname__icontains=search_keyword)

                return search_board_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return board_list


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1 :
            context['q'] = search_keyword

        context['type'] = search_type
        context['ad'] = getAd()

        return context



def board_write(request):
    if request.method == 'GET':
        return render(request, './write.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.user
        nickname = request.user.nickname

        if request.FILES:
            upload_files = request.FILES["upload_files"]
            board = Board(
                title = title,
                content = content,
                writer = user_id,
                nickname = nickname,
                upload_files = upload_files,
                filename = upload_files.name,
            )
        else:
            board = Board(
                title = title,
                content = content,
                writer = user_id,
                nickname = nickname,
            )
        count = CountBoard.objects.get()
        count.board_cnt += 1

        board.save()
        count.save()

        return render(request, './writeOk.html', {'board': board})



def board_detail(request, id):
    try:
        board = Board.objects.get(id=id)
        comment_list = Comment.objects.order_by('-id')

        board.save()

        context = {
            'board': board,
            'comments': comment_list,
            'ad': getAd(),
        }
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')

    return render(request, './detail.html', context)



def board_update(request, id):
    if request.method == "GET":
        try:
            board = Board.objects.get(id=id)
        except Board.DoesNotExist:
            raise Http404('게시글을 찾을수 없습니다')

        return render(request, './update.html', {'board': board})
    
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.user
        board = Board.objects.get(id=id)

        if board.upload_files:
            if request.FILES:
                os.remove(board.upload_files.path)
                upload_files = request.FILES["upload_files"]
                board.upload_files = upload_files
                board.filename = upload_files.name
            else:
                os.remove(board.upload_files.path)
                board.upload_files = ''
                board.filename = ''
        else:
            if request.FILES:
                upload_files = request.FILES["upload_files"]
                board.upload_files = upload_files
                board.filename = upload_files.name


        board.title = title
        board.content = content
        board.write = user_id

        board.save()

        return render(request, './updateOk.html', {'board': board})


def board_delete(request):
    if request.method == "POST":
        id = request.POST['b_id']
        board = Board.objects.get(id=id)
        if board.upload_files:
            os.remove(board.upload_files.path)
        board.delete()

        count = CountBoard.objects.get()
        count.board_cnt -= 1
        count.save()

        return render(request, './b_deleteOK.html')

def comment_write(request):
    if request.method == 'POST':
        content = request.POST['content']
        id = request.POST['board_id']
        post = get_object_or_404(Board, id=id)
        user_id = request.user
        nickname = request.user.nickname
        board = Board.objects.get(id=id)

        comment = Comment(
                post = post,
                content = content,
                writer = user_id,
                nickname = nickname,
            )
        
        count = CountBoard.objects.get()
        count.comment_cnt += 1

        count.save()
        comment.save()

        return render(request, './commentOk.html', {'board': board})


def board_comment_delete(request):
    if request.method == "POST":
        c_id = request.POST['c_id']
        b_id = request.POST['b_id']
        comment = Comment.objects.get(id=c_id)
        board = Board.objects.get(id=b_id)
        comment.delete()

        count = CountBoard.objects.get()
        count.comment_cnt -= 1
        
        count.save()

        return render(request, './c_deleteOK.html', {'board': board})



def like_count(request):
    count_like = Board_hits.objects.get()
    id = request.POST['board_id']
    board = Board.objects.get(id=id)

    

    board.like_count += 1
    board.save()

    return redirect('Board:detail', id)