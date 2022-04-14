from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.review_list, name="r_list"),
    path("write/", views.review_write, name="r_write"),
    path("detail/<int:pk>/", views.review_detail, name="r_detail"),
]
