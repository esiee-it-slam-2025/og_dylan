import { fetchMyTickets, deleteTicket } from './api.js';
import { formatDate, showNotification } from './utils.js';

// Télécharge le QR code d'un ticket sous forme d'image
function downloadQRCode(ticketId) {
    const qrCanvas = document.querySelector(`#qr-${ticketId} canvas`);
    if (qrCanvas) {
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = qrCanvas.width + 40;
        tempCanvas.height = qrCanvas.height + 40;
        const ctx = tempCanvas.getContext('2d');

        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);

        ctx.drawImage(qrCanvas, 20, 20);

        const link = document.createElement('a');
        link.download = `ticket-${ticketId}.png`;
        link.href = tempCanvas.toDataURL('image/png', 1.0);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

// Affiche tous les tickets de l'utilisateur regroupés par événement
async function displayTickets() {
    try {
        const tickets = await fetchMyTickets();
        const container = document.getElementById('myTicketsContainer');

        if (!tickets.length) {
            container.innerHTML = '<p class="no-tickets">Vous n\'avez pas encore de tickets</p>';
            return;
        }

        const ticketsByEvent = tickets.reduce((acc, ticket) => {
            const eventId = ticket.event.id;
            if (!acc[eventId]) {
                acc[eventId] = {
                    event: ticket.event,
                    tickets: []
                };
            }
            acc[eventId].tickets.push(ticket);
            return acc;
        }, {});

        container.innerHTML = Object.values(ticketsByEvent).map(group => `
            <div class="event-group">
                <div class="event-header">
                    <h3>${group.event.team_home} vs ${group.event.team_away}</h3>
                    <span>${formatDate(group.event.start)}</span>
                </div>
                <div class="tickets-container">
                ${group.tickets.map(ticket => `
                    <div class="ticket-card ${ticket.is_used ? 'used' : ''}">
                        <div class="ticket-header">
                            <span class="ticket-category ${ticket.category}">${ticket.category}</span>
                            <div class="ticket-status-actions">
                                ${ticket.is_used ? '<span class="used-badge">Déjà utilisé</span>' : ''}
                                <button class="delete-button" data-ticket-id="${ticket.id}">Supprimer</button>
                            </div>
                        </div>
                        <div class="ticket-details">
                            <p class="seat">Place: ${ticket.seat}</p>
                            <div class="qr-code" id="qr-${ticket.id}"></div>
                            <div class="dl-button">
                                <button class="download-qr" data-ticket-id="${ticket.id}">
                                    <img src="assets/images/download_icon.png" alt="Download QR">
                                </button>
                            </div>
                            <p class="dl_t">Télécharger mon billet</p>
                            <div class="dl-button">
                                <button class="download-ticket" data-ticket='${JSON.stringify(ticket)}'>
                                    <img src="assets/images/ticket_icon.png" alt="Download Ticket">
                                </button>
                            </div>
                        </div>
                    </div>
                `).join('')}
                </div>
            </div>
        `).join('');

        document.querySelectorAll('.event-header').forEach(header => {
            header.addEventListener('click', () => {
                header.parentElement.classList.toggle('expanded');
            });
        });

        tickets.forEach(ticket => {
            new QRCode(document.getElementById(`qr-${ticket.id}`), {
                text: ticket.id,
                width: 128,
                height: 128
            });
        });

        document.querySelectorAll('.delete-button').forEach(button => {
            button.addEventListener('click', async (e) => {
                e.stopPropagation();
                const ticketId = button.dataset.ticketId;
                await deleteTicket(ticketId);
                await displayTickets();
                showNotification('Ticket supprimé');
            });
        });

        document.querySelectorAll('.download-qr').forEach(button => {
            button.addEventListener('click', () => {
                downloadQRCode(button.dataset.ticketId);
            });
        });

        document.querySelectorAll('.download-ticket').forEach(button => {
            button.addEventListener('click', async function () {
                const ticket = JSON.parse(this.dataset.ticket);
                await downloadTicket(ticket);
            });
        });

    } catch (error) {
        console.error('Erreur:', error);
        document.getElementById('myTicketsContainer').innerHTML =
            '<p class="error">Une erreur est survenue</p>';
    }
}

// Génère le HTML du template de ticket pour l'impression
function generateTicketTemplate(ticket) {
    const defaultProfilePic = 'assets/images/profile_icon.png';
    const userProfilePic = localStorage.getItem('profilePic');
    const userDisplayName = localStorage.getItem('displayName');

    const showOwnerSection = userProfilePic || userDisplayName;

    return `
        <div class="ticket-template">
            <div class="ticket-header">
                <img src="assets/JO Icons.svg" alt="JO 2024" class="logo">
                <div class="ticket-type">${ticket.category}</div>
            </div>
            
            <div class="ticket-content">
                <div class="event-details">
                    ${showOwnerSection ? `
                        <div class="ticket-owner">
                            ${userProfilePic ? `
                                <img src="${userProfilePic}" alt="Photo de profil" class="owner-pic" 
                                    onerror="this.src='${defaultProfilePic}'; this.onerror=null;">
                            ` : ''}
                            ${userDisplayName ? `
                                <span class="owner-name">${userDisplayName}</span>
                            ` : ''}
                        </div>
                    ` : ''}
                    <div class="teams">
                        <span class="team-name">${ticket.event.team_home}</span>
                        <span class="vs">VS</span>
                        <span class="team-name">${ticket.event.team_away}</span>
                    </div>
                    <div class="event-info">
                        <p class="stadium">${ticket.event.stadium}</p>
                        <p class="date">${formatDate(ticket.event.start)}</p>
                        <p class="seat">Place : ${ticket.seat}</p>
                    </div>
                </div>
                
                <div class="ticket-footer">
                    <div class="qr-code" id="temp-qr-${ticket.id}"></div>
                    <div class="ticket-number">N° ${ticket.id}</div>
                </div>
            </div>
        </div>
    `;
}

// Télécharge un ticket au format PDF
async function downloadTicket(ticket) {
    let renderContainer = null;
    let addedStyleSheet = null;
    try {
        const uniqueId = `ticket-render-${Date.now()}`;
        renderContainer = document.createElement('div');
        renderContainer.id = uniqueId;
        renderContainer.style.position = 'fixed';
        renderContainer.style.left = '-9999px';
        renderContainer.style.top = '0';
        renderContainer.style.width = '800px';
        renderContainer.style.height = '350px';
        renderContainer.style.pointerEvents = 'none';
        renderContainer.style.zIndex = '-1000';

        renderContainer.innerHTML = generateTicketTemplate(ticket);

        addedStyleSheet = document.createElement('style');
        const cssText = await fetch('styles/ticketTemplate.css').then(res => res.text());
        const scopedCss = cssText.replace(/([^}]*){/g, (match) => {
            const selectors = match.slice(0, -1).split(',');
            return selectors
                .map(selector => `#${uniqueId} ${selector.trim()}`)
                .join(',') + '{';
        });
        addedStyleSheet.textContent = scopedCss;

        document.head.appendChild(addedStyleSheet);
        document.body.appendChild(renderContainer);

        new QRCode(renderContainer.querySelector(`#temp-qr-${ticket.id}`), {
            text: ticket.id,
            width: 180,
            height: 180
        });

        await new Promise(resolve => setTimeout(resolve, 500));

        const canvas = await html2canvas(renderContainer.querySelector('.ticket-template'), {
            scale: 4,
            logging: false,
            useCORS: true,
            allowTaint: true,
            backgroundColor: null,
            imageTimeout: 0,
            removeContainer: true,
            letterRendering: true,
            windowWidth: 800,
            windowHeight: 350
        });

        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF({
            orientation: 'landscape',
            unit: 'px',
            format: [canvas.width / 2, canvas.height / 2],
            compress: true,
            hotfixes: ["px_scaling"],
            precision: 16
        });

        pdf.addImage(
            canvas.toDataURL('image/png', 1.0),
            'PNG',
            0,
            0,
            canvas.width / 2,
            canvas.height / 2,
            undefined,
            'FAST'
        );

        pdf.save(`ticket-${ticket.event.team_home}-vs-${ticket.event.team_away}.pdf`);

    } catch (error) {
        console.error('Erreur lors de la génération du PDF:', error);
        showNotification('Erreur lors de la génération du PDF', 'error');
    } finally {
        if (addedStyleSheet && addedStyleSheet.parentNode) {
            addedStyleSheet.parentNode.removeChild(addedStyleSheet);
        }
        if (renderContainer && renderContainer.parentNode) {
            renderContainer.parentNode.removeChild(renderContainer);
        }
    }
}

// Initialise l'affichage des tickets au chargement de la page
document.addEventListener('DOMContentLoaded', displayTickets);