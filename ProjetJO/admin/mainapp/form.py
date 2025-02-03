<<<<<<< HEAD
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
    class Meta:
        model = Event
        fields = ['stadium','team_home', 'team_away', 'score', 'start']
=======
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
    class Meta:
        model = Event
        fields = ['team_home', 'team_away', 'score', 'start']
>>>>>>> 4b9efafc97361e76536dc3be53676cbeebfe08b9
