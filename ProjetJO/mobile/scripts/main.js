// main.js - Initialisation des événements DOM

import { setupModalEvents } from "./modal.js";
import { handleAuth, setupProfileMenu } from "./auth.js";
import { initEvents } from "./events.js";

document.addEventListener("DOMContentLoaded", () => {
    const toggleAuthBtn = document.getElementById('toggleAuth');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const modalTitle = document.getElementById('modalTitle');

    toggleAuthBtn.addEventListener('click', () => {
        if (loginForm.classList.contains('hidden')) {
            loginForm.classList.remove('hidden');
            registerForm.classList.add('hidden');
            modalTitle.textContent = 'Connexion';
            toggleAuthBtn.textContent = 'Pas encore inscrit ?';
        } else {
            loginForm.classList.add('hidden');
            registerForm.classList.remove('hidden');
            modalTitle.textContent = 'Inscription';
            toggleAuthBtn.textContent = 'Déjà inscrit ?';
        }
    });

    setupModalEvents();
    initEvents();
    setupProfileMenu();

    document.getElementById("loginForm")?.addEventListener("submit", (e) => handleAuth(e, false));
    document.getElementById("registerForm")?.addEventListener("submit", (e) => handleAuth(e, true));
});
