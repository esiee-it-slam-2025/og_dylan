import { API_LOGIN, API_REGISTER } from "./api.js";
import { getCookie, showNotification } from "./utils.js";
import { closeModalWithAnimation } from "./modal.js";
import { checkAuthStatus } from './api.js';

// Met à jour l'interface pour un utilisateur connecté
export function updateUIForLoggedInUser() {
    const loginButton = document.getElementById('loginButton');
    const profileMenu = document.getElementById('profileMenu');
    const buyButtons = document.querySelectorAll('.buy-button');
    const headerProfilePic = document.getElementById('headerProfilePic');

    loginButton.classList.add('hidden');
    profileMenu.classList.remove('hidden');
    buyButtons.forEach(button => button.classList.remove('hidden'));

    fetch('http://127.0.0.1:8000/api/profile/', {
        credentials: 'include'
    })
        .then(response => response.json())
        .then(data => {
            headerProfilePic.src = data.profile_pic || '../admin/mainapp/media/profil/profile_icon.png';
        })
        .catch(error => {
            console.error('Error fetching profile:', error);
        });
}

// Efface les données utilisateur du stockage local
function clearUserData() {
    localStorage.removeItem('profilePic');
    localStorage.removeItem('displayName');
}

// Gère l'authentification (connexion ou inscription)
export async function handleAuth(event, isRegister) {
    event.preventDefault();
    try {
        const form = isRegister ? document.getElementById("registerForm") : document.getElementById("loginForm");
        const username = form.querySelector('input[type="text"]').value;
        const password = form.querySelector('input[type="password"]').value;

        if (isRegister) {
            const confirmPassword = document.getElementById('confirmPassword').value;
            if (password !== confirmPassword) {
                showNotification('Les mots de passe ne correspondent pas', 'error');
                return;
            }
        }

        clearUserData();

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

        if (response.ok) {
            closeModalWithAnimation();
            showNotification("Compte créé avec succès !");
            if (!isRegister) {
                location.reload();
            }
        } else {
            if (data.error === 'Ce nom d\'utilisateur est déjà pris.') {
                showNotification("Ce nom d'utilisateur est déjà pris", 'error');
            } else if (data.error === 'Nom d\'utilisateur ou mot de passe incorrect.') {
                showNotification("Identifiants incorrects", 'error');
            } else {
                showNotification("Une erreur est survenue", 'error');
            }
        }
    } catch (error) {
        console.error('Erreur:', error);
        showNotification("Une erreur est survenue", 'error');
    }
}

// Configure le menu de profil et les événements de déconnexion
export function setupProfileMenu() {
    const profileButton = document.getElementById('profileButton');
    const dropdownContent = document.getElementById('profileDropdown');
    const logoutButton = document.getElementById('logout');
    const myTicketsLink = document.getElementById('myTickets');

    profileButton.addEventListener('click', () => {
        dropdownContent.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
        if (!profileButton.contains(e.target)) {
            dropdownContent.classList.add('hidden');
        }
    });

    myTicketsLink.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.href = 'mestickets.html';
    });

    logoutButton.addEventListener('click', async (e) => {
        e.preventDefault();
        try {
            clearUserData();

            const response = await fetch('http://127.0.0.1:8000/api/logout/', {
                method: 'POST',
                credentials: 'include',
            });

            if (response.ok) {
                location.reload();
            }
        } catch (error) {
            console.error('Erreur lors de la déconnexion:', error);
        }
    });
}

// Vérifie l'état d'authentification initial lors du chargement de la page
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