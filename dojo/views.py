from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .forms import PostForm
from .models import Post

import os


# Create your views here.


def mysum(request, numbers):
    # request : HttpRequest의 인스턴스
    # 추출한 문자 그대로 넘겨주기 때문에 numbers는 문자열로 넘어옴.
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))

    return HttpResponse(result)


def myname(request, name, age):
    # 내가 푼것.
    # result = '안녕하세요.'+name+'.'+age+'살이시네요'
    # return HttpResponse(result)

    # 해답
    return HttpResponse('안녕하세요.{}.{} 살 이시네요.'.format(name, age));


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>Askdjango</h1>
    <p>{name}</p>
    <p>여러분의 아주 찰진</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬 장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': True})


def excel_download(request):
    # filepath = 'C:\\Users\\jungal\\dev\\vod-django\\gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')

    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법 1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            # 방법 2)
            # post = Post(title=form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # post.save()

            # 방법 3)
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # 방법 4)
            # post = Post(**form.cleaned_data)
            # post.save()
            # 방법 5)
            # post = Post.objects.create(**form.cleaned_data)

            # ip를 받아야하므로 일단 commit을 지연
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')

    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')

    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form
    })
