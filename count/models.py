from django.db import models
from django.utils.timezone import now
# auto_now_add=True

class CountBoard(models.Model):
    # 기록일
    reg_date = models.DateField(default=now, unique=True)
    # 로그인 횟수
    login_cnt = models.IntegerField(default=0)
    # 회원가입 횟수
    join_cnt = models.IntegerField(default=0)
    # 새 개시글 개수
    board_cnt = models.IntegerField(default=0)
    # 게시글 조회수
    board_view_cnt = models.IntegerField(default=0)
    # 새 댓글 수
    comment_cnt = models.IntegerField(default=0)
    # 여행지 조회수
    trip_view_cnt = models.IntegerField(default=0)
    # 맛집 조회수
    food_view_cnt = models.IntegerField(default=0)
    # 숙소 조회수
    lodging_view_cnt = models.IntegerField(default=0)
    # 축제 조회수
    festival_view_cnt = models.IntegerField(default=0)
    # 리뷰 개수
    review_cnt = models.IntegerField(default=0)
    # 리뷰 조회수
    review_view_cnt = models.IntegerField(default=0)
    # 이벤트 조회수
    event_view_cnt = models.IntegerField(default=0)
    # 광고 조회수
    ad_view_cnt = models.IntegerField(default=0)
    


    class Meta:
        db_table = 'count_board'

    def __str__(self):
        return str(self.reg_date)