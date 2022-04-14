from tabnanny import verbose
from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    r_api_id = models.IntegerField(verbose_name='식당api_id')
    view_cnt = models.PositiveIntegerField(default=0, verbose_name='검색수')

    class Meta:
        db_table = 'restaurant'
        verbose_name = '식당컨텐츠'
        verbose_name_plural = '식당컨텐츠(들)'

    def __str__(self):
        return self.r_api_id

class R_bookmark(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='검색사용자')
    r_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='식당id')

    class Meta:
        db_table = 'r_bookmark'
        verbose_name = '식당북마크'
        verbose_name_plural = '식당북마크(들)'

    def __str__(self):
        return self.text[:20]

class R_tag(models.Model):
    r_tag = models.CharField(max_length=32, verbose_name='태그')
    r_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='식당id')

    class Meta:
        db_table = 'r_tag'
        verbose_name = '식당태그'
        verbose_name_plural = '식당태그(들)'

    def __str__(self):
        return self.text[:20]

class Hotel(models.Model):
    h_api_id = models.IntegerField(verbose_name='숙소api_id')
    view_cnt = models.PositiveIntegerField(default=0, verbose_name='검색수')

    class Meta:
        db_table = 'hotel'
        verbose_name = '숙소컨텐츠'
        verbose_name_plural = '숙소컨텐츠(들)'

    def __str__(self):
        return self.h_api_id

class H_bookmark(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='검색사용자')
    h_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='숙소id')

    class Meta:
        db_table = 'h_bookmark'
        verbose_name = '숙소북마크'
        verbose_name_plural = '숙소북마크(들)'

    def __str__(self):
        return self.text[:20]

class H_tag(models.Model):
    h_tag = models.CharField(max_length=32, verbose_name='태그')
    h_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='숙소id')

    class Meta:
        db_table = 'h_tag'
        verbose_name = '숙소태그'
        verbose_name_plural = '숙소태그(들)'

    def __str__(self):
        return self.text[:20]

class Festival(models.Model):
    f_api_id = models.IntegerField(verbose_name='축제api_id')
    view_cnt = models.PositiveIntegerField(default=0, verbose_name='검색수')

    class Meta:
        db_table = 'festival'
        verbose_name = '축제컨텐츠'
        verbose_name_plural = '축제컨텐츠(들)'

    def __str__(self):
        return self.f_api_id

class F_bookmark(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='검색사용자')
    f_id = models.ForeignKey(Festival, on_delete=models.CASCADE, verbose_name='축제id')

    class Meta:
        db_table = 'f_bookmark'
        verbose_name = '축제북마크'
        verbose_name_plural = '축제북마크(들)'

    def __str__(self):
        return self.text[:20]

class  F_tag(models.Model):
    f_tag = models.CharField(max_length=32, verbose_name='태그')
    f_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='축제id')

    class Meta:
        db_table = 'f_tag'
        verbose_name = '축제태그'
        verbose_name_plural = '축제태그(들)'

    def __str__(self):
        return self.text[:20]

class Travel(models.Model):
    t_api_id = models.IntegerField(verbose_name='여행api_id')
    view_cnt = models.PositiveIntegerField(default=0, verbose_name='검색수')

    class Meta:
        db_table = 'travel'
        verbose_name = '여행컨텐츠'
        verbose_name_plural = '여행컨텐츠(들)'

    def __str__(self):
        return self.t_api_id

class T_bookmark(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='검색사용자')
    t_id = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name='여행id')

    class Meta:
        db_table = 't_bookmark'
        verbose_name = '여행북마크'
        verbose_name_plural = '여행북마크(들)'

    def __str__(self):
        return self.text[:20]

class  T_tag(models.Model):
    t_tag = models.CharField(max_length=32, verbose_name='태그')
    t_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='여행id')

    class Meta:
        db_table = 't_tag'
        verbose_name = '여행태그'
        verbose_name_plural = '여행태그(들)'

    def __str__(self):
        return self.text[:20]

class Content(models.Model):
    title = models.CharField(max_length=100, blank = True, null = True)
    addr1 = models.CharField(max_length=100, blank = True, null = True)
    firstimage = models.CharField(max_length=100, blank = True, null = True)
    mapx = models.CharField(max_length=100, blank = True, null = True)
    mapy = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.title