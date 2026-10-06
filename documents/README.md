# LLUFAN — Boutique Shopify reconstruite sur la référence de design Doomoo

Ce dossier contient :

| Fichier / dossier | Contenu |
|---|---|
| `LLUFAN-theme-Shopify.zip` | **Thème Shopify importable** (96 fichiers) : sections réglables dans l'éditeur, Liquid, CSS, JS, polices embarquées, visuels de démonstration |
| `theme/` | Le même thème, décompressé (pour lecture, Git, ou `shopify theme push`) |
| `demo/` | Contenus et visuels de la démonstration, **source unique** du contenu du thème et de l'aperçu |
| `LLUFAN-DEMO-mode-emploi.md` | **Mode d'emploi** : import du thème, des produits, des collections et des pages, puis où modifier chaque élément dans Shopify |
| `LLUFAN-DEMO-produits.csv`, `LLUFAN-DEMO-collections.csv` | Fichiers d'import Shopify (10 produits, 28 variantes / 5 collections) |
| `LLUFAN-DEMO-journal-a-publier.md` | 3 articles de blog de démonstration, prêts à coller (Shopify n'importe pas les articles par CSV) |
| `LLUFAN-produit-Nomad-a-importer.csv` | **Fiche produit Nomad** (fiche réelle fournie par LLUFAN) prête à importer |
| `preview/` | **Aperçu statique** : 38 pages cliquables (fichiers autonomes : CSS et polices en ligne, aucune ressource externe) |
| `valider_theme.py`, `valider_shopify.py`, `audit_cta.py` | Contrôles automatiques : balises Liquid, structure des modèles « comme à l'import Shopify », liens et formulaires |
| `build_preview.py`, `generer_demo.py`, `generer_csv_demo.py` | Générateurs (aperçu, modèles du thème, CSV, branchements du mode démonstration) |

---

## 1. Méthode — ce qui a été examiné avant de construire

Le site de référence a été analysé sur son **rendu public**, page par page, en desktop et en mobile :

- **Accueil** : bandeau d'annonce, pré-bandeau, en-tête, héros, bandeau de réassurance (icônes au-dessus du libellé, centrés), section « univers » (grille de 4 cartes collection), carrousel produits + « Voir tout », section vidéo, avis (« Elles en parlent »), bloc éditorial (2 visuels qui se chevauchent), pied de page.
- **Collection** : bandeau visuel panoramique + titre + description, barre d'outils (Filtrer / Trier par / nombre de produits), grille 4 colonnes, bloc « Besoin d'aide ? / Questions fréquentes ».
- **Fiche produit** : galerie (visuel principal + vignettes verticales), ordre des blocs (badges → titre → sous-titre → prix → note → sélecteur de variantes → quantité → bouton → accordéons → description → réassurance), accordéons `UTILISATION / ENTRETIEN / COMPOSITION`, produits associés, produits consultés récemment.
- **Panier** : tiroir latéral (état vide, lignes, sous-total, bouton) **et** page panier (mise à jour, note, commande).
- **États interactifs** : ouverture du menu (tiroir mobile + sous-menus desktop), sélection de variante (pastilles rondes, valeurs indisponibles barrées, mise à jour prix/disponibilité), ajout au panier, filtres (tiroir) et tri (popover), accordéons, carrousels aimantés, apparition au défilement.

Les valeurs ci-dessous ont été **mesurées** (échantillonnage des pixels et lecture des feuilles de style publiques) et non estimées.

### Jetons de design relevés et repris

| Élément | Valeur relevée sur la référence | Repris dans LLUFAN |
|---|---|---|
| Bleu foncé (texte, fonds) | `#1F3462` | identique |
| Bleu des boutons | `#183264` | identique |
| Corail CTA | `#EB735B` | identique |
| Corail doux (pré-bandeau, pastille) | `#F19B84` | identique |
| Pêche (badges) | `#FAC0AA` | identique |
| Sauge (badges) | `#A9CBB6` | identique |
| Lilas (badges) | `#DCC8ED` | identique |
| Étoiles d'avis | `#FAC075` | identique |
| Gris des bandes de section | `#EFEFEF` | identique |
| Sable des cartes | `#E2E0DC` | repris comme fond des visuels manquants |
| Titres | sans-serif géométrique, **capitales**, 600/700 | Jost 600/700 (voir §4) |
| Taille h1 / h2 / h3 / h4 / h5 / h6 | 22→32 / 20→28 / 18→22 / 16→18 / 14 / 12 px | identiques (clamp fluide) |
| Texte courant | serif 14 px, interligne 1,65 | Fraunces 14 px, interligne 1,65 |
| Boutons | rayon 2,5 rem, capitales, interlettrage 0,1 em, min 50 px de haut | identiques |
| Ajout au panier | rayon 2 rem, 16 px, gras | identique |
| Grille produit | 4 colonnes, écart 32 px | identique |
| Image de carte produit | carré 1:1, 2ᵉ image au survol, voile zoom au survol | identique |
| Titre produit (fiche) | 30 px capitales, interlettrage −0,02 em, max 680 px | identique |
| Prix (fiche) | 36 px gras | identique |
| Pastilles de variante | cercles 28 px, écart 8 px | identique |
| Conteneur | 1360 px max, marge 20 px | identique (réglable) |
| Espacement vertical de section | 40 px | identique (réglable) |
| Rayons / ombres | pilules 9999 px ; ombre `0 5px 15px rgb(0 0 0 / .05)` | identiques |

---

## 2. Pages reproduites dans le thème

| Page | Modèle | Sections |
|---|---|---|
| **Accueil** | `templates/index.json` | Héros → Icônes + texte (3) → Cartes de collection (4) → Carrousel produits + « Voir tout » → Vidéo → Avis → Bloc éditorial 2 visuels |
| **Collection** | `templates/collection.json` | Bandeau panoramique (3:1) + titre serif → Barre d'outils (filtrer / trier / compteur) + grille 4 col. + pagination → Questions fréquentes |
| **Fiche produit** | `templates/product.json` | Galerie + vignettes → 13 blocs réordonnables → bloc éditorial → Produits associés → Consultés récemment → bandeau de réassurance et pied de page |
| **Panier** | `templates/cart.json` + `sections/cart-drawer.liquid` | Page panier et **tiroir panier** (mêmes composants) |
| **Recherche** | `templates/search.json` | Barre de recherche, résultats en grille, pagination |
| **Liste des collections** | `templates/list-collections.json` | Grille de cartes collection |
| **Pages d'information** | `templates/page.json` (+ `page.contact.json`) | Titre serif + contenu ; formulaire de contact natif |
| **Blog / article** | `templates/blog.json`, `article.json` | Grille d'articles, article |
| **Compte client** | `templates/customers/*` | Connexion, inscription, mot de passe, compte, commandes, adresses |
| **Protection par mot de passe, carte cadeau, 404** | `templates/password.liquid`, `gift_card.liquid`, `404.json` | — |

En-tête, pré-bandeau, bandeau d'annonce, bandeau de réassurance et pied de page sont des **groupes de sections** (`sections/header-group.json`, `sections/footer-group.json`) : ils s'affichent sur toutes les pages et sont modifiables dans l'éditeur.

**Pied de page** : logo LLUFAN sur sa propre ligne, puis **quatre colonnes** (pastilles d'univers, deux colonnes de liens, raison sociale et mentions légales) et la ligne légale du bas — la référence n'ayant pas de logo dans son pied de page, il occupe une ligne à part et ne décale aucune colonne.

**Tout est réglable depuis l'éditeur Shopify** : couleurs (3 palettes + 6 teintes d'accent), typographie, largeur du conteneur, espacements, format d'image des cartes, seconde image au survol, note, ajout rapide, type de panier, sélecteurs de langue/pays, icônes de paiement — plus les réglages propres à chaque section et bloc.

---

## 3. Contenus LLUFAN à fournir (aucun contenu n'a été inventé)

Chaque champ listé ci-dessous est **volontairement vide** dans le thème. L'aperçu HTML les affiche entre crochets.

> **Mise à jour** — les informations du **prototype LLUFAN** (`llufan-landing-nomad.html`) ont été reprises et préremplies dans le thème : réassurance, raccourcis de l'écosystème, FAQ, textes du pied de page, informations produit, parcours de commande et base de livraison. Détail au **§7**. La liste ci-dessous ne concerne donc que ce qui **reste** à fournir.

**Identité**
- [x] Logo — **reçu** : mot-symbole « Llufan » (en-tête, recoloré encre/blanc) et emblème encadré blanc (pied de page). *Reste souhaitable : le fichier vectoriel (SVG/AI/EPS) pour un rendu parfait à toutes les tailles.*
- [ ] Favicon
- [ ] Palette définitive si différente (l'actuelle est celle mesurée sur la référence)
- [ ] Polices définitives si LLUFAN détient des licences (voir §4)

**Accueil**
- [ ] Héros : photo, sur-titre, titre, libellé + lien du bouton
- [ ] Bandeau d'annonce : 1 à 2 messages (+ liens)
- [ ] Pré-bandeau : 4 raccourcis (libellé, lien, icône)
- [ ] Section « univers » : titre, 4 collections (ou visuels + titres + liens) + badges éventuels
- [ ] Carrousel produits : titre, collection liée, libellé du bouton « Voir tout », badges éventuels
- [ ] Vidéo : titre + lien YouTube/Vimeo
- [ ] Avis : titre + 3 à 5 avis **authentiques** (citation, nom, étoiles)
- [ ] Bloc éditorial : 2 visuels, sur-titre, titre, texte, bouton

**Fiche produit (par produit)**
- [ ] Titre, sous-titre serif, prix en DZD
- [ ] Images des produits et des variantes
- [ ] Options et valeurs de variantes
- [ ] Accordéons : utilisation, entretien, composition
- [ ] Description
- [ ] Badges éventuels (« best-seller », « fabrication »…) — uniquement s'ils sont exacts

**Structure de la boutique**
- [ ] Collections et menus (principal, pied de page, mentions légales)
- [ ] Pages : à propos, livraison, retours, CGV, confidentialité, cookies, FAQ, contact
- [ ] Nom de domaine, e-mails transactionnels, logo de notification

**Réglages Shopify (à ne pas saisir dans le thème)**
- [ ] Devise : **DZD** (confirmé) et marché Algérie
- [ ] **Paiement à la livraison (COD)** : à activer comme moyen de paiement (application ou paiement manuel) — le thème n'affiche aucune icône de paiement tant que l'option est désactivée
- [ ] Frais et délais de livraison, zones desservies, transporteur
- [ ] Politique de retour
- [ ] Mentions de la société (raison sociale, adresse, registre) pour le pied de page

---

## 4. Choix techniques et écarts assumés

1. **Polices.** La référence utilise *Brandon Grotesque* (titres) et *Bogue Regular* (texte), deux polices commerciales dont les fichiers appartiennent à leurs éditeurs — ils n'ont pas été réutilisés. Le thème embarque leurs équivalents libres (licence SIL OFL) : **Jost** pour les titres (géométrique, capitales, même rythme) et **Fraunces** pour le texte (serif classique, même rôle éditorial), avec les mêmes tailles et interlignes. Si LLUFAN détient des licences, il suffit de remplacer les quatre fichiers `assets/*.woff2` et les familles dans `theme.css` : la mise en page ne bouge pas.
2. **Aucune ressource de marque de la référence** n'est présente : ni logo, ni photo, ni texte, ni fichier CSS/JS, ni balisage. Les visuels manquants sont des SVG neutres « Visuel LLUFAN à fournir ».
3. **Icônes** redessinées en SVG simple (style linéaire arrondi observé), stockées dans `snippets/icons.liquid`.
4. **Comportements repris** : en-tête et bandeau collants, tiroirs latéraux (panier, menu, filtres, recherche), carrousels à défilement aimanté avec flèches, sélecteur de variantes qui met à jour prix/disponibilité/état des pastilles, accordéons animés, apparition au défilement, survol zoom des visuels — minutages et courbes identiques à ceux de la référence (voir la table ci-dessous).
5. **Avis** : le thème lit la note via les métadonnées d'avis (`reviews.rating`) et masque l'élément s'il n'y a aucun avis. Aucun témoignage n'est généré. Pour des avis détaillés (widget type Judge.me utilisé par la référence), installer une application d'avis et activer le bloc « Avis » de la fiche produit.

### Logo LLUFAN

Fichier reçu : **1835 × 595 px, PNG à fond transparent, tracé noir**. Le noir
appartient au fichier, pas à la charte : le logo a donc été **recoloré** aux
couleurs de LLUFAN, sans modifier le tracé (le masque du fichier d'origine sert
d'opacité, ce qui conserve l'anticrénelage des lettres).

| Fichier livré | Couleur | Usage |
|---|---|---|
| `assets/llufan-logo-navy.png` | encre `#1F3462` | fonds clairs — **en-tête du site**, par défaut tant que le marchand n'en dépose pas un autre |
| `assets/llufan-logo-white.png` | blanc `#FFFFFF` | fonds foncés — variante du mot-symbole, disponible pour tout autre usage |
| `assets/llufan-logo-footer.png` | blanc `#FFFFFF` | **pied de page** (fond bleu foncé `#1F3462`) — emblème encadré + mot-symbole, d'après le fichier fourni par LLUFAN |

- Le logo a été **recadré sur le tracé** (marges transparentes retirées) : 1699 × 450 px, ratio 3,78:1, 22 Ko par variante.
- **Hauteur affichée** : 30 px dans l'en-tête (26 px sur mobile) ; largeur calculée automatiquement, donc aucun décalage. À 1699 px de large, le logo reste net même sur un écran à très haute densité.
- **Logo du pied de page** : fichier fourni par LLUFAN (blanc sur fond transparent), **marges transparentes retirées** → 700 × 687 px, 23 Ko, ratio conservé. Affiché à **104 px de haut** (88 px sur mobile), soit un mot-symbole d'environ 32 px, lisible ; dimensions bornées par `max-width` / `max-height`, donc tout autre visuel déposé par le marchand reste dans le même gabarit sans déformation.
- **Placement dans le pied de page** : sur **sa propre ligne, au-dessus des quatre colonnes**, aligné à gauche comme elles. Le pied de page de la référence ne comporte pas de logo (3 colonnes de liens + 1 colonne texte) : les quatre colonnes restent donc strictement à leur place et le logo n'en décale aucune.
- **Remplacer** : éditeur de thème → *En-tête* → *Logo*, et *Pied de page* → bloc *Logo*. Un logo déposé dans l'éditeur prend toujours le pas sur les fichiers livrés.
- **Autres variantes** : si LLUFAN veut le logo en corail `#EB735B` (fond sombre) ou en blanc sur photo, la même recolorisation se fait en quelques secondes. Envoyez également le **fichier vectoriel d'origine (SVG, AI ou EPS)** si vous l'avez : le rendu serait alors parfait à toutes les tailles, y compris pour l'impression.

Le logo n'est pas posé sur les autres emplacements (écran de mot de passe, carte
cadeau) : ces gabarits utilisent déjà le nom de la boutique. Dites-moi si vous
voulez la variante blanche sur l'écran de mot de passe.

### Visuel fourni par LLUFAN (photo du coussin Nomad)

`theme/assets/llufan-nomad-coussin.jpg` — **1200 × 896 px, 331 Ko**, déposée
dans le thème. Elle est utilisée à deux endroits :

1. **Héros de l'accueil** — visuel par défaut de la première diapositive tant
   que LLUFAN n'en envoie pas un autre dans l'éditeur (*Héros → Diapositive 1 →
   Visuel*). Les deux autres diapositives restent vides.
2. **Fiche produit** — premier visuel de la galerie dans l'aperçu HTML.

**Résolution.** 1200 px de large : net jusqu'à environ 1500 px d'écran, sans
perte. Au-delà (grands moniteurs 2560 px, bannières), fournir le fichier
d'origine — idéalement **2600 px de large ou plus** — et je remplace l'asset :
la mise en page ne change pas. Aucune retouche n'a été faite sur la photo.

**Cadrage.** Le fichier est au format 4:3 (1200 × 896). Dans le héros, la zone
fait 78 % de la hauteur de la fenêtre ; l'image est donc remplie en « cover »,
c'est-à-dire recadrée légèrement en haut et en bas lorsque la fenêtre est moins
haute que large. Vérifié à 1568 px et à 390 px : le coussin reste entièrement
visible. Si LLUFAN veut un héros plein écran **sans recadrage**, il faut une
variante panoramique (par exemple 3:1, comme le suggère le nom du fichier
d'origine) ; l'affichage sera alors identique à celui observé sur la référence.

**Remplacer la photo.** Éditeur de thème → section *Héros* → diapositive
concernée → *Visuel*. Pour la fiche produit, c'est l'image du produit dans
Shopify (Produits → le produit → Médias).

### Bandeau et en-tête : repris de la page d'atterrissage LLUFAN

Le bandeau d'annonce, le pré-bandeau et l'en-tête suivent désormais la
**page d'atterrissage fournie par LLUFAN** (`llufan-landing-nomad.html`) et non
plus la composition de la référence : ces trois éléments ont été mesurés dans
ce fichier, puis réécrits dans le thème (sections `announcement-bar`,
`preheader`, `header` + styles `6.` et `7.` de `theme.css`).

| Élément | Valeur relevée sur la page LLUFAN | Reprise dans le thème |
|---|---|---|
| Bandeau | bleu foncé `#1F3462`, hauteur 38 px, texte en capitales `.72rem`, interlettrage `.09em`, message centré seul visible | identique ; **message strictement centré sur la largeur de l'écran** (écart mesuré : 0 px de 360 à 1568 px), **sans flèches** (choix LLUFAN), défilement automatique **3,5 s** ; **reste collé en haut pendant tout le défilement** (réglage *Bandeau → Bandeau collant*, actif), l'en-tête venant juste en dessous |
| Pré-bandeau | pêche `#F19B84`, raccourcis centrés, icônes 16 px, texte `.78rem` encre foncée, écart `2.2rem` | identique ; sous 560 px les raccourcis passent en défilement horizontal |
| En-tête | fond blanc à 95 % + flou `blur(10px)`, filet bas 1 px, rangée de 66 px, ombre `0 8px 26px -16px rgba(31,52,98,.28)` dès 8 px de défilement, transition `.3s` | identique |
| Rangée | grille `1fr auto 1fr` : hamburger à gauche (mobile), **logo centré**, icônes à droite (22 px, écart 1rem) | identique ; hauteur du logo réglable (30 px par défaut, 26 px sur mobile) |
| Pastille « MAMA'S CLUB » | corail, `.68rem` en capitales, interlettrage `.08em`, rayon 999 px | identique ; texte et lien réglables, masquée sous 900 px |
| Panier | pastille corail ronde avec le compteur (16 px, en haut à droite de l'icône) | identique ; la pastille passe en corail dès qu'un article est présent |
| Langue | pastille dépliante `<details>` avec chevron, carte blanche, rayon 12 px, ombre `0 14px 34px -14px`, liens `.85rem` | identique, alimentée par les langues publiées dans Shopify ; masquée sous 560 px |
| Navigation | **ligne séparée** par un filet pleine largeur, liens centrés `.8rem` en capitales, interlettrage `.1em`, écart `2.2rem` | identique ; soulignement corail 2 px qui entre de la gauche en `.25s` au survol |
| Bascule mobile | ≤ 900 px : navigation masquée, hamburger affiché, pastille masquée ; ≤ 560 px : sélecteur de langue masqué | identique |
| Composition de l'en-tête | d'après les indications LLUFAN : **logo centré au-dessus de la ligne de navigation**, **pas de trait de séparation** entre les deux, **« MAMA'S CLUB » sur la même ligne que Maternité / Bébé / Nouveautés** (à droite de cette ligne), icônes seules à droite de la rangée du logo | identique ; le logo est centré sur la largeur de l'en-tête (vérifié : centre 784 px pour une fenêtre de 1568 px, à tous les paliers de largeur) |

**Cohérence volontairement conservée** : le **bandeau reste collé** en haut avec l'en-tête (demande LLUFAN) et le **pré-bandeau défile** avec la page ; en position collée, l'en-tête se place automatiquement sous le bandeau (hauteur mesurée par `theme.js`, réglage *Bandeau → Bandeau collant*). Le hamburger ouvre le tiroir plein écran déjà en place sur mobile. Réglages correspondants dans l'éditeur : *En-tête → Comportement au défilement* propose « reste visible, ombre portée » (valeur par défaut : **l'en-tête reste apparent pendant tout le défilement**), « se masque vers le bas » (comportement de la référence) ou « aucun ».

**En-tête au passage à l'achat.** Le réglage *Panier → Masquer l'en-tête au passage à l'achat* (actif par défaut) fait disparaître **le bandeau, le pré-bandeau et l'en-tête** sur la page panier : le client n'a plus que le tunnel d'achat sous les yeux. Ailleurs sur le site, l'en-tête reste visible en permanence, y compris pendant le défilement. Le réglage se désactive en un clic si vous préférez garder l'en-tête sur la page panier.

**Écarts restants sur ces trois éléments**

1. **Police** : la page LLUFAN utilise Poppins (Google Fonts) ; le thème conserve Jost (équivalent libre déjà embarqué) avec les mêmes tailles, graisses, capitales et interlettrages. Un passage à Poppins ne demande que de remplacer le fichier de police.
2. **Flèches du bandeau** : retirées à la demande de LLUFAN. Les messages continuent de défiler seuls (3,5 s) ; dites-le si vous les voulez de retour.
3. **Menu mobile** : le fichier LLUFAN réaffichait la ligne de navigation sous le hamburger ; le thème conserve le tiroir plein écran, déjà aligné sur le reste du site.
4. **Langue** : le fichier simulait le français, l'arabe et l'anglais ; le thème n'affiche que les langues réellement publiées dans Shopify (donc rien tant qu'une deuxième langue n'est pas publiée).
5. **Contenus** : les messages du bandeau, les quatre raccourcis, le texte de la pastille et le menu restent **vides par défaut** (à renseigner dans l'éditeur). L'aperçu HTML, lui, affiche les libellés de la page LLUFAN (LIVRAISON DANS LES 58 WILAYAS, Espace maman, La marque, Pièces détachées, Aide / FAQ, MAMA'S CLUB) pour que la ressemblance soit visible.

### Animations reprises de la référence (étape 3)

Toutes les animations ont été relevées dans le rendu public de la référence
(valeurs mesurées dans ses feuilles de style et ses scripts publics), puis
réécrites dans `assets/theme.css` et `assets/theme.js`. Aucune animation qui
n'existe pas sur la référence n'a été ajoutée, et les fichiers de la référence
ne sont pas réutilisés.

| Élément | Valeur relevée | Implémentation LLUFAN |
|---|---|---|
| Boutons (remplissage) | deux dégradés superposés, `background-size` 101 %→0 puis 0→101 %, `.45 s cubic-bezier(.785,.135,.15,.86)`, `background-position .45 s step-end`, texte et bordure prenant la couleur du bouton ; uniquement pointeur fin | `section 5` de `theme.css` + variantes `--outline`, `--coral`, `--peach`, `--navy` |
| Apparition des cartes produit | `opacity 0→1`, `translateY(20px→0)`, `.2 s ease-in-out`, décalage 0,4 s puis 0,05 s par carte réparti sur `ease-out` (cubic-bezier(0,0,.58,1)) | `<product-list>` de `theme.js` (IntersectionObserver) |
| Zoom lent des visuels | `scale` jusqu'à 1,2 en `8 s cubic-bezier(.25,.46,.45,.94)` au survol, sur pointeur fin | `.features--zoom-image` |
| Diaporama d'accueil | entrée : fondu `.8 s cubic-bezier(.25,.46,.45,.94)`, image `scale 1.2→1`, contenu `translateY(30px→0)` `.6 s` après `.4 s` `cubic-bezier(.215,.61,.355,1)` ; sortie du contenu `.25 s cubic-bezier(.55,.055,.675,.19)` | `<slideshow-carousel>` de `theme.js` |
| Tiroirs (panier, recherche, filtres) | voile et contenu `.3 s cubic-bezier(.645,.045,.355,1)`, glissement `translateX(100 %→0)` | `.drawer` |
| Tiroir de menu (mobile) | plein écran par la droite, entrée `.4 s cubic-bezier(.4,0,.2,1)`, sortie `.3 s` ; panneaux internes `opacity .3 s ease` puis `panelFadeIn .4 s ease` | `.drawer--menu` + `.is-animating-in/out` |
| En-tête escamotable | masqué après 100 px de défilement vers le bas, réaffiché à la remontée ou quand le pointeur revient en haut ; jamais masqué si un menu est ouvert | règle `hide-on-scroll` de `theme.js` |
| Flèches de carrousel | `animateIconInline` / `animateIconBlock` `.35 s ease-in-out`, flèche désactivée à `opacity 0` | `theme.css` |
| Accordéons | hauteur `.25 s ease`, contenu `.15 s` en `translateY(4px→0)`, signe `+` animé | `theme.js` + `span.animated-plus` |
| Chevrons des accordéons (menu mobile) | `transition: transform .2 s ease`, rotation de 90° à l'ouverture | `.drawer-header__accordion summary svg` |
| Quantité | rotation du sélecteur `2.5 s` (720°) pendant l'enregistrement | `quantitySelectorSpinner` |
| Ajout au panier | cercle tracé `.6 s` puis coche `.3 s` après `.4 s`, vert `#22c55e` | `.adding-to-cart` |
| Liens de contenu | soulignement qui se retire au survol, `.3 s ease-in-out` | `.link` |
| Points de pagination | progression circulaire `24 px` sur la diapositive active | `.page-dots` |
| Bandeau d'annonce | fondu par `visibility` `.3 s` entre les messages (les flèches de la référence ont été retirées à la demande de LLUFAN) | `.announcement-bar` |
| Barre de chargement | `scaleX` `.25 s` à la navigation | `<loading-bar>` |

**Non repris, faute de composant correspondant** : `ping` (halo pulsé des
« hotspots » d'image — la référence n'en affiche sur aucune des pages
reproduites) et `marquee-text` (texte défilant infini — absent de ces mêmes
pages). Si LLUFAN ajoute un jour ces composants, les valeurs relevées sont
`.8 s→1 s` en `scale(.8→1)` alterné sur `2 s ease-in-out` pour le halo, et un
défilement `linear` infini dont la durée vaut `1 / vitesse × (largeur / 300)`.

### Différences imposées par Shopify (et non par le design)

| Point | Réalité Shopify | Traitement dans LLUFAN |
|---|---|---|
| Pages de compte, recherche, 404, carte cadeau, mot de passe | Modèles distincts obligatoires | Reproduits avec la même charte |
| Tiroir panier | Nécessite un rafraîchissement de section après ajout | Implémenté en JS (`theme.js`), sans dépendance externe |
| Filtres de collection | Dépendent des filtres réellement configurés dans Shopify | Le bouton « Filtrer » n'apparaît que si des filtres existent |
| Moyens de paiement | Fournis par Shopify selon les passerelles actives | Icônes **désactivées** par défaut ; à activer quand le COD/passerelles seront configurés |
| Vidéo d'accueil | Hébergement YouTube/Vimeo ou fichiers Shopify | Emplacement vide tant que le lien n'est pas fourni |
| Sélecteurs pays / langue | Nécessitent des marchés/ langues publiés | Désactivés par défaut (marché Algérie uniquement) |
| Mentions « Propulsé par Shopify » | Imposée sur certains forfaits | Affichée, activable/désactivable |
| Niveau de fidélité pixel | Un thème Shopify reste modifiable ; certains réglages de la référence (polices commerciales, module d'avis) dépendent de ressources externes | Écart décrit ci-dessus |

---

## 5. Installation et vérification

**Importer le thème**
1. Admin Shopify → *Boutique en ligne* → *Thèmes* → *Ajouter un thème* → *Importer un fichier ZIP* → `LLUFAN-theme-Shopify.zip`.
2. *Personnaliser* : renseigner logo, menus, collections, contenus, puis publier.

**Variante développeur**
```bash
shopify theme dev --store votre-boutique.myshopify.com   # depuis le dossier theme/
```

**Vérifier l'aperçu statique** : ouvrir `preview/accueil.html` (navigation vers `collection.html`, `produit.html`, `panier.html` depuis le menu et les cartes).

---

## 7. Contenus et données repris du prototype LLUFAN

`uploads/llufan-landing-nomad.html` a été traité comme une **source de contenu** (et non comme une maquette) : ses
informations, messages, données produit et logiques commerciales ont été récupérés et replacés dans la structure du
site. **Aucun texte n'a été inventé et aucun code du prototype n'a été copié.**

### Où chaque élément du prototype a été replacé

| Élément du prototype | Emplacement dans le thème |
|---|---|
| « Livraison dans les 69 wilayas », « Paiement à la livraison », « Conçu pour l'allaitement » | Bandeau de réassurance de l'accueil **et** du pied de page (`templates/index.json`, `sections/footer-group.json`), plus la réassurance de la fiche produit |
| Espace maman · La marque · Pièces détachées · Aide / FAQ | Les 4 raccourcis du pré-bandeau et leurs icônes (cœur, étoile, étiquette, enveloppe) — **liens encore à créer** |
| Mama's Club | Pastille de l'en-tête (déjà en place) |
| Français · العربية · English | Sélecteur de langue de l'en-tête (localisation Shopify) |
| Compte · Recherche · Panier · Maternité · Bébé · Nouveautés | En-tête et menu principal (déjà en place) |
| Nomad · Best-seller · Maternité · Coton 100 % · Nouveau · 3 200 DA · Bleu, Rose, Gris | Fiche produit : 4 étiquettes (4ᵉ emplacement ajouté), pastilles aux teintes du prototype (`#8FB4D9`, `#E8A6B8`, `#9A9A9A`), et le fichier d'import `LLUFAN-produit-Nomad-a-importer.csv` |
| Description — les 4 axes | Description du produit (CSV) et fiche produit de l'aperçu |
| Utilisation · Entretien · Composition | Les trois accordéons de la fiche produit, préremplis |
| FAQ — les 3 questions/réponses | Section **Questions fréquentes** sur la fiche produit (`sections/faq.liquid`), 3 blocs préremplis |
| « Parce que / Chaque détail compte » | Bloc éditorial de l'accueil ; un **visuel tertiaire** a été ajouté au bloc pour recevoir la 3ᵉ intention |
| « Essentiels d'allaitement · Algérie · llufan.com » | Texte sous le logo du pied de page |
| « © 2026 Llufan — Paiement à la livraison · Livraison 69 wilayas » | Ligne légale du pied de page (nouveau réglage prérempli ; année et nom de la boutique restent automatiques) |
| « Sans paiement en ligne », « Commande protégée », « Livraison 2 à 5 jours ouvrés », « Partout en Algérie · Paiement à la livraison » | Réassurance et informations sous le formulaire de commande |
| « Merci ! Commande enregistrée. On vous rappelle pour confirmer. » | Message de confirmation du formulaire |
| CTA mobile « Commander » avec le montant | Barre persistante sous 700 px : montant du panier, frais inclus dès que la wilaya est choisie |

### Parcours de commande — paiement à la livraison

Nouvelle section **Commande (paiement à la livraison)** (`sections/commande-livraison.liquid`), placée sur la page
panier : nom complet, téléphone, wilaya, commune, type de livraison (à domicile / stop-desk), puis sous-total, frais
de livraison et total, et le bouton **Commander maintenant**.

- La **wilaya** choisie remplit la liste des **communes**, affiche les tarifs **à domicile** et **stop-desk** et
  calcule le **total** (sous-total du panier + frais). Vérifié dans l'aperçu : `16 - Alger` → 400 DA / 250 DA →
  total 3 600 DA (domicile) puis 3 450 DA (stop-desk).
- À l'envoi, la commande part vers **l'adresse e-mail de la boutique** (formulaire de contact Shopify) : le message
  contient le récapitulatif complet — articles, quantités, variante, nom, téléphone, wilaya, commune, type de
  livraison, sous-total, frais, total. **Aucun paiement en ligne**, et aucun moyen de paiement n'est nécessaire pour
  que le formulaire fonctionne.
- Le bouton de passage en caisse Shopify est **masqué sur la page panier** (réglage *Panier → Afficher le bouton de
  passage en caisse*) ; à réactiver si un paiement en ligne est ajouté un jour.
- Shopify exige une adresse e-mail dans un formulaire de contact : un champ masqué est rempli avec l'adresse de la
  boutique ; l'information utile reste le **téléphone**.
- Si LLUFAN préfère que la commande crée une **vraie commande Shopify** (stock et statuts suivis), il faut activer un
  moyen de paiement « Paiement à la livraison », créer les zones de livraison par wilaya dans l'administration et
  repasser par la caisse — dites-le-moi et j'adapte le parcours.

### Base de livraison Algérie

`assets/llufan-livraison-dz.json` — wilayas et **tarifs repris tels quels du prototype** (jamais recréés) :
**58 wilayas d'origine, passées à 69 le 2026-10-04** (voir plus bas), tarifs **à domicile de 400 à 800 DA**, **stop-desk de 250 à 500 DA**.

**Communes — complétées le 2026-10-04.** Le prototype ne contenait que **327 communes** (2 à 15 par wilaya, soit la
plupart du temps uniquement les principales) : il en manquait donc dans **toutes** les wilayas. Elles ont été
complétées d'après la **liste administrative officielle des 1 541 communes d'Algérie**, sans toucher aux tarifs :

| | Avant | Après |
|---|---|---|
| Communes | 327 | **1 541** |
| Exemples | Tizi Ouzou 7 · Médéa 6 · Batna 7 · Sétif 7 · Alger 15 | **Tizi Ouzou 67 · Médéa 64 · Batna 61 · Sétif 60 · Alger 57** |

- L'orthographe de LLUFAN a été **conservée** quand la commune existait déjà (« Ténès », « Aïn Madhi », « Béjaïa »…) ;
  les communes ajoutées portent le nom de la liste administrative, **sans accents** (« Tenes »-style n'est pas
  introduit, mais « Ain Defla » pourra s'écrire « Aïn Defla » si LLUFAN le souhaite).
- **Astérisques résolus** : les 6 entrées marquées `*` (`Timimoun*`, `Ouled Djellal*`, `In Salah*`, `Touggourt*`,
  `Djanet*`, `Djamaa*`) étaient des communes rattachées à leur **ancienne wilaya** — Timimoun figurait sous Adrar,
  Touggourt sous Ouargla, Djanet sous Illizi, Djamaa sous El Oued, etc. Elles sont désormais rattachées à leur wilaya
  de plein droit (Timimoun → 49, Touggourt → 55, Djanet → 56, Djamaa → 57…) et **plus aucun astérisque ne subsiste**.
- Trois variantes d'orthographe ont été fusionnées au profit de celle du prototype : « Aïn Berda » (Annaba),
  « Aïn El Turck » (Oran), « Bordj Bou Arréridj » ; et **Tabelbala** a été laissée dans **Béni Abbès** (le rattachement
  officiel depuis 2019), et non dans Béchar.
- Contrôle final : **1 541 communes**, et le compte de **chacune des 58 wilayas est conforme au compte officiel**
  (les 11 wilayas issues de la réforme, ajoutées ensuite, sont ajustées sur les mêmes 1 541 communes).
- Les tarifs ne sont **écrits nulle part en dur** : le thème lit ce fichier à l'affichage, une mise à jour des prix se
  fait donc dans un seul fichier.

### 7.1 Passage aux 69 wilayas — décision LLUFAN du 2026-10-04

> **⚠️ Réforme territoriale du 4 avril 2026 (loi n° 26-06, JO n° 25 du 5 avril 2026).** Le découpage passe à
> **69 wilayas** — les **1 541 communes ne changent pas**, elles sont redistribuées. Transition des compétences
> jusqu'au 31 décembre 2026, budgets 2026 exécutés par les wilayas mères.

**Votre réponse : « 69 wilayas maintenant » + « chaque commune reprend le tarif de sa wilaya ».**

Ce qui a été fait dans `assets/llufan-livraison-dz.json` :

| | Avant | Après |
|---|---|---|
| Wilayas | 58 | **69** |
| Communes | 1 541 | **1 541** (inchangées, redistribuées) |
| Mentions dans le thème | « Livraison dans les 58 wilayas » | « Livraison dans les 69 wilayas » (bandeau, réassurance, pied de page) |

Les onze wilayas nouvelles, avec le nombre de communes que la loi leur attribue et la wilaya d'origine dont le tarif
est repris :

| Code | Wilaya | Communes | Tarif repris de | Domicile / Stop-desk |
|---|---|---|---|---|
| 59 | Aflou | 12 | 03 — Laghouat | 600 / 350 DA |
| 60 | Barika | 8 | 05 — Batna | 600 / 350 DA |
| 61 | El Kantara | 5 | 07 — Biskra | 600 / 350 DA |
| 62 | Bir El Ater | 4 | 12 — Tébessa | 600 / 350 DA |
| 63 | El Aricha | 4 | 13 — Tlemcen | 500 / 300 DA |
| 64 | Ksar Chellala | 6 | 14 — Tiaret | 600 / 350 DA |
| 65 | Aïn Oussara | 10 | 17 — Djelfa | 600 / 350 DA |
| 66 | Messaad | 8 | 17 — Djelfa | 600 / 350 DA |
| 67 | Ksar El Boukhari | 21 | 26 — Médéa | 400 / 250 DA |
| 68 | Bou Saada | 23 | 28 — M'Sila | 600 / 350 DA |
| 69 | El Abiodh Sidi Cheikh | 7 | 32 — El Bayadh | 800 / 500 DA |

**Ces onze tarifs sont provisoires** : ils sont recopiés de la wilaya d'origine, et chaque entrée le porte
(`note_tarif`) pour qu'aucun tarif ne soit pris pour une donnée validée. Un tarif propre par wilaya se saisit dans
le même fichier ; donner les onze montants suffit.

**Comment les 108 communes transférées ont été identifiées.** Le thème utilisait la liste des 1 541 communes
réparties sur 58 wilayas ; le découpage officiel à 69 a été apparié commune par commune, sous contrôle du nombre de
communes de chaque wilaya (12, 8, 5, 4, 4, 6, 10, 8, 21, 23, 7 — toutes conformes). Neuf communes portent un
**nom différent** dans les deux listes ; l'appariement s'est fait après vérification de leur identité :

| Nom officiel (réforme) | Nom utilisé dans le thème | Vérification |
|---|---|---|
| Beidha | El Beidha | même commune (Laghouat) |
| Metkaouak | Azil Abedelkader | commune renommée en 1993 (daïra de Djezzar) |
| El Bouihi | Bouihi | même commune (Tlemcen) |
| Meftaha | M'fatha | même commune (Médéa) |
| Deux Bassins | El Haoudane | même commune (daïra de Tablat, codes ONS 2636/2653) |
| Ouled Maaref | Ouled Emaaraf | variante d'écriture |
| Sidi Damed | Sidi Demed | variante d'écriture |
| Oued Chair | Mohamed Boudiaf | commune renommée en 1992 |
| Ouled Atia | Menaa | commune renommée |

Le nom **du thème** a été conservé partout (c'est celui que voient vos clients), sauf pour les communes qui
n'existaient pas encore dans la liste. Les homonymes inter-wilayas (« Menaa », « Sidi Ameur », « Deldoul »,
« El Ogla », « Bougara », « Aïn Fares », « Sidi M'hamed ») ont été traités **par wilaya** : seul l'exemplaire
concerné par la réforme a changé de wilaya, les autres sont restés en place.

### Informations signalées comme provisoires

| Information | Traitement retenu |
|---|---|
| Composition — « Garnissage : microbilles moelleuses et modulables… » | Affichée, suivie d'une mention en italique *« Composition à confirmer : information provisoire, en attente de la fiche produit définitive. »* — à retirer dès réception de la fiche définitive |
| FAQ — « 2 à 5 jours ouvrés selon la wilaya » | Affiché avec la mention *« Délai à confirmer selon le transporteur. »* |
| FAQ — échange sous 7 jours | Repris du prototype (qui ne le signalait pas comme à valider) — **à valider par LLUFAN** avant publication : une politique de retour erronée engage la boutique |

### Reste à faire pour que ce parcours soit complet

- [ ] **Relier les 4 raccourcis** du pré-bandeau (Espace maman, La marque, Pièces détachées, Aide / FAQ) : libellés en place, liens vides
- [ ] Créer les pages correspondantes (aide/FAQ, livraison & retours, à propos) et les menus du pied de page
- [ ] **Importer** `LLUFAN-produit-Nomad-a-importer.csv`, ajouter les **photos**, renseigner le **stock et le poids**, puis publier
- [ ] Confirmer : composition du garnissage, délai transporteur, règle d'échange, signification des 6 astérisques
- [ ] Traductions **العربية** et **English** : le sélecteur est en place, les textes restent à activer et traduire (thème livré en français)
- [ ] Adresse e-mail de la boutique dans les réglages Shopify : c'est elle qui reçoit les commandes

---

## 6. Points à confirmer par LLUFAN

1. **Contenus existants ?** Le site public `llufan.com` présente déjà des produits (Nomad — coussin d'allaitement 3 200 DA, Poncho d'allaitement 2 200 DA, Housse de rechange Nomad 1 200 DA) et un paiement à la livraison. Ces informations **n'ont pas été importées** : elles n'ont pas été fournies et je ne crée pas de produits à votre place. Dites-moi si je dois les reprendre comme contenus de référence.
2. **Devise et paiement** : DZD + COD confirmés pour la configuration ; reste à préciser si un paiement en ligne (CIB / Edahabia) doit être prévu.
3. **Livraison et retours** : non configurés (frais, délais, transporteur, zones, politique de retour) — à fournir avant publication.
4. **Nom commercial et mentions légales** : raison sociale, adresse, registre de commerce pour le pied de page.
5. **Bandeau, pré-bandeau et en-tête** : fournir les messages du bandeau (les trois de votre page d'atterrissage ?), les quatre raccourcis, le texte et le lien de la pastille, et le menu de la ligne de navigation.
6. **Palette et polices définitives** : je suis resté sur les valeurs mesurées sur la référence ; si LLUFAN veut sa propre palette, elle se change en un écran (réglages du thème).
7. **Sous-menus du menu mobile.** La référence ouvre les sous-menus dans des « panneaux » plein écran qui se remplacent (fondu `panelFadeIn`), alors que le thème LLUFAN déplie les sous-menus sur place en accordéon (la même animation de panneau y est appliquée au contenu). Le rendu visible — rangées en capitales, chevrons, séparateurs, tiroir plein écran venant de la droite avec les mêmes minutages — est identique ; dites-moi si vous voulez aussi le remplacement de panneaux.
8. **Bas de page de la référence** : la page panier de la référence n'affiche pas de module de paiement visible dans les captures transmises ; le parcours COD sera donc à valider sur votre boutique une fois le moyen de paiement activé.
- ~~**Découpage territorial** : rester sur 58 wilayas ou passer aux 69 wilayas~~ → **tranché le 2026-10-04 : 69 wilayas** (voir §7.1).

---

## 8. Parcours d'achat raccourci et points de conversion (ajout du 4 octobre 2026)

Demande : « que la page et le site soient ultra convertisseurs et simplifier les étapes à l'achat ».
Le parcours est passé de **4 écrans à 2** : *fiche produit → formulaire sur place*. Rien n'a été inventé pour autant : aucun moyen de paiement nouveau, aucune promesse de livraison ou de délai.

### 8.1 Ce que voit le client

| Avant | Maintenant |
| --- | --- |
| Fiche produit → Ajouter au panier → Tiroir panier → Caisse Shopify → Formulaire | **Fiche produit → Commander maintenant → Formulaire** (envoyé à la boutique) |
| Le tiroir panier menait à la caisse Shopify (inutilisable en COD) | Le tiroir panier mène à la **page panier**, qui contient le formulaire de commande |
| — | **Barre « Commander » collante en mobile** sous 700 px, qui amène au formulaire |
| Panier : lignes → sous-total → « Mettre à jour » → formulaire (sous-total répété) | Panier : **lignes, « Mettre à jour » discret, puis le formulaire** (sous-total, frais et total affichés une seule fois) |

Le panier reste en place pour les commandes de plusieurs articles : c'est la seule partie du parcours qui n'a pas été raccourcie, parce que le formulaire de commande ne porte qu'un produit à la fois. Il a tout de même été allégé : le sous-total n'y est plus affiché deux fois (le formulaire le porte), « Mettre à jour » est passé en lien discret sous les articles, et le bouton « Commander » du tiroir ouvre **directement le formulaire** de la page panier (ancre `#commander`) au lieu du haut de page.

### 8.2 Réglages correspondants (modifiables dans l'éditeur Shopify)

- `main-product` → bloc **Buy buttons** : « Afficher un raccourci « Commander maintenant » au-dessus du formulaire » (`cta_direct`, **désactivé** par défaut, car le formulaire est juste en dessous) et son libellé (`cta_direct_label`). « Ajouter au panier » reste en bouton contour dans tous les cas.
- `main-product` → bloc **Commande** (8e position, après les boutons) : titre, libellé du bouton, barre mobile.
- `cart-drawer` → « Afficher le bouton de caisse » (`show_checkout_button`, désactivé par défaut) et libellé `cta_label` (« Commander » → page panier, ancrée sur le formulaire).
- `main-cart` → « Afficher le sous-total au-dessus du formulaire » (`show_subtotal`, désactivé par défaut), « Afficher “Mettre à jour” » (`show_update_button`, activé) et « Afficher le bouton de passage en caisse Shopify » (`show_checkout_button`, désactivé par défaut).
- Section **Commande — livraison DZ** (`commande-livraison`) : uniquement sur `cart`.
- Composant partagé `snippets/forme-commande.liquid` (modes `produit` / `panier`).

### 8.3 Conversion — ce qui a été fait, uniquement à partir de vos données

- **Un seul formulaire, sur place**, sans changer de page : nom, téléphone, wilaya → commune → tarif, type de livraison, sous-total / frais / total visibles en continu.
- **Le prix suit la variante et la quantité** dans le formulaire produit (couleur et quantité choisies sur la fiche produit sont reprises, sous-total recalculé en direct).
- **Réassurance** au-dessus du bouton : « Sans paiement en ligne », « Commande protégée » et le délai marqué provisoire.
- **Confirmation en place** après envoi : le client voit le récapitulatif de sa commande sans quitter la page.
- **Barre mobile collante** : le total et « Commander » restent accessibles ; elle s'efface d'elle-même quand le bouton du formulaire est déjà à l'écran (pour ne pas doubler le bouton).
- **L'en-tête reste visible** au défilement et il ne disparaît qu'à l'arrivée sur la page panier.

### 8.3 ter Le bloc de commande reprend le dessin de la page d'atterrissage LLUFAN

Le formulaire fonctionnait, mais son habillage était celui du thème (champs arrondis en pastille, bouton bleu foncé, séparateurs fins), alors que la page d'atterrissage fournie met le bloc de commande en avant autrement. C'est ce dessin-là qui a été repris, valeurs relevées dans le fichier :

| Élément | Page d'atterrissage LLUFAN | Thème, maintenant |
| --- | --- | --- |
| Carte | rayon 14 px, ombre `0 24px 50px -35px rgba(31,52,98,.3)` | identique |
| En-tête du bloc | fond bleu foncé, texte blanc, capitales, .85 rem, lettres espacées | identique |
| Bouton d'envoi | **corail** `#EB735B`, pastille, texte blanc | identique (était bleu foncé) |
| Lignes de totaux | encadré crème `#FBF7F2`, filet **pointillé**, rayon 8 px | identique (était des lignes nues) |
| Total | 1.1 rem, gras, filet plein au-dessus | identique |
| Choix de livraison | deux tuiles côte à côte, cadre 1,5 px, **corail + fond pêche `#FDF1EC`** sur l'option cochée | identique (était en pastille grise) |
| Étiquettes de champs | casse normale, .8 rem, semi-gras | identique (étaient en capitales espacées) |
| Champs | rayon 8 px, filet 1,5 px | identique |
| Réassurance | « ✓ » corail + texte gris bleuté | identique |
| Confirmation | fond vert `#E7F3EA`, texte `#2f6b3f` | identique |
| Barre mobile | pastille corail + montant | identique (était bleu foncé) |

Le formulaire porte aussi les exemples de saisie de la page d'atterrissage (« Nom et prénom », « 05 / 06 / 07 … ») : ils aident à remplir, ils n'affirment rien.

**Un doublon supprimé au passage.** La fiche produit affichait deux fois « Commander maintenant » : un bouton qui **ne faisait que défiler** jusqu'au formulaire, puis le bouton du formulaire lui-même. Le premier est désormais **désactivé par défaut** (`cta_direct`), et « Ajouter au panier » reste en bouton contour, juste sous les champs de choix : le parcours est **une seule action visible** — choisir la couleur et la quantité, puis remplir le formulaire juste en dessous.

### 8.3 bis Deux corrections de fond apportées après vérification visuelle

1. **Le visuel de la fiche produit suit le défilement** (au-dessus de 1000 px de large). La fiche est devenue longue — le formulaire de commande y est intégré — et la colonne d'informations dépasse largement la hauteur du visuel : sans cela, la moitié gauche de l'écran restait vide pendant toute la lecture. La mesure faite sur la référence donne l'inverse : chez Doomoo, c'est la colonne d'informations qui est collante (`.product-info`, `position: sticky`, `top: 64px`), parce que sa colonne d'informations est courte. Ici, c'est donc le visuel qui reste — la position collante est reprise, l'élément qui la porte est celui qui a du sens avec ce contenu.
2. **`--sticky-area-height` n'était jamais renseigné.** Le thème composait cette variable (`calc(bandeau × hauteur + en-tête × hauteur)`) mais aucune section ne publiait les deux indicateurs qui la composent : elle valait donc toujours `0`, en boutique comme dans l'aperçu. Les sections **Bandeau** (`--announcement-bar-is-sticky`) et **En-tête** (`--header-is-sticky`, qui passe à 0 sur la page panier quand l'en-tête est masqué au passage à l'achat) les publient désormais. Conséquence visible : le visuel de la fiche se cale juste sous l'en-tête au défilement, et les autres éléments collants calculés sur cette variable sont enfin corrects.

### 8.4 À valider par LLUFAN sur ce parcours

1. La commande arrive par e-mail à l'adresse de la boutique (formulaire de contact Shopify). **Confirmez que c'est acceptable** : sinon il faut passer par une application de commande, ce qui sort du thème.
2. Le client ne reçoit pas d'e-mail de confirmation automatique (Shopify n'en envoie pas pour un formulaire de contact) — dire si c'est à prévoir.
3. Une seule commande par produit : le multi-articles passe toujours par le panier.
4. Aucune promesse affichée n'a été ajoutée : « paiement à la livraison » et « 69 wilayas » viennent de vos informations ; le délai reste entre crochets tant que le transporteur n'est pas confirmé.

---

## 9. Pied de page (refonte du 4 octobre 2026)

Le pied de page est traité comme une partie du site à part entière : identité, navigation, contact, réassurance, réseaux et mentions légales, avec la même exigence de finition que le reste.

### 9.1 Composition

| Zone | Contenu | État |
| --- | --- | --- |
| Identité | Logo blanc encadré + **LLUFAN** + « Une marque algérienne dédiée au confort de la maman et du bébé. » | **fourni, affiché** |
| Colonne **LLUFAN** | La marque · Contact · FAQ | libellés en place, **adresses à renseigner** |
| Colonne **Nos univers** | Maternité · Allaitement · Bébé · Nouveautés | libellés en place, **adresses à renseigner** |
| Colonne **Aide** | Livraison · Paiement · Échanges et retours · FAQ | libellés en place, **adresses à renseigner** |
| Contact | « Contactez-nous sur WhatsApp » + **0772 415 120** (lien `https://wa.me/213772415120`) et **contact@llufan.com** (`mailto:`) | **fourni, affiché et fonctionnel** |
| Réassurance | Livraison partout en Algérie · Paiement à la livraison · Service client LLUFAN | **fourni, affiché** — rangée secondaire, plus discrète que la navigation |
| Réseaux sociaux | Emplacements Facebook, Instagram, TikTok | **vides** : les icônes n'apparaissent que si l'adresse est renseignée (aucun lien fictif) |
| Mentions légales | Mentions légales · CGV · Politique de confidentialité · Politique de retour / échange | libellés en place, **pages et adresses à fournir** |
| Copyright | « © 2026 LLUFAN. Tous droits réservés. » puis « Algérie · llufan.com » | **fourni, affiché** |

**Règle appliquée** : un lien n'apparaît **que** si son adresse est renseignée dans l'éditeur. Il n'existe donc aucun lien menant à une page inexistante : dans l'état actuel, les trois colonnes sont affichées en libellés, et dès que vous collez l'adresse d'une page, le lien devient cliquable — sans autre intervention.

### 9.2 Numéro WhatsApp et e-mail centralisés

Les deux valeurs sont des **réglages du thème**, rubrique **« Contact et identité LLUFAN »** (`config/settings_schema.json`) :

| Réglage | Valeur livrée |
| --- | --- |
| Numéro WhatsApp | `0772 415 120` |
| Libellé du contact | `Contactez-nous sur WhatsApp` |
| Message prérempli | *(vide)* |
| Adresse e-mail de contact | `contact@llufan.com` |
| Nom de la marque | `LLUFAN` |
| Phrase de présentation | `Une marque algérienne dédiée au confort de la maman et du bébé.` |

Le lien WhatsApp **n'est pas écrit en dur** : il est calculé à partir du numéro par `snippets/whatsapp.liquid`, et l'e-mail par `snippets/courriel.liquid`. Ces deux composants sont les **seuls** endroits autorisés à produire ces valeurs, et le pied de page, la page contact et tout futur bouton de contact les appellent. Changer le numéro dans les réglages met donc à jour **toutes** ses occurrences et **le lien en même temps** : les deux ne peuvent pas se désynchroniser.

Le calcul du lien a été testé sur toutes les écritures plausibles d'un numéro algérien :

| Saisie | Lien produit |
| --- | --- |
| `0772 415 120` | `https://wa.me/213772415120` |
| `0772415120` | `https://wa.me/213772415120` |
| `+213 772 415 120` | `https://wa.me/213772415120` |
| `00213 772 415 120` | `https://wa.me/213772415120` |
| champ vidé | rien n'est affiché (aucun lien mort) |

> Correction faite au passage : le message prérempli était encodé **après** avoir été ajouté à l'adresse, ce qui abîmait l'adresse entière. Le message est maintenant encodé seul : `https://wa.me/213772415120?text=Bonjour+LLUFAN%2C+je+souhaite+commander.`

### 9.3 Nouveaux fichiers et réglages

- `snippets/whatsapp.liquid` — lien WhatsApp, numéro affiché, bouton (modes `lien`, `numero`, `texte`, `bouton`).
- `snippets/courriel.liquid` — adresse e-mail et lien `mailto:`.
- `sections/footer.liquid` — réécrit : blocs **Marque**, **Colonne de navigation** (6 liens, affichés seulement s'ils sont renseignés), **Contact**, **Réassurance** ; réglages pour les quatre mentions légales ; réglages `copyright_text` et `copyright_line`.
- `sections/main-contact.liquid` — le bouton WhatsApp et l'adresse e-mail sont placés **avant** le formulaire.
- `templates/page.faq.json` — gabarit de la page FAQ (le contenu vient de la section « Questions fréquentes ») : créez une page dans Shopify, choisissez ce gabarit, puis collez son adresse sur les deux liens « FAQ ».
- Réseaux sociaux : réglages déjà présents (`social_facebook`, `social_instagram`, `social_tiktok`) — **vides**, à renseigner.

### 9.4 Ce qu'il reste à fournir pour finir le pied de page

1. **Les pages** : La marque, Contact, FAQ, Livraison, Paiement, Échanges et retours — puis leurs adresses dans les trois colonnes.
2. **Les comptes** Facebook, Instagram, TikTok de LLUFAN.
3. **Les textes juridiques** : mentions légales, CGV, politique de confidentialité, politique de retour / échange — je ne les rédige pas.
4. **Le logo officiel du pied de page** si celui livré (celui de votre fichier blanc) doit être remplacé ; sinon il reste tel quel.

### 9.5 Optimisation de la hauteur (même jour)

Le pied de page tenait tout, mais occupait trop de place. Il a été resserré **sans retirer une seule information** :

| | Avant | Après | Après le passage au logo seul (9.6) |
| --- | --- | --- | --- |
| Ordinateur (1400 px) | 492 px | 392 px | **385 px** |
| Ordinateur (1200–1280 px) | 492 px | 395 px | **385 px** |
| Petite tablette (1024–1100 px) | 576 px | 411 px | **407 px** |
| Tablette (940 px) | 576 px | 500 px | **475 px** |
| Tablette (768 px) | — | 649 px | **633 px** |
| Mobile (390 px) | 1 401 px | 844 px | **841 px** |

Toutes les largeurs de 390 à 1400 px ont été remesurées après le changement de logo (colonne « Après le passage au logo seul ») : aucune n'a augmenté.

Ce qui a changé :

- **Rythme vertical resserré** : espacements internes et hauteur du logo réduits, phrase de présentation sur deux lignes maximum, colonnes de liens plus serrées.
- **Titre « Nos engagements » passé en lecture d'écran** : la ligne reste utile à la structure de la page, mais n'occupe plus de place à l'écran — les trois engagements se lisent d'eux-mêmes.
- **Colonnes repliables en mobile** : les trois colonnes de navigation deviennent des accordéons (LLUFAN, Nos univers, Aide). Le contenu reste **entier et accessible**, mais la page reste courte. Si une page n'a pas de script, les accordéons restent ouverts : rien ne devient inaccessible.
- **Ligne du bas réorganisée** : copyright sur deux lignes, mentions légales à gauche, sélecteurs et « Propulsé par Shopify » à droite — une ligne de moins.
- **Trois paliers de grille** au lieu d'un : cinq colonnes au-dessus de 1200 px, cinq colonnes plus serrées de 940 à 1199 px, puis repli progressif. Auparavant, la plage 1024–1199 px passait à quatre colonnes et faisait **s'allonger** le pied de page (576 px contre 392 px en grand écran) : c'était le défaut principal.

Contrôle à sept largeurs d'écran, sans aucun lien coupé sur deux lignes et sans accordéon ouvert par défaut.

### 9.6 Logo transmis seul et respect de la charte typographique (même jour)

Deux demandes : « ne laisser que le logo transmis » et « respecter la charte de polices du site ».

**Le logo.** Le pied de page n'affiche plus que le fichier fourni (`uploads/llufan_logo_blanc.png`, livré sous `assets/llufan-logo-footer.png`) : le nom « LLUFAN » qui était recomposé en texte à côté du logo a été retiré. L'identité du pied de page repose donc entièrement sur le logo transmis, comme sur une signature. Sa hauteur maximale est de 80 px (72 px de 940 à 1199 px pour que la colonne de marque ne dicte pas la hauteur du pied de page, 74 px en mobile) : le pied de page reste plus court qu'à l'étape 9.5 à toutes les largeurs.

La phrase « Une marque algérienne dédiée au confort de la maman et du bébé. » reste sous le logo : c'est le texte d'identité validé à l'étape 13, en **style texte** (serif), pas en style titre.

**La charte des polices.** Le site n'utilise que deux familles : `LLUFAN Sans` (Jost) pour les titres, les libellés et les liens, `LLUFAN Serif` (Fraunces) pour les textes rédigés. Le pied de page était le seul endroit où des liens reprenaient la police du texte par héritage. C'est corrigé :

| Élément du pied de page | Police | Graisse | Taille |
| --- | --- | --- | --- |
| Logo (image) | — | — | 80 px de haut |
| Phrase de présentation | LLUFAN Serif | 400 | 13 px |
| Titres de colonne (LLUFAN, Nos univers, Aide, Contact) | LLUFAN Sans | 600 | 12 px |
| Liens de colonne | LLUFAN Sans | 500 | 13 px |
| Contact WhatsApp (libellé et numéro) | LLUFAN Sans | 400 / 600 | 13 px |
| Engagements de réassurance | LLUFAN Sans | 500 | 13 px |
| Mentions légales | LLUFAN Sans | 500 | 12 px |
| Copyright | LLUFAN Serif | 400 | 12 px |
| Sélecteur de devise | LLUFAN Sans | — | 11 px |

Contrôles faits sur l'aperçu : tous les éléments du pied de page sont dans l'une des deux familles du site, aucune déclaration `font-family` hors charte dans le bloc « pied de page » du CSS (11 déclarations, toutes `var(--heading-font-family)`), aucun style en ligne dans `sections/footer.liquid`, et aucune hauteur de pied de page dégradée.

Vérification automatisée du thème (script `valider_theme.py`, livré à côté du thème) : **48/48 fichiers Liquid** équilibrés, tous les snippets appelés existent, tous les réglages de section sont déclarés, 18 fichiers JSON valides.

**Un point à confirmer :** la phrase de présentation sous le logo. Si l'intention était « uniquement le logo, rien d'autre » dans le bloc de marque, elle part d'un mot et il ne reste que l'image ; si elle reste, le pied de page garde son texte d'identité validé.

## 10. Vérifications de fidélité (même jour)

Trois points restaient en suspens depuis l'analyse d'origine. Ils sont tranchés par la mesure, pas au jugé.

### 10.1 Les deux sections d'application de l'accueil

L'accueil de la référence contient **deux sections produites par une application**, en plus des sections du thème : `ai-reassurance-slider` (bandeau de réassurance, juste après le héros) et `ai-image-grid` (« Votre moment, votre univers ♡ », quatre tuiles avec pastille et bouton « Découvrir »). Ce ne sont pas des sections du thème de la référence ; elles sont donc traitées comme des modèles à reproduire, et non à copier.

| | Référence (application) | Thème LLUFAN |
| --- | --- | --- |
| Bandeau de réassurance | `flex`, colonne centrée de **900 px** au plus, **20 px** entre les items, items de **280 px** au plus, icône **au-dessus** du libellé | `section type="text-with-icons"` avec `stacked: true` : mêmes valeurs (900 px / 20 px / 280 px), icônes du site |
| Tuiles « univers » | 4 tuiles (pastille + « Découvrir ») | `section type="featured-collections"` : 4 cartes collection (pastille + bouton) |

Ce qui diffère, et pourquoi :

- **Icônes** : la référence utilise des visuels de **100 × 100 px** ; le thème garde ses icônes au trait de 34 px, dans la couleur d'accent du site. Un visuel 100 × 100 px n'étant pas fourni par LLUFAN, agrandir un trait fin aurait donné un rendu pauvre.
- **Mobile** : la référence fait défiler le bandeau **horizontalement** ; ici les trois arguments s'empilent, **tous visibles sans geste**. C'est un choix de conversion (étape 10) : aucun des trois messages ne doit être caché.
- **Comportement** : les sections d'application n'ont pas de réglages dans l'éditeur Shopify ; les nôtres en ont (icône, titre, sous-titre, disposition, espacement, trait) et sont donc modifiables par LLUFAN.

### 10.2 Le bandeau de réassurance du bas de page

La référence a **deux** bandeaux distincts : celui de l'application après le héros (icône au-dessus) et celui du thème, juste avant le pied de page (`text-with-icons`, icône **à gauche**, deux lignes de texte). Le nôtre reprend le second tel quel sous forme de section `text-with-icons` en disposition « icône à gauche », affichée avant le pied de page sur toutes les pages — et l'accueil utilise la disposition empilée pour le bandeau de tête, exactement comme la référence. Les deux dispositions sont donc désormais celles observées, chacune à sa place.

### 10.3 La page panier : ce que la référence montre vraiment

La page `/cart` de la référence a été capturée **panier vide**. Sa structure utile est donc exactement celle-ci :

```html
<div class="container container--xs">      <!-- 42,5 rem = 680 px -->
  <div class="empty-state">
    <div class="prose">
      <h1 class="h4">Panier</h1>
      <p>Votre panier est vide</p>
      <a class="button" href="/collections/all">Explorer nos produits</a>
```

Ce que le thème a repris : la **colonne étroite de 680 px** (`.container--xs`), le **titre au niveau `h1` à la taille des titres de section** (`--text-h4`, soit 16 px en mobile et 18 px en desktop), et le regroupement titre + message + bouton dans un même bloc centré.

Ce qui diffère : la référence laisse **100 px de vide en mobile et 200 à 250 px en desktop** au-dessus et au-dessous du bloc. Le thème garde **40 px en mobile et 56 px en desktop** — l'espace vide avait été explicitement refusé à l'étape 12, et un panier vide n'est pas l'endroit où l'ajouter.

Pour le **panier rempli**, la référence n'offre **aucun modèle** : la capture a été faite panier vide. La page remplie suit donc les composants du thème (ligne d'article, mise à jour discrète) et le parcours de commande choisi à l'étape 10 : le formulaire de commande sur place, sous-total, frais et total. Il n'y a rien à comparer, et c'est écrit ici pour que personne ne croie à une omission.

### 10.4 Aperçus et contrôles

- **Nouvelle page d'aperçu** `preview/panier-vide.html` : l'état panier vide existait dans le thème mais n'était pas montré. Il l'est maintenant.
- **Icônes des aperçus** : les bandeaux de réassurance affichaient un caractère de remplacement (`▭`). Ils utilisent désormais les **mêmes icônes SVG que le thème** (livraison, paiement, cœur, cadenas) — l'aperçu et la boutique montrent la même chose.
- **Contrôles automatisés** (voir `valider_theme.py`) : 48/48 fichiers Liquid équilibrés, tous les snippets appelés existent, tous les réglages de section déclarés, 18 fichiers JSON valides.
- **Contrôles d'affichage** sur les cinq pages d'aperçu à 1400, 768 et 390 px : aucune image cassée, aucune icône manquante, aucune erreur JavaScript, et les hauteurs de pied de page de l'étape 9.6 inchangées (385 / 633 / 841 px).

## 11. Boutons et CTA : une destination pour chacun (même jour)

Chaque bouton, chaque lien et chaque formulaire du thème a été passé en revue. La règle appliquée distingue trois familles, parce qu'elles n'ont pas les mêmes exigences :

1. **Les CTA d'achat** (fiche produit, collections, catalogue, panier) doivent toujours mener quelque part. Destination : l'objet choisi dans l'éditeur, sinon le lien saisi à la main, sinon le **catalogue** (`/collections/all`, que Shopify génère automatiquement). Un client ne tombe donc jamais sur un bouton inerte.
2. **Les liens de service ou éditoriaux** (raccourcis du pré-bandeau, pastille de l'en-tête, mentions légales, réseaux sociaux) ne s'affichent **comme liens que si leur destination existe**. Sinon le texte reste visible mais n'est pas cliquable — la même règle que pour les colonnes du pied de page (étape 13). Aucune page n'est inventée.
3. **Les CTA de commande** utilisent des **ancres internes vérifiées** : `#commande-produit` sur la fiche (le formulaire de commande sur place), `#commander` et `#commande-panier` sur la page panier. Les ancres sont produites par le même fichier que le formulaire : elles ne peuvent pas diverger.

### 11.1 Ce qui a été corrigé

| Élément | Avant | Maintenant |
| --- | --- | --- |
| Cartes « univers » | `href="#"` quand aucune collection n'était choisie | collection → lien manuel → catalogue |
| « Voir tout » du carrousel | lien vide si ni bouton ni collection | lien → collection → catalogue |
| Bouton du bloc éditorial | `href="#"` | lien saisi → catalogue |
| Bouton d'une diapositive du héros | `href="#"` | lien saisi → catalogue |
| Pré-bandeau (4 raccourcis) | `href="#"` | lien si renseigné, sinon texte non cliquable |
| Pastille de l'en-tête | `href="#"` | lien si renseigné, sinon texte non cliquable |
| Bouton contact de la FAQ | `routes.contact_url`, **qui n'existe pas** dans l'objet `routes` de Shopify (l'attribut `href` sortait vide) | lien saisi → page « contact » si elle existe → WhatsApp → bouton masqué |

Le point sur `routes.contact_url` mérite d'être noté : c'est une erreur classique qui ne se voit pas à la lecture du code. L'objet `routes` de Shopify contient dix-neuf propriétés (`cart_url`, `root_url`, `search_url`…) et **aucune** `contact_url` ; l'attribut sortait donc vide, c'est-à-dire un lien qui recharge la page courante. Vérifié sur la documentation Shopify le 4 octobre 2026.

### 11.2 La table des destinations

| Bouton ou lien | Destination | État |
| --- | --- | --- |
| Logo (en-tête, pied de page) | Accueil | Connecté |
| Carte produit (visuel, titre) | Fiche produit | Connecté |
| « Ajouter au panier » | Panier Shopify (formulaire d'ajout) | Connecté |
| « Commander maintenant » | Formulaire de commande de la fiche (`#commande-produit`) | Connecté |
| Barre mobile collante « Commander » | `#commande-produit` ou `#commande-panier` | Connecté |
| Cartes « univers » | Collection, lien manuel ou catalogue | Connecté |
| « Voir tout » du carrousel | Lien, collection ou catalogue | Connecté |
| Bloc éditorial · diapositive du héros | Lien saisi ou catalogue | Connecté |
| Titre d'article du panier | Fiche produit | Connecté |
| Tiroir panier : « Commander », « Voir le panier », « Continuer mes achats » | Page panier (+ ancre `#commander`), page panier, catalogue | Connecté |
| Panier vide : « Continuer mes achats » | Catalogue | Connecté |
| Icône panier (en-tête) | Page panier, avec ouverture du tiroir | Connecté |
| Icône recherche | Tiroir de recherche → page de recherche | Connecté |
| Icône compte | Page compte — **réglage** pour la masquer si les comptes clients sont fermés | Connecté |
| Flèche du héros | Section suivante (`#section-after-hero`) | Connecté |
| Bandeau d'annonce | Lien s'il est renseigné, sinon texte | Connecté |
| Bouton contact de la FAQ (pages collection, produit, panier) | Lien → page « contact » → WhatsApp | Connecté |
| WhatsApp (pied de page, page contact) | `https://wa.me/213772415120` | Connecté |
| E-mail | `mailto:contact@llufan.com` | Connecté |
| Partage produit (Facebook, Pinterest) | Liens de partage | Connecté |
| Mentions légales, CGV, confidentialité, retours | Emplacements : lien seulement si renseigné | À renseigner |
| Réseaux sociaux | Emplacements : lien seulement si renseigné | À renseigner |
| Pré-bandeau, pastille de l'en-tête | Lien seulement si renseigné | À renseigner |
| Navigation de l'en-tête | Menu Shopify à créer dans la boutique | À créer |

### 11.3 Contrôles automatisés

- `audit_cta.py` — passe en revue **chaque lien et chaque formulaire** du thème (54 au total) et vérifie la destination : route Shopify existante, objet de la boutique, ancre réellement présente (y compris dans les snippets rendus), lien externe, e-mail, ou réglage à renseigner. Résultat : **0 destination morte**.
- `valider_theme.py` — 48/48 fichiers Liquid, snippets et réglages résolus, 18 JSON valides.
- **Parcours cliqué** dans l'aperçu (navigateur sans interface) : 19 contrôles sur les cinq pages — carte produit → fiche, « Voir tout » → collection, « Ajouter au panier » → panier, « Commander » du tiroir → panier + ancre `#commander`, WhatsApp, e-mail, retour à l'accueil, ancres de commande présentes. **19/19**.
- Les seuls liens volontairement inertes de l'aperçu sont l'icône « Compte » et « Propulsé par Shopify » : l'aperçu n'a pas de page de compte, et « Propulsé par Shopify » pointe vers Shopify dans la boutique. Ils sont mentionnés ici pour ne pas être pris pour des oublis.

### 11.4 Ce qu'il suffit de créer dans la boutique

Dès que ces éléments existeront, les CTA concernés s'allumeront **tout seuls**, sans toucher au thème :

| À créer | Ce que cela active |
| --- | --- |
| Collections « Maternité », « Allaitement », « Bébé », « Nouveautés » | Les quatre cartes « univers » et les menus du pied de page |
| Pages « À propos / La marque », « Livraison », « Paiement », « Échanges et retours », « FAQ », « Contact » | Les colonnes du pied de page, le pré-bandeau, la pastille, le bouton contact de la FAQ |
| Pages « Mentions légales », « CGV », « Politique de confidentialité », « Politique de retour / échange » | La ligne légale du pied de page |
| Comptes Facebook, Instagram, TikTok | Les icônes du pied de page |
| Menus Shopify « principal » et « pied de page » | La navigation de l'en-tête et du tiroir mobile |

## 12. Club Maman (même jour)

Demande : « crée le club maman, inspire-toi toujours de doomoo.com ».

### 12.1 Ce que la référence fait, exactement

Le raccourci **« Mama's Club »** de l'en-tête de doomoo.com ne mène pas à une page de la boutique mais à un **espace communautaire hébergé ailleurs** (`nobodytoldme-blog.com`, le hub éditorial *#NobodyToldMe*). Relevé du 4 octobre 2026 :

| Sur la référence | Détail observé |
| --- | --- |
| Page du club | Titre, texte d'accueil (espace bienveillant, sans jugement, sororité), puis le club lui-même |
| Le club | Un **forum** : tableau Sujet / Personnes / Réponses / Likes / Vues / Mis à jour |
| Espaces | Quatre : *Projet bébé, Grossesse, Accouchement, Post-partum* |
| Tri | Plus ancien, plus récent, récemment mis à jour, plus de vues, plus de likes |
| État vide | « No topics have been created. » |
| Ressources | Bandeau avec un bouton « Découvrir nos ressources » |
| Rejoindre | Bloc **Connexion / Inscription** : identifiant ou e-mail, mot de passe, se souvenir de moi, mot de passe oublié, puis e-mail + pseudonyme + mot de passe |
| Ailleurs | Une section d'accueil « MAMA'S CLUB » avec trois discussions en cartes (titre, début du message, prénom, réponses, likes) et un bouton « Rejoignez notre communauté » |

### 12.2 Ce qui a été construit

Une **page « Club Maman »** (`templates/page.club-maman.json` + section `Club Maman`), avec le même déroulé : accueil → espaces d'échange → discussions → ressources → rejoindre le club.

- **Espaces d'échange** : blocs répétables (icône, titre, texte, lien). Affichés en cartes ; un espace sans lien reste lisible mais n'est pas cliquable.
- **Discussions** : blocs répétables (titre, début du message, prénom, réponses, likes). **Tant qu'aucune discussion n'est saisie, la page affiche un état vide** — exactement comme la référence, qui affiche « No topics have been created. » quand le forum est neuf.
- **Bandeau ressources** : titre, texte, bouton — affiché seulement s'il est rempli.
- **Rejoindre le club** : un **vrai formulaire d'inscription** (mécanisme Shopify), la **création d'un compte client** (route Shopify), et **WhatsApp** via le numéro centralisé de l'étape 13. Trois mécanismes qui fonctionnent réellement, aucun promesse inventée.

### 12.3 La différence qu'il faut connaître

**Shopify n'a pas de forum.** La référence fait tourner un forum externe avec comptes membres ; ce n'est ni un réglage ni une fonction du thème. La page a donc été construite pour fonctionner dès maintenant **sans forum**, et pour accueillir un forum plus tard sans être refaite :

| Aujourd'hui, sans forum | Demain, avec un forum ou un espace externe |
| --- | --- |
| Les espaces d'échange mènent où LLUFAN le décide (page, réseau social, WhatsApp) | Chaque espace mène à sa catégorie de forum |
| Les discussions affichent l'état vide | Les discussions deviennent des cartes cliquables vers chaque sujet |
| On rejoint le club par e-mail, compte client ou WhatsApp | L'inscription au forum s'ajoute dans le même bloc |

Le tri (plus récent, plus liké…) et les compteurs de vues de la référence n'ont **pas** été repris : sans forum derrière, ce seraient des boutons et des chiffres décoratifs. Mieux vaut ne rien afficher que faire semblant.

### 12.4 Les points d'entrée sont déjà raccordés

| Point d'entrée | Comportement |
| --- | --- |
| **Pastille de l'en-tête** « CLUB MAMAN » (sur toutes les pages) | Mène à la page du club dès qu'elle existe ; sans lien saisi, la pastille s'affiche sans être cliquable — jamais de lien mort |
| **Raccourci « Espace maman »** du pré-bandeau | Nouveau réglage par raccourci : « Ce raccourci mène au Club Maman », activé sur ce raccourci |
| Ressources, espaces, discussions | Liens à renseigner dans les blocs ; tant qu'ils sont vides, rien n'est cliquable |

La pastille est passée de « MAMA'S CLUB » (libellé du prototype anglais) à **« CLUB MAMAN »**, le nom que vous avez donné. Elle se change en un seul champ : *En-tête → Texte de la pastille*.

### 12.5 Ce que LLUFAN doit fournir

Rien n'a été inventé sur cette page : tout ce qui est vide est visible dans l'aperçu entre pointillés (`preview/club-maman.html`).

| À fournir | Où |
| --- | --- |
| **Créer la page** avec le handle exact `club-maman` | Boutique → Pages. Sans ce handle, la pastille et le raccourci ne pointent nulle part (et restent donc inactifs, sans casser) |
| Texte d'ouverture du club | Section *Club Maman* → Texte d'accueil |
| Nom et rôle des espaces d'échange (les 4 de la référence sont un point de départ, pas une obligation) | Blocs « Espace d'échange » |
| Premières discussions, ou le texte d'attente | Blocs « Discussion » ou réglage « Texte affiché tant qu'aucune discussion n'est saisie » |
| Bandeau ressources (titre, texte, bouton) | Réglages du même nom |
| Texte du bloc « Rejoindre » et mention sous le formulaire | Réglages du même nom |
| Décision sur le forum (page externe, application Shopify, ou réseau social) | — |

Pour ajouter le club à l'accueil comme le fait la référence, la section *Club Maman* peut être ajoutée à n'importe quelle page depuis l'éditeur ; sur l'accueil, elle se place naturellement après le bloc éditorial.

---

# 13. Contenus et produits de démonstration (2026-10-04)

Demande : « remplace le site avec du contenu et produit fictifs pour le tester
réellement, avec option d'accès partout, et pouvoir le modifier dans la
plateforme Shopify. »

## 13.1 Principe retenu

- **Une seule source de contenu** : `demo/contenu_demo.py`. Elle alimente à la
  fois les modèles JSON du thème (via `generer_demo.py`) et l'aperçu HTML (via
  `build_preview.py`). Aucune divergence possible entre les deux.
- **Tout reste modifiable dans l'éditeur Shopify** : les textes de démonstration
  sont écrits **dans les champs des sections** (templates `*.json` et
  `settings_data.json`), jamais codés en dur dans le Liquid. Les supprimer ou
  les réécrire se fait à la souris, sans toucher au code.
- **Visuels** : un réglage `mode_demo` (Réglages du thème → Identité) fait
  apparaître 8 visuels `assets/demo-*.jpg` là où aucun visuel n'a encore été
  choisi (diaporama, cartes d'univers, bandeau de collection, bloc éditorial,
  liste des collections). Un visuel choisi dans une section reprend toujours la
  main. Décoché, le thème retombe sur les cadres neutres.
- **Aucun lien mort** : nouveau snippet `snippets/lien.liquid`. Les réglages
  d'adresse acceptent une cible lisible (`pages/la-marque`,
  `collections/bebe`, `products/<handle>`) ou une adresse complète ; la cible
  est résolue dans la boutique et, tant que la page n'existe pas, **le lien
  n'est pas affiché** (chaque section garde son repli). Branché sur : héros,
  cartes d'univers, produits en avant, médias et texte, FAQ, bandeau d'annonces,
  pré-bandeau, pastille d'en-tête, pied de page (colonnes + mentions légales),
  Club Maman (espaces, discussions, ressources), section *Page d'information*.

## 13.2 Fichiers ajoutés ou modifiés

| Fichier | Nature |
|---|---|
| `demo/contenu_demo.py` | source unique des contenus, produits, collections, pages |
| `generer_demo.py` | écrit les modèles JSON du thème depuis cette source |
| `generer_csv_demo.py` | écrit les deux CSV d'import |
| `patch_demo.py` (désormais dans `historique/`, son travail est fait) | passe unique : réglage `mode_demo` + résolution des adresses dans 11 sections |
| `sections/information.liquid` | **nouvelle** section de page d'information (sur-titre, titre, intro, blocs, note, bouton) |
| `snippets/lien.liquid` | **nouveau** snippet de résolution d'adresse |
| `templates/page.{la-marque,livraison,paiement,politique-de-retour,mentions-legales,cgv,confidentialite}.json` | **7 nouveaux** modèles de page |
| `templates/{index,collection,product,page.faq,page.club-maman}.json` | remplis de contenus de démonstration |
| `sections/{header-group,footer-group}.json` | liens et pastille pré-remplis |
| `config/settings_schema.json` + `settings_data.json` | réglage `mode_demo` (actif) |
| `assets/demo-*.jpg` (8) | visuels de démonstration du thème |
| `assets/theme.css` §24 | styles de la page d'information |
| `LLUFAN-DEMO-produits.csv` | 10 produits, 28 variantes |
| `LLUFAN-DEMO-collections.csv` | 5 collections |
| `demo/produits/*.jpg` (10) | visuels produits à glisser dans Shopify |
| `LLUFAN-DEMO-mode-emploi.md` | mode d'emploi remis à LLUFAN |

Le thème passe de 79 à **96 fichiers** ; l'archive `LLUFAN-theme-Shopify.zip`
est régénérée depuis `theme/` (1,5 Mo). L'ancienne archive sans démonstration
est conservée sous `LLUFAN-theme-Shopify-sans-demo.zip`.

## 13.3 Catalogue de démonstration

10 produits (28 variantes, 900 à 5 500 DA, devise DZD, paiement à la livraison) :
Nomad (fiche réelle LLUFAN, 3 couleurs), Luna (coussin de grossesse, 3 couleurs),
Amira (poncho, 2 couleurs × 2 tailles), Housse Nomad, Cocon (gigoteuse, 2 tailles),
Couverture nid, Bavoirs bandana, Coussinets lavables, Nour (robe, 3 tailles ×
2 couleurs), Sahara (sac à langer). Collections : Maternité, Allaitement, Bébé,
Nouveautés, Accessoires et pièces détachées. Étiquettes posées pour créer les
collections automatiques en une règle.

## 13.4 Aperçu HTML

`build_preview.py` produit désormais **31 pages** (15,9 Mo au total, images en
données, aucune ressource externe) : accueil, 5 collections, 10 fiches produit,
panier, panier vide, Club Maman, FAQ, contact, recherche et les 7 pages
d'information. Tous les liens du menu, du pied de page et des cartes produit
pointent vers ces fichiers : le contrôle automatique du générateur affiche
**0 lien interne mort**. Les alias `collection.html` et `produit.html` restent
générés.

## 13.5 Ce qui reste fictif (à ne pas mettre en ligne tel quel)

9 produits sur 10, leurs prix, les 10 visuels produits, les 3 avis de l'accueil,
les 3 discussions du Club, les textes des 7 pages d'information (bandeau
« Contenu de démonstration » affiché en haut de chacune), les délais
« 2 à 5 jours ouvrés » et les tarifs de livraison. Les réseaux sociaux du pied
de page restent des emplacements sans lien, et aucune donnée juridique n'a été
inventée : les mentions légales / CGV / confidentialité / retour sont des
gabarits à trous, marqués comme tels.

## 13.6 Mise en route

Voir `LLUFAN-DEMO-mode-emploi.md` : import du thème, des produits et des
collections, les 10 pages à créer (handle + modèle), le menu principal, les
visuels produits, puis où modifier chaque élément dans l'éditeur.

## 13.7 Contrôles et correctifs de la passe de vérification

Vérification faite dans Chromium (Playwright) sur l'aperçu : 12 pages × 3 largeurs
(1400 / 768 / 390 px) — **0 image cassée, 0 erreur JavaScript, aucun débordement
horizontal** (après correctif), 31 pages générées, **0 lien interne mort**.
Captures (non conservées : elles se régénèrent en quelques secondes avec
`build_apercu.py` et les scripts Chromium de contrôle).

Trois correctifs issus de cette passe, tous dans le thème :

1. **`.color-scheme` sans règle de base** — la classe posait les variables mais pas
   le fond ni la couleur de texte ; le titre du diaporama et celui du bandeau de
   collection s'affichaient donc en bleu foncé sur des visuels sombres. Règle
   ajoutée (`background-color: rgb(var(--page-background)); color: rgb(var(--text-color))`).
   Elles s'affichent maintenant en blanc sur les visuels, comme dans la référence.
2. **Débordement horizontal sur mobile** — un carrousel (contenu intrinsèquement
   large) élargissait la page à 493 px sur un écran de 390 px. Ajout de
   `.section-stack > * { min-width: 0 }` et `.carousel-wrapper { min-width: 0 }`.
3. **Visuels de démonstration** — léger voile dégradé vers le bas sur les deux
   visuels du diaporama et sur le bandeau de collection, pour garantir la
   lisibilité du texte blanc (les visuels définitifs de LLUFAN se choisissent
   dans l'éditeur et n'ont pas besoin de ce voile).

Le carrousel de l'accueil ne passe pas par l'apparition au défilement (il n'est
pas dans un `product-list` dans le thème) : l'aperçu a été aligné sur ce
comportement, pour que ce qui est vu soit exactement ce que fait la boutique.

## 13.8 Suite de la passe démonstration (2026-10-04)

**Visuels d'ambiance enfin dédiés.** Au tour précédent, la limite de génération
d'images (10 par tour) avait obligé à fabriquer les visuels d'ambiance par
recadrage des visuels produits. Les 8 visuels `assets/demo-*.jpg` sont
maintenant des images dédiées : diaporama (maman et bébé / coin de nursery),
4 cartes d'univers (grossesse, allaitement, chambre, nouveautés), bandeau de
collection (textiles pliés sur un banc) et bloc éditorial (gros plan sur la
texture du coton). Deux générations ont été refusées par le filtre automatique
du service d'images (scènes d'allaitement) : elles ont été reformulées en scènes
pudiques et en natures mortes — aucune image n'est reprise d'un site tiers.

**Pages de l'aperçu complétées : 31 → 36.** Ajout du journal (liste), des 3
articles, et de la page « introuvable » (modèle `404.json` du thème). Le
contrôle automatique du générateur reste à **0 lien interne mort** ; les pages
ajoutées sont testées à 1400 et 390 px (0 image cassée, 0 erreur JS, aucun
débordement).

**Journal.** Contenu de boutique (données), pas de thème : 3 articles de
démonstration écrits dans `demo/contenu_demo.py` et livrés prêts à coller dans
`LLUFAN-DEMO-journal-a-publier.md` (titre, adresse, chapeau, texte HTML,
visuel). Les articles parlent de choix du coussin, d'organisation des premières
tétées et des essentiels de la chambre ; **aucun conseil médical**, chaque texte
renvoyant explicitement vers les professionnels. Constat à retenir : **Shopify
n'importe pas les articles de blog par CSV** (contrairement aux produits et aux
collections) — l'interface du journal est donc manuelle, ou passe par une
application.

## 13.9 Contrôle « comme à l'import Shopify » — et le défaut qu'il a révélé

Nouveau contrôleur `valider_shopify.py` (celui qui manquait) : il vérifie ce que
le validateur de balises ne regardait pas, c'est-à-dire les cinq causes
d'avertissement ou de rendu vide à l'import :

1. chaque **type de section** utilisé dans un modèle ou un groupe existe dans
   `sections/`, et n'est pas employé dans le mauvais emplacement (`enabled_on`) ;
2. chaque **type de bloc** existe dans le schéma de sa section ;
3. chaque **réglage** écrit dans un modèle (au niveau section **et** bloc) est
   déclaré dans le schéma correspondant ;
4. chaque clé de `config/settings_data.json` existe dans le schéma des réglages ;
5. chaque clé de traduction `… | t` existe dans `locales/fr.default.json`.

**Défaut trouvé et corrigé — 9 sections sans type.** En réécrivant les modèles du
thème pour la démonstration (§13.2), la fonction qui assemblait les sections
(`ordonner()`) écrivait les blocs, l'ordre et les réglages **mais pas la clé
`type`**. Neuf sections étaient concernées : héros, réassurance, cartes
d'univers, avis, questions fréquentes (accueil, collection, fiche produit, page
FAQ), page d'information (× 7) et la réassurance du pied de page. Une section
sans `type` ne s'affiche pas dans la boutique : l'accueil aurait perdu son
diaporama, ses cartes d'univers, ses avis et ses questions fréquentes, et les
pages d'information auraient été vides. `generer_demo.py` corrigé, modèles
régénérés, contrôle désormais à **0 anomalie**.

**Défaut trouvé et corrigé — traductions manquantes.** Quatre clés de la page
« carte cadeau » (`gift_cards.issued.*`) n'existaient pas dans la locale
française : la page aurait affiché « translation missing ». Groupe `gift_cards`
ajouté à `locales/fr.default.json`.

**Section vidéo : ne s'affiche plus vide.** Elle était dans l'ordre de l'accueil
avec un emplacement d'attente : dans la boutique, elle aurait produit un grand
bandeau noir vide. Désormais, sans vidéo fournie, la section **ne s'affiche pas
dans la vitrine** mais reste visible dans l'éditeur (avec son texte d'attente)
pour pouvoir y déposer le lien le jour venu. L'accueil garde donc la place de
cette section, fidèle à la référence.

**Aperçu : 36 → 37 pages.** Ajout de la liste des collections (`/collections`,
modèle `list-collections.json`), dernière adresse du thème qui n'avait pas
d'aperçu. Contrôle final : **37 pages × 3 largeurs = 111 vérifications, aucune
en échec** (0 image cassée, 0 erreur JS, aucun débordement).

**Archive sans démonstration retirée.** Le doublon
`LLUFAN-theme-Shopify-sans-demo.zip` (état du thème avant le §13.2) a été
supprimé pour qu'il n'y ait qu'une seule archive dans le dossier : importer la
mauvaise aurait donné une boutique vide. Le thème livré se vide d'ailleurs
depuis l'éditeur (chaque texte de démonstration est dans un champ) ; une
version vierge peut être régénérée à la demande.

## 13.10 Parcours de commande testé en conditions réelles

La commande est **le** point sensible de la boutique : elle a été testée dans le
navigateur, en pilotant le formulaire comme le ferait un client (« Fiche produit → wilaya → commune → mode de
livraison → total »).

**Sur la fiche produit (Coussin Nomad, 3 200 DA)**

| Wilaya | Communes proposées | À domicile | Stop-desk | Total domicile | Total stop-desk |
|---|---|---|---|---|---|
| 16 — Alger | 57 | 400 DA | 250 DA | 3 600 DA | 3 450 DA |
| 31 — Oran | 26 | 500 DA | 300 DA | 3 700 DA | 3 500 DA |
| 69 — El Abiodh Sidi Cheikh | 7 | 800 DA | 500 DA | 4 000 DA | 3 700 DA |

**Sur la page panier (2 articles : 3 200 + 1 200 = 4 400 DA)** : Alger → 4 800 DA
(domicile) / 4 650 DA (stop-desk) ; Oran → 4 900 / 4 700 DA.

**Balayage complet des 69 wilayas** (bout-en-bout, dans le navigateur, via le
formulaire réel) : **0 anomalie**. Chaque wilaya propose ses communes, affiche
les deux tarifs, et le total vaut exactement sous-total + frais, à domicile
comme en stop-desk. La barre mobile collante affiche le même montant que le
total. Tarifs constatés : **400 à 800 DA** à domicile (médiane 600) et
**250 à 500 DA** en stop-desk (médiane 350). Aucune erreur JavaScript.

## 13.11 Contrôle d'accessibilité — et deux défauts corrigés

Passage de contrôle sur les 38 pages (attributs `alt`, étiquettes de champs,
plan du document, titres) :

1. **Deux titres de niveau 1 sur chaque page.** Le logo de l'en-tête était
   balisé `<h1>` sur *toutes* les pages, en plus du titre de la page. Corrigé :
   le logo n'est un `<h1>` que sur l'accueil (motif des thèmes Shopify), ailleurs
   c'est un `<div>` de même classe — le plan du document redevient `h1` unique.
2. **Saut de niveau dans les fiches produit.** La description enchaînait
   directement d'un `h1` à des `h3` (Utilisation, Entretien, Composition).
   Corrigé : un titre **« Description »** de niveau 2 précède désormais la
   description, avec un nouveau réglage *Titre de la description* (modifiable et
   masquable dans l'éditeur). Les sous-titres des articles de démonstration sont
   passés en `h2` pour la même raison.

Après correction : **0 image sans `alt`, 0 champ sans étiquette, 0 saut de
niveau, un seul `h1` par page** — sauf l'accueil, où le `h1` porte le logo
(nommé par le texte alternatif), comme dans les thèmes Shopify de référence.

**Compatibilité des pages spéciales, vérifiée dans la documentation Shopify** :
`layout/theme.liquid` enveloppe *toutes* les pages par défaut (« By default, the
theme.liquid layout is used »), y compris le mot de passe, la carte cadeau et
les pages de compte client : ces modèles n'ont donc pas besoin de `{% layout %}`
explicite et profitent bien des polices, de la feuille de style et de
l'en-tête/pied de page du thème.

## 13.12 Aperçu : 38 pages

Ajout de la page **compte client** (connexion + création de compte, reprenant
les classes des modèles `templates/customers/login.liquid` et
`register.liquid`) : le lien « Compte » de l'en-tête et « Créer mon compte » du
Club Maman y mènent désormais. C'était la dernière adresse du thème sans aperçu,
avec la liste des collections (§13.9) et le journal (§13.8).

Contrôle final : **38 pages × 3 largeurs = 114 vérifications, aucune en échec**.

## 13.13 Les vidéos (2026-10-04)

**Ce que fait la référence**, relevé dans le code public de sa page d'accueil :
une seule vidéo, un lecteur **YouTube sans commandes** qui démarre seul, **en
sourdine**, **en boucle** et non cliquable
(`autoplay=1&mute=1&loop=1&controls=0`, `playsinline=1`, `pointer-events` neutralisé).
Sa fiche produit, elle, accepte des **vidéos dans la galerie** (lecteur avec
commandes, en sourdine, en boucle, bouton de lecture sur l'image).

**Ce que fait le thème LLUFAN**

| Emplacement | Comment on met une vidéo | Comportement |
|---|---|---|
| Accueil (section *Vidéo*) | Éditeur → Accueil → bloc *Vidéo* → champ « Lien de la vidéo » (YouTube ou Vimeo) ou « Fichier vidéo hébergé par Shopify » | Lecture automatique, sans son, en boucle, sans commandes — **comportement de la référence**, réglable par la case « Lecture automatique en boucle, sans son » |
| Fiche produit (galerie) | Admin → Produits → ouvrir le produit → Médias → Ajouter → coller un lien YouTube/Vimeo ou téléverser un fichier | Lecteur avec commandes, en sourdine, en boucle (comme la référence) ; vignette = image d'aperçu de la vidéo |
| Description produit, pages, articles | Éditeur de texte → mode HTML → coller le code d'intégration fourni par YouTube/Vimeo | Le contenu est rendu tel quel par le thème |

**Formes de liens reconnues** (testées avec un moteur Liquid réel) :
`youtube.com/watch?v=…`, `youtu.be/…`, YouTube Shorts, `/live/`, `/embed/`,
`vimeo.com/…`. Dans tous les cas, le thème reconstruit lui-même l'adresse de
lecture et y ajoute les paramètres de la référence : le marchand colle le lien
qu'il a sous la main, rien à composer à la main.

**Points à connaître**

- Une vidéo **ne peut pas démarrer avec du son** dans un navigateur : la lecture
  automatique est toujours muette (règle des navigateurs, d'où le choix de la
  référence). Si la vidéo a une voix off, décocher la case de lecture
  automatique : le lecteur affiche alors ses commandes et le son est disponible.
- Aucune vidéo n'a été inventée : tant qu'aucun lien n'est saisi, la section ne
  s'affiche pas dans la boutique (elle reste visible dans l'éditeur). Elle
  réapparaîtra seule dès qu'un lien sera collé.
- Plusieurs vidéos sur une même page : ajouter la section *Vidéo* plusieurs fois
  dans l'éditeur (chaque ajout est réglable indépendamment).
- Test `liqtest/test-video.mjs` (moteur Liquid réel) : **9/9 cas conformes** —
  chaque forme de lien, avec et sans lecture automatique, la vidéo hébergée par
  Shopify, et le masquage de la section quand elle est vide.

## 13.14 Aperçu d'ensemble (2026-10-04)

`preview/apercu.html` — une page unique qui montre **les 38 pages** de l'aperçu
en vignettes cliquables, groupées par famille (Accueil, Collections, Fiches
produit, Panier et commande, Information, Journal, Compte et technique). Chaque
carte porte son **rôle** et un **statut** :

- **Structure validée** : la mécanique, le parcours, les données LLUFAN
  (tarifs, wilayas, WhatsApp, e-mail) — déjà à leur place définitive ;
- **Contenu de démonstration** : textes, prix, visuels ou produits fictifs,
  créés pour tester, à remplacer ou à valider ;
- **À compléter par LLUFAN** : les quatre gabarits juridiques, où **aucun texte
  n'a été inventé** (CGV, mentions légales, confidentialité, retours).

L'en-tête rappelle les chiffres de la boutique et **ce qui reste à fournir**
(vidéo d'accueil, photos définitives, prix à confirmer, textes juridiques,
articles du journal). Générateur : `build_apercu.py` — Chromium capture chaque
page à 1440 px, les vignettes sont recadrées puis **incorporées en données**
(la page reste autonome), et le script vérifie que chaque lien mène à une page
existante. Contrôlé à 1440 / 768 / 390 px : 38 cartes, aucune vignette cassée,
aucun débordement, aucune erreur JavaScript.

**Barre d'outils de collection complétée (2026-10-04).** L'aperçu affichait
« Filtrer » et « Trier par » comme de simples libellés. Il reprend maintenant
l'ensemble du bloc du thème (`snippets/facets.liquid`) : icônes, **tiroir de
filtres** (groupes Collection et Étiquette avec leurs compteurs, prix de/à,
boutons *Appliquer* / *Tout effacer*) et **popover de tri** avec les cinq
options de la référence (En vedette, prix croissant/décroissant, Nouveautés,
Meilleures ventes). Deux pages d'état ont été ajoutées pour que ces écrans
soient visibles sans clic : `collection-filtres.html` (tiroir ouvert) et
`collection-tri.html` (tri affiché) — l'aperçu compte donc **40 pages**.

Ces deux pages ont aussi mis au jour un oubli : le **voile** affiché derrière
les tiroirs (`div.page-overlay`, présent dans le layout du thème) manquait à
l'aperçu, et le script le cherche au chargement — il est désormais présent, dans
le bon ordre. Les étiquettes de filtre sont par ailleurs affichées avec leurs
accents (« Pièces détachées », « Prêt-à-porter ») à partir du catalogue, comme
elles le seront sur la boutique.

Contrôle final de l'aperçu : **41 fichiers × 3 largeurs = 123 vérifications,
aucune en échec** (0 image cassée, 0 erreur JavaScript, aucun débordement).

## 13.15 Aperçu local, à emporter (2026-10-04)

`LLUFAN-apercu-local.zip` (13 Mo) — la boutique seule, prête à regarder **hors
ligne sur n'importe quel ordinateur**, sans installation ni connexion. Elle
contient les 40 pages plus la page d'ensemble, un `LIRE-MOI.txt` (comment
ouvrir, ce qui est fictif, ce qui reste à fournir) et un petit serveur local
facultatif (`servir-en-local.py`, avec lanceurs `.command` pour macOS/Linux et
`.bat` pour Windows) au cas où un navigateur restreindrait les scripts en mode
« fichier ».

Vérifié **depuis un autre dossier** (comme sur une autre machine) : 41 fichiers
ouverts, 0 image cassée, 0 erreur JavaScript, aucun débordement, chaque lien
vers une page qui existe réellement — et le parcours de commande fonctionne
toujours (Alger → 3 600 DA). Les pages n'ont **aucun chemin absolu** et aucune
ressource externe : chaque fichier est autonome, donc transmissible tel quel.

## 13.16 Voir où et comment s'ajoute une vidéo (2026-10-04)

`preview/comment-ajouter-une-video.html` — une page de **démonstration visuelle**
(c'est aussi le mode d'emploi de la vidéo), ouverte depuis l'aperçu d'ensemble,
famille « Compte et technique ». Elle montre, côte à côte :

1. **La vidéo de l'accueil** — à gauche la reproduction du panneau Shopify
   (section *Vidéo* : titre, *Lien de la vidéo*, *Fichier vidéo hébergé par
   Shopify*, case *Lecture automatique en boucle, sans son*), à droite le rendu
   correspondant ; puis l'adresse de lecture que le thème construit à partir du
   lien collé, avec le rôle de chaque paramètre.
2. **Les vidéos d'un produit** — même principe : panneau *Produits → Médias*
   (glisser un fichier ou coller un lien), vignette de galerie, lecteur avec
   commandes.
3. **Les liens reconnus** (`youtube.com/watch?v=…`, `youtu.be/…`, Shorts,
   `vimeo.com/…`, fichier MP4) et ce que chacun donne.

**Représentation, pas simulation trompeuse** : l'aperçu local n'a pas d'accès
réseau, donc le lecteur YouTube/Vimeo y est *représenté* (cadre 16/9, styles et
libellés du thème), et la page le dit explicitement. Dans la boutique, c'est le
vrai lecteur qui s'affiche, avec les réglages du §13.13. Générateur :
`build_guide_video.py` (il reprend les libellés exacts du schéma de
`sections/video.liquid`). Contrôlé à 1440 / 768 / 390 px : 0 image cassée,
0 erreur JavaScript, aucun débordement. L'aperçu compte désormais **42 pages**
(126 vérifications, aucune en échec).

## 14. Nettoyage du plan de travail (2026-10-04)

Le dossier était devenu encombré de fichiers de travail : **la copie
décompressée de l'aperçu (24 Mo), les pages et feuilles de style de la
référence de design récoltées pendant l'analyse (19 Mo, avec des polices d'un
tiers) et nos captures d'écran de vérification (16 Mo)** ont été supprimées.
Aucune de ces pièces n'était nécessaire : les deux premières sont des documents
de tiers conservés le temps de l'analyse, les dernières se régénèrent en
quelques secondes.

**Ce qui reste, et pourquoi** :

| Élément | Rôle |
|---|---|
| `theme/` | la source du thème — c'est ce qu'on modifie |
| `demo/` | la source unique des contenus (textes, produits, visuels) |
| `preview/` | l'aperçu, régénéré par `build_preview.py` |
| `tests/` | le test de la section vidéo (moteur Liquid réel) |
| scripts `.py` | générateurs et contrôles |
| `README.md`, `LLUFAN-*.md` | la documentation, dont la **liste de contrôle avant mise en ligne** |
| `LLUFAN-theme-Shopify.zip`, CSV | les fichiers d'import Shopify |

Tout le reste se **reconstruit à partir de ces sources** : l'aperçu
(`build_preview.py`), la page d'ensemble (`build_apercu.py`), le guide vidéo
(`build_guide_video.py`), le dossier à emporter (`build_package_apercu.py`), les
modèles du thème (`generer_demo.py`) et les CSV (`generer_csv_demo.py`).

Les mesures de la référence de design n'ont pas été perdues : elles sont
consignées dans les §1 à §6 du présent document (couleurs, tailles, marges,
durées d'animation, structures de page). Si un doute revient sur un point
précis, la page publique peut être relue à tout moment.

**Liste de contrôle.** `LLUFAN-checklist-mise-en-ligne.md` rassemble les treize
étapes de la mise en ligne sous forme de cases à cocher — de « ce qu'il faut
avoir sous la main » jusqu'à la publication, en passant par les produits, les
collections, les dix pages, les menus, le journal, les réglages, **ce qui est
fictif et ne doit pas partir en ligne**, et le test de commande de bout en bout
à refaire sur téléphone. C'est la version « à suivre le jour J » du mode
d'emploi.

---

## 15. Deux langues : français et arabe (2026-10-04)

Demande du client : « une fonction choix de langue : une version fr et une
version arabe ; le client a le choix de choisir, ou qu'elle prenne la langue de
son système automatiquement ». Les deux sont faits — avec, plus bas, une
explication honnête de la part qui revient à Shopify et de celle qui revient au
thème.

### 15.1 Ce qui a été ajouté ou modifié

| Fichier | Ce qu'il apporte |
|---|---|
| `locales/ar.json` | **la version arabe des libellés du thème** : les clés de l'interface (aujourd'hui **121**, formes plurielles de l'arabe incluses : duel, pluriel 3-10, pluriel 11+) |
| `assets/llufan-ar-heading-500/600.woff2`, `assets/llufan-ar-body-400/600.woff2` | quatre fichiers de police (272 Ko) — IBM Plex Sans Arabic pour les titres, Noto Naskh Arabic pour les phrases, équivalents arabes de la charte ; licences libres (OFL) |
| `assets/llufan-langue.js` | le choix automatique de la langue d'après celle du système (voir §15.3) |
| `layout/theme.liquid` | attribut `dir` calculé d'après la langue, liens `hreflang` pour les moteurs de recherche, chargement du script |
| `assets/theme.css` | les polices arabes embarquées et **88 lignes de règles pour le sens droite→gauche** |
| `config/settings_schema.json` + `settings_data.json` | un réglage « Choisir la langue d'après celle du navigateur » (activé par défaut) |
| `snippets/forme-commande.liquid` | les 23 libellés du formulaire de commande passent par les traductions |
| `assets/llufan-livraison.js` | le « à calculer » affiché dans le formulaire suit la langue |
| `build_arabe.py` + `preview/ar-accueil.html` | la page d'aperçu de la version arabe |

L'en-tête portait déjà un sélecteur de langue (`sections/header.liquid`) ; il a
depuis été transformé en **bascule à une seule langue** — voir le §18, écrit
après une remarque du client sur la capture d'écran.

### 15.2 Comment le sens de lecture est retourné

Le thème était déjà écrit en **propriétés logiques** (`inset-inline`,
`margin-inline`, `padding-inline`, `text-align: start`, `border-inline`) : le
miroir est donc automatique pour l'essentiel. Ce qui manquait a été ajouté
après relevé :

* **18 positions physiques** (`left:` / `right:`) basculées — pastille des
  cartes produit, bouton d'ajout rapide, image secondaire des blocs éditoriaux,
  barre de soulignement des menus ;
* **44 interlettrages** (`letter-spacing`) neutralisés en arabe : l'arabe est une
  écriture liée, un interlettrage détache les lettres. Les majuscules
  (`text-transform: uppercase`) sont neutralisées aussi, elles n'ont pas de sens
  en arabe ;
* **tiroirs** : le panier vient de la gauche, le menu et les filtres de la
  droite — l'inverse du français, comme il se doit ;
* **flèches et chevrons** retournés (`scaleX(-1)`) ;
* **chiffres, prix, téléphones isolés** en lecture gauche→droite
  (`direction: ltr; unicode-bidi: isolate`) : sans cette précaution, « 3 200 DA »
  s'affiche « DA 200 3 » et « 0772 415 120 » ressort à l'envers. C'est ce qu'a
  montré le premier contrôle visuel, et c'est corrigé ;
* **polices** : les polices latines restent en premier, les arabes suivent. Le
  navigateur choisit la première police qui possède le glyphe, donc un texte
  français s'affiche en Jost / Fraunces et un texte arabe en IBM Plex Sans
  Arabic / Noto Naskh Arabic. Grâce au `unicode-range`, **un visiteur
  francophone ne télécharge jamais les polices arabes** (elles ne partent que si
  la page contient réellement de l'arabe).

### 15.3 Le choix automatique de la langue — qui fait quoi

Il faut distinguer deux choses, souvent confondues :

1. **Ce que Shopify fait lui-même.** Chaque langue publiée a sa propre adresse
   (`llufan.com` pour le français, `llufan.com/ar` pour l'arabe). Shopify note
   aussi la langue choisie dans la session du visiteur : une fois qu'on a cliqué
   sur « العربية », on reste en arabe pendant la visite, avec les bonnes
   adresses.
2. **Ce que fait le thème.** `assets/llufan-langue.js` regarde la ou les langues
   du système (`navigator.languages`). Si le système est en arabe et que la page
   affichée est le français, il emmène la visiteuse vers l'adresse arabe — **une
   seule fois par session**, en conservant la page consultée et les éventuels
   paramètres d'adresse.

Trois garde-fous, volontaires :

* un **choix explicite** (clic sur le sélecteur) est mémorisé et n'est plus
  jamais remis en cause ;
* **aucune redirection pour les robots** des moteurs de recherche (le
  référencement passe par les liens `hreflang` du layout, qui déclarent les deux
  versions de chaque page) ;
* **une seule redirection par session** et jamais vers une langue non publiée :
  impossible de créer une boucle.

Le réglage est dans l'éditeur : **Réglages du thème → Sélecteurs et mentions
légales → « Choisir la langue d'après celle du navigateur »**. Le décocher
laisse le choix entièrement à la visiteuse.

### 15.4 Ce qu'il reste à faire dans la boutique (une dizaine de minutes)

| # | Étape | Où |
|---|---|---|
| 1 | Ajouter la langue **العربية** et la publier | Paramètres → Langues → Ajouter une langue |
| 2 | Vérifier que le **sélecteur de langue** est affiché | Éditeur → Réglages du thème → Sélecteurs et mentions légales |
| 3 | Traduire les **contenus** (produits, collections, pages, articles, politiques, menus) | Applications → **Traduire et adapter** (gratuite, fournie par Shopify) — le thème, lui, est déjà traduit |
| 4 | Ouvrir `llufan.com/ar` et vérifier l'en-tête, une fiche produit et le formulaire de commande | — |

**Ce qui ne sera pas traduit par le thème, et qu'il faut savoir :**

* les **noms des 1 541 communes et des 69 wilayas** viennent d'un fichier du
  thème (`assets/llufan-livraison-dz.json`) et restent en caractères latins —
  c'est d'ailleurs l'usage pour les adresses de livraison en Algérie ;
* les **intitulés de champs envoyés à Shopify** dans la commande
  (`Nom complet`, `Téléphone`, `Wilaya`, `Commune`, `Type de livraison`) restent
  en français : ce sont les étiquettes que vous lisez dans la commande, côté
  administration, et elles doivent rester identiques quelle que soit la langue
  de la cliente ;
* les **e-mails de notification** de Shopify ont leurs propres modèles, à
  traduire séparément si besoin ;
* les contenus des produits et des pages : tant qu'ils ne sont pas traduits dans
  « Traduire et adapter », la version arabe les affiche en français. Les textes
  arabes de la page d'aperçu `preview/ar-accueil.html` sont des **propositions**
  à valider, pas des textes définitifs.

### 15.5 Vérifications faites le 4 octobre 2026

* **Page arabe** (`preview/ar-accueil.html`, controls automatiques
  `verifier_arabe.py`) : `dir="rtl"` et `lang="ar"` sur toute la page ; les deux
  polices arabes réellement chargées ; en-tête en miroir (le logo passe à droite
  du menu) ; **aucun débordement horizontal** aux trois largeurs ; formulaire de
  commande testé pour de vrai : wilaya choisie → 17 communes proposées →
  à domicile 800 DA → **total 4 000 دج** (3 200 + 800).
* **Toutes les pages** (`verifier_pages.py`) : **43 pages × 3 largeurs = 129
  contrôles, 0 échec** — aucune ressource manquante, aucun débordement, un seul
  `<h1>` par page, toutes les images avec un texte de remplacement.
* **Validateurs** : 51/51 fichiers Liquid conformes, 27 fichiers JSON valides,
  **0 anomalie**, 110 clés de traduction utilisées toutes présentes en français
  **et en arabe**, 60 liens ou formulaires sans destination morte, 9/9 au test de
  la section vidéo.

### 15.6 Ce qu'il faut savoir en regardant la version arabe

* Les **prix** gardent la disposition « 3 200 DA » (chiffres puis devise) : c'est
  volontaire, c'est ainsi qu'ils se lisent en Algérie ;
* l'**interlettrage et les majuscules** disparaissent en arabe, les titres
  restent en revanche dans la même graisse et la même couleur que la charte ;
* la **page arabe de l'aperçu** est une démonstration : elle montre l'en-tête,
  l'accueil, une fiche produit avec son formulaire de commande et le pied de
  page en arabe. Les autres pages de l'aperçu n'ont pas été dupliquées en
  arabe — inutile, la mise en page est identique, seul le contenu change.

---

## 16. La version arabe, page par page, et le texte arabe à coller (2026-10-04)

La veille (§15), le thème est devenu bilingue. Cette passe complète le travail
sur trois points : **la boutique arabe est maintenant visible dans l'aperçu**,
**le texte arabe des contenus est écrit** (produits, collections, pages,
articles), et **un défaut d'affichage de la galerie produit a été corrigé** —
dans les deux langues.

### 16.1 Quatre pages arabes dans l'aperçu

| Fichier | Ce qu'il montre |
|---|---|
| `preview/ar-accueil.html` | l'accueil : diaporama, réassurance, 4 univers, sélection produits, avis, bloc éditorial |
| `preview/ar-collection-allaitement.html` | une collection : bandeau, barre d'outils, filtres et tri en arabe, grille, questions fréquentes |
| `preview/ar-produit-coussin-allaitement-nomad.html` | une fiche produit complète : galerie, couleurs, quantité, **formulaire de commande à la livraison**, description, produits associés |
| `preview/ar-panier.html` | le panier : lignes, commande à la livraison, aperçu du tiroir, panier vide |
| `preview/ar-collection-tri.html` | la même collection, **panneau de tri ouvert** : il s'ouvre vers l'intérieur de la page, comme en français |
| `preview/ar-collection-filtres.html` | la même collection, **tiroir de filtres ouvert** : il entre par la droite, à l'inverse du panier |

Elles sont produites par `build_arabe.py`, à partir de
`demo/contenu_demo_ar.py` (le pendant arabe de `demo/contenu_demo.py`). Le
sommaire `preview/apercu.html` les présente avec les autres : **47 vignettes**.
Le sélecteur de langue de l'en-tête fait le lien entre les deux versions dans
tout l'aperçu.

Ce qui a été vérifié sur ces quatre pages (`verifier_arabe.py`, aux trois
largeurs) : `dir="rtl"` et `lang="ar"`, polices arabes réellement chargées,
en-tête en miroir, interlettrage neutralisé, **aucun débordement horizontal**, et
le formulaire de commande qui calcule juste — sur la fiche : 3 200 + 800 =
**4 000 دج**, sur le panier (coussin + housse) : 4 400 + 800 = **5 200 دج**.

### 16.2 Le texte arabe des contenus : `LLUFAN-DEMO-traductions-ar.csv`

Shopify ne traduit pas les contenus tout seul, et son export de traduction exige
les identifiants internes de chaque fiche — impossibles à connaître avant que
les produits existent. Le fichier livré prend donc l'autre bout du problème :

* il contient, en face du texte français, **le texte arabe déjà écrit** ;
* il couvre aujourd'hui **133 lignes, une par champ tel que Shopify l'exporte** (le 6 octobre ; c'était 249 lignes écrites en blocs avant cette date — une page s'y trouvait découpée en 11 lignes, ce qui obligeait à recoller les morceaux) : les 10 produits (titre,
  description, type), leurs options et leurs valeurs de couleur ou de taille,
  les 5 collections, les 7 pages d'information, la FAQ, le Club Maman, la page
  contact, les 3 articles du journal et les 17 textes saisis dans les réglages
  de sections ;
* il se lit à cinq colonnes (`Type`, `Ressource`, `Champ`, `Français`,
  `العربية`) et se colle dans la colonne « Translated content » de l'export
  Shopify, après avoir publié la langue arabe.

**Ce qui n'y est pas, volontairement** : les **libellés de l'interface**
(« Ajouter au panier », « Votre nom »…) — ils vivent dans le thème, fichier
`locales/ar.json`, et se publient avec lui — et les **textes juridiques** :
aucun n'a été inventé, il n'y a donc rien à traduire pour l'instant.

Deux mécanismes à connaître, qui complètent le fichier :

1. **Les textes des sections du thème** (titres d'accueil, bandeaux, réassurance)
   se traduisent **directement dans l'éditeur** : le sélecteur de langue de la
   barre d'outils permet de saisir la version arabe champ par champ.
2. **Les politiques de la boutique** (CGV, confidentialité, retours) ont leur
   propre écran dans Paramètres → Politiques, avec les mêmes boutons de langue.

### 16.3 Un défaut corrigé au passage : la galerie produit

En comparant la fiche produit arabe et la fiche française, le grand visuel
s'affichait en **80 px** au lieu de toute la colonne. La cause : dans l'aperçu,
le bloc des vignettes de galerie manquait, et le carrousel se retrouvait placé
dans la colonne des vignettes (5 rem). Le thème, lui, était correct — l'aperçu
ne reproduisait pas fidèlement sa structure.

Correction faite dans les deux langues : les vignettes sont maintenant rendues
(`.product-gallery__thumbs`), et le grand visuel occupe sa colonne — mesuré à
**632 × 632 px** en 1440. C'est un exemple d'écart entre l'aperçu et le thème
qui valait la peine d'être trouvé : il ne se voyait ni dans les chiffres, ni
dans les contrôles automatiques, seulement à l'œil.

### 16.4 Fichiers ajoutés ou modifiés

| Fichier | Rôle |
|---|---|
| `demo/contenu_demo_ar.py` | le contenu de démonstration en arabe (produits, collections, FAQ, panier, titres des pages) |
| `build_arabe.py` | produit les quatre pages arabes (+ contrôle des liens internes) |
| `generer_kit_shopify.py` | produit `LLUFAN-DEMO-traductions-ar.csv` (une ligne par champ Shopify) **et** `LLUFAN-DEMO-contenus-a-coller.md` (pages, collections, articles — français et arabe assemblés) |
| `verifier_arabe.py` | contrôle des pages arabes (sens, polices, miroir, formulaire) |
| `verifier_pages.py` | contrôle de **toutes** les pages aux trois largeurs |
| `preview/ar-*.html` | les quatre pages arabes |
| `LLUFAN-DEMO-traductions-ar.csv` | le texte arabe à coller dans Shopify (133 lignes, une par champ) |

### 16.5 État des contrôles

* **48 pages × 3 largeurs = 144 contrôles** (`verifier_pages.py`) : aucune
  ressource manquante, aucun débordement, un seul `<h1>` par page, toutes les
  images avec un texte de remplacement ;
* **6 pages arabes** contrôlées séparément, formulaire de commande compris ;
* **41 pages françaises forcées en droite→gauche** (82 contrôles, §17) ;
* 51/51 fichiers Liquid conformes, 27 JSON valides, 0 anomalie, 60 liens sans
  destination morte, 9/9 au test de la section vidéo.

### 16.6 Ce qu'il reste à faire sur la partie arabe

1. **Faire relire les textes arabes** : ils sont écrits, cohérents et marqués
   « تجريبي », mais une relecture par un locuteur est indispensable avant
   publication — c'est un texte commercial, pas une traduction technique.
2. **Coller les traductions** dans l'export Shopify (§16.2).
3. **Traduire les textes longs** (pages d'information, articles) quand les
   versions françaises définitives seront écrites.
4. **Vérifier dans la boutique** : `llufan.com/ar`, tiroirs, formulaire de
   commande.

---

## 17. Audit « droite → gauche » de toutes les pages (2026-10-04)

Les quatre pages arabes de l'aperçu couvrent l'accueil, une collection, une fiche
produit et le panier. Elles ne montrent pas tout : **le tableau du Club Maman, le
tiroir de filtres, le tri, le compte client, la recherche, les pages
d'information** n'avaient jamais été vus en arabe. Une page peut très bien
s'afficher correctement en français et se casser en sens inverse.

### 17.1 La méthode

`verifier_rtl.py` prend **chaque page française**, force `dir="rtl"` et
`lang="ar"` sur toute la page — exactement ce que fait le thème quand la langue
est l'arabe — puis cherche, aux largeurs 1440 et 390 :

* un débordement horizontal ;
* un élément qui sort du cadre par le bord ;
* un texte rogné dans un bloc qui masque son contenu ;
* deux éléments qui se chevauchent alors qu'ils ne devraient pas.

Le texte reste en français : ce n'est pas un contrôle de traduction, seulement de
**géométrie**. C'est bien ce qu'on veut vérifier ici.

### 17.2 Le défaut trouvé

Un seul, mais réel : le **panneau « Trier par »** des collections. En français, il
s'ouvre vers la gauche du bouton, dans la page. En arabe, il partait vers la
droite et **sortait de l'écran** (bords mesurés à 1054 et 1452 px pour une page
de 1440 px).

La cause : le panneau était aligné sur `inset-inline-end` — une propriété
logique, donc correcte en soi, mais dans une barre d'outils qui se retourne elle
aussi, « le bord de fin » se retrouve du côté extérieur de la page. Le même
raisonnement vaut pour la vraie boutique : les filtres de collection sont rendus
par `snippets/facets.liquid`, qui utilise ce même panneau.

**Correction** (dans le bloc arabe de la feuille de style) :

```css
[dir="rtl"] .popover__panel { inset-inline-end: auto; inset-inline-start: 0; }
```

Le panneau s'ouvre maintenant vers l'intérieur : mesuré de 1054 à **1294 px**,
aligné sur son bouton, entièrement dans la page.

Deux signalements du premier passage se sont révélés être de **faux
positifs**, et le contrôle a été affiné en conséquence : la pastille du panier
(qui dépasse volontairement de son icône) et l'icône elle-même n'étaient pas des
textes rognés — le contrôle ne considère désormais comme rogné qu'un bloc qui
masque réellement son contenu.

### 17.3 Le second défaut, trouvé en montrant les écrans ouverts

Pour rendre le premier correctif visible, deux écrans d'état ont été ajoutés en
arabe : la collection avec le **tri ouvert** et avec les **filtres ouverts** —
comme ils existent déjà en français. Ils ont révélé un second défaut :

**le tiroir de filtres s'ouvrait du mauvais côté** (mesuré de 0 à 376 px, donc à
gauche, alors qu'en arabe il doit venir de la droite — c'est l'inverse du panier).
La règle de miroir que j'avais écrite pour ce tiroir ajoutait une correction de
position (`inset-inline-end`) déjà faite par la propriété logique d'origine : le
tiroir était donc repoussé deux fois, du même côté que le panier.

Correction — il ne fallait garder que le **sens d'entrée** :

```css
[dir="rtl"] .drawer { transform: translateX(-100%); }        /* panier : par la gauche */
[dir="rtl"] .drawer--start { transform: translateX(100%); }  /* filtres : par la droite */
```

Vérifié après correction : le tiroir de filtres occupe 1064 → 1440 px en
1440 (donc le bord droit), et 14 → 390 px en 390 ; le tiroir de menu, lui, part
hors écran par la gauche (−1440 → 0), ce qui est le bon sens d'entrée.

### 17.4 Résultat

**41 pages × 2 largeurs = 82 contrôles, aucun défaut.** La mise en page tient en
sens droite→gauche sur l'ensemble du thème, y compris les composants qui n'ont
pas de version arabe visible dans l'aperçu. Les deux défauts de la passe (§17.2 et
§17.3) sont corrigés dans `theme.css`, donc dans la vraie boutique aussi.

### 17.5 Un détail connu, non corrigé volontairement

En 390 px, ce même panneau peut dépasser d'environ **14 px sur la gauche en
français** : il fait au minimum 15 rem (240 px) et s'aligne sur un bouton situé
près du bord. Ce n'est pas un défaut dû à l'arabe, c'est le comportement du
design d'origine, relevé tel quel. Le corriger demanderait de changer la largeur
ou l'ancrage du panneau sur téléphone — une décision de design à valider, pas une
correction technique. C'est noté ici pour ne pas l'oublier.

### 17.6 Fichier ajouté

| Fichier | Rôle |
|---|---|
| `verifier_rtl.py` | force le sens droite→gauche sur toutes les pages et signale débordements, éléments hors cadre, textes rognés et chevauchements |

---

## 18. Le sélecteur de langue devient une bascule (2026-10-04)

### 18.1 Ce qui n'allait pas

Le sélecteur de l'en-tête était un dépliant : il affichait la langue courante
(« Français ») et, au clic, la liste des langues — dont la langue courante
elle-même. En arabe, le mot arabe et le mot français se retrouvaient **collés
l'un à l'autre** (« العربيةFrançais »), comme le montre la capture envoyée par le
client. Un sélecteur qui montre les deux langues en même temps n'est pas un
changement de langue : c'est une liste à dérouler.

### 18.2 Ce qui a été fait

L'en-tête n'affiche plus **qu'un seul mot : la langue vers laquelle on bascule.**

| Page lue | Ce que l'en-tête affiche | Le clic mène à |
|---|---|---|
| version française | **العربية** | la version arabe de la même page |
| version arabe | **Français** | la version française de la même page |

Un clic, et la langue change — sans ouvrir de liste, sans montrer les deux mots.
Le mot est écrit dans sa propre langue et dans sa propre police (le nom arabe
s'affiche en IBM Plex Sans Arabic), avec `lang` et `hreflang` corrects pour les
moteurs de recherche.

### 18.3 Dans le thème

`sections/header.liquid` : le bloc `<details>` dépliant est remplacé par un
formulaire `localization` à **une seule valeur**. La langue cible est trouvée par
comparaison des langues publiées (`localization.available_languages`) : le
système prend la première langue différente de la langue courante. Shopify
enregistre le choix dans la session du visiteur, ce qui fait basculer la page.

* deux langues publiées (le cas de LLUFAN) : la bascule alterne d'une langue à
  l'autre, dans les deux sens ;
* plus de deux langues publiées un jour : la bascule propose la langue suivante
  de la liste. C'est suffisant, mais si vous dépassez deux langues il faudra
  repasser à un menu déroulant — c'est noté ici pour ne pas l'oublier.

Les styles du dépliant sont conservés : le **sélecteur de pays** (désactivé par
défaut) s'en sert toujours pour sa liste déroulante.

### 18.4 Dans l'aperçu

Les pages françaises affichent « العربية », les pages arabes « Français ». La
bascule est aussi précise que la vraie :

| Page de départ | Après le clic |
|---|---|
| accueil (fr) | accueil arabe |
| fiche produit Nomad (fr) | fiche produit arabe |
| collection Allaitement (fr) | collection arabe |
| panier (fr) | panier arabe |
| les six pages arabes | la page française correspondante |

Les pages françaises qui n'ont pas encore de version arabe (FAQ, Club Maman,
pages d'information…) renvoient à l'accueil arabe : dans la boutique, la bascule
conserve toujours la page consultée, c'est une commodité de l'aperçu.

**Vérification faite au clic**, sur sept allers-retours : chaque bascule atteint
la bonne page, et il n'y a **qu'un seul** élément de langue dans l'en-tête —
plus de doublon.

### 18.5 Fichiers touchés

| Fichier | Modification |
|---|---|
| `theme/sections/header.liquid` | dépliant → bascule à une seule langue |
| `theme/assets/theme.css` | styles `.header__langue` (le dépliant reste pour le pays) |
| `build_preview.py` | bascule « العربية » sur les 41 pages françaises |
| `build_arabe.py` | bascule « Français » sur les 6 pages arabes |
| `patch_langue_bascule.py` (désormais dans `historique/`) | le script qui a appliqué la modification |

## 19. Tout le site en arabe : chaque page a sa jumelle (2026-10-04)

### 19.1 Ce qui n'allait pas

L'étape précédente avait donné une version arabe à **six pages** : l'accueil, une
collection, une fiche produit, le panier, plus l'état « filtres ouverts » et
« tri ouvert ». Le reste du site restait en français : quelqu'un qui lisait la
FAQ, le Club Maman, le journal, une page d'information ou son compte voyait du
français, et la bascule « العربية » le renvoyait à l'accueil arabe au lieu de la
page consultée. Deux détails s'ajoutaient : les **noms de wilayas** du formulaire
de commande restaient en français (« Alger » au lieu de « الجزائر »), et deux
libellés du gabarit d'adresses du compte étaient écrits en dur dans le thème.

### 19.2 Ce qui a été fait

**Chaque page française a maintenant sa jumelle arabe complète** — même structure,
mêmes composants, mêmes réglages, en droite → gauche.

| Famille | Pages françaises | Jumelles arabes |
|---|---|---|
| Accueil | 1 | 1 |
| Collections | 9 | 9 |
| Fiches produit | 11 | 11 |
| Panier et commande | 2 | 2 |
| Information (7 pages + FAQ + Club Maman + contact) | 10 | 10 |
| Journal (liste + 3 articles) | 4 | 4 |
| Compte et technique (compte, recherche, 404) | 4 | 3 |
| **Total** | **41** | **40** |

La seule page sans jumelle est le **guide technique** « Comment ajouter une
vidéo » : c'est un mode d'emploi pour vous, pas une page de la boutique.

**Ce qui suit la langue, désormais :**

* les **69 wilayas et leurs 1 541 communes** dans le formulaire de commande : le
  nom affiché est arabe (`nom_ar`), la valeur envoyée à Shopify ne change pas ;
* les **messages du formulaire** (champs, erreurs, récapitulatif, prix en دج),
  les **libellés de l'interface** (panier, filtres, tri, recherche, compte,
  page introuvable) et l'**onglet du navigateur** ;
* la **bascule de langue**, qui mène à la jumelle de la page lue : 40 pages
  arabes → leur page française, 40 pages françaises → leur page arabe.

**Deux libellés français étaient encore écrits en dur** dans le gabarit
d'adresses du compte (« Adresse », « Ville ») : ils sont passés en clés de
langue (`customers.address`, `customers.city`), présentes dans les deux fichiers
de langue. Le thème compte maintenant **121 clés**, toutes les deux langues.

### 19.3 Ce qui reste volontairement en français ou en chiffres

| Élément | Pourquoi |
|---|---|
| « LLUFAN », « llufan.com », le logo | le nom de la marque ne se traduit pas |
| les prix (« 3 200 دج ») | les montants gardent leurs chiffres, seule l'unité est arabe |
| le numéro WhatsApp et l'adresse e-mail | identiques dans les deux langues |
| les textes juridiques (CGV, mentions, confidentialité, retours) | toujours **à écrire par LLUFAN** — aucun texte n'a été inventé |
| le **nom** des champs du formulaire de commande (`contact[Téléphone]`, objet « Commande — paiement à la livraison ») | invisible pour la cliente : ce libellé n'apparaît que dans l'e-mail de commande que vous recevez |

Les textes arabes sont des **traductions de démonstration** : elles doivent être
relues par un arabophone avant la mise en ligne.

### 19.4 Contrôles passés

| Contrôle | Résultat |
|---|---|
| `verifier_arabe.py` — les 40 pages arabes en 390 px | **0 problème** : polices arabes chargées, miroir droite → gauche, formulaire de commande en دج, aucune page qui déborde |
| `verifier_pages.py` — 82 fichiers × 3 largeurs | **246 contrôles, 0 défaut** |
| `verifier_rtl.py` — 41 pages forcées en droite → gauche, 2 largeurs | **82 contrôles, 0 défaut** |
| `valider_theme.py` | 51/51 fichiers Liquid, 27 JSON valides, 121 clés, 0 anomalie |
| `valider_shopify.py` | 22 modèles contrôlés, 0 anomalie |
| `audit_cta.py` | 0 bouton sur `#`, 0 lien mort |
| Recherche de mots français visibles sur les 40 pages arabes | seule occurrence : le mot **« Français »** de la bascule — c'est-à-dire l'invitation à changer de langue, rien d'autre |

### 19.5 Le fichier de traduction s'étend à tout le site

`LLUFAN-DEMO-traductions-ar.csv` passe de 94 à **249 lignes** :

| Type | Contenu | Lignes |
|---|---|---|
| PRODUCT / PRODUCT_OPTION / PRODUCT_OPTION_VALUE | 10 produits, options et valeurs | 69 |
| COLLECTION | 5 collections (titre + description) | 10 |
| PAGE | les 7 pages d'information, la FAQ (8 questions), le Club Maman (4 espaces, 3 discussions), la page Contact | 138 |
| BLOG / ARTICLE | le journal et ses 3 articles (titre, chapeau, texte) | 13 |
| ONLINE_STORE_THEME | les 17 textes saisis dans les réglages de sections (Club Maman, formulaire de commande, pied de page, bandeau de démonstration) | 17 |

Deux points de méthode, notés en tête du fichier :

* les **libellés de l'interface** ne passent pas par ce CSV : ils sont déjà
  traduits dans le thème (`locales/ar.json`), donc publiés avec lui. Rien à
  coller ;
* les **réglages de sections** apparaissent dans l'export Shopify sous le type
  `ONLINE_STORE_THEME` (champ du genre `section.<id>.<réglage>`) : on les repère
  par leur texte français. Ils peuvent aussi se saisir directement dans
  l'éditeur de thème, en basculant la langue d'édition — les valeurs arabes sont
  prêtes dans le CSV.

### 19.6 Dans l'aperçu

L'aperçu d'ensemble liste maintenant **81 pages (41 françaises + 40 arabes)**
dans une famille « Version arabe », avec la même vignette et le même rôle que
leur jumelle française, et cette phrase en tête de famille : *chaque page
française a sa jumelle arabe complète… les textes arabes sont des traductions de
démonstration, à relire avant publication*. Le sommaire passe de 1,6 à 3,0 Mo.

### 19.7 Fichiers touchés

| Fichier | Modification |
|---|---|
| `build_arabe.py` | générateur du site arabe entier (40 pages) — réécrit |
| `demo/contenu_demo_ar.py` | contenu arabe des pages d'information, FAQ, Club Maman, journal, contact, recherche, compte, 404 |
| `demo/produits/llufan-livraison-dz.json` | 69 noms de wilayas en arabe (`nom_ar`) |
| `assets/llufan-livraison.js` | lit la langue de la page et ses libellés (`data-libelle-*`) |
| `snippets/forme-commande.liquid` | 10 attributs `data-libelle-*` — en arabe dans la version arabe |
| `locales/fr.default.json`, `locales/ar.json` | 9 clés `commande.*` + 2 clés d'adresse → 121 clés |
| `templates/customers/addresses.liquid` | « Adresse » / « Ville » écrits en dur → clés de langue |
| `build_preview.py` | bascule « العربية » vers la jumelle exacte (table des 40 pages arabes) |
| `build_apercu.py` | famille « Version arabe » : 40 vignettes, 81 pages au total |
| `generer_csv_traductions.py` | CSV de traductions étendu : 249 lignes |
| `patch_wilayas_ar.py` (désormais dans `historique/`) | le script qui a appliqué la traduction des wilayas |

---

## 20. Allègement de l'espace de travail (2026-10-04)

À la demande du client — « libère l'espace, laisse les fichiers importants pour
continuer le travail » — l'espace de travail passe de **139 Mo à 85 Mo**. Rien
n'a été perdu : ce qui a été retiré était soit dupliqué, soit reconstruit en
quelques secondes par les scripts déjà présents.

| Retiré | Taille | Comment le retrouver |
|---|---|---|
| `LLUFAN-sauvegarde-2026-10-04.zip` | 31 Mo | `bash llufan/refaire_archives.sh` |
| `LLUFAN-apercu-local.zip` | 36 Mo | idem |
| `llufan/__pycache__/` | — | se recrée tout seul |

Est conservé, parce que c'est ce qui sert à travailler : la source du thème
(`theme/`, 2,5 Mo), les contenus et visuels (`demo/`, 6,2 Mo), les 82 pages de
l'aperçu (`preview/`, 59 Mo), la documentation, les scripts, les CSV de
traduction, et les fichiers d'origine (`uploads/`, 3 Mo).

Une **sauvegarde légère des sources** reste à la racine :
`LLUFAN-sources-2026-10-04.zip` (176 fichiers, 12 Mo) — le thème, les contenus,
les scripts et la documentation, sans les pages de l'aperçu, qui se régénèrent
avec `python3 build_preview.py` puis `python3 build_arabe.py`.

Le script `llufan/refaire_archives.sh` reconstruit les trois archives d'un coup
(et recrée les pages de l'aperçu d'abord si elles manquent). Si la place manque
encore un jour, le plus gros poste restant est `preview/` — 59 Mo, entièrement
régénérable sans navigateur.

### 20.1 Incident du 4 octobre : six fichiers revenus à leur état d'avant

L'allègement a été fait juste après un redémarrage de la machine de travail, qui
a remis le plan de travail en place — et cette remise en place avait été prise
**avant** la traduction du site entier. Résultat : six fichiers du thème étaient
revenus à leur état de la veille, alors que l'aperçu, lui, montrait bien la
version bilingue complète :

| Fichier | Ce qui avait disparu |
|---|---|
| `assets/llufan-livraison-dz.json` | les 69 noms de wilayas en arabe (`nom_ar`) |
| `assets/llufan-livraison.js` | le choix de la langue à l'affichage |
| `snippets/forme-commande.liquid` | les 10 libellés transmis au script |
| `locales/fr.default.json`, `locales/ar.json` | 11 clés (`commande.*`, adresse du compte) |
| `templates/customers/addresses.liquid` | « Adresse » / « Ville » en clés de langue |

Les fichiers ont été restaurés depuis `LLUFAN-theme-Shopify.zip`, qui portait
l'état vérifié, et l'aperçu a été régénéré : les deux sont de nouveau identiques
et les contrôles repassent (121 clés, 0 anomalie).

Pour que ce genre d'écart se voie tout de suite, un contrôle a été ajouté :

    python3 verifier_theme_zip.py                 montre ce qui diffère
    python3 verifier_theme_zip.py --archive-saine  l'archive sert-elle la référence ?
    python3 verifier_theme_zip.py --restaurer      remet theme/ dans l'état de l'archive
                                                   — REFUSÉ si l'archive a reculé
    python3 verifier_empreintes.py --restaurer     restaure depuis reference/ (l'état sûr)

À lancer après toute restauration d'espace de travail, avant de se fier au
dossier `theme/`.

**La règle ajoutée le 6 octobre, après la quatrième alerte.** Restaurer le dossier
depuis l'archive était le bon réflexe — à condition que l'archive soit saine. Or
ce jour-là, une archive construite *pendant* un recul servait elle aussi
l'ancienne feuille de style : `--restaurer --forcer` a donc écrasé une copie
saine du dossier par une version dépassée. Deux garde-fous en sont nés :

1. `reference/theme.css` + `empreintes-reference.json` : la copie de référence de
   la feuille de style, avec son empreinte. C'est la **seule** source de vérité
   pour un fichier surveillé — l'archive, elle, peut mentir ;
2. `verifier_theme_zip.py --restaurer` **refuse** désormais de restaurer depuis
   une archive non conforme à la référence (code de sortie 3), et le message dit
   quoi faire : restaurer depuis `reference/`, puis reconstruire.

Le contrôle avant envoi applique cet ordre : la référence d'abord, l'archive
ensuite.

### 20.2 Inventaire : ce qui est gardé, et pourquoi

Deuxième passe le même jour, à la demande du client — « garde tout ce qui sert à
continuer le travail, ne supprime que le redondant ». L'espace de travail ne
contient plus rien de redondant à l'échelle du mégaoctet : **84 Mo**, dont voici
la répartition tenue par `llufan/audit_espace.py` (script ajouté pour ça, avec la
détection des doublons par empreinte) :

| Pièce | Nature | Taille |
|---|---|---|
| `llufan/theme/` (102 fichiers) | SOURCE — ce qu'on modifie | 2,2 Mo |
| `llufan/demo/` (111 fichiers) | SOURCE — contenus, visuels, vignettes | 6,9 Mo |
| `llufan/preview/` (82 fichiers) | LIVRABLE — l'aperçu à regarder | 58,0 Mo |
| `llufan/` racine (34 fichiers) | SOURCE — doc, scripts, CSV | 0,5 Mo |
| `llufan/LLUFAN-theme-Shopify.zip` | LIVRABLE — à importer dans Shopify | 1,9 Mo |
| `uploads/` | SOURCE — vos fichiers d'origine | 3,0 Mo |
| `LLUFAN-sources-2026-10-04.zip` | SAUVEGARDE — la copie de sûreté demandée *(remplacée depuis par la sauvegarde complète ; voir §22.4 et §23)* | 11,5 Mo |

Le contenu strictement identique présent deux fois représente **0,5 Mo**, et
chaque paire a sa raison :

* la **photo du coussin Nomad** existe dans `uploads/` (votre fichier d'origine)
  et dans `theme/assets/` (ce que Shopify affiche) — 323 Ko. Retirer l'un des
  deux, c'est soit perdre votre original, soit casser le thème ;
* les **deux fichiers de la police arabe de texte** (`llufan-ar-body-400.woff2`
  et `-600.woff2`) sont identiques au bit près : le demi-gras arabe du corps de
  texte s'affiche donc comme le poids normal. **Invisible en pratique**, et
  volontairement laissé tel quel : corriger ce détail voudrait dire retoucher un
  thème vérifié pour 92 Ko — le genre de changement qui a déjà coûté cher le
  4 octobre (voir §20.1). À faire un jour, proprement, avec le vrai fichier 600 ;
* **quatre vignettes** sont identiques à leur voisine parce que la page
  « alias » (`collection.html`, `produit.html`) et sa page « modèle » donnent
  exactement le même rendu — c'est le résultat attendu, pas un doublon.

Ce qui **n'est pas** compté comme redondance : les images, les polices et les
styles sont recopiés dans chacune des 82 pages de l'aperçu. C'est précisément ce
qui les rend ouvrables hors ligne, sans serveur ni connexion — la contrainte
posée à l'étape 19.

La seule réserve de place qui reste est `llufan/preview/` : un livrable, mais qui
se régénère en 4 secondes (`build_preview.py` puis `build_arabe.py`). À noter
toutefois : `apercu.html` et les vignettes, eux, demandent un navigateur — donc
si l'espace devenait critique, on garderait ces deux-là et on retirerait les 82
pages, ou l'inverse.

---

## 21. La version téléphone, alignée sur la référence (2026-10-04)

### 21.1 Ce qui a été mesuré chez la référence

Plutôt que d'ajuster à l'œil, la version téléphone de la référence de design a
été chargée dans Chromium en 390 px (puis 320, 360 et 430) et mesurée. Ce qui a
été relevé, en pixels :

| Élément de la référence | Mesure |
|---|---|
| Bandeau d'annonce | 37 px de haut, texte de **14 px** (police serif maison), message tenant sur une ligne |
| Bandeau corail (nos raccourcis) | 47 px, texte de 14 px, contenu qui défile à l'horizontale |
| En-tête | 54 px : burger à gauche, logo centré, puis langue + recherche + panier à droite |
| Icônes de l'en-tête | 22 px, espacées de 20 px, sans fond |
| Titre de la fiche produit | 24 px, sans capitales forcées, léger resserrement de l'interlettrage |
| Bouton principal | 350 × **57 px** (pleine largeur), texte de 14 px |
| Grille de collection | 2 colonnes, images carrées, marges de page 10 px, 10 px entre les cartes → cartes de **180 px** à 390 px |

La référence **ne fait aucune distinction d'écran** dans son en-tête : il est
identique de 320 à 430 px.

### 21.2 Ce qui a été repris, et ce qui a été écarté

**Repris :** les hauteurs de bandeaux, la taille du texte des bandeaux, la
composition de l'en-tête (burger / logo / langue, recherche, panier — le compte
n'apparaît que dans le menu), le titre de fiche produit, la grille à deux
colonnes resserrée, les boutons pleine largeur de 56 px, la marge de page de
15 px qui élargit les cartes.

**Écarté, volontairement :** les icônes de 22 px de la référence. Une cible
tactile de 22 px est deux fois plus petite que ce que recommandent Apple et
Android (44 px) et sous le plancher d'accessibilité (24 px). Nos commandes
d'en-tête font **44 px de côté**, avec la même icône de 22 px à l'intérieur :
l'aspect est celui de la référence, la prise est confortable.

### 21.3 Ce qui a été corrigé au passage — et c'était grave

Le contrôle `verifier_mobile.py` (81 pages × 9 largeurs de téléphone, 729
contrôles) a trouvé des défauts qu'aucun contrôle à 390 px seul ne voyait :

| Défaut | Effet sur un téléphone |
|---|---|
| Icônes d'en-tête écrasées à **0-7 px** | compte, recherche et panier invisibles et intouchables |
| Bouton menu **sans taille** | le menu était inaccessible |
| Boutons « Filtrer » et « Trier par » de **20 px** de haut | filtres et tri difficiles à ouvrir |
| Lignes de filtres et cases de **23 px** | on coche à côté |
| Panneau « Trier par » **hors écran** sous 380 px | tri inatteignable |
| Pastilles de couleur de **28 px**, quantité de **25 px** | choix de la couleur et quantité laborieux |
| Bandeau de démonstration sur **3 lignes** | 130 px perdus en haut de chaque page |
| Page panier **sans en-tête** dans l'aperçu | l'aperçu ne ressemblait pas à la vraie page Shopify |

Sept de ces huit défauts existaient **avant** cette demande : le site n'était
pas seulement « perfectible » sur téléphone, il était partiellement inutilisable
sous 430 px. Aucun n'est visible sur les captures d'ordinateur.

### 21.4 Résultat mesuré

| Colonne | Référence | LLUFAN |
|---|---|---|
| Bandeau d'annonce | 37 px | 38 px |
| Raccourcis | 47 px | 46 px |
| En-tête | 54 px | 60 px (cibles tactiles de 44 px) |
| Carte produit à 390 px | 180 px | 174 px |

`verifier_mobile.py` : **81 pages × 9 largeurs = 729 contrôles, 0 page en
défaut** (aucun débordement, aucune zone tactile sous 24 px, aucun texte sous
11 px, aucun texte tronqué). Les 66 zones entre 24 et 40 px sont les liens
« secondaires » de la fiche produit et de la grille (liens de la barre
d'outils) : au-dessus du plancher d'accessibilité, notés comme à surveiller,
aucun n'est une commande d'achat.

Les contrôles plus anciens repassent tous : `verifier_pages.py` 246/0,
`verifier_rtl.py` 82/0, `verifier_arabe.py` 0 problème.

### 21.5 Ce que la référence nous a appris sur nos propres textes

Deux messages du bandeau d'annonce et un titre de section étaient trop longs
pour une ligne de téléphone. Ils ont été raccourcis **sans rien perdre** :
« Paiement à la livraison partout en Algérie » → « Paiement à la livraison ·
69 wilayas ». Les messages arabes ont été réécrits pour dire exactement la même
chose que les français (ils parlaient d'autre chose), et le pré-bandeau arabe,
qui n'avait ni liens ni mêmes entrées que le français, est devenu sa
traduction exacte — mêmes quatre raccourcis, mêmes destinations.

### 21.6 Fichiers touchés

| Fichier | Modification |
|---|---|
| `theme/assets/theme.css` | §24 « téléphones : tout ce qui se touche » et §25 « rythme mobile de la référence », + en-tête `< 561 px` |
| `theme/sections/header.liquid` | repères `header__icone`, recherche et compte ajoutés au menu mobile |
| `theme/sections/header-group.json` | messages du bandeau raccourcis |
| `demo/contenu_demo.py`, `demo/contenu_demo_ar.py` | bandeaux et pré-bandeau, dans les deux langues |
| `build_preview.py` | icônes SVG dimensionnées, en-tête de l'aperçu aligné sur le thème, panier avec en-tête, bandeau de démonstration court sur téléphone |
| `build_arabe.py` | pré-bandeau cliquable, mêmes repères que le français |
| `build_guide_video.py` | cases et légendes lisibles au doigt |
| `generer_kit_shopify.py` | le kit à coller et les traductions arabes, **133 lignes, une par champ** |
| `verifier_mobile.py` | **nouveau** : 81 pages × 9 largeurs de téléphone |
| `ref-mobile/` | captures de la référence et de LLUFAN, côte à côte, pour comparaison |
| `comparaison-mobile.html` | **la page à ouvrir** : les captures de la référence et de LLUFAN face à face, avec les mesures et l'écart volontaire |
| `verifier_theme_zip.py` | compare `theme/` et l'archive livrée ; **refuse** de restaurer quand l'archive a reculé ou pris du retard (`--archive-saine`) |
| `verifier_empreintes.py` | la feuille de style est-elle celle de `reference/` ? (`--restaurer` la remet en état ; lit le dossier comme l'archive) |
| `tests/liquidjs/` | le moteur Liquid fourni avec le contrôle vidéo (184 Ko, licence MIT) : `node tests/test-section-video.mjs` marche sans npm et sans réseau |

---

## 22. Garder le thème, l'aperçu et les archives d'accord (2026-10-05)

### 22.1 Le problème, et pourquoi il faut s'en occuper

Le 5 octobre, la session de travail a repris sur un espace de travail **remis en
place** entre deux tours : le dossier `theme/` avait reculé sur deux fichiers
(`assets/theme.css`, `sections/header-group.json`) — c'est-à-dire que les
correctifs mobiles de la veille avaient disparu du dossier, mais pas de
l'archive du thème ni de l'aperçu. Un import Shopify à cet instant aurait livré
un thème sans les correctifs.

La cause est banale : une remise en place rétablit les fichiers tels qu'ils
étaient à un instant antérieur. Ce qui est moins banal, c'est que **l'ancien
garde-fou ne pouvait pas le voir** : il comparait les dates, et la remise en
place avait réécrit toutes les dates à la même valeur. Il a donc conclu
« le dossier est plus récent, ne pas restaurer » — soit **l'exact contraire de
la vérité**.

### 22.2 Ce qui permet de trancher maintenant

`verifier_theme_zip.py` tient un **journal des états** (`etat-theme.json`).
À chaque reconstruction de l'archive du thème, il inscrit une empreinte de
chaque fichier. Il en garde les douze derniers. Le diagnostic devient
mécanique :

| Situation | Ce que le script répond | Ce qu'il faut faire |
|---|---|---|
| Le dossier correspond à un **état ancien** du journal | « LE DOSSIER A RECULÉ » | `--restaurer` : la restauration est sûre |
| Le dossier ne correspond à **aucun état** et les dates ne disent plus rien | « JE NE PEUX PAS TRANCHER » | comparer à la main, puis `--restaurer` ou `--forcer` |
| Le dossier a été **modifié après** l'archive | « L'ARCHIVE A PRIS DU RETARD » | refaire l'archive — surtout **pas** restaurer |
| Les deux sont identiques | « rien à faire » | — |

Deuxième filet : l'**aperçu**. Comme il vit dans un autre dossier, il survit
presque toujours à une remise en place. Chaque état du journal conserve les
empreintes de l'aperçu de l'époque ; si l'aperçu du disque correspond à un état
dont l'archive est la même, c'est que le dossier du thème est celui qui est en
retard. C'est ce qui a permis, le 5 octobre, de restaurer en connaissance de
cause malgré un journal encore vide.

### 22.3 Les quatre cas, essayés pour de vrai

Les quatre lignes du tableau ont été **testées** le 5 octobre, dans un dossier
isolé (pour ne pas abîmer le vrai thème) : dossier en retard → verdict correct
puis restauration automatique ; fichier modifié à la main → « archive en
retard » et **refus** de restaurer ; dates illisibles → « je ne peux pas
trancher » et refus. Un défaut a été trouvé et corrigé à cette occasion : le
verdict « le dossier a reculé » était écrasé par le verdict suivant, et la
restauration était refusée à tort.

### 22.4 Les archives

`bash llufan/refaire_archives.sh` produit désormais trois archives :

| Archive | Contenu | Taille |
|---|---|---|
| `LLUFAN-sauvegarde-2026-10-04.zip` | tout : thème, aperçu, contenus, scripts, docs | 55 Mo |
| `LLUFAN-apercu-local.zip` | la boutique hors ligne à emporter | 37 Mo |
| `llufan/LLUFAN-theme-Shopify.zip` | le thème à importer dans Shopify | 2 Mo |

La quatrième — `LLUFAN-sources-2026-10-04.zip`, 17 Mo — n'est qu'un
**sous-ensemble** de la sauvegarde complète (les mêmes fichiers, sans
l'aperçu). Elle n'est plus conservée en permanence pour ne pas recopier deux
fois les mêmes sources ; elle se refait avec `--complet`. C'est le seul
allègement, et il est réversible en une commande.

### 22.5 Le bon réflexe, dans l'ordre

1. `python3 verifier_theme_zip.py` — lire le verdict avant de toucher à quoi que ce soit.
2. Si un écart apparaît après un travail sur le thème : `bash llufan/refaire_archives.sh`.
3. Après une remise en place de l'espace : contrôler l'aperçu (`preview/`), puis restaurer si le script le confirme.
4. Ne jamais lancer `--restaurer` « pour voir » : c'est ce qui a effacé trois fichiers le 4 octobre.

---

## 23. Alléger l'espace de travail (2026-10-05)

### 23.1 Pourquoi maintenant

Deux constats, le même jour.

1. **Votre demande** : ne garder que la dernière archive et ce dont le travail
   inachevé a besoin.
2. **Un fait que j'avais mal interprété** : la sauvegarde complète (57 Mo) a
   *disparu* deux fois de l'espace de travail. Ce n'était pas un accident : avec
   l'aperçu (60 Mo), la boutique hors ligne (37 Mo) et le reste, l'espace
   dépassait la limite de ce qui peut être conservé d'une séance à l'autre — et
   c'est le plus gros fichier qui saute. Autrement dit : **cette sauvegarde
   n'était pas une sauvegarde**, puisqu'elle ne survivait pas.

### 23.2 Ce qui reste sur le disque

| Élément | Taille | Pourquoi il reste |
|---|---|---|
| `llufan/theme/` | 2,5 Mo | la source qu'on modifie |
| `llufan/demo/` | 7,1 Mo | contenus, visuels des produits, vignettes de la page d'ensemble |
| `llufan/ref-mobile/` | 5,0 Mo | captures et mesures de la référence : seule trace visuelle, la référence n'est plus en ligne ici |
| `llufan/*.py`, `*.sh`, `*.md`, `*.csv` | ~1,5 Mo | scripts, documents, CSV d'import |
| `llufan/tests/` | 192 Ko | le contrôle vidéo, autonome |
| `uploads/` | 3,0 Mo | vos fichiers d'origine |
| `llufan/LLUFAN-theme-Shopify.zip` | 2,0 Mo | **le livrable** à importer dans Shopify |
| `LLUFAN-sauvegarde-2026-10-04.zip` | 57 Mo | **la sauvegarde** : tout, y compris l'aperçu |

Soit environ 75 Mo — sous la limite, donc l'archive survit d'une séance à
l'autre. C'était le point à corriger.

### 23.3 Ce qui se refait tout seul

| Retiré | Taille | Se refait par | Durée |
|---|---|---|---|
| `llufan/preview/` (82 pages) | 60 Mo | `bash llufan/refaire_apercu.sh` | quelques secondes |
| `LLUFAN-apercu-local.zip` | 37 Mo | `bash llufan/refaire_archives.sh` | quelques secondes |
| `LLUFAN-sources-2026-10-04.zip` | 17 Mo | `bash llufan/refaire_archives.sh --complet` | quelques secondes |

Rien n'est perdu : l'aperçu est dans la sauvegarde, et il se reconstruit sans
navigateur — c'est nouveau : la page d'ensemble réutilise les vignettes déjà
prises (`SANS_CAPTURE=1`), au lieu d'exiger Chromium.

### 23.4 Les deux commandes à retenir

    bash llufan/refaire_apercu.sh      revoir l'aperçu (82 pages + page d'ensemble)
    bash llufan/refaire_archives.sh    reconstruire les archives (--complet = + les sources)

Et pour libérer la place de nouveau après un travail :

    bash llufan/liberer_espace.sh         montre ce qui peut être libéré
    bash llufan/liberer_espace.sh --oui   le fait (il vérifie d'abord que la
                                          sauvegarde contient bien l'aperçu)

### 23.5 Second passage : ne garder que ce qui sert à la suite (5 octobre 2026)

Trois retraits de plus, après inventaire :

| Retiré | Taille | Justification |
|---|---|---|
| `patch_*.py` (7 scripts) | 106 Ko | leur travail est **dans** les fichiers ; aucun script ne les appelle ; les relancer modifierait des fichiers déjà modifiés. Déplacés dans `historique/` (92 Ko) plutôt que supprimés : ils racontent comment le thème a été construit |
| `ref-mobile/llufan-*.png` (7 captures) | 1,9 Mo | nos propres captures de téléphone, qui deviendraient fausses au prochain changement du thème. Elles survivent là où c'est utile : dans `comparaison-mobile.html` et dans la sauvegarde. Les 6 captures **de la référence**, elles, restent : c'est une preuve extérieure qu'on ne peut pas refaire à l'identique |
| `__pycache__/` | 90 Ko | caches Python, jamais conservés |

Ce qui reste — 71 Mo — et pourquoi :

| Élément | Taille | Rôle |
|---|---|---|
| `LLUFAN-sauvegarde-2026-10-04.zip` | 53 Mo | la copie de sûreté demandée : **tout**, aperçu compris |
| `llufan/theme/` + `LLUFAN-theme-Shopify.zip` | 4,3 Mo | la source qu'on modifie et le livrable à importer |
| `llufan/demo/` | 7,0 Mo | contenus et visuels : sans eux, plus d'aperçu ni de fiches produit |
| `llufan/ref-mobile/` | 3,0 Mo | mesures et captures de la référence de design |
| `llufan/*.py`, `*.sh`, `*.md`, `*.csv` | 1,6 Mo | scripts, contrôles, documents, CSV d'import |
| `uploads/` | 3,0 Mo | vos fichiers d'origine |

Règle retenue, valable pour la suite : **est conservé** ce qui n'existe nulle
part ailleurs (sources, contenus, documents, script, vos fichiers) ; **est
retiré** ce qui se refait à l'identique en quelques secondes (l'aperçu, la
boutique hors ligne, les archives secondaires) — à condition d'être dans la
sauvegarde, ce que `liberer_espace.sh --oui` vérifie avant de supprimer.

---

## 24. Rien n'a été retiré qui serve à la boutique (2026-10-05)

### 24.1 La question, et la réponse

Après les deux allègements, la question était : **est-ce que la suite de la
construction sur Shopify est intacte ?** Réponse : oui, et c'est vérifiable en
une commande.

Les six fichiers qui construisent la boutique sont tous sur le disque, et
aucun n'a jamais été retiré :

| # | Fichier | Où dans Shopify |
|---|---|---|
| 1 | `llufan/LLUFAN-theme-Shopify.zip` | Thèmes → Ajouter un thème → Importer un fichier ZIP |
| 2 | `llufan/LLUFAN-DEMO-produits.csv` | Produits → Importer |
| 3 | `llufan/LLUFAN-DEMO-collections.csv` | Produits → Collections |
| 4 | `llufan/LLUFAN-DEMO-journal-a-publier.md` | Blog → Ajouter un article (copier-coller) |
| 5 | `llufan/LLUFAN-DEMO-traductions-ar.csv` | Paramètres → Langues |
| 6 | `llufan/demo/produits/*.jpg` | à glisser sur les fiches produit |

Ce qui a été retiré ne concerne que la **vérification visuelle** — et l'aperçu
se régénère à l'identique, ce qui a été refait et vérifié le 5 octobre :
82 pages reconstruites, puis 81 pages × 3 largeurs de téléphone = 243
contrôles, **0 défaut**.

### 24.2 Le contrôle qui le prouve : `verifier_import_shopify.py`

Les contrôles existants regardaient le dossier `theme/`. Aucun ne regardait
**l'archive elle-même**, c'est-à-dire ce que Shopify reçoit. Le nouveau
contrôle l'ouvre, l'extrait dans un dossier temporaire et vérifie sept choses :

1. la structure attendue — les sept dossiers, `layout/theme.liquid`,
   `config/settings_schema.json`, une langue par défaut ;
2. chaque `{% render %}` a son snippet, chaque `{% section %}` sa section,
   chaque groupe de sections ses sections ;
3. chaque fichier d'`assets/` cité en toutes lettres existe (police, feuille
   de style, script, visuel) — un asset manquant donne une page sans style,
   **sans aucun message d'erreur** ;
4. tous les JSON sont lisibles ;
5. aucun chemin de la machine de travail (`/home/user`, `file://`) : dans
   Shopify, un tel chemin ne mène nulle part ;
6. les quatre fichiers d'import sont là, avec les colonnes attendues ;
7. rien de superflu (`__MACOSX`, `.DS_Store`, `node_modules`).

Réponse sur l'état actuel :

    Archive : LLUFAN-theme-Shopify.zip (1,9 Mo, 110 entrées)
      Langues : fr.default.json, ar.json
      assets/ 25 · config/ 2 · layout/ 1 · locales/ 2 · sections/ 31
      snippets/ 12 · templates/ 23
      ✓ Le thème est prêt à être téléversé dans Shopify, tel quel.

**Le contrôle a été éprouvé** : sur une copie volontairement abîmée du thème
(snippet supprimé, JSON tronqué, asset manquant, domaine externe inconnu), il
signale les dix problèmes — il ne dit donc pas « prêt » à tort.

### 24.3 Trois défauts trouvés en préparant cette réponse

| Défaut | Conséquence si on ne l'avait pas vu |
|---|---|
| Le mode d'emploi et la liste de contrôle renvoyaient à `preview/apercu.html` et `LLUFAN-apercu-local.zip` comme s'ils étaient là | on aurait cherché des fichiers absents, en croyant à une perte |
| `refaire_apercu.sh` oubliait le guide « ajouter une vidéo » | l'aperçu reconstruit aurait eu 81 pages au lieu de 82, avec un lien mort |
| Chromium n'est pas conservé d'une séance à l'autre (ni les paquets Python) | les contrôles visuels échouent au premier essai ; c'est la première chose à réinstaller (`pip install playwright` + `python3 -m playwright install chromium`) |

### 24.4 Ce qui reste fragile, et ce qu'il faut faire

Deux éléments de l'environnement **ne survivent pas** à une pause : le
navigateur de contrôle et les paquets Python. Ce ne sont pas des fichiers du
projet, ils se réinstallent en deux commandes. Le reste — thème, contenus,
documents, CSV, vos fichiers d'origine — est dans l'espace de travail **et**
dans la sauvegarde, qui contient tout, aperçu compris.

---

## 25. Le visuel du produit réel utilisait une image générée (2026-10-05)

### 25.1 Ce qui a été trouvé

En recensant les contenus encore provisoires, un contrôle systématique des
visuels a montré que **la vignette du seul produit réel** — le coussin
d'allaitement Nomad, tiré de votre fichier `llufan-landing-nomad.html` — était
une image **générée** (un coussin bleu sur fond crème), alors que **votre photo**
du coussin existait dans `uploads/` depuis le début.

L'écart était d'autant plus visible que le **héros de l'accueil** utilisait,
lui, la vraie photo (`theme/assets/llufan-nomad-coussin.jpg`) : deux visuels
différents pour le même produit, sur la même boutique.

### 25.2 Ce qui a été fait

La vignette produit a été remplacée par un **cadrage carré de votre photo**
(1200 × 1200, le format des autres visuels produit), centré sur le coussin.
Vérifié à l'écran : sur la fiche produit comme dans la grille de collection, la
photo réelle s'affiche correctement.

Rien d'autre n'a été touché : les 9 autres produits sont fictifs, leurs visuels
aussi — c'est cohérent, et ils partiront avec eux.

### 25.3 Un dossier mort retiré — mais une règle enfreinte

`demo/img/` contenait **18 images (3,2 Mo)** — `final-hero-1.jpg`,
`produit-nomad.jpg`, `final-univers-*.jpg`… — plus citées par **aucun** script ni
aucune section du thème. À l'évidence, une génération antérieure des mêmes
visuels : les versions réellement utilisées sont dans `theme/assets/demo-*.jpg`
(affiches, éditorial, univers, héros) et `demo/produits/*.jpg` (produits).

**Ce que j'ai fait de travers.** Je les ai supprimées **avant** de refaire la
sauvegarde, et l'archive précédente — la seule qui les contenait — a été
écrasée par la nouvelle. Elles **ne sont plus récupérables**. La règle que
j'avais moi-même posée était : *on ne retire que ce qui est déjà protégé
ailleurs, et reconstruit en une commande*. Elle n'a pas été respectée.

Ce qui limite la portée de l'erreur :

* rien ne les citait — vérifié par recherche sur tous les scripts, sections et
  modèles ;
* les visuels en service sont intacts : `theme/assets/` (25 fichiers) et
  `demo/produits/` (10 visuels) sont ceux que la boutique utilise, et le
  contrôle d'import vérifie que chacun est bien là ;
* ce n'étaient pas des copies conformes des visuels en service : leurs tailles
  diffèrent (283 Ko contre 173 Ko pour l'éditorial, par exemple), donc probablement
  les mêmes photos à une compression plus lourde. *Déduction, pas certitude — je
  ne peux plus comparer.*

**Ce qui a été mis en place pour que cela ne recommence pas : `retirer.py`.**
Toute suppression passe désormais par lui : il compare chaque fichier à
l'empreinte de sa version sauvegardée et **refuse de supprimer** si un seul
manque ou diffère — « refaites l'archive d'abord ». Éprouvé dans les deux sens :
il autorise la suppression d'un fichier protégé, et la refuse pour un fichier
absent de la sauvegarde.

### 25.4 Ce qui reste à remplacer, et par qui

| Contenu | État | Qui peut le fournir |
|---|---|---|
| Vignette du coussin Nomad | **votre photo** ✔ | — |
| Héros de l'accueil | **votre photo** ✔ | — |
| Logo (en-tête, pied de page) | **vos fichiers** ✔ | — |
| 9 autres produits (visuels, prix, descriptions) | fictifs | à fournir avec les vrais produits |
| 3 avis de la page d'accueil | fictifs, marqués « Avis de démonstration » | vos clientes |
| 3 discussions du Club Maman | fictives | vos clientes |
| 3 articles du journal | fictifs | vous |
| CGV, mentions légales, retours, confidentialité | gabarits à trous `[à compléter]` | vous (ou un juriste) |
| Composition et entretien de chaque produit | « Composition de démonstration à remplacer » | vos fiches techniques |
| Délais de livraison « 2 à 5 jours ouvrés » | à confirmer | vous, selon le transporteur |

---

## 26. La version arabe montrait les communes en lettres latines (2026-10-05)

### 26.1 Le défaut, trouvé en éprouvant le parcours d'achat

En remplissant le formulaire de commande comme le ferait une cliente, la
version arabe affichait :

    الولاية : 01 - أدرار          ← wilaya en arabe
    البلدية : Adrar               ← commune en lettres latines

Les wilayas avaient leur nom arabe depuis l'étape 19 (`nom_ar`), les
**1 541 communes** non. C'était exactement le mélange des deux langues à
l'écran que vous aviez refusé le 4 octobre. Le récapitulatif de commande (le
texte qui part avec la commande) avait le même défaut, et il affichait en plus
« À domicile » en français au milieu de l'arabe.

### 26.2 La correction

**Les noms arabes viennent de la même source officielle** que la liste des
communes déjà dans le thème : `algeria-wilayas-communes`, qui publie `name_ar`
pour chacune des 1 541 communes. Aucun nom n'a été translittéré à la main.

Ce qui a été fait :

1. `theme/assets/llufan-livraison-dz.json` reçoit **`communes_ar`**, aligné
   index par index avec `communes` (même ordre, même longueur). **Les valeurs
   envoyées à Shopify ne changent pas** (`communes`, en lettres latines) :
   c'est le repère administratif que vous lisez dans la commande ;
2. `theme/assets/llufan-livraison.js` affiche `communes_ar` quand la page est
   en arabe, le nom latin sinon — et **le récapitulatif suit la langue de la
   page** (wilaya, commune, type de livraison) ;
3. l'aperçu (`build_arabe.py`) reçoit les deux libellés de livraison qui
   manquaient : il affichait « À domicile » faute de traduction.

### 26.3 L'appariement des noms : trois passes, rien d'inventé

Les deux listes contiennent les mêmes communes, mais rangées dans un **ordre
différent** et avec des **orthographes qui varient** (`Timekten`/`Timokten`,
`Tichy`/`Tichi`, `Tabelbala`/`Tabalbala`, `Mécheria`/`Mechria`…). Le script
`ajouter_communes_ar.py` apparie donc en trois passes :

| Passe | Méthode | Résultat |
|---|---|---|
| 1 | nom identique (accents, tirets et casse mis à part) | 1 246 |
| 2 | le nom le plus proche **dans la même wilaya** (seuil 0,55, marge nette sur le suivant) | +224 |
| 3 | le nom le plus proche **dans toute l'Algérie** (seuil 0,80) — la nouvelle carte a déplacé quelques communes d'une wilaya à l'autre | +64 |

**1 534 noms arabes sur 1 541 (99,5 %).** Les 224 rapprochements sont imprimés
par le script et ont été relus un par un. Le script **refuse d'écrire** dès
qu'une commune reste sans réponse — c'est ce qui garantit qu'aucun nom
approximatif n'est enregistré.

### 26.4 Les 7 communes laissées sans nom arabe

    Bouira            Z'barbar (El Isseri)
    Tlemcen           Oued Lakhdar
    Tiaret            Djebilet Rosfa
    Skikda            Djendel Saadi Mohamed
    Bordj Bou Arréridj  Tassamert
    Barika            Azil Abedelkader
    Bou Saada         Mohamed Boudiaf

Pour celles-là, la source officielle porte encore l'**ancien nom** (la loi
n° 26-06 du 4 avril 2026 a renommé `Metkaouak` → Abdelkader Azil, `Oued Chaïr`
→ Mohammed Boudiaf, `Ouled Atia` → Menaa) ou listait une autre commune au même
emplacement. Plutôt que d'écrire un nom arabe déduit — qui aurait pu désigner
la mauvaise commune —, la case est restée vide : **le formulaire affiche alors
le nom latin**, et ces 7 communes sont recensées dans le fichier lui-même
(`communes_ar_sans_nom`) comme ici. À compléter le jour où la liste officielle
sera à jour.

### 26.5 Vérification

Parcours rejoué dans un navigateur, sur les deux langues, desktop et téléphone :

| | Version française | Version arabe |
|---|---|---|
| Wilaya choisie | `01 - Adrar` | `01 - أدرار` |
| Communes affichées | Adrar · Reggane · Aoulef… | أدرار · رڨان · أولف… |
| Valeur envoyée à Shopify | `Adrar` | `Adrar` (**inchangée**) |
| Type de livraison (récapitulatif) | À domicile | إلى المنزل |
| Totaux | 5 200 DA → 4 900 DA en stop-desk | 5 200 دج → 4 900 دج |

Les contrôles repassent tous : `verifier_arabe.py` 0 problème ·
`verifier_rtl.py` 82/0 · `verifier_mobile.py` 729/0 · `verifier_pages.py` 246/0 ·
`verifier_import_shopify.py` ✓ prêt à téléverser.

## 27. Le référencement : partage sur les réseaux et données structurées (2026-10-05)

Inventaire d'abord, avant d'écrire quoi que ce soit : le thème portait déjà
l'adresse canonique de chaque page (`canonical`) et les liens entre les langues
(`hreflang`). Il ne portait **ni balises de partage, ni données structurées**.
Conséquence concrète : un lien LLUFAN envoyé sur WhatsApp ou Facebook
s'affichait comme une adresse nue — pas de titre, pas d'image — et Google
n'avait aucune description de la boutique ni des fiches produits.

### 27.1 Les deux greffons ajoutés

| Fichier | Rôle |
|---|---|
| `theme/snippets/seo-partage.liquid` | les balises de partage (Open Graph + carte Twitter) |
| `theme/snippets/seo-donnees-structurees.liquid` | les données structurées, en JSON-LD |
| `theme/layout/theme.liquid` | les appelle sur **toutes** les pages (deux `render` avant le bloc de langue) |
| `theme/config/settings_schema.json` | un réglage **« Image de partage »** à remplir dans l'éditeur |

### 27.2 Les balises de partage

Le titre, la description et l'adresse de la page ; l'image, avec une chaîne de
repli qui donne **toujours** une image :

    visuel de la page (produit, article, collection)
      → réglage « Image de partage » choisi dans l'éditeur (1200 × 630)
        → logo LLUFAN

Sur une fiche produit, la page annonce en plus son **prix**, sa **devise** et sa
**disponibilité** ; sur un article, sa **date de publication**. La version
partagée signale aussi qu'une version arabe existe (`og:locale:alternate`).
La carte Twitter passe en `summary_large_image` **seulement** quand il y a un
vrai visuel — un logo ne fait pas une grande carte (voir 27.4, cas n° 22).

### 27.3 Les données structurées

Quatre blocs, et seulement là où ils ont un sens :

| Bloc | Où | Ce qu'il dit |
|---|---|---|
| `Organization` | toutes les pages | le nom LLUFAN, le contact WhatsApp (`0772 415 120` → `+213772415120`), l'e-mail, le logo, et les réseaux **seulement s'ils sont renseignés** |
| `WebSite` | accueil uniquement | le nom de la boutique et la recherche interne (`SearchAction`) |
| `BreadcrumbList` | fiche produit | accueil → collection → produit (2 étapes s'il n'y a pas de collection, 1 sinon) |
| `Product` | fiche produit | titre, description nettoyée, jusqu'à 5 images, référence (seulement si elle existe), **une offre par variante** avec prix, devise et disponibilité |

Le bloc `Organization` indique aussi la langue du contact : il reprend la liste
des langues **publiées** par la boutique, telle quelle (`localization.available_languages`).
Rien n'est écrit en dur — aujourd'hui le français et l'arabe, puisque les deux
versions existent — et si la boutique n'en publiait qu'une, une seule
apparaîtrait.

Le prix est donné en **nombre** et non en texte, parce que c'est ce que Google
attend. Dans Liquid, `product.price` est toujours en **centimes**, quelle que
soit la devise : la conversion est `| divided_by: 100.0`. Le `.0` n'est pas
cosmétique — sans lui, Liquid arrondit à l'entier.

### 27.4 Ce qui n'a délibérément PAS été publié

Trois silences, qui sont des décisions et non des oublis :

* **aucune note d'avis** (`aggregateRating`) — les avis de démonstration sont
  fictifs ; publier une note inventée serait exactement ce qui est interdit ;
* **ni garanties ni délais** (`hasMerchantReturnPolicy`, `shippingDetails`) —
  les politiques de retour et les délais ne sont pas encore arrêtés ;
* **aucun prix barré, aucune promotion** : le thème n'annonce une remise que si
  la boutique en porte une réellement (voir §22 sur les garde-fous).

### 27.5 Le test, et les trois erreurs qu'il a attrapées

`node tests/test-seo.mjs` — **25 cas**, autonome (le moteur Liquid est fourni
dans `tests/liquidjs/`, aucun navigateur, quelques dixièmes de seconde). Il
rejoue une fiche produit, une page et l'accueil dans les deux langues.

Trois vraies erreurs, invisibles à l'œil nu, attrapées avant livraison :

| Erreur | Symptôme | Correction |
|---|---|---|
| un commentaire `/* … */` **dans** un `{% liquid %}` | `TokenizationError` : le thème refusait de s'analyser | commentaire en `#` (les `/* … */` des blocs `<style>` restent normaux) |
| `{search_term_string}` écrit dans une sortie `{{ }}` | `valider_theme.py` : « accolades déséquilibrées » | une variable `assign cible_recherche` avant la sortie |
| la clé `general.accueil` **inventée** | `valider_shopify.py` : « traduction manquante » | la clé a été écrite pour de bon dans `fr.default.json` (« Accueil ») et `ar.json` (« الرئيسية ») |

La troisième mérite d'être notée : notre propre contrôle a refusé une clé qui
n'existait pas. C'est le garde-fou qui fonctionne — **ne jamais inventer une clé
de traduction**, exactement comme on n'invente pas un prix.

Le test lui-même contenait trois attentes fausses, corrigées : un média de
démonstration sans `preview_image`, les prix attendus en dinars au lieu de
centimes (`320 000` centimes = `3 200` DA), et l'apostrophe du titre échappée
en `&#39;` par `| escape`.

### 27.6 Contrôles, tous verts

| Contrôle | Résultat |
|---|---|
| `node tests/test-seo.mjs` | 25/25 |
| `node tests/test-section-video.mjs` | 9/9 |
| `valider_theme.py` | 53/53 conformes · 27 JSON valides |
| `valider_shopify.py` | 122 clés utilisées / 122 présentes · **0 anomalie** |
| `verifier_import_shopify.py` | ✓ prêt à être téléversé |
| `verifier_arabe.py` · `verifier_rtl.py` | 0 problème · 82/0 |
| `verifier_mobile.py` · `verifier_pages.py` | 729/0 · 246/0 |
| `audit_cta.py` | aucun lien mort |
| `verifier_theme_zip.py` | dossier et archive identiques (104 fichiers) |

L'aperçu n'a pas bougé d'un octet (comparé à l'archive, page par page) : cette
étape n'ajoute que des balises invisibles dans l'en-tête des pages, donc **aucun
contrôle visuel des étapes précédentes n'est invalidé**.

### 27.7 La preuve, en une page

`llufan/preuve-referencement.html` — ces balises ne se voient dans aucune page :
cette page les donne à voir. Le avant / après d'un lien partagé sur WhatsApp, la
fiche telle que Google l'affiche (fil d'Ariane, prix, disponibilité), le code
exact produit pour quatre cas (accueil, fiche produit en français, la même en
arabe, page d'information), et les trois silences volontaires.

Elle est construite par `python3 llufan/build_preuve_referencement.py`, qui
demande au **vrai moteur Liquid** ce que le thème écrit
(`node tests/rendre-seo.mjs`) et vérifie au passage que les 10 blocs JSON-LD
produits sont des JSON valides. Les valeurs affichées sortent du thème : rien
n'est dessiné à la main.

### 27.8 Ce qu'il reste à faire, et par qui

* **Dans l'éditeur du thème** : choisir une image dans le réglage « Image de
  partage » (1200 × 630). Sans elle, le partage retombe sur le logo — ce qui
  marche, mais un vrai visuel est plus vendeur. Cela relève du contenu : c'est
  donc à faire côté Shopify.
* **Côté boutique** : `robots.txt` et le plan du site sont fournis par Shopify,
  rien à écrire.
* **Vérification finale**, une fois la boutique en ligne : coller l'adresse d'une
  fiche produit dans le test de résultats enrichis de Google, et l'adresse du
  site dans le débogueur de partage de Facebook. Les deux doivent lire le titre,
  l'image et le prix sans erreur.

## 28. Le style vidéo, relevé sur la référence (2026-10-05)

La vidéo de la référence n'est pas un lecteur posé dans la page : c'est une
**bande**. Nous l'avons mesurée dans un navigateur, neuf largeurs de fenêtre,
des deux côtés, et nous avons appliqué le résultat au thème.

### 28.1 Ce qui a été mesuré sur la référence

| Ce qui est mesuré | Valeur relevée |
|---|---|
| Hauteur de la bande | `clamp(25rem, 100vw, 36rem)` — voir le tableau ci-dessous |
| Largeur | plein écran, bord à bord, **aucun espacement** avec les sections voisines |
| Arrondi | **0** (l'ancienne version arrondissait à 2,5rem) |
| Remplissage | la vidéo **remplit** le cadre (`object-fit: cover`, `min-width/min-height: 100%`) |
| Lecture | autoplay, **muette**, en boucle, **sans commandes** |
| Clics | le lecteur ne capte pas les clics (`pointer-events: none`) |
| Texte | posé **par-dessus**, centré, blanc, largeur maximale 48rem — vide aujourd'hui sur la référence |

Relevé des hauteurs, largeur par largeur (le même tableau que dans la page de
comparaison) :

| Fenêtre | Référence | LLUFAN |
|---|---|---|
| 1920 / 1440 / 1280 / 1024 / 820 / 600 px | 576 px | 576 px |
| 480 px | 480 px | 480 px |
| 390 / 320 px | 400 px | 400 px |

### 28.2 Un détail découvert en capturant la référence

Sa vidéo d'accueil est **verticale**. Le lecteur remplit bien la bande, mais
comme la vidéo est plus haute que large, YouTube la centre et laisse des bandes
noires de chaque côté. Chez nous, c'est le même mécanisme : la bande se remplit
toujours, et c'est la forme de la vidéo qui décide de ce qu'on voit. **Une
vidéo horizontale (16/9) remplit la bande bord à bord** — c'est désormais écrit
dans l'éditeur, sous le champ du lien, là où cela sert.

### 28.3 Ce qui a changé dans le thème

| Fichier | Ce qui change |
|---|---|
| `sections/video.liquid` | la section devient une **bande** (plein écran, hauteur mesurée, texte en recouvrement) ; l'ancienne pastille de marque est retirée — elle n'existe pas sur la référence d'aujourd'hui |
| `assets/theme.css` | les règles de la bande ; la vidéo est recadrée (fichier Shopify) ou agrandie et recentrée (lecteur YouTube, qui n'applique pas `object-fit`) |
| `sections/main-product.liquid` | une vidéo hébergée affiche son image d'aperçu, un **bouton de lecture rond et blanc** (4rem, comme la référence) et ne se charge **qu'au moment où on la regarde** (`preload: none`) |
| `assets/theme.js` | le bouton lance la vidéo et s'efface ; il revient dès qu'elle est en pause |
| `locales/fr.default.json` · `ar.json` | `products.product.play_video` — « Lire la vidéo » / « تشغيل الفيديو » |

**Ajout de notre part, assumé** : la case « Bande vidéo » décochée donne un
lecteur 16/9 classique, avec commandes et son — pour une vidéo que l'on regarde
vraiment. La référence n'a pas ce mode ; une boutique peut en avoir besoin.

### 28.4 Une erreur sérieuse, attrapée par nos propres contrôles

En retirant la ligne `[dir="rtl"] .video-section__brand { … }`, j'ai supprimé
**l'accolade de fermeture de tout un groupe de sélecteurs arabes** : cette ligne
était la dernière d'un groupe de onze qui portait la déclaration
`{ letter-spacing: 0; text-transform: none; }`. Résultat : sur les fiches
produit, l'arabe reprenait un interlettrage négatif (`-0.3px`) — l'écriture liée
se détache, ce que la référence et nous-mêmes évitons.

C'est `verifier_arabe.py` qui l'a vu : **33 problèmes** du jour au lendemain
(zéro la veille). Réparé, puis **un garde-fou ajouté** : `valider_theme.py`
compte désormais les accolades de chaque feuille de style (`theme.css` : 786
ouvrantes, 786 fermantes). Ce genre de panne ne fait aucune erreur visible — le
navigateur ignore silencieusement les règles qui suivent.

Au passage, ce contrôle a révélé une **requête média jamais refermée** en fin de
`theme.css` (présente avant cette étape ; sans effet sur l'affichage, un
navigateur la referme tout seul). Elle est refermée, la feuille est propre.

### 28.5 Contrôles, tous verts

| Contrôle | Résultat |
|---|---|
| `node tests/test-section-video.mjs` | **20/20** (comportement + style mesuré) |
| `valider_theme.py` | 53/53 · accolades équilibrées · 27 JSON valides |
| `verifier_arabe.py` · `verifier_rtl.py` | **0** · ✓ |
| `verifier_mobile.py` · `verifier_pages.py` | ✓ · aucun problème |
| `node tests/test-seo.mjs` | 25/25 (rien n'a bougé de ce côté) |
| Mesures de la bande | **9 largeurs sur 9 identiques** à la référence, vidéo recadrée partout, aucun débordement |

### 28.6 La page de comparaison

`llufan/comparaison-video-reference.html` — les deux bandes côte à côte, à
1440 px et 390 px, avec le tableau des hauteurs et le texte de recouvrement.
Elle est construite par `python3 llufan/build_comparaison_video.py`, qui rend
notre section avec le **vrai moteur Liquid** (`node tests/rendre-video.mjs`),
ouvre la référence dans un navigateur, mesure les deux et capture les deux.
La vidéo d'essai (Big Buck Bunny, Blender, CC-BY) ne sert qu'à la mesure :
**aucune vidéo n'est livrée avec le thème**.

## 29. Le défilement des produits sur téléphone (2026-10-05)

Demande : « dans la version smartphone je voudrais que le scroll des produits
passe en horizontal comme dans doomoo.com ». Relevé d'abord, appliqué ensuite.

### 29.1 Ce que fait la référence, mesuré à 390 px

| Endroit | Comportement relevé |
|---|---|
| Carrousel de l'accueil (« Nos Coussins de maternité ») | défile horizontalement : cartes **`min(300px, 65 %)`** (227 px mesurés), écart **20 px** |
| Fiche produit (« VOUS AIMEREZ AUSSI ») | **le même** défilement, mêmes valeurs |
| Barre de défilement | masquée (`scrollbar-width: none`) |
| Accroche | **`none`** — défilement **libre** (vérifié : `scrollLeft` reste à 137 quand on le place à 137) |
| Marge de défilement | 20 px (`scroll-padding-inline-start`) |
| Flèches | **masquées** en téléphone (boutons mesurés **0×0** sous 700 px, 44×44 au bureau) |
| Page de collection | **ne défile pas** : c'est une grille de **2 colonnes** (180 px, écart 10 px) |
| Diaporama de l'accueil | ses flèches, elles, **restent** visibles (40×40) |

Distinction retenue, donc : **les rangées de produits défilent, la page de
collection reste une grille** — et les flèches restent pour le diaporama.

### 29.2 Ce qui a été appliqué

| Fichier | Ce qui change |
|---|---|
| `assets/theme.css` | le carrousel prend les valeurs mesurées (`min(300px, 65%)`, écart 20 px, accroche `none`, marge 20 px) ; nouvelle variante `product-list--carousel-tel` qui ne s'active que **sous 1000 px** — au-dessus, ces rangées restent une grille, le bureau ne change pas |
| `assets/theme.css` | les flèches du carrousel produit sont masquées sous 700 px (on balaye au doigt) |
| `assets/theme.css` | la règle de gouttière mobile (§25, étape 26) **ne s'applique plus aux rangées qui défilent** : elle écrasait l'écart de 20 px mesuré |
| `sections/related-products.liquid` | « Produits associés » défile sur téléphone |
| `sections/recently-viewed.liquid` | « Consultés récemment » défile sur téléphone |
| `build_preview.py` | l'aperçu reflète le thème (produits associés) |

L'accueil défilait déjà (`product-list--carousel`) : il est simplement aligné sur
les bonnes valeurs.

### 29.3 Un défaut réel, trouvé en vérifiant — et il était là avant

En mesurant la rangée de produits associés, **les deux premières cartes
mesuraient 0 px de large** : invisibles, avec la deuxième carte d'une rangée
affichée *par-dessus* la première. Cause : la règle de base `.product-list`
impose `grid-template-columns: repeat(2, minmax(0, 1fr))`, et l'ancien
carrousel **ne l'annulait pas**. Comme la rangée ne comptait rien dans cette
trame de deux colonnes, les items placés au-delà voyaient leur `min-width: auto`
se calculer à zéro. Les cartes n'étaient visibles qu'en se superposant.

Ce défaut **existait avant cette étape** (il venait avec la section, à l'étape
13) et ne se voyait pas au bureau par coïncidence. Correction : les deux
carrousels déclarent `grid-template-columns: none`. **Deux garde-fous** dans le
test, pour que ce piège ne revienne pas.

### 29.4 Le résultat, mesuré dans l'aperçu (390 px)

| Page | Cartes | Largeur | Visibles | Écart | Défilable | Page |
|---|---|---|---|---|---|---|
| Accueil (sélection) | 5 | 234 px | **5/5** | 20 px | 1 250 px | aucun débordement |
| Fiche produit (associés) | 4 | 234 px | **4/4** | 20 px | 996 px | aucun débordement |
| Collection | 5 | 174 px (2 colonnes) | 5/5 | 12 px | *ne défile pas* | aucun débordement |

Le rapport 234/360 px laisse voir **une carte entière et le début de la
suivante** : c'est exactement ce que fait la référence, et c'est ce qui invite à
balayer.

### 29.5 Contrôles, tous verts

| Contrôle | Résultat |
|---|---|
| `node tests/test-defilement-produits.mjs` | **17/17** (nouveau) |
| `node tests/test-section-video.mjs` · `test-seo.mjs` | 20/20 · 25/25 |
| `valider_theme.py` | 53/53 · accolades équilibrées · 27 JSON valides |
| `verifier_mobile.py` · `verifier_pages.py` | ✓ · aucun problème |
| `verifier_arabe.py` · `verifier_rtl.py` | 0 · ✓ |
| `audit_cta.py` · `verifier_import_shopify.py` | 0 destination morte · ✓ prêt à téléverser |

À vérifier une dernière fois **sur un vrai téléphone** après la mise en ligne :
le balayage au doigt (le banc d'essai simule le tactile, il ne le remplace pas).

---

## 30. Conformité Shopify et vitesse de chargement (2026-10-05)

Deux questions auxquelles il fallait répondre par une mesure, pas par une
impression : **le thème s'importe-t-il dans Shopify sans incompatibilité ?** et
**la boutique s'affiche-t-elle assez vite pour ne pas perdre des commandes ?**

La réponse complète est dans
`llufan/LLUFAN-conformite-et-vitesse.html` — un rapport d'une page, à ouvrir
d'un double-clic. Ce qui suit est la méthode et le raisonnement.

### 30.1 Conformité : 19 points vérifiés, aucun avertissement

Le contrôle automatique (`audit_conformite_shopify.py`) vérifie ce qui fait
échouer un import ou dégrader la boutique **après** l'import :

| Ce qui est vérifié | Constat |
|---|---|
| Fichiers obligatoires | 22 présents (modèles, langues, compte, caisse-cadeau) |
| Fichiers obsolètes ou parasites | aucun (ni `checkout.liquid`, ni `.DS_Store`, ni archive) |
| Balises du gabarit principal | `content_for_header`, `content_for_layout`, `sections` — les trois |
| Modèles de page | 20 modèles, 41 sections posées, aucune section inconnue |
| Schémas de section | 29 lisibles, identifiants uniques |
| Réglages globaux | 11 groupes, 54 réglages, 53 valeurs — toutes déclarées |
| Liquid obsolète | aucun filtre ni balise déprécié dans les 53 fichiers |
| Images du CDN | 22 appels, tous avec une largeur demandée |
| Sélection dans l'éditeur | 10 sections à blocs portent `shopify_attributes` |
| Langue et traductions | `fr.default.json` présent ; 136 clés dans les deux langues ; 123 clés utilisées, toutes définies |
| Poids | archive 2 Mo (limite 50 Mo), plus gros fichier 323 Ko (limite 20 Mo) |

Sortie de la commande : **19 ✓ · 0 avertissement · 0 bloquant.**

### 30.2 Vitesse : la mesure et son banc d'essai

Le point sensible est le **LCP** : l'instant où le plus grand élément visible
s'affiche enfin. Au-delà de 2,5 s, une partie des visiteuses est déjà partie.

Mesurer l'aperçu depuis son propre disque ne veut rien dire (tout est local et
instantané). `build_rapport_vitesse.py` monte donc un **banc d'essai** : un
serveur local qui imite le comportement de Shopify — feuille de style servie à
part et compressée, polices et images en fichiers séparés, en-têtes de cache.
Les pages y sont chargées dans un vrai navigateur, sur un profil réseau
« mobile » (1,6 Mb/s, 150 ms d'aller-retour, processeur ralenti 4 fois), **cache
désactivé** — sans quoi les rechargements renvoyaient « 304 sans télécharger »
et la mesure devenait absurde.

| Page | Affichage (LCP) | Élément qui décide | Stabilité | Poids | Requêtes |
|---|---|---|---|---|---|
| Accueil | ≈ 1,3 s | l'image de la 1re diapositive | 0,008 | 584 Ko | 18 |
| Fiche produit | ≈ 2,0 s | l'image principale | 0,008 | 417 Ko | 13 |

Le CLS de 0,008 (limite recommandée : 0,1) confirme que la page ne bouge pas :
la place des images est réservée avant leur arrivée.

Répartition du poids de l'accueil : **images 407 Ko (70 %)**, polices 154 Ko
(26 %), style 23 Ko (4 %) — et **zéro script externe**. Les visuels de
démonstration pèsent l'essentiel : sur la vraie boutique ce sont les photos
LLUFAN, et le CDN Shopify les redimensionne (le thème demande toujours une
largeur précise).

### 30.3 Le correctif du 5 octobre : ce qu'il change vraiment

Les deux diapositives du diaporama d'accueil étaient **toutes** chargées en
priorité haute. Seule la première décide de l'affichage : les suivantes
attendent maintenant leur tour (`loading="lazy"`).

Mesuré sur l'accueil actuel (deux diapositives) : l'écart avant/après reste
**dans le bruit de mesure**. Il serait malhonnête de l'annoncer comme un gain.
Le mécanisme, lui, se vérifie sur une maquette contrôlée — quatre grandes images
superposées, en liaison lente :

| Maquette | Affichage | Écart |
|---|---|---|
| 4 grandes images, une seule prioritaire | ≈ 6,8 s | référence |
| 4 grandes images, toutes prioritaires | ≈ 7,6 s | **+0,85 s** |

Conclusion, dite sans arrondir : **le correctif n'apporte presque rien
aujourd'hui, et évite une lenteur qui apparaîtrait dès que le diaporama aura
trois ou quatre visuels** — ce qui est l'usage courant d'une boutique. Le gain
à venir est là, pas dans la mesure du jour.

### 30.4 Ce qui reste, et qui le fait

- **Remplacer les visuels de démonstration** par les photos LLUFAN, allégées
  avant l'envoi (1600 px de large suffisent). C'est du contenu : cela se fait
  dans Shopify.
- **Rester sobre en applications** : chacune ajoute ses scripts. Sous une
  dizaine d'applications, la boutique garde sa vitesse.
- **Vérifier en ligne** avec PageSpeed Insights, sur un vrai téléphone en 4G.
  Les chiffres ci-dessus sont une mesure de **laboratoire** : ils décrivent le
  comportement du thème dans des conditions comparables d'une mesure à l'autre,
  pas la vitesse finale (le CDN de Shopify accélère, la distance au serveur et
  le forfait de la visiteuse ralentissent).

### 30.5 Refaire la mesure

```bash
bash llufan/preparer_controles.sh          # une fois : les bibliothèques du navigateur
python3 llufan/build_rapport_vitesse.py    # conformité + vitesse → le rapport HTML
python3 llufan/audit_conformite_shopify.py # la conformité seule
python3 llufan/audit_conformite_shopify.py --json   # la même, lisible par un programme
```

Le rapport est **régénéré** à chaque exécution : il porte la date et les valeurs
du jour. S'il est relu plus tard, les valeurs auront bougé de quelques dizaines
de millisecondes — c'est la dispersion normale d'une mesure réseau ; les
conclusions, elles, ne bougent pas.

---

## 31. Le paquet `llufan.com` — la boutique en un seul dossier (2026-10-05)

Tout le travail se trouvait jusqu'ici dans un espace de travail : pratique pour
construire, peu pratique pour **transmettre**. D'où `llufan.com.zip`, à la
racine : un dossier, quatre sacs, une notice.

```
llufan.com/
  LIRE-MOI.txt    ouvrir, importer dans Shopify, mettre sur GitHub (5 étapes)
  docs/           les 82 pages hors ligne — index.html = l'accueil
  theme/          le thème à importer dans Shopify
  contenus/       les CSV, le journal, les traductions arabes
  documents/      liste de contrôle, pas à pas, méthode, conformité + vitesse
```

**Pourquoi `docs/` et pas autre chose.** GitHub Pages ne publie que la racine
d'un dépôt ou un dossier nommé `docs`. En plaçant le site là, l'archive se
dépose telle quelle dans un dépôt et se publie sans rien réorganiser : c'est
un choix technique, pas esthétique.

**Ce que le paquet n'est pas.** Ce n'est pas la boutique en ligne, et ce n'est
pas un remplacement de la sauvegarde : c'est une copie autonome pour regarder,
transmettre ou héberger une **démonstration**. Les contenus (photos, prix,
textes) restent les contenus de démonstration, à remplacer ; la boutique réelle
vit dans Shopify, avec le thème de `theme/`.

**Il se refait en une commande**, après n'importe quelle modification :

```bash
python3 llufan/build_paquet_llufan_com.py
```

Le script reconstruit l'aperçu s'il n'est pas là, assemble le dossier, vérifie
que les 81 pages sont présentes et que la page arabe existe, puis écrit
l'archive. Il pèse 41 Mo — c'est le plus gros fichier entièrement régénérable
de l'espace de travail : s'il faut de la place, il peut être retiré sans perte.

**Sur GitHub.** Le dépôt ne se crée pas d'ici : publier suppose un compte et
une autorisation d'écriture, que cet espace de travail n'a pas — et la consigne
était de ne rien publier. La notice du paquet donne les cinq étapes (créer le
dépôt, déposer le contenu, activer Pages sur `/docs`, brancher le domaine), à
faire avec votre compte, en cinq minutes.
