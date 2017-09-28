from django.views.generic import CreateView
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class= PostForm
    #success_url = '//'
    #success_url이 제공되어있지 않다.
    #models.py에 get_absolute_url이 구현되어 있으므로 자동으로 detailview로 이동한다.

post_new = PostCreateView.as_view()