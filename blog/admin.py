from .models import Post
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title', 'author', 'counted_views',
                    'status', 'published_date')
    empty_value_display = '-empty'
    list_filter = ('status', )
    search_fields = ['title', 'content']


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'post', 'approved', 'created_date')
    empty_value_display = '-empty'
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
