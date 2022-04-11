import os
from django.conf import settings
from django.db import models

class Board(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    upload_files = models.FileField(upload_to="UploadedFiles/", null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'

class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='게시글')
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='댓글작성자')
    content = models.TextField(verbose_name='댓글내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    deleted = models.BooleanField(default=False, verbose_name='삭제여부')
    
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'