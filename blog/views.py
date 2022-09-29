from django.views.generic import ListView
from blog.models import Blog 

class BlogListView(ListView):

    template_name = 'blog/blog_list.html'
    queryset = Blog.objects.all()
    context_object_name = 'blogs'


