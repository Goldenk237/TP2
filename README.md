# Header Template (header.php)

Ce dépôt fournit un header moderne accessible pour intégrer dans un site PHP ou thème WordPress.

Caractéristiques principales:
- Compatible WordPress (appelle `wp_head()`/`wp_footer()` si présent) et plain PHP
- Navigation responsive (menu hamburger + overlay menu mobile)
- Recherche dans l'en-tête
- Bouton Call-to-Action (CTA)
- Skip-to-content pour l'accessibilité
- Sticky header qui se compacte quand on défile
- Menu déroulant pour sous-menus

Fichiers créés:
- `header.php` - Template d'en-tête
- `assets/css/header.css` - Styles pour le header
- `assets/js/header.js` - JS pour le comportement mobile & sticky
- `index.php` - Page de démonstration / test

Installation:
1. Copier les fichiers dans le dossier de votre thème ou dans votre projet.
2. Si vous utilisez WordPress: assurez-vous d'enregistrer un menu `primary` via `register_nav_menu` et d'enqueuer `assets/css/header.css` et `assets/js/header.js` via `wp_enqueue_style` et `wp_enqueue_script` — header.php contient déjà `wp_head()` et `wp_footer()`.
3. Pour un site PHP simple, incluez `header.php` dans vos pages et placez les dossiers `assets/css` et `assets/js` dans le répertoire racine ou mettez à jour les chemins.

Exemple WordPress (functions.php):

function theme_scripts() {
  wp_enqueue_style('theme-header', get_template_directory_uri() . '/assets/css/header.css', array(), '1.0');
  wp_enqueue_script('theme-header', get_template_directory_uri() . '/assets/js/header.js', array(), '1.0', true);
}
add_action('wp_enqueue_scripts', 'theme_scripts');

Notes d'accessibilité et d'améliorations possibles:
- Ajouter un focus trap quand le menu mobile est ouvert pour garder le focus dans le menu.
- Ajouter des animations CSS et transitions pour un meilleur rendu.
- Remplacer les icônes textuelles par des SVGs inline pour meilleure performance.
- Améliorer la logique pour gérer l'ouverture/fermeture du menu via `prefers-reduced-motion`.

License: MIT (libre d'utilisation)
