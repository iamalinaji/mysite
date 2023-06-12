from django import template
from blog.models import Post, Category

register = template.Library()


@register.simple_tag(name='totalPosts')
def totalPosts():
    return Post.objects.all.filter(status=1).count()


@register.inclusion_tag('blog/blog-popular-post.html')
def blogPopularPost(arg=3):
    return {'posts': Post.objects.all().filter(status=1).order_by('published_date')[:arg]}


@register.inclusion_tag('blog/blog-category.html')
def blogCategory():
    posts = Post.objects.all().filter(status=1)
    categories = Category.objects.all()
    categoryDict = {}
    for name in categories:
        categoryDict[name] = posts.filter(category=name).count()
    return {'categories': categoryDict}
