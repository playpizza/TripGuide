from tabnanny import verbose
from turtle import update
from django.db import models

class R_review(models.Model):
    title = models.CharField(max_length=32, verbose_name='식당후기제목')
    content = models.TextField(verbose_name='식당후기내용')
    grade = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='식당평점') # 소수점 1자리까지 표현
    thumbnail = models.ImageField(blank=True, upload_to="images", null=True, verbose_name='식당썸네일')
    # r_relation_review = models.ManyToManyField('self', verbose_name='관련후기', blank=True)
    # h_relation_review = models.ManyToManyField('H_review', through='Relation_rh', through_fields=('R_review', 'H_review'), verbose_name='관련후기', blank=True)
    # f_relation_review = models.ManyToManyField('F_review', through='Relation_rf', through_fields=('R_review', 'F_review'), verbose_name='관련후기', blank=True)
    # t_relation_review = models.ManyToManyField('T_review', through='Relation_rt', through_fields=('R_review', 'T_review'), verbose_name='관련후기', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='식당후기등록시간')
    up_date = models.DateTimeField(auto_now_add=True, verbose_name='식당후기최신화시간')
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='식당후기작성자')

    class Meta:
        db_table = 'r_review'
        verbose_name = '식당후기'
        verbose_name_plural = '식당후기(들)'

    def __str__(self):
        return self.title

class H_review(models.Model):
    title = models.CharField(max_length=32, verbose_name='숙소후기제목')
    content = models.TextField(verbose_name='숙소후기내용')
    grade = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='숙소평점') # 소수점 1자리까지 표현
    thumbnail = models.ImageField(blank=True, upload_to="images", null=True, verbose_name='숙소썸네일')
    # h_relation_review = models.ManyToManyField('self', verbose_name='관련후기', blank=True)
    # f_relation_review = models.ManyToManyField('F_review', through='Relation_hf', through_fields=('H_review', 'F_review'), verbose_name='관련후기', blank=True)
    # t_relation_review = models.ManyToManyField('T_review', through='Relation_ht', through_fields=('H_review', 'T_review'), verbose_name='관련후기', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='숙소후기등록시간')
    up_date = models.DateTimeField(auto_now_add=True, verbose_name='숙소후기최신화시간')
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='숙소후기작성자')

    class Meta:
        db_table = 'h_review'
        verbose_name = '숙소후기'
        verbose_name_plural = '숙소후기(들)'

    def __str__(self):
        return self.title

class F_review(models.Model):
    title = models.CharField(max_length=32, verbose_name='축제후기제목')
    content = models.TextField(verbose_name='축제후기내용')
    grade = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='축제평점') # 소수점 1자리까지 표현
    thumbnail = models.ImageField(blank=True, upload_to="images", null=True, verbose_name='축제썸네일')
    # f_relation_review = models.ManyToManyField('self', verbose_name='관련후기', blank=True)
    # t_relation_review = models.ManyToManyField('T_review', through='Relation_ft', through_fields=('F_review', 'T_review'), verbose_name='관련후기', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='축제후기등록시간')
    up_date = models.DateTimeField(auto_now_add=True, verbose_name='축제후기최신화시간')
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='축제후기작성자')

    class Meta:
        db_table = 'f_review'
        verbose_name = '축제후기'
        verbose_name_plural = '축제후기(들)'

    def __str__(self):
        return self.title

class T_review(models.Model):
    title = models.CharField(max_length=32, verbose_name='여행후기제목')
    content = models.TextField(verbose_name='여행후기내용')
    grade = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='여행평점') # 소수점 1자리까지 표현
    thumbnail = models.ImageField(blank=True, upload_to="images", null=True, verbose_name='여행썸네일')
    # t_relation_review = models.ManyToManyField('self', verbose_name='관련여행후기', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='여행후기등록시간')
    up_date = models.DateTimeField(auto_now_add=True, verbose_name='여행후기최신화시간')
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='여행후기작성자')

    class Meta:
        db_table = 't_review'
        verbose_name = '여행후기'
        verbose_name_plural = '여행후기(들)'

    def __str__(self):
        return self.title

class R_comment(models.Model):
    # 후기글에 댓글
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기댓글작성자')
    review_comment = models.TextField(verbose_name='후기댓글')
    target = models.ForeignKey(R_review, on_delete=models.CASCADE, verbose_name='후기댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='댓글등록시간')

    def __str__(self):
        return self.text[:20]

class H_comment(models.Model):
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기댓글작성자')
    review_comment = models.TextField(verbose_name='후기댓글')
    target = models.ForeignKey(H_review, on_delete=models.CASCADE, verbose_name='후기댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='댓글등록시간')

    def __str__(self):
        return self.text[:20]

class F_comment(models.Model):
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기댓글작성자')
    review_comment = models.TextField(verbose_name='후기댓글')
    target = models.ForeignKey(F_review, on_delete=models.CASCADE, verbose_name='후기댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='댓글등록시간')

    def __str__(self):
        return self.text[:20]

class T_comment(models.Model):
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기댓글작성자')
    review_comment = models.TextField(verbose_name='후기댓글')
    target = models.ForeignKey(T_review, on_delete=models.CASCADE, verbose_name='후기댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='댓글등록시간')

    def __str__(self):
        return self.text[:20]

class R_reply(models.Model):
    # 대댓글
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기대댓글작성자')
    review_reply = models.TextField(verbose_name='후기대댓글')
    target = models.ForeignKey(R_comment, on_delete=models.CASCADE, verbose_name='대상댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='대댓글등록시간')

    def __str__(self):
        return self.text[:20]

class H_reply(models.Model):
    # 대댓글
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기대댓글작성자')
    review_reply = models.TextField(verbose_name='후기대댓글')
    target = models.ForeignKey(H_comment, on_delete=models.CASCADE, verbose_name='대상댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='대댓글등록시간')

    def __str__(self):
        return self.text[:20]

class F_reply(models.Model):
    # 대댓글
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기대댓글작성자')
    review_reply = models.TextField(verbose_name='후기대댓글')
    target = models.ForeignKey(F_comment, on_delete=models.CASCADE, verbose_name='대상댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='대댓글등록시간')

    def __str__(self):
        return self.text[:20]

class T_reply(models.Model):
    # 대댓글
    writer = models.ForeignKey('member.User', on_delete=models.CASCADE, verbose_name='후기대댓글작성자')
    review_reply = models.TextField(verbose_name='후기대댓글')
    target = models.ForeignKey(T_comment, on_delete=models.CASCADE, verbose_name='대상댓글')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='대댓글등록시간')

    def __str__(self):
        return self.text[:20]