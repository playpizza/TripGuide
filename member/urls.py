from django.urls import path
from . import views

app_name = "Member"

urlpatterns = [
    path("info/detail/<int:user_id>/", views.member_info_detail, name="info_detail"),
    path("info/update/<int:user_id>/", views.member_info_update, name="info_update"),
    path("withdrawal/", views.member_withdrawal, name="withdrawal"), # 탈퇴
]
