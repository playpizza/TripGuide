from unicodedata import name
from django.urls import path
from . import views

app_name = "Contents"

urlpatterns = [
    path("list/", views.contents_list, name="list"),
    path("detail/<int:id>/", views.contents_detail, name="detail"),
    path("review/write/", views.contents_write, name="review_write"),
    path("review/delete/", views.contents_delete, name="review_delete"), 
]
