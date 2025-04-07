from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    # Vues d'authentification
    connexion, inscription, deconnexion, 
    user_login, register, check_auth, user_logout,
    
    # Vues de pages
    administration, 
    
    # Vues liées aux événements
    events, edit_event,
    
    # Vues liées aux équipes
    teams, team_detail,
    
    # Vues des stades
    stadiums,
    
    # Vues liées aux billets
    buy_ticket, my_tickets, delete_ticket, verify_ticket,

    # Vues liées aux utilisateurs
    get_profile, update_profile, upload_profile_pic
)

urlpatterns = [
    # Routes d'authentification
    path('', connexion, name="connexion"),
    path('inscription/', inscription, name="inscription"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    
    # Routes d'administration
    path('administration/', administration, name='admin'),  
    path('admin/', admin.site.urls),
    
    # Endpoints API pour l'authentification
    path('api/login/', user_login, name='api_login'),
    path('api/register/', register, name='api_register'),
    path('api/check-auth/', check_auth, name='check-auth'),
    path('api/logout/', user_logout, name='logout'),
    
    # Endpoints API pour les événements
    path('api/events/', events, name="api_events"),
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
    
    # Endpoints API pour les équipes
    path('api/teams/', teams, name="api_teams"),
    path('api/teams/<int:team_id>/', team_detail, name='api_team_detail'),
    
    # Endpoints API pour les stades
    path('api/stadiums/', stadiums, name="api_stadiums"),

    # Endpoints API pour le profil
    path('api/profile/', get_profile, name='get_profile'),
    path('api/profile/update/', update_profile, name='update_profile'),
    path('api/profile/upload-pic/', upload_profile_pic, name='upload_profile_pic'),
    
    # Endpoints API pour les billets
    path('api/buy-ticket/', buy_ticket, name='buy_ticket'),
    path('api/my-tickets/', my_tickets, name='my_tickets'),
    path('api/my-tickets/<uuid:ticket_id>/', delete_ticket, name='delete_ticket'),
    path('api/verify-ticket/<uuid:ticket_id>/', verify_ticket, name='verify_ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)