from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_no_special_characters

class User(AbstractUser):
    # username은 이미 유저모델에 정의되어있음.
    # password은 이미 유저모델에 정의되어있음.
    
    name = models.CharField(
        max_length=32, 
        null=True,
        validators=[validate_no_special_characters], 
        verbose_name="성명",
        )

    nickname = models.CharField(
        max_length=32, 
        unique=True, 
        null=True, 
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
        validators=[validate_no_special_characters],
        verbose_name="닉네임",
        )
    
    # email은 이미 유저모델에 정의되어있음.
    
    address = models.CharField(
        max_length=256, 
        null=True,
        validators=[validate_no_special_characters], 
        verbose_name="주소"
        )

    mobile = models.CharField(
        max_length=16, 
        unique=True, 
        null=True, 
        error_messages={'unique': '이미 사용중인 핸드폰번호입니다.'},
        verbose_name="폰번호",
        )
        
    gender = models.CharField(max_length=2, null=True, verbose_name="성별")
    age = models.CharField(max_length=8, null=True, verbose_name="연령대")
    is_social_login = models.CharField(max_length=16, null=True, default="default", verbose_name="소셜로그인여부")
    # date_joined는 이미 유저모델에 정의되어있음.
    is_banned = models.IntegerField(default=0, verbose_name="ban여부")

    def __str__(self):
        return self.email