# Create your views here.
from django.views.generic.base import TemplateView
from scores.models import Match, Tabel
from operator import itemgetter

class MatchesView(TemplateView):
    template_name = "matches.html"
    
    def get_context_data(self, **kwargs):
        context = super(MatchesView, self).get_context_data(**kwargs)
        context['matches'] = Match.objects.order_by('date').all()
        return context

class ActualMatchesView(TemplateView):
    template_name = "matches.html"
    
    def get_context_data(self, **kwargs):
        context = super(ActualMatchesView, self).get_context_data(**kwargs)
        context['matches'] = Match.objects.order_by('date').filter(staus='actual').all()
        return context

class TabelView(TemplateView):
    template_name = 'tabel.html'
    
    def get_context_data(self, **kwargs):
        context = super(TabelView, self).get_context_data(**kwargs)
        tabel = Tabel.objects.get(name='Grupa A')
        context['matches'] = Match.objects.order_by('date').filter(tabel=tabel).all()
        
        teams = {}
        for match in context['matches']:
            for team in [match.team_1, match.team_2]:
                if not teams.has_key(team.name):
                    teams[team.name] = {
                        'team': team,
                        'score': 0,
                        'small_score': 0,
                        'matches': 0,
                        'wins': 0,
                    }
                tdata = teams[team.name]
                if match.staus == 'finished':
                    tdata['matches'] += 1
                    score = match.get_team_data(tdata['team'])
                    tdata['small_score'] += score['points']
                    if score['status'] == 'win':
                        tdata['wins'] += 1
                        tdata['score'] += 2
                    elif score['status'] == 'draw':
                        tdata['score'] += 1
            
        context['teams'] = [ team for key, team in teams.items() ]
        itemgetter('matches')
        context['teams'].sort( key=itemgetter( 'score', 'matches',)  )
        context['teams'].reverse()
        return context
