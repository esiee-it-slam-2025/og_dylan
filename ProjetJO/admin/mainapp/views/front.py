from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from ..models import Event, Stadium, Team
from ..form import EventForm

@login_required
def admin(request):
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
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})
