
from django.contrib import admin
import main.models as M

#admin.site.register(Choice)

#class PollAdmin(admin.ModelAdmin):
    #list_display = ('question', 'pub_date')
    
#admin.site.register(Poll, PollAdmin)

class PlayerInline(admin.TabularInline):
    model = M.Player
    extra = 1
    fields = ['number', 'name', 'surname', 'staus']

class MatchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['place', 'team_1', 'team_2']}),
        ('Kwarta 1', {'fields': ['quart_1_d1', 'quart_1_d2'] }),
        ('Kwarta 2', {'fields': ['quart_2_d1', 'quart_2_d2'] }),
        ('Kwarta 3', {'fields': ['quart_3_d1', 'quart_3_d2'] }),
        ('Kwarta 4', {'fields': ['quart_4_d1', 'quart_4_d2'] }),
    ]
    list_display = ('place','team_1', 'team_2')
    #inlines = [QuartInline]

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]
    #list_display = ['']

class PlaceAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(M.Match, MatchAdmin)
admin.site.register(M.Team, TeamAdmin)
admin.site.register(M.Place, PlaceAdmin)
admin.site.register(M.UserProfile, UserProfileAdmin)
