from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import main.views as main
import mikroblog.views as mikroblog
import scores.views as scores

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', mikroblog.BlogView.as_view(), name='blog'),
    url(r'^matches/$', scores.MatchesView.as_view(), name='matches'),
    url(r'^matches/actual/$', scores.ActualMatchesView.as_view(), name='matches_actual'),
    url(r'^tabel/$', scores.TabelView.as_view(), name='tabel'),
    url(r'^highscore/$', scores.HighscoreView.as_view(), name='highscore'),
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^admin_match/$', scores.MatchesScoresView.as_view(), name='matches_admin'),
    url(r'^forms/match/(\d)/$', scores.MatchScoresView.as_view(), name='form_match'),
)
