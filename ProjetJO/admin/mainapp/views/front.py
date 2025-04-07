from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from ..models import Event, Stadium, Team
from ..form import EventForm
from django.http import HttpResponseForbidden

@login_required
def administration(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")
    
    events = Event.objects.all().order_by('start').select_related('stadium')
    stadiums = Stadium.objects.all()
    teams = Team.objects.all()

    events_with_stadiums = []
    for event in events:
        event_stadiums = [
            {
                'id': stadium.id,
                'name': stadium.name,
                'location': stadium.location,
                'selected': (event.stadium and event.stadium.id == stadium.id),
            }
            for stadium in stadiums
        ]
        event_teams = [
            {
                'id': team.id,
                'name': team.name,
                'is_home': team.id == event.team_home_id,
                'is_away': team.id == event.team_away_id,
            }
            for team in teams
        ]
        events_with_stadiums.append({
            'event': event,
            'stadiums': event_stadiums,
            'teams': event_teams,
        })

    return render(request, 'admin.html', {'events_with_stadiums': events_with_stadiums})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        team_home_id = request.POST.get('team_home')
        team_away_id = request.POST.get('team_away')
        score_home = request.POST.get('score_home')
        score_away = request.POST.get('score_away')
        start = request.POST.get('start')
        stadium_id = request.POST.get('stadium')

        event.team_home = Team.objects.get(id=team_home_id) if team_home_id else None
        event.team_away = Team.objects.get(id=team_away_id) if team_away_id else None
        event.stadium = Stadium.objects.get(id=stadium_id) if stadium_id else None
        event.start = start

        if not score_home and not score_away:
            event.score = None
        elif score_home and score_away:
            try:
                score_home = int(score_home)
                score_away = int(score_away)
                if 0 <= score_home <= 99 and 0 <= score_away <= 99:
                    event.score = f"{score_home}-{score_away}"
            except ValueError:
                pass
        
        event.save()
        return redirect('admin')
    else:
        if event.score:
            try:
                score_home, score_away = event.score.split('-')
                initial = {
                    'score_home': score_home,
                    'score_away': score_away,
                }
            except ValueError:
                initial = {}
        else:
            initial = {}
            
        form = EventForm(instance=event, initial=initial)
        return render(request, 'edit_event.html', {
            'form': form, 
            'event': event
        })