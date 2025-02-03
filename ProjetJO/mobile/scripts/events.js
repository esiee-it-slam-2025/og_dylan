// events.js - Gestion des événements

import { fetchEvents, fetchTeamDetails } from "./api.js";
import { formatDate } from "./utils.js";

let eventsData = [];
let teamsCache = {};

// Charger les détails des équipes
async function loadTeamsDetails() {
    const teamIds = new Set();
    eventsData.forEach(event => {
        if (event.team_home) teamIds.add(event.team_home.id);
        if (event.team_away) teamIds.add(event.team_away.id);
    });

    await Promise.all([...teamIds].map(async id => {
        teamsCache[id] = await fetchTeamDetails(id);
    }));
}

// Afficher les événements
function displayEvents() {
    const container = document.getElementById('eventsList');
    if (!container) return;
    container.innerHTML = '';

    eventsData.sort((a, b) => new Date(a.start) - new Date(b.start))
        .forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.className = 'event-card';

            const teamHome = teamsCache[event.team_home?.id] || { name: "À déterminer", nickname: "", flag: "assets/flags/FW.svg" };
            const teamAway = teamsCache[event.team_away?.id] || { name: "À déterminer", nickname: "", flag: "assets/flags/FW.svg" };

            // Dans la fonction displayEvents de events.js, modifiez la partie HTML :
            eventDiv.innerHTML = `
                <div class="event-flags">
                    <div class="flag-container"><img src="${teamHome.flag}" alt="${teamHome.name}" class="team-flag"></div>
                    <div class="flag-container"><img src="${teamAway.flag}" alt="${teamAway.name}" class="team-flag"></div>
                </div>
                <div class="event-nicknames">
                    <div class="team-nickname">${teamHome.nickname}</div>
                    <div class="team-nickname">${teamAway.nickname}</div>
                </div>
                <div class="event-info">
                    <div class="event-venue">${event.stadium?.name || "Lieu inconnu"}</div>
                    <div class="event-date">${formatDate(event.start)}</div>
                    <button class="buy-button hidden">Acheter</button>
                </div>
            `;

            container.appendChild(eventDiv);
        });
}

// Initialisation des événements
export async function initEvents() {
    eventsData = await fetchEvents();
    await loadTeamsDetails();
    displayEvents();
}
