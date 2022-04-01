from django.urls import path
from . import views

app_name = "Member"

urlpatterns = [
    path("login/", views.member_login, name="login"), 
    path("loginOK/", views.member_loginOK, name="loginOK"), 
    path("logout/", views.member_logout, name="logout"), 
    path("join/", views.member_join, name="join"), 
    path("joinOK/", views.member_joinOK, name="joinOK"), 
    path("info/detail/", views.member_info_detail, name="info_detail"),
    path("info/update/", views.member_info_update, name="info_update"),
    path("qusetion/list/", views.member_qusetion_list, name="qusetion_list"), 
    path("qusetion/detail/<int:id>", views.member_qusetion_detail, name="qusetion_detail"), 
    path("qusetion/write/", views.member_qusetion_write, name="qusetion_write"), 
    path("withdrawal/", views.member_withdrawal, name="withdrawal"), # 탈퇴
]
