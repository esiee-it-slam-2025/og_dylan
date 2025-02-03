// modal.js - Gestion des fenêtres modales

export function openModal() {
    const backdrop = document.querySelector('.modal-backdrop');
    const authModal = document.getElementById("authModal");

    backdrop.style.visibility = 'visible';
    authModal.style.visibility = 'visible';

    requestAnimationFrame(() => {
        backdrop.style.opacity = '1';
        authModal.style.opacity = '1';
        authModal.style.transform = 'translate(-50%, -50%)';
    });
}

export function closeModalWithAnimation() {
    const backdrop = document.querySelector('.modal-backdrop');
    const authModal = document.getElementById("authModal");

    backdrop.style.opacity = '0';
    authModal.style.opacity = '0';
    authModal.style.transform = 'translate(-150%, -50%)';

    setTimeout(() => {
        backdrop.style.visibility = 'hidden';
        authModal.style.visibility = 'hidden';
    }, 300);
}

export function setupModalEvents() {
    document.getElementById("loginButton")?.addEventListener("click", openModal);
    document.querySelector(".close")?.addEventListener("click", closeModalWithAnimation);
    document.querySelector(".modal-backdrop")?.addEventListener("click", closeModalWithAnimation);
}
