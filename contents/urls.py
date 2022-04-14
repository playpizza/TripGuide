from unicodedata import name
from django.urls import path
from . import views

app_name = "Contents"

urlpatterns = [
    path("list/", views.get_contents, name="get_contents"),
    path("detail/<int:id>/", views.content_detail, name="detail"),
    # path("review/write/", views.contents_write, name="review_write"),
    # path("review/delete/", views.contents_delete, name="review_delete"), 
]
