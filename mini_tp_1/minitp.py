import sys
from datetime import datetime

from django.conf import settings
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

################################################################################
# Données
################################################################################

teams = {
    "france": {
        "nickname": "Les bleus",
        "win": 12
    },
    "bresil": {
        "nickname": "La selecao",
        "win": 11
    },
    "belgique": {
        "nickname": "Les diables rouges",
        "win": 2
    }
}

################################################################################
# Vues
################################################################################

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'teams': teams})


class TeamView(View):
    def get(self, request, team_name):
        if team_name in teams:
            team = teams[team_name]
            if team['win'] >= 10:
                message = "Cette équipe a beaucoup de victoires !"
            else:
                message = "Cette équipe est nulle !"
            return render(request, 'team.html', {'team': team, 'message': message, 'team_name': team_name})
        else:
            return redirect('home')

class TeamDataView(View):
    def get(self, request, team_name):
        if team_name in teams:
            team = teams[team_name]
            return JsonResponse(team)
        else:
            return redirect('home')

################################################################################
# Paramètres et exécution
################################################################################

# Router
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipe/<str:team_name>/', TeamView.as_view(), name='team'),
    path('equipe/<str:team_name>/data', TeamDataView.as_view(), name='team_data'),
]

# Settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                "templates",
            ],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                ],
            },
        },
    ],
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
