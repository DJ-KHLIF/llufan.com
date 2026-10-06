# LLUFAN — inventaire de la boutique

**Ce qui a été créé, et ce que la boutique sait faire.**
Mis à jour le 5 octobre 2026 · détail complet de chaque étape : `README.md` (§1 à §30)

---

## 1. En un coup d'œil

| | |
|---|---|
| Fichiers du thème | **104** (29 sections, 15 fragments, 26 ressources, 22 modèles de page, 7 modèles de compte, 2 langues) |
| Pages de l'aperçu local | **82** (41 en français, 40 en arabe, + la page d'index à ouvrir) |
| Langues | **français et arabe**, deux versions complètes du site, sens droite → gauche |
| Wilayas livrables | **69**, avec **1 541 communes** (1 534 avec leur nom arabe) |
| Produits de démonstration | **10** produits (28 lignes de variantes), **5** collections, **3** articles |
| Visuels | **81** vignettes + **10** visuels produit (démonstration, à remplacer) |
| Lignes de traduction arabe | **255** |
| Conformité Shopify | **19 points vérifiés · 0 avertissement · 0 bloquant** (prêt à importer) |
| Vitesse mesurée | accueil **≈ 1,3 s**, fiche produit **≈ 2,0 s**, rien ne saute (0,008) |
| Contrôles automatiques | **14** contrôles + **5** tests, tous verts |

**Rien n'a été inventé** : ni prix, ni avis, ni promesse de livraison, ni politique.
Ce qui manquait est signalé, vide, ou identifié « démonstration ».

---

## 2. Les livrables — ce que vous téléversez ou ouvrez

### Pour construire la boutique dans Shopify

