from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Event

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'autocomplete': 'username'}),
    )
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")


class EventForm(forms.ModelForm):
    score_home = forms.IntegerField(required=False, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'class': 'score-input'}))
    score_away = forms.IntegerField(required=False, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'class': 'score-input'}))

    class Meta:
        model = Event
        fields = ['team_home', 'team_away', 'start', 'stadium']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.score:
            try:
                home, away = self.instance.score.split('-')
                self.initial['score_home'] = int(home)
                self.initial['score_away'] = int(away)
            except (ValueError, AttributeError):
                pass
