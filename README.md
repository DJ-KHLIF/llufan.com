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
| `build_preview.py`, `generer_demo.py`, `generer_csv_demo.py`, `patch_demo.py` | Générateurs (aperçu, modèles du thème, CSV, branchements du mode démonstration) |

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
| `patch_demo.py` | passe unique : réglage `mode_demo` + résolution des adresses dans 11 sections |
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
Captures : `ref/shots/DEMO_*.png`.

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
