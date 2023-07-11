from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed


app_name = 'blog'
urlpatterns = [
    path('', blog_view, name='home'),
    path('single/', redirect_to_single_default, name='single_default'),
    path('single/<int:post_id>', blog_single, name='single'),
    path('category/<str:category>', blog_category, name='category'),
    path('tag/<str:tag>', blog_tag, name='tag'),
    path('search/', blog_search, name='search'),
    path('test/', test, name='test'),
    path('rss/feed/', LatestEntriesFeed()),
]
