# -*- encoding: utf-8 -*-
from django.views.generic.base import TemplateView
from scores.models import Match, Tabel, Team, Highscore
from mikroblog.models import Post
from operator import itemgetter
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import resolve
from scores.form import MatchForm
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import Http404

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
        def generate_data(matches):
            teams = {}
            for match in matches:
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
                
            teams_list = [ team for key, team in teams.items() ]
            teams_list.sort( key=itemgetter( 'score', 'matches',)  )
            teams_list.reverse()
            return teams_list
        #####
        context = super(TabelView, self).get_context_data(**kwargs)
        
        tabel = Tabel.objects.get(name='Grupa A')
        matches = Match.objects.order_by('date').filter(tabel=tabel).all()
        context['group_a'] = generate_data(matches)
        
        tabel = Tabel.objects.get(name='Grupa B')
        matches = Match.objects.order_by('date').filter(tabel=tabel).all()
        context['group_b'] = generate_data(matches)
        
        return context

class HighscoreView(TemplateView):
    template_name = "highscore.html"
    
    def get_context_data(self, **kwargs):
        context = super(HighscoreView, self).get_context_data(**kwargs)
        
        teams = {}
        teams_all = Team.objects.all()
        for team in teams_all:
            try:
                place = team.highscore.number
                name = team.name
                teams[place] = name
            except Highscore.DoesNotExist:
                pass
        
        for loop in range(len(teams_all)):
            place = loop + 1
            if not teams.has_key(place):
                teams[place] = ''
        
        context['teams'] = teams
        
        return context

class MatchScoresView(UpdateView):
    template_name = "forms/match.html"
    form_class = MatchForm
    
    @property
    def success_url(self):
        return '/forms/match/' + self.args[0]
    
    def get_context_data(self, **kwargs):
        context = super(MatchScoresView, self).get_context_data(**kwargs)
        match = self.get_object()
        
        context['team_1'] = match.team_1.name
        context['team_2'] = match.team_2.name
        return context
    
    def get_object(self, queryset=None):
        match_id = int(self.args[0])
        return Match.objects.get(id=match_id)

    def form_valid(self, form):
        user = self.request.user
        match = form.instance
        post = Post()
        post.author = user
        post.place = match.place
        txt = u'''Zaktualizowano wynik meczu.<br />
        %(team_1_name)s %(team_1_score)s - %(team_2_name)s %(team_2_score)s<br />
        %(status)s
        '''
        tab = {
            'team_1_name' : match.team_1.name,
            'team_2_name' : match.team_2.name,
            'team_1_score': match.team1_result,
            'team_2_score': match.team2_result,
        }
        if match.staus == 'actual':
            tab['status'] = u'Mecz w trakcie gry.'
        elif match.staus == 'finished':
            tab['status'] = u'Mecz został zakończony.'
        else:
            tab['status'] = ''
        post.text = txt % tab    
        post.save()
        return super(MatchScoresView, self).form_valid(form)
   
    def dispatch(self, *args, **kwargs):
        request = args[0]
        
        if not request.user.has_perm('scores.change_match'):
            raise Http404
        return super(MatchScoresView, self).dispatch(*args, **kwargs)

class MatchesScoresView(TemplateView):
    template_name = "adminmatches.html"

    def get_context_data(self, **kwargs):
        context = super(MatchesScoresView, self).get_context_data(**kwargs)
        context['matches'] = Match.objects.order_by('date').all()
        return context

class MatchView(TemplateView):
    template_name = "match_view.html"
    
    def get_context_data(self, **kwargs):
        context = super(MatchView, self).get_context_data(**kwargs)
        match_id = int(self.args[0])
        match = Match.objects.get(id=match_id)
        context['match'] = match
        return context
