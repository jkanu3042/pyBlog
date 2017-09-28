"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic import RedirectView

def root(request):
    return redirect('blog:post_list')

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #url(r'^$', root, name='root'),
    #url(r'^$', RedirectView.as_view(pattern_name='blog:post_list')),
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),

    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^shop/', include('accounts.urls', namespace='shop')),

]

#개발 환경에서의 media 파일 서빙을 위한 코드. (static files와 다르게 개발서버에서의 서빙을 미지원하기 때문.
#이렇게 해도 settings.DEBUG = false일 떄는 static이 빈 리스트를 출력함.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#sub_urlconf


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
     url(r'^__debug__/', include(debug_toolbar.urls)),
    ]