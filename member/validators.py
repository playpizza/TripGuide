import string
from django.core.exceptions import ValidationError

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

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (len(password) < 8 or not contains_alphabet(password) or not contains_number(password)):
            raise ValidationError("8자 이상이며 영문 대/소문자, 숫자를 포함해야 합니다.")

    def get_help_text(self):
        return "8자 이상이며 영문 대/소문자, 숫자를 포함해야 합니다."