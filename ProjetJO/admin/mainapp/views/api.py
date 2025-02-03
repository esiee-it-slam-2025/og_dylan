from django.http import JsonResponse
from ..models import Event, Stadium, Team
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date

@csrf_exempt 
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            username = data.get('username')
            password = data.get('password')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Ce nom d\'utilisateur est déjà pris.'}, status=400)
            
            user = User.objects.create_user(username=username, password=password)
            user.save()

            return JsonResponse({'message': 'Inscription réussie !'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                return JsonResponse({'message': 'Connexion réussie !', 'user_id': user.id}, status=200)
            else:
                return JsonResponse({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

def stadiums(request):
    stadiums = Stadium.objects.all()
    stadium_id = request.GET.get('id')

    if stadium_id:
        stadiums = stadiums.filter(id=stadium_id)

    stadiums_data = [{
        "id": stadium.id,
        "name": stadium.name,
        "location": stadium.location,
    } for stadium in stadiums]

    return JsonResponse(stadiums_data, safe=False)

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_data = {
        "id": team.id,
        "name": team.name,
        "nickname": team.nickname,
        "code": team.code,
        "flag": f"assets/flags/{team.code}.svg"
    }
    return JsonResponse(team_data)

def teams(request):
    teams = Team.objects.all()
    teams_data = [{
        "id": team.id,
        "name": team.name,
        "nickname": team.nickname,
        "code": team.code,
        "flag": f"assets/flags/{team.code}.svg"
    } for team in teams]
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
    start_date = request.GET.get('start')

    if stadium_id:
        events = events.filter(stadium_id=stadium_id)
    if team_id:
        events = events.filter(team_home_id=team_id) | events.filter(team_away_id=team_id)
    if game_id:
        events = events.filter(id=game_id)
    if start_date:
        parsed_date = parse_date(start_date)
        if parsed_date:
            events = events.filter(start__date=parsed_date)

    event_list = [{
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
    } for event in events]

    return JsonResponse(event_list, safe=False)
