from django.core.urlresolvers import resolve
from django.conf import settings

MENU = {
    'mikroblog': {
        'name' : 'blog',
        'title' : 'Mikroblog',
    },
    'home' : {
        'name' : 'home',
        'title' : 'Home',
    },
    'scores' : {
        'name' : '',
        'title' : 'Wyniki',
    },
    'matches' : {
        'name' : 'matches',
        'title': u'Mecze',
    }
}
CHRONOLOGY=('home', 'mikroblog', 'matches', 'scores')

_menu = [ MENU[name] for name in CHRONOLOGY ]

def menu(request):
    url_name = resolve(request.path).url_name
    
    return { 'MENU' : _menu,
            'url_name' : url_name,
            'STATIC_URL' : settings.STATIC_URL,
    }
