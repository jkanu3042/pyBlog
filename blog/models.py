import re
from django.db import models
from django import forms
from django.forms import ValidationError
from django.conf import settings

from django.core.urlresolvers import reverse


from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        return ValidationError('Invalid LngLat Type')

def min_length_3_validator(value):
    if len(value) < 3 :
        raise forms.ValidationError('3 글자 이상 입력해주세요.')



class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw'),
    )


    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외',
                             validators=[min_length_3_validator]) # CharField 길이 제한이 있음.
    content = models.TextField(verbose_name='내용') # TextField 길이 제한이 없는


    #디렉터리에 저장 할 때
    #photo = models.ImageField(blank=True, upload_to='blog/post')
    #시간대별로 저장 할 때
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    photo_thumbnail =ImageSpecField(source='photo',
                                    processors=[Thumbnail(300,300)],
                                    format='JPEG',
                                    options = {'quality':60})


    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='경도,위도 포맷으로 입력',
                              validators=[lnglat_validator],
                              blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 첫 추가시에만 저장
    updated_at = models.DateTimeField(auto_now=True) #갱신이 될 때마다 저장

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    class Meta:
        ordering = ['-id']



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Comment(models.Model):
    post = models.ForeignKey(Post) #post_id 생성
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


