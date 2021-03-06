from django import forms
from .models import Post
from askdjango.widgets.naver_map_point_widget import NaverMapPointWidget

class PostForm(forms.ModelForm):
    #dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width':"100%", 'height':200}))

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width':600, 'height':300}),
        }

