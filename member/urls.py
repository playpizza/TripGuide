from django.urls import path
from . import views

app_name = "Member"

urlpatterns = [
    path("info/detail/<int:user_id>/", views.member_info_detail, name="info_detail"),
    path("info/update/<int:user_id>/", views.member_info_update, name="info_update"),
    path("qusetion/list/", views.member_qusetion_list, name="qusetion_list"), 
    path("qusetion/detail/<int:id>", views.member_qusetion_detail, name="qusetion_detail"), 
    path("qusetion/write/", views.member_qusetion_write, name="qusetion_write"), 
    path("withdrawal/", views.member_withdrawal, name="withdrawal"), # 탈퇴
]
