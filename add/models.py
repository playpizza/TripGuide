from django.db import models

class AdBoard(models.Model):
    # 제목
    title = models.CharField(max_length=128)
    # 이미지
    mainphoto = models.FileField(upload_to="AdFiles/", blank=True, null=True)
    # 이미지 이름
    image_name = models.CharField(max_length=200, null=True)
    # 링크
    link = models.CharField(max_length=128, null=True)
    # 내용
    contents = models.TextField()
    # 조회수
    view_cnt = models.IntegerField(default=0)
    # 작성일
    reg_date = models.DateTimeField(auto_now_add=True)
    # 만료일
    exp_date = models.DateField()

    class Meta:
        db_table = 'ad_board'

    def __str__(self):
        return self.title