| Fichier | Ce que c'est | Où il va |
|---|---|---|
| `LLUFAN-theme-Shopify.zip` | **Le thème complet** (104 fichiers), prêt à importer | Boutique en ligne → Thèmes → Ajouter un thème |
| `LLUFAN-DEMO-produits.csv` | Les **10 produits** de démonstration, avec leurs 28 variantes | Produits → Importer |
| `LLUFAN-DEMO-collections.csv` | Les **5 collections** : Maternité, Allaitement, Bébé, Nouveautés, Accessoires | Produits → Collections |
| `LLUFAN-DEMO-journal-a-publier.md` | Les **3 articles** du journal, à coller (Shopify n'importe pas les articles par fichier) | Boutique en ligne → Articles |
| `LLUFAN-DEMO-traductions-ar.csv` | Les **133 lignes** de traduction arabe, une par champ Shopify (les corps de page sont assemblés en HTML) | Paramètres → Langues → Importer |
| `LLUFAN-DEMO-contenus-a-coller.md` | Les **10 pages, 5 collections et 3 articles** en français **et** en arabe, prêts à coller (titre + corps) | Boutique en ligne → Pages / Collections / Articles |
| `LLUFAN-produit-Nomad-a-importer.csv` | Le **produit phare** seul, si vous voulez commencer par un | Produits → Importer |
| `demo/produits/*.jpg` | Les **10 visuels produit** | À glisser sur les fiches |

Le pas à pas est dans `LLUFAN-DEMO-mode-emploi.md`, la liste de contrôle avant
publication dans `LLUFAN-checklist-mise-en-ligne.md`.

### Pour regarder la boutique sans Shopify

| Fichier | Ce que c'est |
|---|---|
| `llufan.com.zip` | **Le paquet à partager** (41 Mo) : la boutique hors ligne (`docs/index.html`), le thème, les contenus et les documents, dans un seul dossier — avec la notice qui explique comment le mettre sur GitHub (README §31) |
| `LLUFAN-apercu-local.zip` | **Toute la boutique hors ligne** : double-clic sur `apercu.html`, 82 pages, aucune connexion requise |
| `formulaire-commande-fr-ar.png` | Le formulaire de commande rempli, français et arabe côte à côte |
| `preuve-referencement.html` | Ce que voient WhatsApp et Google quand on partage un lien LLUFAN |
| `comparaison-video-reference.html` | La bande vidéo mesurée contre la référence, à 1440 et 390 px |
| `comparaison-mobile.html` | La version téléphone, mesurée contre la référence |
| `LLUFAN-conformite-et-vitesse.html` | **La conformité Shopify et la vitesse mesurée**, en une page : 19 points, les temps d'affichage, le poids, ce qui reste à faire. À ouvrir d'un double-clic |
| `LLUFAN-REMARQUES-6-OCTOBRE.md` | **La bascule français / arabe et l'audit du 6 octobre**, confrontés à nos fichiers : ce qui vient de la boutique, ce qui vient de nous, et les corrections dans l'ordre | À lire avant de retoucher la boutique |
| `LLUFAN-reponse-audit-6-octobre.html` | **La réponse à l'audit en une page** : le tableau « ce qui vient du thème / ce qui vient de la boutique », les corrections et les sept gestes à faire | À montrer ou à transmettre |
| `visuel-produit-nomad-avant-apres.png` | Le visuel du produit réel, avant / après |

### Les documents qui expliquent tout

| Fichier | À quoi il sert |
|---|---|
| `LIRE-MOI.txt` | Le repère de départ : où sont les fichiers, comment tout relancer |
| `README.md` | Le journal de construction, étape par étape (28 chapitres) |
| `LLUFAN-DEMO-mode-emploi.md` | Construire la boutique, du premier import à la publication |
| `LLUFAN-checklist-mise-en-ligne.md` | La liste de contrôle avant d'ouvrir au public |
| `SAUVEGARDE.txt` · `LLUFAN-sauvegarde-2026-10-04.zip` | La sauvegarde de tout l'espace de travail (54 Mo) |

---

## 3. Les fonctionnalités, page par page

### 3.1 Les bandeaux et l'en-tête (sur presque toutes les pages)

* **Pré-bandeau** — la fine bande du haut, défilable au doigt sur téléphone.
* **Bandeau d'annonce** — défilement automatique, centré, sans flèches, collé en haut.
* **En-tête** — logo centré au-dessus du menu (Maternité · Bébé · Nouveautés),
  pastille **MAMA'S CLUB** sur la même ligne (masquée sous 900 px), sans trait.
* **Bascule de langue** — affiche **une seule langue** : celle vers laquelle on bascule.
* **Icônes** — recherche, compte, panier (avec tiroir latéral).
* **Barre mobile collante** — le bouton d'achat reste sous le pouce sur téléphone.
* **Rangées de produits qui défilent au doigt, en téléphone** — la sélection de
  l'accueil, les produits associés d'une fiche et les produits consultés
  récemment : cartes de 234 px, écart 20 px, la carte suivante s'entame à droite
  (valeurs relevées sur la référence). La page de collection, elle, reste une
  grille de deux colonnes, comme la référence. Flèches masquées sur téléphone,
  conservées pour le diaporama d'accueil.
* L'en-tête s'efface **seulement** au moment d'aller payer, comme sur la référence.

### 3.2 L'accueil (7 sections, toutes réglables)

| Section | Ce qu'elle fait |
|---|---|
| **Héros (diaporama)** | Images, titre, bouton, défilement automatique (8 s), indications cliquables |
| **Icônes avec texte** | Trois arguments courts avec icônes |
| **Cartes de collection** | Les univers (Maternité, Bébé…) en cartes d'images |
| **Produits d'une collection** | Une sélection en carrousel, avec prix et badges |
| **Vidéo** | La **bande pleine largeur** au style de la référence (voir §4) |
| **Avis clients** | Défilement automatique, note en étoiles — **avis de démonstration** |
| **Médias et texte** | Bloc éditorial image + texte (présentation de marque) |

### 3.3 Les collections

Bandeau de collection, grille de produits, **filtres** et **tri** (le menu de tri
se place correctement en arabe), pagination, cartes produit avec badges de
nouveauté et pastilles de couleur. Une page « toutes les collections » existe aussi.

### 3.4 La fiche produit — le cœur de la conversion

* **Galerie** : vignettes sur côté, carrousel au doigt sur téléphone.
* **Vidéo produit** : image d'aperçu, **bouton de lecture rond et blanc**, chargement
  seulement quand on la regarde (`preload: none`).
* **Variantes** : pastilles de couleur, tailles, quantité, prix mis à jour.
* **Commande immédiate** : un **bouton « Commander maintenant » en tête de fiche**,
  qui ouvre le formulaire de commande sans passer par le panier.
* **Formulaire de commande complet** (voir §4.3) : nom, téléphone, wilaya, commune,
  type de livraison, sous-total / frais / **total**.
* **Produits associés** et **consultés récemment** en bas de fiche.
* Deux sections peuvent s'ajouter où vous voulez : **Produits associés** et
  **Consultés récemment** (le rappel des produits déjà vus).

### 3.5 Le panier et la commande

* **Tiroir panier** qui s'ouvre sans quitter la page, et **page panier** complète.
* Multi-articles, quantités, sous-total, suppression d'une ligne.
* **Paiement à la livraison (COD)** : aucun paiement en ligne, conforme au marché
  algérien — et aux décisions prises avec vous.
* Le formulaire de commande fonctionne **aussi bien sur la fiche produit que dans le panier**.

### 3.6 Le Club Maman

Page dédiée et section d'accueil : les **quatre espaces** (Projet Bébé ·
Grossesse · Accouchement · Post-Partum), cartes de discussion, **tableau**
(Sujet · Personnes · Réponses · Vues · Mis à jour), tri, **état vide**, bandeau de
ressources, bloc connexion / inscription. Contenu de démonstration.

