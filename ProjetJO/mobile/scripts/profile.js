import { getCookie } from './utils.js';
import { showNotification } from './utils.js';

// Charge les données du profil de l'utilisateur connecté
async function loadProfileData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/profile/', {
            credentials: 'include'
        });
        
        if (!response.ok) {
            throw new Error('Non autorisé');
        }

        const data = await response.json();
        
        document.getElementById('username').value = data.username;
        document.getElementById('displayName').value = data.display_name || '';
        
        if (data.display_name) {
            localStorage.setItem('displayName', data.display_name);
        }
        if (data.profile_pic) {
            localStorage.setItem('profilePic', data.profile_pic);
            document.getElementById('currentProfilePic').src = data.profile_pic;
        }
    } catch (error) {
        console.error('Erreur lors du chargement du profil:', error);
        if (error.message === 'Non autorisé') {
            window.location.href = 'index.html';
        }
    }
}

// Configure l'upload de la photo de profil
function setupImageUpload() {
    const profilePicInput = document.getElementById('profilePicInput');
    
    profilePicInput.addEventListener('change', async (e) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];
            
            if (file.size > 5 * 1024 * 1024) {
                showNotification('L\'image ne doit pas dépasser 5MB', 'error');
                return;
            }

            if (!file.type.startsWith('image/')) {
                showNotification('Veuillez sélectionner une image', 'error');
                return;
            }

            const formData = new FormData();
            formData.append('image', file);

            try {
                const response = await fetch('http://127.0.0.1:8000/api/profile/upload-pic/', {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: formData
                });

                const data = await response.json();
                
                if (response.ok) {
                    document.getElementById('currentProfilePic').src = data.profile_pic;
                    localStorage.setItem('profilePic', data.profile_pic);
                    window.opener?.location.reload();
                    showNotification('Photo de profil mise à jour');
                } else {
                    showNotification(data.error || 'Erreur lors de l\'upload', 'error');
                }
            } catch (error) {
                console.error('Erreur lors de l\'upload:', error);
                showNotification('Erreur lors de l\'upload', 'error');
            }
        }
    });
}

// Configure le formulaire de mise à jour du profil
function setupProfileForm() {
    const profileForm = document.getElementById('profileForm');
    
    profileForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const displayName = document.getElementById('displayName').value;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/profile/update/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ display_name: displayName })
            });

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem('displayName', displayName);
                showNotification('Profil mis à jour avec succès');
            } else {
                showNotification(data.error || 'Erreur lors de la mise à jour', 'error');
            }
        } catch (error) {
            console.error('Erreur lors de la mise à jour:', error);
            showNotification('Erreur lors de la mise à jour', 'error');
        }
    });
}

// Initialise la page de profil au chargement du document
document.addEventListener('DOMContentLoaded', () => {
    loadProfileData();
    setupImageUpload();
    setupProfileForm();
});