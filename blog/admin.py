from django.contrib import admin
## html 태그가 해석되어 나오게끔.
from django.utils.safestring import mark_safe
from .models import Post,Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at']
    actions = ['make_published',]

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))

    #열 이름을 변경.
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        update_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경')
    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경합니다.'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'
                          .format(updated_count))
        #django message framework 사용
    make_published.short_description = '지정 포스팅을 Published 상태로 변경합니다.'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]




# Register your models here.
#admin.site.register(Post, PostAdmin)

