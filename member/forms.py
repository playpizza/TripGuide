from django import forms

from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'nickname', 'address', 'mobile', 'gender', 'age']

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.nickname = self.cleaned_data['nickname']
        user.address = self.cleaned_data['address']
        user.mobile = self.cleaned_data['mobile']
        user.gender = self.cleaned_data['gender']
        user.age = self.cleaned_data['age']
        user.save()