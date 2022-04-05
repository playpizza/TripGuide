from django.db import models

class AdBoard(models.Model):
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

    class Meta:
        db_table = 'ad_board'

    def __str__(self):
        return self.title


class AdDocument(models.Model):
    # 제목
    title = models.CharField(max_length=200)
    # 업로드된 파일
    uploadedFile = models.FileField(upload_to="AdFiles/")
    # 원본파일 이름
    originalName = models.CharField(max_length=200, null=False)
    # 이벤트 글
    adBoard = models.ForeignKey(AdBoard, on_delete=models.CASCADE)

    class Meta:
        db_table = 'adfile_board'
    
    def __str__(self):
        return self.title