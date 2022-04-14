from django import forms

class ReviewForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required' : '제목을 입력해주세요'
        },
        max_length=32, label="제목") 
       
    content = forms.CharField(
        error_messages={
            'required' : '내용을 입력해주세요'
        },
        widget=forms.Textarea, label="내용")
    
    grade = forms.IntegerField(
        error_messages={
            'required' : '점수를 입력해주세요'
        },
        label="점수") 
