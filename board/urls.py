from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Board"

urlpatterns = [
    path('list/', views.BoardListView.as_view(), name='list'),
    path("write/", views.board_write, name="write"),
    path("detail/<int:id>/", views.board_detail, name="detail"),
    path("update/<int:id>/", views.board_update, name="update"),
    path("delete/", views.board_delete, name="delete"),
    path('comment/write/', views.comment_write, name='comment_write'),
    path('<int:id>/comment/delete/', views.board_comment_delete, name='comment_delete'),
    path('like_count/', views.like_count, name="like_count"),
]

urlpatterns += static(
    settings.MEDIA_URL, 
    document_root = settings.MEDIA_ROOT
)