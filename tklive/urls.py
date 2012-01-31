from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import main.views as main
import mikroblog.views as mikroblog
import scores.views as scores

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', main.HomeView.as_view(), name='home'),
     url(r'^blog/$', mikroblog.BlogView.as_view(), name='blog'),
     url(r'^matches/$', scores.MatchesView.as_view(), name='matches'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
