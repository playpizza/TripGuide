from django.shortcuts import render
from django.urls import reverse
from .forms import UpdateForm
from allauth.account.views import PasswordChangeView
from .models import User
from django.http import Http404

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('home')

def member_info_detail(request, user_id):
    try:
        profile_user = User.objects.get(pk=user_id)
        this_user = User.objects.get(email=request.user)
    except:
        raise Http404("잘못된 접근입니다.")
    if profile_user.id == this_user.id:
        return render(request, 'info/detail.html', {'profile_user': profile_user})
    else:
        raise Http404("잘못된 접근입니다.")



def member_info_update(request, user_id):
    if request.method == "GET":
        try:
            profile_user = User.objects.get(pk=user_id)
            this_user = User.objects.get(email=request.user)
        except:
            raise Http404("잘못된 접근입니다.")
        if profile_user.id == this_user.id:
            form = UpdateForm(instance=profile_user)
            return render(request, 'info/update.html', {'profile_user': profile_user, "form": form})
        else:
            raise Http404("잘못된 접근입니다.")
    
    elif request.method == "POST":
        try:
            profile_user = User.objects.get(pk=user_id)
        except:
            raise Http404("잘못된 접근입니다.")
        form = UpdateForm(request.POST, instance=profile_user)

        if form.is_valid():      
            profile_user = form.save()
            return render(request, 'info/updateOk.html', {"pk": profile_user.id})

        return render(request, 'info/update.html', {'profile_user': profile_user, "form": form})

def member_withdrawal(request):
    if request.method == "POST":
        id = request.POST['id']
        profile_user = User.objects.get(id=id)
        profile_user.delete()

        return render(request, 'info/deleteOk.html')


