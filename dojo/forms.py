#dojo/forms.py
from django import forms
from .models import Post

# def min_length_3_validator(value):
#     if len(value)<3 :
#         raise forms.ValidationError('3 글자 이상 입력해주세요.')


# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])
#     content = forms.CharField(widget=forms.Textarea)
#
#     def save(self, commit=True):
#         post = Post(**self.cleaned_data)
#         if commit:
#             post.save()
#         return post


#ModelForm을 쓸 것이면, Validator는 model에 정의를 한다.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }


    # ModelForm에 save함수가 아래와 같이 이미 정의되어 있으므로 따로 정의할 필요 없다.
    # def save(self, commit=True):
    #     self.instance = Post(**self.cleaned_data)
    #     if commit:
    #         self.instance.save()
    #     return self.instance