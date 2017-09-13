from django.http.response import HttpResponse
from django.views.generic import View,TemplateView

class PostListView1(View):
    def get(self,request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>Askdjango</h1>
        <p>{name}</p>
        <p>여러분의 아주 찰진</p>
        '''

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name']= '공유'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(View):
    pass

class ExcelDownloadView(object):
    pass