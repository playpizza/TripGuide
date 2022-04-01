from django.urls import path
from . import views

app_name = "Event"

urlpatterns = [
    path("list/", views.event_list, name="list"), 
    path("detail/<int:id>/", views.event_detail, name="detail"), 
]
