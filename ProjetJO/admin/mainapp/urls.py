from django.urls import path
<<<<<<< HEAD
from .views import (
    stadiums, events, teams, team_detail, 
    inscription, connexion, deconnexion, administration, 
    edit_event, user_login, register
=======
from .views import stadiums,events,teams,inscription,connexion,deconnexion,admin,edit_event


urlpatterns = (
    path('inscription/', inscription, name="inscription"),
    path('', connexion, name="connexion"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('admin/', admin, name="admin"),
    path("api/stadiums/", stadiums),
    path('api/events/', events),
    path('api/teams/', teams),
     path('edit_event/<int:event_id>/', edit_event, name='edit_event'),

>>>>>>> 4b9efafc97361e76536dc3be53676cbeebfe08b9
)
from django.contrib import admin

urlpatterns = [
    # Pages classiques
    path('', connexion, name="connexion"),
    path('inscription/', inscription, name="inscription"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('administration/', administration, name='admin'),  
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/login/', user_login, name='api_login'),
    path("api/stadiums/", stadiums, name="api_stadiums"),
    path('api/events/', events, name="api_events"),
    path('api/teams/', teams, name="api_teams"),
    path('api/teams/<int:team_id>/', team_detail, name='api_team_detail'),
    path('api/register/', register, name='api_register'), 

    # Édition d'un événement
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
]
