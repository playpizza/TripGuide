from django.urls import path
from . import views

app_name = "Board"

urlpatterns = [
    path("board/list/", views.board_list, name="list"),
    path("board/write/", views.board_write, name="write"),
    path("board/detail/<int:id>/", views.board_detail, name="detail"),
    path("board/update/<int:pk>/", views.board_update, name="update"),
    path("board/delete/", views.board_delete, name="delete"),
    path("board/comment/", views.board_comment, name="comment"),
    path("board/per_page/", views.board_per_page, name="per_page"), 
]