### 3.7 Le journal et les articles

Blog (liste des articles) et page article, avec image, date, auteur, contenu
rédigé. Les 3 articles sont prêts à coller dans Shopify.

### 3.8 Les pages d'information (11 modèles)

La marque · Livraison · Paiement · Échanges et retours · CGV · Mentions légales ·
Politique de confidentialité · FAQ (accordéons) · Contact (formulaire + WhatsApp) ·
Club Maman · page générique. Chacune affiche, en démonstration, un bandeau
« contenu à remplacer » qui se vide d'un réglage.

### 3.9 Les pages techniques

Recherche (avec résultats et état vide), page 404, liste des collections,
**compte client** (connexion, inscription, mot de passe oublié, adresses, commandes),
carte-cadeau, et page de garde du magasin fermé.

### 3.10 Le pied de page

Contacts réels (WhatsApp **0772 415 120**, `contact@llufan.com`), emplacements de
réseaux sociaux sans lien fictif, moyens de paiement, sélecteur de langue,
mentions légales, « © 2026 LLUFAN. Tous droits réservés. · Algérie · llufan.com ».
Hauteur comprimée sans perte d'information.

---

## 4. Les fonctions qui traversent tout le site

### 4.1 Le français et l'arabe, entièrement

* **40 pages jumelles** en arabe, en plus des pages françaises.
* **Sens droite → gauche** complet : en-tête en miroir, menus, tableaux, flèches,
  animations directionnelles — et **interlettrage neutralisé** (en arabe, les
  lettres liées ne doivent pas être écartées).
* **Polices arabes embarquées** (Noto Naskh et IBM Plex Sans Arabic) : elles
  s'affichent même sans connexion.
* Traduits jusqu'au bout : wilayas, **communes**, libellés du formulaire,
  messages de confirmation, récapitulatif de commande.
* Les **valeurs envoyées à Shopify ne changent pas** avec la langue : seule
  l'écriture à l'écran change.

### 4.2 Le téléphone, de 320 à 480 px

Testé sur **9 largeurs**, page par page : aucun débordement, zones tactiles
d'au moins 44 px, textes lisibles. La mise en page suit les mesures relevées sur
la référence en version mobile.

### 4.3 La commande : wilaya → commune → tarif → total

* **69 wilayas**, **1 541 communes** (1 534 nommées en arabe).
* La commune se débloque après la wilaya, et son tarif est celui de sa wilaya.
* **2 modes de livraison** : à domicile et stop-desk, avec le bon tarif.
* Le **total se recalcule à chaque choix** (5 200 DA → 4 900 DA en stop-desk, par ex.).
* Les tarifs sont **dans un fichier de données** : modifiables sans toucher au thème.
* Paiement **à la livraison**, aucun paiement en ligne.

### 4.4 La vidéo (style de la référence)

Bande **pleine largeur**, hauteur `clamp(25rem, 100vw, 36rem)` — **relevée sur la
référence et identique aux 9 largeurs mesurées** —, vidéo **recadrée** qui
démarre seule, **muette**, en boucle, **sans commandes**, et qui ne capte pas les
clics. Le texte se pose par-dessus, centré, en blanc. Une variante « lecteur
16/9 classique avec commandes » existe pour les vidéos que l'on regarde vraiment.

### 4.5 Les animations

Relevées dans la référence (valeurs mesurées, pas imitées) : boutons 0,45 s,
cartes 0,2 s, tiroirs 0,3 s, menu 0,4 s, diaporama 0,8 s. Aucune animation qui
empêche d'acheter, et le mouvement est réduit si l'appareil le demande.

### 4.6 Le référencement (partage et Google)

* **Partage WhatsApp / Facebook** : titre, description, image (repli automatique
  sur l'image choisie dans l'éditeur, puis sur le logo) — le lien n'apparaît
  jamais nu.
