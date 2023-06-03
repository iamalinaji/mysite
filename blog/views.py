from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.http import Http404
import datetime
from django.shortcuts import redirect


def blog_view(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lt=current_time)
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


def test(request):
    posts = Post.objects.filter(status=0)
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)
