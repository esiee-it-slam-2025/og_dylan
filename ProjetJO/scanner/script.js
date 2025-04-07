import { verifyTicket } from '../mobile/scripts/api.js';

const html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    {
        fps: 10,
        qrbox: { width: 250, height: 250 }
    },
    /* verbose= */ false
);

function displayTicketInfo(ticket) {
    html5QrcodeScanner.clear();
    const ticketInfo = document.getElementById('ticket-info');
    const detailsContainer = ticketInfo.querySelector('.ticket-details');

    if (ticket.valid) {
        detailsContainer.innerHTML = `
            <div class="ticket-card">
                <div class="ticket-header">
                    <div class="valid-badge">Billet Valide</div>
                </div>
                
                <div class="ticket-main">
                    <div class="event-name">
                        ${ticket.event.team_home} vs ${ticket.event.team_away}
                    </div>
                    
                    <div class="ticket-info-grid">
                        <div class="info-item">
                            <span class="label">Date</span>
                            <span class="value">${new Date(ticket.event.start).toLocaleString('fr-FR')}</span>
                        </div>
                        <div class="info-item">
                            <span class="label">Stade</span>
                            <span class="value">${ticket.event.stadium}</span>
                        </div>
                        <div class="info-item">
                            <span class="label">Catégorie</span>
                            <span class="value">${ticket.category}</span>
                        </div>
                        <div class="info-item">
                            <span class="label">Place</span>
                            <span class="value">${ticket.seat}</span>
                        </div>
                    </div>
                </div>
                
                <div class="ticket-footer">
                    <div class="ticket-id">ID: ${ticket.id}</div>
                </div>
            </div>
            <button id="scanAgain" class="scan-again-btn">Scanner un autre ticket</button>
        `;
        document.getElementById('scanAgain')?.addEventListener('click', () => {
            ticketInfo.classList.add('hidden');
            html5QrcodeScanner.render(handleTicketId, onScanError);
        });
    } else {
        detailsContainer.innerHTML = `
            <div class="ticket-card invalid">
                <div class="invalid-badge">Billet Invalid</div>
                <p class="error-message">${ticket.error || "Billet invalide"}</p>
                <button id="scanAgain" class="scan-again-btn">Scanner un autre ticket</button>
            </div>
        `;
        document.getElementById('scanAgain')?.addEventListener('click', () => {
            ticketInfo.classList.add('hidden');
            html5QrcodeScanner.render(handleTicketId, onScanError);
        });
    }

    ticketInfo.classList.remove('hidden');
}

async function handleTicketId(ticketId) {
    try {
        // Cacher le scanner quelle que soit la réponse
        html5QrcodeScanner.clear();
        
        const ticketInfo = await verifyTicket(ticketId);
        displayTicketInfo(ticketInfo);
    } catch (error) {
        // Le scanner est déjà caché par l'appel à clear() ci-dessus
        console.error("Erreur de vérification:", error);
        displayError(error.message || "Erreur lors de la vérification du ticket");
    }
}

function displayError(message) {
    const ticketInfo = document.getElementById('ticket-info');
    const detailsContainer = ticketInfo.querySelector('.ticket-details');
    
    // Vérifier si c'est une erreur de ticket déjà scanné
    const isUsedTicketError = message.includes('déjà été scanné');
    
    detailsContainer.innerHTML = `
        <div class="ticket-card invalid ${isUsedTicketError ? 'used-ticket-error' : ''}">
            <div class="invalid-badge">Billet Invalid</div>
            <p class="error-message">${message}</p>
            <button id="scanAgain" class="scan-again-btn">Scanner un autre ticket</button>
        </div>
    `;
    
    document.getElementById('scanAgain')?.addEventListener('click', () => {
        ticketInfo.classList.add('hidden');
        html5QrcodeScanner.render(handleTicketId, onScanError);
    });

    ticketInfo.classList.remove('hidden');
}

html5QrcodeScanner.render(handleTicketId, onScanError);

function onScanError(error) {
    // Fonction silencieuse pour éviter les logs d'erreurs de scan
}

const qrInput = document.getElementById('qrInput');
if (qrInput) {
    qrInput.addEventListener('change', async (e) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];
            try {
                const result = await html5QrcodeScanner.scanFile(file);
                handleTicketId(result);
            } catch (error) {
                displayError("Impossible de lire le QR code");
            }
        }
    });
}