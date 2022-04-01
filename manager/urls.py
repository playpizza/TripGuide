from django.urls import path
from . import views

app_name = "Manager"

urlpatterns = [
    path("home/", views.manage_home, name="home"), 
]
