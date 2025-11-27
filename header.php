<!-- header.php -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $page_title ?? 'MonSite' ?></title>
    
    <!-- Police Google (optionnel mais joli) -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Ton CSS -->
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/header.css"> <!-- si tu veux séparer -->
</head>
<body>

<header class="header">
    <div class="container header__container">
        
        <!-- Logo / Titre -->
        <a href="index.php" class="header__logo">
            MonSite
        </a>

        <!-- Menu desktop -->
        <nav class="header__nav">
            <a href="index.php">Accueil</a>
            <a href="about.php">À propos</a>
            <a href="services.php">Services</a>
            <a href="contact.php">Contact</a>
        </nav>

        <!-- Burger mobile -->
        <button class="header__burger" aria-label="Ouvrir le menu" aria-expanded="false">
            <span></span>
            <span></span>
            <span></span>
        </button>
    </div>

    <!-- Menu mobile (caché par défaut) -->
    <div class="header__mobile-menu">
        <a href="index.php">Accueil</a>
        <a href="about.php">À propos</a>
        <a href="services.php">Services</a>
        <a href="contact.php">Contact</a>
    </div>
</header>

<script>
    // Petit script pour le menu burger (sans jQuery)
    document.querySelector('.header__burger').addEventListener('click', function() {
        this.classList.toggle('active');
        document.querySelector('.header__mobile-menu').classList.toggle('open');
    });
</script>
