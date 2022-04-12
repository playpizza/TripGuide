from django.urls import path
from . import views

app_name = "Manager"

urlpatterns = [
    path("home/", views.manage_home, name="home"), 
    path("user/stats/", views.m_user_stats, name="userStats"), 
    path("user/manage/", views.m_user_manage, name="userManage"), 
    path("user/detail/<int:id>/", views.m_user_detail, name="userDetail"),
    path("contents/stats/", views.m_contents_stats, name="contentsStats"), 
    path("contents/manage/", views.m_contents_manage, name="contentsManage"), 
    path("board/stats/", views.m_board_stats, name="boardStats"), 
    path("board/manage/", views.m_board_manage, name="boardManage"), 
    path("review/stats/", views.m_review_stats, name="reviewStats"), 
    path("review/manage/", views.m_review_manage, name="reviewManage"), 
    path("comment/stats/", views.m_comment_stats, name="commentStats"), 
    path("comment/manage/", views.m_comment_manage, name="commentManage"), 
    path("event/manage/", views.m_event_manage, name="eventManage"), 
    path("event/detail/<int:id>/", views.m_event_detail, name="eventDetail"), 
    path("ad/manage/", views.m_ad_manage, name="adManage"), 
    path("ad/detail/<int:id>/", views.m_ad_detail, name="adDetail"),  
]
