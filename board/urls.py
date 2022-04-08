from django.urls import path
from . import views

app_name = "Board"

urlpatterns = [
    path('list/', views.BoardListView.as_view(), name='list'),
    path("write/", views.board_write, name="write"),
    path("detail/<int:id>/", views.board_detail, name="detail"),
    path("update/<int:pk>/", views.board_update, name="update"),
    path("delete/", views.board_delete, name="delete"),
    path("comment/", views.board_comment, name="comment"),
    path("per_page/", views.board_per_page, name="per_page"), 
]
