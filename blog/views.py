from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.http import Http404
import datetime
from django.shortcuts import redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_view(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lt=current_time)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def redirect_to_single_default(request):
    return redirect('blog:single', post_id=1)


def blog_single(request, post_id):
    current_time = timezone.now()
    post = get_object_or_404(Post, pk=post_id, published_date__lt=current_time)
    next_post = Post.objects.filter(
        published_date__gt=post.published_date).order_by('published_date').first()
    previous_post = Post.objects.filter(
        published_date__lt=post.published_date).order_by('-published_date').first()
    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
    }
    post.counted_views += 1
    post.save()
    return render(request, 'blog/blog-single.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(category__name=category)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lt=current_time)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test(request):
    posts = Post.objects.filter(status=0)
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)
