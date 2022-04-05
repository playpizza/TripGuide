from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_field
from allauth.utils import valid_email_or_none

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        name = sociallogin.account.extra_data['name']
        nickname = sociallogin.account.extra_data['nickname']
        email = sociallogin.account.extra_data['email']
        mobile = sociallogin.account.extra_data['mobile']
        gender = sociallogin.account.extra_data['gender']
        age = sociallogin.account.extra_data['age']
        is_social_login = sociallogin.account.provider.upper()

        user = sociallogin.user
        user_email(user, valid_email_or_none(email) or "")
        user_field(user, "name", name or "")
        user_field(user, "nickname", nickname or "")
        user_field(user, "mobile", mobile or "")
        user_field(user, "gender", gender or "U")
        user_field(user, "age", age or "")
        user_field(user, "is_social_login", is_social_login or "")
        
        return user
