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
        'title': u'Ranking',
    }
}

ADMIN_MENU = {
    'matches_admin' : {
        'name' : 'matches_admin',
        'title': u'Mecze',
    }
}
CHRONOLOGY=('mikroblog', 'matches', 'matches_actual', 'tabel', 'highscore')
ADMIN_CHRONOLOGY=('matches_admin', )

_menu = [ MENU[name] for name in CHRONOLOGY ]
_admin_menu = [ ADMIN_MENU[name] for name in ADMIN_CHRONOLOGY ]

def menu(request):
    url_name = resolve(request.path).url_name
    
    return { 'MENU' : _menu,
            'ADMIN_MENU' : _admin_menu,
            'url_name' : url_name,
            'STATIC_URL' : settings.STATIC_URL,
            'request' : request,
    }
