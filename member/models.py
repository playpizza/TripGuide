from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_no_special_characters, validate_mobile, validate_gender, validate_age

class User(AbstractUser):
    # username(우리가 흔히 id라고 부르는 것)은 이미 유저모델에 정의되어있음.
    # 근데 어차피 로그인도 이메일로 하기 때문에 쓸 일 없을 것임. 네이버에서도 이건 제공하지 않음.

    # password은 이미 유저모델에 정의되어있음. 소셜 계정에는 비밀번호가 없음.
    
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
    # 주소도 네이버에서 제공해주지 않기 때문에 소셜로그인으로 들어온 사람은 address가 null일 것임.

    mobile = models.CharField(
        max_length=16, 
        unique=True, 
        null=True, 
        error_messages={'unique': '이미 사용중인 핸드폰번호입니다.'},
        validators=[validate_mobile],
        verbose_name="폰번호",
        )
        
    gender = models.CharField(max_length=2, null=True, validators=[validate_gender], verbose_name="성별")
    # M은 남자, W은 여자, U는 확인되지 않음.
    
    age = models.CharField(max_length=4, null=True, validators=[validate_age], verbose_name="나이")
    # 나이는 "문자열" 형태임. int 아님.
    
    is_social_login = models.CharField(max_length=16, null=True, default="default", verbose_name="소셜로그인여부")
    # default이면 일반 사용자, 만약 소셜로그인이면 해당 문자열이 저장됨. e.g. 네이버 소셜로그인이라면 NAVER 저장.

    # date_joined는 이미 유저모델에 정의되어있음.
    
    is_banned = models.IntegerField(default=0, verbose_name="ban여부")
    # 0이면 일반 사용자, 1이면 벤 먹은 사용자

    def __str__(self):
        return self.email