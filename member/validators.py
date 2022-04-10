import string
from django.core.exceptions import ValidationError
import re

# 특수문자가 있는지 확인
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")

# 영문자 있는지 확인
def contains_alphabet(value):
    for char in value:
        if char.isalpha():
            return True
    return False

# 숫자가 있는지 확인
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False

# 핸드폰 번호 폼에 맞는지 확인
def is_mobile(value):
    mobile_regex = re.compile(r"^(01)\d{1}-\d{3,4}-\d{4}$")
    return mobile_regex.search(value)

# 핸드폰 번호 정규식 통과해야 함
def validate_mobile(value):
    if not is_mobile(value):
        raise ValidationError("휴대폰 번호를 제대로 입력해주세요. (-까지 입력)")

# 성별은 M이나 W이나 U값만을 가져야 함
def validate_gender(value):
    if not(value.upper() == 'M' or value.upper() == 'W' or value.upper() == 'U'):
        raise ValidationError("올바른 성별을 입력해주세요. (M or W or U)") 

# 말도 안 되는 나이를 입력하지 않아야 함
def validate_age(value):
    try:
        if int(value) < 1 or int(value) > 150:
            raise ValidationError("나이를 제대로 입력해주세요.")
    except:
        raise ValidationError("숫자만 입력해주세요.")



class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (len(password) < 8 or not contains_alphabet(password) or not contains_number(password)):
            raise ValidationError("8자 이상이며 영문, 숫자를 포함해야 합니다.")

    def get_help_text(self):
        return "8자 이상이며 영문, 숫자를 포함해야 합니다."