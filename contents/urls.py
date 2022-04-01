from django.urls import path
from . import views

app_name = "Contents"

urlpatterns = [
    path("list/", views.contents_list, name="list"),
]
