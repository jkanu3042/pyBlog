from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings

import os
# Create your views here.


def mysum(request, numbers):
    #request : HttpRequest의 인스턴스
    #추출한 문자 그대로 넘겨주기 때문에 numbers는 문자열로 넘어옴.
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))

    return HttpResponse(result)

def myname(request, name, age):
    #내가 푼것.
    # result = '안녕하세요.'+name+'.'+age+'살이시네요'
    # return HttpResponse(result)

    #해답
    return HttpResponse('안녕하세요.{}.{} 살 이시네요.'.format(name,age) );

def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>Askdjango</h1>
    <p>{name}</p>
    <p>여러분의 아주 찰진</p>
    '''.format(name=name))


def post_list2(request):
    name='공유'
    return render(request, 'dojo/post_list.html',{'name' : name})

def post_list3(request):

    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii':True})

def excel_download(request):
    #filepath = 'C:\\Users\\jungal\\dev\\vod-django\\gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')

    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
