document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileNavMenu = document.getElementById('mobile-nav-menu');
    const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
    const iconMenu = document.getElementById('icon-menu');
    const iconClose = document.getElementById('icon-close');

    if (mobileMenuBtn && mobileNavMenu && mobileMenuBackdrop) {
        const toggleMenu = () => {
            const isClosed = mobileNavMenu.classList.contains('invisible');

            if (isClosed) {
                // Open Menu
                mobileNavMenu.classList.remove('invisible', 'pointer-events-none', 'opacity-0', '-translate-y-4', 'scale-y-95');
                mobileNavMenu.classList.add('opacity-100', 'translate-y-0', 'scale-y-100');

                mobileMenuBackdrop.classList.remove('invisible', 'opacity-0');
                mobileMenuBackdrop.classList.add('opacity-100');

                iconMenu.classList.add('hidden');
                iconClose.classList.remove('hidden');
            } else {
                // Close Menu
                mobileNavMenu.classList.add('invisible', 'pointer-events-none', 'opacity-0', '-translate-y-4', 'scale-y-95');
                mobileNavMenu.classList.remove('opacity-100', 'translate-y-0', 'scale-y-100');

                mobileMenuBackdrop.classList.add('invisible', 'opacity-0');
                mobileMenuBackdrop.classList.remove('opacity-100');

                iconMenu.classList.remove('hidden');
                iconClose.classList.add('hidden');
            }
        };

        mobileMenuBtn.addEventListener('click', toggleMenu);
        mobileMenuBackdrop.addEventListener('click', toggleMenu);

        // Close menu when clicking a link inside it
        const mobileLinks = mobileNavMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', toggleMenu);
        });
    }
});
