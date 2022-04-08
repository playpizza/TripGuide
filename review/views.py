from django.shortcuts import redirect, render
from .models import F_review, H_review, R_review, T_review
from .forms import ReviewForm
from member.models import User

def review_write(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)  
        if form.is_valid():
            user_id = request.session.get('user') 
            user = User.objects.get(pk=user_id)

            review = R_review()  
            review.title = form.cleaned_data['title']
            review.content = form.cleaned_data['contents']
            review.writer = user
            review.save() 
           
            return redirect('/review/list/')
    else:
        form = ReviewForm()

    return render(request, 'review_write.html', {'form': form})

def review_list(request):
    r_reviews = R_review.objects.all().order_by('-id') 
    h_reviews = H_review.objects.all().order_by('-id') 
    f_reviews = F_review.objects.all().order_by('-id') 
    t_reviews = T_review.objects.all().order_by('-id') 

    return render(request, 'review_list.html', {'r_reviews': r_reviews}, {'h_reviews': h_reviews}, {'f_reviews': f_reviews}, {'t_reviews': t_reviews})

def review_detail(request, pk):  
    r_review = R_review.objects.get(pk=pk)  
    return render(request, 'review_detail.html', {'r_review': r_review})
