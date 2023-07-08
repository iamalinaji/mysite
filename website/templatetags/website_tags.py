from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag('website/latest-posts.html')
def latest_posts():
    latest_posts = Post.objects.order_by('-published_date')[:6]
    return {'posts': latest_posts}
