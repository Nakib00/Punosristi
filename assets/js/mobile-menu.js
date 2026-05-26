document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (!mobileMenuBtn || !mobileMenu) return;

    const menuIcon = mobileMenuBtn.querySelector('.material-symbols-outlined');

    function closeMenu() {
        mobileMenu.classList.add('hidden');
        if (menuIcon) menuIcon.textContent = 'menu';
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }

    function openMenu() {
        mobileMenu.classList.remove('hidden');
        if (menuIcon) menuIcon.textContent = 'close';
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
    }

    mobileMenuBtn.setAttribute('aria-expanded', 'false');
    mobileMenuBtn.setAttribute('aria-controls', 'mobile-menu');
    mobileMenuBtn.setAttribute('aria-label', 'Open navigation menu');

    mobileMenuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (mobileMenu.classList.contains('hidden')) {
            openMenu();
        } else {
            closeMenu();
        }
    });

    // Close menu when a nav link is clicked
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenu.classList.contains('hidden') &&
            !mobileMenu.contains(e.target) &&
            !mobileMenuBtn.contains(e.target)) {
            closeMenu();
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeMenu();
    });
});
