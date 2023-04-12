from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
import datetime


def blog_view(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__gt=current_time)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,post_id=1):
    post = Post.objects.get(id=post_id)
    published_date = post.published_date
    date = published_date.date()
    formatted_date = date.strftime('%B, %d, %Y')
    context={'post':post,'date':formatted_date}
    post.counted_views+=1
    post.save()
    return render(request,'blog/blog-single.html',context)



def test(request):
    posts=Post.objects.filter(status=0)
    context = {'posts': posts}
    return render(request,'blog/test.html',context)
    

# Create your views here.
