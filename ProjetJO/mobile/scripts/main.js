import { setupModalEvents } from "./modal.js";
import { handleAuth, setupProfileMenu, checkInitialAuth } from "./auth.js";
import { initEvents } from "./events.js";

// Initialise toutes les fonctionnalités de l'application au chargement
document.addEventListener("DOMContentLoaded", async () => {
    await checkInitialAuth();

    const toggleAuthBtn = document.getElementById('toggleAuth');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const modalTitle = document.getElementById('modalTitle');

    // Configure la bascule entre les formulaires de connexion et d'inscription
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