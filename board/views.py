from django.shortcuts import render
from django.views.generic import ListView
from .models import Board
from django.contrib import messages
from django.db.models import Q

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
    # TODO
    pass


def board_detail(request, id):
    # TODO
    pass


def board_update(request, id):
    # TODO
    pass


def board_delete(request):
    # TODO
    pass


def board_comment(request): # 댓글달기
    # TODO
    pass


def board_per_page(request):
    # TODO
    pass