# teams/forms.py

from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'nickname', 'color1', 'color2']
