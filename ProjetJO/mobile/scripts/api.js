import { getCookie } from './utils.js';

// URLs des endpoints API
export const API_REGISTER = "http://127.0.0.1:8000/api/register/";
export const API_LOGIN = "http://127.0.0.1:8000/api/login/";
export const API_EVENTS = "http://127.0.0.1:8000/api/events/";
export const API_TEAMS = "http://127.0.0.1:8000/api/teams/";
export const API_MY_TICKETS = "http://127.0.0.1:8000/api/my-tickets/";
export const API_BUY_TICKET = "http://127.0.0.1:8000/api/buy-ticket/";
export const API_CHECK_AUTH = "http://127.0.0.1:8000/api/check-auth/";
export const API_VERIFY_TICKET = "http://127.0.0.1:8000/api/verify-ticket/";

// Récupère les détails d'une équipe par son ID
export async function fetchTeamDetails(teamId) {
    if (!teamId) return { name: "À déterminer", nickname: "", flag: "assets/flags/FW.svg" };
    
    const response = await fetch(`${API_TEAMS}${teamId}`);
    return response.json();
}

// Récupère tous les événements
export async function fetchEvents() {
    const response = await fetch(API_EVENTS);
    return response.json();
}

// Vérifie le statut d'authentification de l'utilisateur
export async function checkAuthStatus() {
    const response = await fetch(API_CHECK_AUTH, {
        credentials: 'include'
    });
    return response.json();
}

// Récupère les tickets de l'utilisateur connecté
export async function fetchMyTickets() {
    const response = await fetch(API_MY_TICKETS, {
        credentials: 'include'
    });
    return response.json();
}

// Achète un ticket pour un événement
export async function buyTicket(eventId, category) {
    const response = await fetch(API_BUY_TICKET, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            event_id: eventId,
            category: category
        })
    });
    return response.json();
}

// Supprime un ticket
export async function deleteTicket(ticketId) {
    const response = await fetch(`${API_MY_TICKETS}${ticketId}/`, {
        method: 'DELETE',
        credentials: 'include',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    });
    return response.ok;
}

// Vérifie la validité d'un ticket
export async function verifyTicket(ticketId) {
    try {
        const url = `${API_VERIFY_TICKET}${ticketId}/`;

        const response = await fetch(url, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Ticket invalide');
        }
        
        return data;
    } catch (error) {
        console.error("Erreur dans verifyTicket:", error);
        throw error;
    }
}