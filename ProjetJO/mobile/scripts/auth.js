// auth.js - Gestion de l'authentification

import { API_LOGIN, API_REGISTER } from "./api.js";
import { getCookie } from "./utils.js";
import { closeModalWithAnimation } from "./modal.js";
import { checkAuthStatus } from './api.js';

// auth.js
export async function handleAuth(event, isRegister) {
    event.preventDefault();
    const form = isRegister ? document.getElementById("registerForm") : document.getElementById("loginForm");
    const username = form.querySelector('input[type="text"]').value;
    const password = form.querySelector('input[type="password"]').value;

    const response = await fetch(isRegister ? API_REGISTER : API_LOGIN, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ username, password }),
    });

    const data = await response.json();
    if (data.user_id || data.message) {
        alert(isRegister ? "Inscription réussie !" : "Connexion réussie !");
        closeModalWithAnimation();
        updateUIForLoggedInUser();
    } else {
        alert(data.error);
    }
}

export function updateUIForLoggedInUser() {
    const loginButton = document.getElementById('loginButton');
    const profileMenu = document.getElementById('profileMenu');
    const buyButtons = document.querySelectorAll('.buy-button');
    
    loginButton.classList.add('hidden');
    profileMenu.classList.remove('hidden');
    buyButtons.forEach(button => button.classList.remove('hidden'));
}

export function setupProfileMenu() {
    const profileButton = document.getElementById('profileButton');
    const dropdownContent = document.getElementById('profileDropdown');
    const logoutButton = document.getElementById('logout');

    profileButton.addEventListener('click', () => {
        dropdownContent.classList.toggle('hidden');
    });

    // Fermer le menu si on clique ailleurs
    document.addEventListener('click', (e) => {
        if (!profileButton.contains(e.target)) {
            dropdownContent.classList.add('hidden');
        }
    });

    logoutButton.addEventListener('click', async (e) => {
        e.preventDefault();
        // Ajouter ici la logique de déconnexion
        const loginButton = document.getElementById('loginButton');
        const profileMenu = document.getElementById('profileMenu');
        const buyButtons = document.querySelectorAll('.buy-button');
        
        loginButton.classList.remove('hidden');
        profileMenu.classList.add('hidden');
        buyButtons.forEach(button => button.classList.add('hidden'));
    });
}

export async function checkInitialAuth() {
    try {
        const data = await checkAuthStatus();
        if (data.is_authenticated) {
            updateUIForLoggedInUser();
            return true;
        }
        return false;
    } catch (error) {
        console.error('Erreur lors de la vérification de l\'authentification:', error);
        return false;
    }
}

export function updateUIForLoggedInUser() {
    const loginButton = document.getElementById('loginButton');
    const profileMenu = document.getElementById('profileMenu');
    const buyButtons = document.querySelectorAll('.buy-button');
    
    loginButton.classList.add('hidden');
    profileMenu.classList.remove('hidden');
    buyButtons.forEach(button => button.classList.remove('hidden'));
}