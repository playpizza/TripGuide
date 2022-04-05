from django.db import models

class Event(models.Model):
    # 제목
    title = models.CharField(max_length=128)
    # 내용
    contents = models.TextField()
    # 조회수
    view_cnt = models.IntegerField(default=0)
    # 작성일
    reg_date = models.DateTimeField(auto_now_add=True)
    # 만료일
    exp_date = models.DateField()

    def __str__(self):
        return self.title