* **Données structurées** : boutique et contact, site et recherche interne, fil
  d'Ariane, fiche produit avec **une offre par variante**, prix en nombre, devise
  DZD, disponibilité.
* **Trois silences volontaires** : pas de note d'avis (les avis sont fictifs), pas
  de garanties ni de délais (non arrêtés), pas de faux prix barré.
* Adresse canonique et liens entre langues, déjà en place.

### 4.7 Les garde-fous permanents

* **Aucun CTA sans destination réelle** : contrôle automatique, 0 lien mort.
* **Aucun contenu inventé** : ce qui n'était pas connu est vide et signalé.
* **Le thème et l'archive ne peuvent pas diverger** : un contrôle compare les 104
  fichiers, et dit de quel côté est le retard.
* **Le thème est prêt à importer** : structure, assets, JSON lus et vérifiés.

---

## 5. Ce qui se règle dans l'éditeur, sans écrire de code

**29 sections** disponibles dans « Ajouter une section », chacune avec ses réglages :

| Sections de page | Sections de contenu | Sections d'aide à la vente |
|---|---|---|
| En-tête · Pré-bandeau · Bandeau d'annonce · Pied de page · Bandeau de collection · Grille de collection · Fiche produit · Panier · Tiroir panier · Page · Article · Blog · Recherche · Contact · Page introuvable · Liste des collections | Héros (diaporama) · Icônes avec texte · Cartes de collection · Produits d'une collection · Médias et texte · Vidéo · Avis clients · Questions fréquentes · Club Maman · Page d'information | Commande (paiement à la livraison) · Produits associés · Consultés récemment |

**Réglages du thème** (globaux, une seule fois) : Identité · Couleurs (23) ·
Typographie (4) · Mise en page (4) · Cartes produit (4) · Panier (3) ·
Avis clients (3) · **Contact et identité LLUFAN (7)** · Réseaux sociaux (3) ·
Sélecteurs et mentions légales (5).

Tout le contenu de démonstration tient dans des **champs de l'éditeur** : rien
n'est caché dans le code. Un réglage **« Mode démonstration »** coupe d'un coup
les visuels et les textes de test.

---

## 6. Ce qui reste à faire, et par qui

**Par vous, dans Shopify** (c'est le contenu, pas la technique) :

1. **Les produits** : remplacer les 10 fiches de démonstration — titres, prix,
   descriptions, photos réelles. Pas de prix inventé de notre côté.
2. **Les textes des pages** : La marque, Livraison, Paiement, Échanges et retours,
   CGV, Mentions légales, Confidentialité, FAQ — la structure est prête, les
   phrases s'écrivent dans l'éditeur.
3. **Les avis clients** : à remplacer par de vrais avis, ou à retirer.
4. **La vidéo d'accueil** : coller un lien (une vidéo **horizontale 16/9** remplit
   la bande bord à bord) — aucune vidéo n'est livrée avec le thème.
5. **L'image de partage** (1200 × 630) : Éditeur → Logo et favicon.
6. **Les réseaux sociaux** : les liens, quand les comptes existeront.
7. **Le compte client** : à activer ou à masquer (un réglage).
8. **Les tarifs de livraison** : déjà dans un fichier de données — dites-nous si
   les montants changent.

**Côté nous, si vous le souhaitez** : le poids des pages (vitesse d'affichage sur
forfait mobile), une relecture arabe ligne à ligne, ou tout autre ajout.

---

## 7. Les outils de contrôle (et ce qu'ils garantissent)

