from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name='totalPosts')
def totalPosts():
    return Post.objects.all.filter(status=1).count()
