# Create your views here.
from django.forms.models import ModelForm
from scores.models import Match

class MatchForm(ModelForm):
    
    class Meta:
        model = Match
        exclude = ('place',)
        fields = ('quart_1_d1', 'quart_2_d1', 'quart_3_d1', 'quart_4_d1', 'quart_1_d2', 'quart_2_d2', 'quart_3_d2', 'quart_4_d2', 'staus')

