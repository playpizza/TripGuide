from django.db import models

class EventBoard(models.Model):
    # 제목
    title = models.CharField(max_length=128)
    # 이미지
    mainphoto = models.FileField(upload_to="EventFiles/", blank=True, null=True)
    # 내용
    contents = models.TextField()
    # 조회수
    view_cnt = models.IntegerField(default=0)
    # 작성일
    reg_date = models.DateTimeField(auto_now_add=True)
    # 만료일
    exp_date = models.DateField()

    class Meta:
        db_table = 'event_board'

    def __str__(self):
        return self.title


class EventDocument(models.Model):
    # 제목
    title = models.CharField(max_length=200)
    # 업로드된 파일
    uploadedFile = models.FileField(upload_to="EventFiles/")
    # 원본파일 이름
    originalName = models.CharField(max_length=200, null=False)
    # 이벤트 글
    eventBoard = models.ForeignKey(EventBoard, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eventfile_board'

    def __str__(self):
        return self.title