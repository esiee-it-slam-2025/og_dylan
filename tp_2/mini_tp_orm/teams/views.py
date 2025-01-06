# teams/views.py

from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm

def home(request):
    return render(request, 'home.html')

def team_list(request):
    teams = Team.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'team_list.html', {'teams': teams, 'form': form})

def delete_team(request, team_id):
    team = Team.objects.get(id=team_id)
    team.delete()
    return redirect('team_list')