| Commande | Ce qu'elle vérifie |
|---|---|
| `python3 verifier_import_shopify.py` | Le thème est-il **prêt à téléverser** ? (structure, assets cités, JSON, fichiers d'import) |
| `python3 valider_theme.py` | Balises Liquid (53/53), fragments appelés, réglages déclarés, JSON, langues, **accolades des feuilles de style** |
| `python3 valider_shopify.py` | Structure des modèles, **clés de traduction** (122 utilisées / 122 présentes) |
| `node tests/test-section-video.mjs` | Le **style vidéo** : 20 cas (liens, lecture, bande mesurée) |
| `node tests/test-seo.mjs` | Le **référencement** : 25 cas (partage, données structurées, prix, silences) |
| `node tests/test-defilement-produits.mjs` | Le **défilement des produits** : 17 cas (valeurs mesurées, trame de grille, flèches) |
| `python3 verifier_arabe.py` | Les **40 pages arabes** : polices, sens, interlettrage, formulaire de commande |
| `python3 verifier_rtl.py` | Le sens droite → gauche sur toutes les pages |
| `python3 verifier_mobile.py` | **9 largeurs de téléphone**, page par page : débordements, zones tactiles |
| `python3 verifier_pages.py` | Toutes les pages × 3 largeurs, dans un navigateur |
| `python3 audit_cta.py` | **Liens et formulaires** : aucune destination morte |
| `python3 verifier_theme_zip.py` | Le dossier du thème et l'archive `.zip` disent-ils la même chose ? |
| `python3 audit_espace.py` | Ce qui occupe la place, ce qui est doublon |
| `python3 audit_conformite_shopify.py` | Les **19 points** que Shopify exigera à l'import (fichiers obligatoires, modèles, schémas, réglages, Liquid obsolète, traductions, poids) |
| `python3 build_rapport_vitesse.py` | La conformité **et** la vitesse : rejoue les pages sur un réseau bridé, cache désactivé, et écrit le rapport d'une page |
| `bash llufan/refaire_apercu.sh` | Reconstruit l'aperçu local (82 pages) en une commande |
| `bash llufan/refaire_archives.sh` | Reconstruit le thème livrable + la sauvegarde complète |
| `bash llufan/refaire_archives.sh --apercu` | Ajoute la boutique à emporter (ZIP hors ligne) |
| `bash llufan/liberer_espace.sh --oui` | Rend la place de l'aperçu, une fois la sauvegarde refaite |

Ils ont attrapé, entre autres : une clé de traduction inventée, un prix divisé
par 100 avec des espaces (que Google refuse), une accolade manquante qui
détachait les lettres arabes, un contrôle d'import passé au vert sur une archive
périmée. Un contrôle qui ne trouve rien est aussi utile qu'un contrôle qui trouve.

---

## 8. Où sont les fichiers

```
/home/user
├── LIRE-MOI.txt                    le repère de départ
├── SAUVEGARDE.txt                  la règle de suppression
├── LLUFAN-sauvegarde-2026-10-04.zip   toute la sauvegarde (54 Mo)
├── uploads/                        vos fichiers d'origine (9)
└── llufan/
    ├── LLUFAN-theme-Shopify.zip    ★ le thème à importer
    ├── LLUFAN-DEMO-*.csv / *.md    ★ les fichiers d'import Shopify
    ├── demo/                       visuels de démonstration (81 + 10)
    ├── theme/                      le thème, fichier par fichier (104)
    ├── preview/                    l'aperçu local (reconstruit à la demande)
    ├── tests/                      les tests automatisés
    ├── README.md                   le journal de construction
    └── *.py · *.sh                 les scripts de contrôle et de reconstruction
```

---

## 9. Les étapes parcourues

1. **Examen de la référence** (doomoo.com) : structure, proportions, couleurs, parcours.
2. **Thème Shopify** réglable dans l'éditeur, cohérent sur ordinateur, tablette, téléphone.
3. **Animations** relevées et appliquées.
4. **Parcours d'achat raccourci** : commande immédiate, sans détour par le panier.
5. **Commande algérienne** : 69 wilayas, communes, tarifs, paiement à la livraison.
6. **Pied de page** et **CTA** : une destination réelle pour chacun.
7. **Club Maman**, **contenus et produits de démonstration**, **journal**.
8. **Vidéos**, **aperçu local hors ligne**, **guide visuel**.
9. **Deux langues** : français et arabe, avec **40 pages jumelles** et le RTL complet.
10. **Téléphone** : affichage correct de 320 à 480 px, aligné sur la référence mobile.
11. **Communes arabes** : 1 534 noms sur 1 541, plus aucun mélange à l'écran.
12. **Référencement** : partage sur les réseaux, données structurées, page de preuve (§27).
13. **Style vidéo** : la bande mesurée contre la référence, 9 largeurs sur 9 identiques (§28).
14. **Défilement des produits en téléphone** : relevé sur la référence, appliqué — et un défaut
    réel corrigé au passage (deux cartes invisibles dans les rangées) (§29).
15. **Conformité et vitesse** : 19 points d'import vérifiés, la boutique rejouée
    sur un réseau bridé (1,6 Mb/s) — 1,3 s pour l'accueil, 2,0 s pour une fiche produit ;
    le correctif des images prioritaires mesuré sur une maquette contrôlée (§30).

Le détail de chacune — ce qui a été mesuré, ce qui a échoué, ce qui a été
corrigé — est dans `README.md`.
