<?php
/*
 * Modern theme header partial
 * - Accessible skip link
 * - Responsive / mobile menu toggle
 * - Search, logo, CTA button, social links
 * - Sticky header when scrolling
 * - Works in WordPress (wp_head) or plain PHP sites
 *
 * Usage (WordPress): copy into your theme root as header.php
 * Usage (Plain PHP): include('header.php') from your template
 */

// The styles and script references are minimal; in WordPress you may enqueue them instead.

// --- WordPress compatibility fallbacks for plain PHP environments ---
if (!function_exists('esc_html')) {
  function esc_html($text) {
    return htmlspecialchars($text, ENT_QUOTES, 'UTF-8');
  }
}
if (!function_exists('wp_head')) {
  function wp_head() { /* noop fallback for non-WP */ }
}
if (!function_exists('wp_footer')) {
  function wp_footer() { /* noop fallback for non-WP */ }
}
if (!function_exists('body_class')) {
  function body_class() { /* noop fallback for non-WP; prints nothing */ }
}
?>
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#ffffff" />
  <title><?php echo isset($page_title) ? esc_html($page_title) : 'Mon site'; ?></title>
  <!-- Minimal fonts and icons (optional) -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/header.css">
  <?php if (function_exists('wp_head')) { wp_head(); } ?>
</head>
<body <?php if (function_exists('body_class')) { body_class(); } ?>>

<a class="sr-only skip-link" href="#main">Aller au contenu</a>

<header class="site-header" role="banner" aria-label="En-tête du site">
  <div class="container site-header__inner">
    <div class="brand">
      <a href="/" class="brand__link" aria-label="Accueil">
        <img src="/assets/images/logo.svg" alt="Logo" class="brand__logo" width="44" height="44">
        <span class="brand__title">MonSite</span>
      </a>
    </div>

    <nav class="main-nav" role="navigation" aria-label="Menu principal">
      <button class="nav-toggle" aria-controls="main-navigation" aria-expanded="false" aria-label="Ouvrir le menu">
        <span class="nav-toggle__bars" aria-hidden="true"></span>
      </button>

      <ul id="main-navigation" class="main-nav__list" data-visible="false">
        <!-- You can dynamically render menu items in WP with wp_nav_menu or hardcode them here -->
        <?php if (function_exists('wp_nav_menu')) : ?>
          <?php wp_nav_menu(array('theme_location' => 'primary', 'container' => false, 'items_wrap' => '%3$s', 'menu_class' => 'main-nav__list')); ?>
        <?php else: ?>
          <li class="main-nav__item"><a href="/" class="main-nav__link">Accueil</a></li>
          <li class="main-nav__item"><a href="/about" class="main-nav__link">À propos</a></li>
          <li class="main-nav__item main-nav__item--has-submenu">
            <a href="/services" class="main-nav__link" aria-haspopup="true">Services</a>
            <ul class="submenu">
              <li><a href="/services/web">Web</a></li>
              <li><a href="/services/seo">SEO</a></li>
            </ul>
          </li>
          <li class="main-nav__item"><a href="/blog" class="main-nav__link">Blog</a></li>
          <li class="main-nav__item"><a href="/contact" class="main-nav__link">Contact</a></li>
        <?php endif; ?>
      </ul>
    </nav>

    <div class="header-controls">
      <form class="header-search" role="search" action="/search" method="get" aria-label="Recherche du site">
        <label class="sr-only" for="header-search-input">Recherche</label>
        <input id="header-search-input" class="header-search__input" type="search" name="q" placeholder="Rechercher…" aria-label="Rechercher" />
        <button class="header-search__btn" type="submit" aria-label="Lancer la recherche">🔍</button>
      </form>

      <div class="header-cta">
        <a href="/signup" class="btn btn--primary">S'inscrire</a>
      </div>
    </div>
  </div>
</header>

<main id="main" class="site-main" role="main">
  <!-- Page content goes here -->

<!-- Note: include a footer.php to close tags and call wp_footer() if in WordPress -->

<script src="/assets/js/header.js" defer></script>
<?php if (function_exists('wp_footer')) { wp_footer(); } ?>
</body>
</html>
