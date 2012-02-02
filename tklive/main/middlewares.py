from django.core.urlresolvers import resolve
from django.conf import settings

MENU = {
    'mikroblog': {
        'name' : 'blog',
        'title' : 'Mikroblog',
    },
    'scores' : {
        'name' : '',
        'title' : 'Wyniki',
    },
    'matches' : {
        'name' : 'matches',
        'title': u'Mecze',
    },
    'matches_actual' : {
        'name' : 'matches_actual',
        'title': u'Aktualnie grane mecze',
    },
    'tabel' : {
        'name' : 'tabel',
        'title': u'Tabela grup',
    },
    'highscore' : {
        'name' : 'highscore',
        'title': u'Miejsca',
    }
}
CHRONOLOGY=('mikroblog', 'matches', 'matches_actual', 'tabel', 'highscore')

_menu = [ MENU[name] for name in CHRONOLOGY ]

def menu(request):
    url_name = resolve(request.path).url_name
    
    return { 'MENU' : _menu,
            'url_name' : url_name,
            'STATIC_URL' : settings.STATIC_URL,
    }
