from django.http import JsonResponse
from ..models import Event, Stadium, Team

def stadiums(request):
    stadiums = Stadium.objects.all()
    stadium_id = request.GET.get('id')

    if stadium_id:
        stadiums = stadiums.filter(id=stadium_id)

    stadiums_data = []
    for stadium in stadiums:
        stadiums_data.append({
            "id": stadium.id,
            "name": stadium.name,
            "location": stadium.location,
        })

    return JsonResponse(stadiums_data, safe=False)

def teams(request):
    teams = Team.objects.all()
    team_id = request.GET.get('id')

    if team_id:
        teams = teams.filter(id=team_id)

    teams_data = []
    for team in teams:
        teams_data.append({
            "id": team.id,
            "name": team.name,
            "nickname": team.nickname,
            "code": team.code,
            "flag": f"flags/{team.code}.svg"  
        })

    return JsonResponse(teams_data, safe=False)

def events(request):
    events = Event.objects.all().select_related('stadium', 'team_home', 'team_away', 'winner')

    stadium_id = request.GET.get('stadium_id')
    team_id = request.GET.get('team_id')
    game_id = request.GET.get('game_id')

    if stadium_id:
        events = events.filter(stadium_id=stadium_id)
    if team_id:
        events = events.filter(team_home_id=team_id) | events.filter(team_away_id=team_id)
    if game_id:
        events = events.filter(id=game_id)

    event_list = []
    for event in events:
        event_list.append({
            "id": event.id,
            "stadium": {
                "id": event.stadium.id,
                "name": event.stadium.name,
                "location": event.stadium.location,
            },
            "team_home": {
                "id": event.team_home.id,
                "name": event.team_home.name,
            } if event.team_home else None,
            "team_away": {
                "id": event.team_away.id,
                "name": event.team_away.name,
            } if event.team_away else None,
            "start": event.start,
            "score": event.score,
            "winner": {
                "id": event.winner.id,
                "name": event.winner.name,
            } if event.winner else None,
        })

    return JsonResponse(event_list, safe=False)