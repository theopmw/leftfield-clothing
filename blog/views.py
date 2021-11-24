from django.views import generic

from .models import Post


# Credit: code for blog views modified from:
# https://djangocentral.com/building-a-blog-application-with-django/
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
