from django.conf.urls import url
from . import views
from . import views_cbv


urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),


    # url(r'^sum/(?P<x>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum)
    # 하나로 많은 숫자들을 처리해보고 싶다면?
    # -> [\d/]를 붙여준다.
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,3})/(?P<age>\d{1,2})/$', views.myname),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),


    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    # url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^cbv/excel/$', views_cbv.excel_download),

]