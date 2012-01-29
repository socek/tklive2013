# Create your views here.
# Create your views here.
from django.views.generic import TemplateView
from mikroblog.models import Post

class BlogView(TemplateView):
    template_name = "blog.html"

    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-pub_date').all()
        return context
