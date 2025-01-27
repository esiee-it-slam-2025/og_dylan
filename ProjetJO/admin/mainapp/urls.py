from django.urls import path
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

)
