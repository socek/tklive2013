# Create your views here.
from django.views.generic.base import TemplateView
from scores.models import Match

class MatchesView(TemplateView):
    template_name = "matches.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MatchesView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['matches'] = Match.objects.order_by('date').all()
        return context
