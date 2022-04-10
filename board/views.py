import os
from django.shortcuts import render
from django.views.generic import ListView
from .models import Board
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
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
                    search_board_list = board_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword) | Q (writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_board_list = board_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
                elif search_type == 'title':
                    search_board_list = board_list.filter(title__icontains=search_keyword)    
                elif search_type == 'content':
                    search_board_list = board_list.filter(content__icontains=search_keyword)    
                elif search_type == 'writer':
                    search_board_list = board_list.filter(writer__user_id__icontains=search_keyword)

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

        return context



def board_write(request):
    if request.method == 'GET':
        return render(request, './write.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.user

        if request.FILES:
            upload_files = request.FILES["upload_files"]
            board = Board(
                title = title,
                content = content,
                writer = user_id,
                upload_files = upload_files,
                filename = upload_files.name,
            )
        else:
            board = Board(
                title = title,
                content = content,
                writer = user_id,
            )

        board.save()

        return render(request, './writeOk.html', {'board': board})



def board_detail(request, id):
    try:
        board = Board.objects.get(id=id)

        board.hits += 1
        board.save()
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')

    return render(request, './detail.html', {'board': board})



def board_update(request, pk):
    if request.method == "GET":
        try:
            board = Board.objects.get(id=pk)
        except Board.DoesNotExist:
            raise Http404('게시글을 찾을수 없습니다')

        return render(request, './update.html', {'board': board})
    
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.user

        if request.FILES:
            board = Board.objects.get(id=pk)
            upload_files = request.FILES["upload_files"]
            board.title = title
            board.content = content
            board.write = user_id
            board.upload_files = upload_files
            board.filename = upload_files.name
        else:
            board = Board.objects.get(id=pk)
            board.title = title
            board.content = content
            board.write = user_id

        board.save()

        return render(request, './updateOk.html', {'board': board})


def board_delete(request):
    if request.method == "POST":
        id = request.POST['id']
        board = Board.objects.get(id=id)
        board.delete()

        return render(request, './deleteOK.html')

def board_comment(request): # 댓글달기
    # TODO
    pass


def board_per_page(request):
    # TODO
    pass