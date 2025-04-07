import { fetchEvents, fetchTeamDetails, checkAuthStatus, buyTicket } from "./api.js";
import { formatDate, showNotification } from "./utils.js";

let eventsData = [];
let teamsCache = {};
let uniqueTeams = new Set();
let uniqueStadiums = new Set();

// Ouvre la modal d'achat de ticket
function openPurchaseModal(event) {
    const modal = document.querySelector('.purchase-modal');
    const backdrop = document.querySelector('.purchase-modal-backdrop');
    const eventSummary = modal.querySelector('.event-summary');
    const teamHome = teamsCache[event.team_home?.id];
    const teamAway = teamsCache[event.team_away?.id];

    eventSummary.innerHTML = `
        <h3>${teamHome?.nickname || 'À déterminer'} vs ${teamAway?.nickname || 'À déterminer'}</h3>
        <p>${event.stadium?.name}</p>
        <p>${formatDate(event.start)}</p>
    `;

    modal.dataset.eventId = event.id;
    backdrop.classList.add('show');
    modal.classList.add('show');
}

// Ferme la modal d'achat de ticket
function closePurchaseModal() {
    const modal = document.querySelector('.purchase-modal');
    const backdrop = document.querySelector('.purchase-modal-backdrop');

    backdrop.classList.remove('show');
    modal.classList.remove('show');

    document.querySelectorAll('.category-option').forEach(option => {
        option.classList.remove('selected');
    });
    document.querySelector('.confirm-purchase').disabled = true;
}

// Charge les détails des équipes pour tous les événements
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

// Affiche les événements dans l'interface
async function displayEvents(filteredEvents = null) {
    const events = filteredEvents || eventsData;
    const container = document.getElementById('eventsList');
    if (!container) return;
    container.innerHTML = '';

    const authStatus = await checkAuthStatus();
    const isLoggedIn = authStatus.is_authenticated;

    eventsData.sort((a, b) => new Date(a.start) - new Date(b.start))
        .forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.className = 'event-card';
            const teamHome = teamsCache[event.team_home?.id] || { name: "À déterminer", nickname: "À déterminer", flag: "assets/flags/FW.svg" };
            const teamAway = teamsCache[event.team_away?.id] || { name: "À déterminer", nickname: "À déterminer", flag: "assets/flags/FW.svg" };
            const isMatchFinished = event.score !== null;

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
                    <div class="event-venue">${event.stadium?.name || "Lieu à déterminer"}</div>
                    <div class="event-date">${formatDate(event.start)}</div>
                    ${isMatchFinished ?
                        `<div class="match-score">Score: ${event.score}</div>` :
                        isLoggedIn ?
                            `<button class="buy-ticket-btn" data-event-id="${event.id}">Acheter un ticket</button>` :
                            ''
                    }
                </div>
            `;

            container.appendChild(eventDiv);

            if (!isMatchFinished && isLoggedIn) {
                const buyButton = eventDiv.querySelector('.buy-ticket-btn');
                if (buyButton) {
                    buyButton.addEventListener('click', () => openPurchaseModal(event));
                }
            }
        });
}

// Initialise la liste des événements et le système d'achat de tickets
export async function initEvents() {
    eventsData = await fetchEvents();
    await loadTeamsDetails();

    eventsData.forEach(event => {
        if (event.team_home?.name) uniqueTeams.add(event.team_home.name);
        if (event.team_away?.name) uniqueTeams.add(event.team_away.name);
        if (event.stadium?.name) uniqueStadiums.add(event.stadium.name);
    });
    await displayEvents();

    document.querySelector('.close-modal')?.addEventListener('click', closePurchaseModal);
    document.querySelector('.purchase-modal-backdrop')?.addEventListener('click', closePurchaseModal);

    document.querySelectorAll('.category-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.category-option').forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            document.querySelector('.confirm-purchase').disabled = false;
        });
    });

    document.querySelector('.confirm-purchase')?.addEventListener('click', async () => {
        const selectedCategory = document.querySelector('.category-option.selected')?.dataset.category;
        const eventId = document.querySelector('.purchase-modal').dataset.eventId;

        if (selectedCategory && eventId) {
            try {
                const response = await buyTicket(eventId, selectedCategory);
                if (response.message) {
                    showNotification(`Ticket acheté avec succès ! Prix : ${response.price}€`);
                    closePurchaseModal();
                }
            } catch (error) {
                showNotification('Erreur lors de l\'achat du ticket', 'error');
            }
        }
    });
}