// api.js - Contient les URLs des API et les requêtes fetch

export const API_REGISTER = "http://127.0.0.1:8000/api/register/";
export const API_LOGIN = "http://127.0.0.1:8000/api/login/";
export const API_EVENTS = "http://127.0.0.1:8000/api/events/";
export const API_TEAMS = "http://127.0.0.1:8000/api/teams/";

// Fonction pour récupérer les détails d'une équipe
export async function fetchTeamDetails(teamId) {
    if (!teamId) return { name: "À déterminer", nickname: "", flag: "assets/flags/FW.svg" };
    
    const response = await fetch(`${API_TEAMS}${teamId}`);
    return response.json();
}

// Fonction pour récupérer les événements
export async function fetchEvents() {
    const response = await fetch(API_EVENTS);
    return response.json();
}


// api.js
export const API_CHECK_AUTH = "http://127.0.0.1:8000/api/check-auth/";

// Fonction pour vérifier l'état de connexion
export async function checkAuthStatus() {
    const response = await fetch(API_CHECK_AUTH, {
        credentials: 'include',  // Pour inclure les cookies
    });
    return response.json();
}