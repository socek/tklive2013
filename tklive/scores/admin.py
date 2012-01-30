
from django.contrib import admin
import scores.models as M

class PlayerInline(admin.TabularInline):
    model = M.Player
    extra = 1
    fields = ['number', 'name', 'surname', 'staus']

class MatchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['match_number', 'place', 'team_1', 'team_2', 'tabel']}),
        ('Kwarta 1', {'fields': ['quart_1_d1', 'quart_1_d2'] }),
        ('Kwarta 2', {'fields': ['quart_2_d1', 'quart_2_d2'] }),
        ('Kwarta 3', {'fields': ['quart_3_d1', 'quart_3_d2'] }),
        ('Kwarta 4', {'fields': ['quart_4_d1', 'quart_4_d2'] }),
    ]
    list_display = ('match_number','team_1', 'team_2', 'place')

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(M.Match, MatchAdmin)
admin.site.register(M.Team, TeamAdmin)
admin.site.register(M.Place, PlaceAdmin)
admin.site.register(M.Tabel)
