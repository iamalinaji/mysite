from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.http import Http404
import datetime


def blog_view(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lt=current_time)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,post_id=1):
    post = get_object_or_404(Post, pk=post_id)
    context={'post':post}
    post.counted_views+=1
    post.save()
    return render(request,'blog/blog-single.html',context)

def test(request):
    posts=Post.objects.filter(status=0)
    context = {'posts': posts}
    return render(request,'blog/test.html',context)
    

# Create your views here.
