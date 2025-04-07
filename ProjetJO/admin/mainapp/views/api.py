from django.http import JsonResponse
from ..models import Event, Stadium, Team, Ticket  
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required


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
                login(request, user)  
                return JsonResponse({
                    'message': 'Connexion réussie !', 
                    'user_id': user.id,
                    'username': user.username
                }, status=200)
            else:
                return JsonResponse({
                    'error': 'Nom d\'utilisateur ou mot de passe incorrect.'
                }, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({})

@csrf_exempt
def check_auth(request):
    return JsonResponse({
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None,
        'user_id': request.user.id if request.user.is_authenticated else None
    })

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Déconnexion réussie'})
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

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
        "flag": f"assets/flags/{team.code}.png"
    }
    return JsonResponse(team_data)

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
            "flag": f"flags/{team.code}.png"  
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
            "id": event.stadium.id if event.stadium else None,
            "name": event.stadium.name if event.stadium else "Lieu à déterminer",
            "location": event.stadium.location if event.stadium else None,
        } if event.stadium else {
            "id": None,
            "name": "Lieu à déterminer",
            "location": None
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

@login_required
def buy_ticket(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event_id = data.get('event_id')
            category = data.get('category')

            if not event_id or not category:
                return JsonResponse({'error': 'event_id et category sont requis'}, status=400)

            event = get_object_or_404(Event, id=event_id)

            ticket = Ticket.objects.create(
                user=request.user,
                event=event,
                category=category,
            )

            return JsonResponse({
                'message': 'Ticket acheté avec succès',
                'ticket_id': str(ticket.id),
                'price': float(ticket.price),
                'seat': ticket.seat
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@csrf_exempt
@login_required
def delete_ticket(request, ticket_id):
    if request.method == 'DELETE':
        ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
        ticket.delete()
        return JsonResponse({'message': 'Ticket supprimé'})
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user).select_related('event', 'event__stadium', 'event__team_home', 'event__team_away')
    tickets_data = [{
        'id': str(ticket.id),
        'event': {
            'id': ticket.event.id,
            'team_home': ticket.event.team_home.name if ticket.event.team_home else "À déterminer",
            'team_away': ticket.event.team_away.name if ticket.event.team_away else "À déterminer",
            'start': ticket.event.start,
            'stadium': ticket.event.stadium.name if ticket.event.stadium else "Lieu à déterminer",
        },
        'category': ticket.category,
        'seat': ticket.seat,
        'price': float(ticket.price),
        'is_used': ticket.is_used
    } for ticket in tickets]
    
    return JsonResponse(tickets_data, safe=False)

@csrf_exempt
def verify_ticket(request, ticket_id):
    try:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        
        if ticket.is_used:
            return JsonResponse({
            'valid': False,
            'error': 'Le ticket n\'est plus valide, il a déjà été scanné.'
        }, status=400)
        
        ticket.is_used = True
        ticket.save()
        
        ticket_data = {
            'id': str(ticket.id),
            'event': {
                'team_home': ticket.event.team_home.name if ticket.event.team_home else "À déterminer",
                'team_away': ticket.event.team_away.name if ticket.event.team_away else "À déterminer",
                'start': ticket.event.start.isoformat(),
                'stadium': ticket.event.stadium.name if ticket.event.stadium else "Lieu à déterminer",
            },
            'category': ticket.category,
            'seat': ticket.seat,
            'valid': True
        }
        return JsonResponse(ticket_data)
    except Exception as e:
        return JsonResponse({
            'valid': False,
            'error': 'Ticket non trouvé'
        }, status=404)
    
@login_required
def get_profile(request):
    profile = request.user.profile
    profile_data = {
        'username': request.user.username,
        'display_name': profile.display_name,
        'profile_pic': request.build_absolute_uri(profile.profile_pic.url) if profile.profile_pic else None
    }
    return JsonResponse(profile_data)

@login_required
@csrf_exempt
def update_profile(request):
    """Mettre à jour le profil"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    
    try:
        data = json.loads(request.body)
        profile = request.user.profile
        
        # Mise à jour du pseudo
        if 'display_name' in data:
            profile.display_name = data['display_name']
            
        profile.save()
        
        return JsonResponse({
            'message': 'Profil mis à jour avec succès',
            'display_name': profile.display_name,
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@login_required
@csrf_exempt
def upload_profile_pic(request):
    """Upload de la photo de profil"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    
    try:
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'Aucune image fournie'}, status=400)
            
        profile = request.user.profile
        profile.profile_pic = request.FILES['image']
        profile.save()
        
        return JsonResponse({
            'message': 'Photo de profil mise à jour',
            'profile_pic': request.build_absolute_uri(profile.profile_pic.url)
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)