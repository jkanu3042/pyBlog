import re
from django.db import models
from django.forms import ValidationError
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')




class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외') # CharField 길이 제한이 있음.
    content = models.TextField(verbose_name='내용') # TextField 길이 제한이 없는
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='경도,위도 포맷으로 입력',
                              validators=[lnglat_validator],
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 첫 추가시에만 저장
    updated_at = models.DateTimeField(auto_now=True) #갱신이 될 때마다 저장




