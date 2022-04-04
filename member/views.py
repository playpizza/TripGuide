from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('home')

def member_login(request):
    # TODO
    pass


def member_loginOK(request):
    # TODO
    pass


def member_logout(request):
    # TODO
    pass


def member_join(request):
    # TODO
    pass


def member_joinOK(request):
    # TODO
    pass


def member_info_detail(request):
    # TODO
    pass


def member_info_update(request):
    # TODO
    pass


def member_qusetion_list(request):
    # TODO
    pass


def member_qusetion_detail(request, id):
    # TODO
    pass


def member_qusetion_write(request):
    # TODO
    pass


def member_withdrawal(request):
    # TODO
    pass



