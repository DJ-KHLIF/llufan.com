# LLUFAN — boutique de démonstration

**Ce que c'est.** Une version de la boutique LLUFAN remplie de contenus et de produits **fictifs**, pour tester réellement le parcours complet (accueil → collection → fiche produit → commande en paiement à la livraison → pages d'information) avant de saisir les contenus définitifs.

**Rien n'est figé dans le code.** Tous les textes, produits, prix, images de démonstration se modifient depuis l'interface Shopify (éditeur de thème, produits, collections, pages). Ce document indique où se trouve chaque chose.

**Durée de mise en route :** environ 15 minutes.

---

## 1. Les fichiers livrés

| Fichier | À quoi ça sert | Où ça se passe dans Shopify |
|---|---|---|
| `LLUFAN-theme-Shopify.zip` | Le thème complet, avec les contenus de démonstration déjà en place | Boutique en ligne → Thèmes → Ajouter un thème → Importer un fichier ZIP |
| `LLUFAN-DEMO-produits.csv` | 10 produits fictifs, 28 variantes, prix en DZD | Produits → Importer |
| `LLUFAN-DEMO-collections.csv` | 5 collections (Maternité, Allaitement, Bébé, Nouveautés, Accessoires) | Produits → Collections → Importer |
| `demo/produits/*.jpg` | 10 visuels produits (nom de fichier = handle du produit) | à glisser sur chaque fiche produit après l'import |
| `preview/*.html` | L'aperçu hors boutique : **38 pages** cliquables (dont journal, articles, liste des collections, compte client, page introuvable), sans installation | à ouvrir dans un navigateur |
| `LLUFAN-DEMO-journal-a-publier.md` | 3 articles de blog de démonstration, prêts à coller | Boutique en ligne → Blog → Ajouter un article |

---

## 2. Mise en route, dans l'ordre

**Étape 1 — Importer le thème.** Boutique en ligne → Thèmes → Ajouter un thème → Importer un fichier ZIP → `LLUFAN-theme-Shopify.zip` → **Publier** (ou Prévisualiser).

**Étape 2 — Importer les produits.** Produits → Importer → `LLUFAN-DEMO-produits.csv` → Importer. Les 10 produits arrivent avec leurs variantes, leurs prix et leurs descriptions.

**Étape 3 — Importer les collections.** Produits → Collections → Importer → `LLUFAN-DEMO-collections.csv`. Ensuite, pour chacune des 5 collections, ajouter les produits :
- **Le plus rapide :** ouvrir la collection → bouton *Produits* → filtrer par étiquette (`allaitement`, `maternite`, `bebe`, `nouveautes`, `accessoires`) → tout sélectionner → *Ajouter*.
- Ou : convertir la collection en **collection automatique** avec la règle « Étiquette de produit est égale à `allaitement` » (etc.).

**Étape 4 — Ajouter les visuels produits.** Pour chaque produit, glisser le fichier du même nom depuis `demo/produits/` sur la fiche produit (Produits → *nom du produit* → zone Image). Les noms correspondent exactement aux handles :

| Fichier | Produit |
|---|---|
| `coussin-allaitement-nomad.jpg` | Coussin d'allaitement Nomad |
| `coussin-grossesse-luna.jpg` | Coussin de grossesse Luna |
| `poncho-allaitement-amira.jpg` | Poncho d'allaitement Amira |
| `housse-coussin-nomad.jpg` | Housse de rechange pour coussin Nomad |
| `gigoteuse-cocon.jpg` | Gigoteuse Cocon |
| `couverture-nid.jpg` | Couverture nid |
| `bavoirs-bandana-lot-2.jpg` | Bavoirs bandana (lot de 2) |
| `coussinets-allaitement-lavables.jpg` | Coussinets d'allaitement lavables |
| `robe-allaitement-nour.jpg` | Robe d'allaitement Nour |
| `sac-a-langer-sahara.jpg` | Sac à langer Sahara |

**Étape 5 — Créer les 10 pages.** Boutique en ligne → Pages → Ajouter une page. Pour chaque ligne : saisir le **titre**, cliquer sur *Modifier les paramètres de la page internet* (ou « Modèle de thème ») et choisir le modèle indiqué. **Le handle doit être exactement celui de la colonne 3**, car c'est lui que les liens du thème utilisent.

| Titre de la page | Handle à saisir | Modèle de thème |
|---|---|---|
| La marque | `la-marque` | `page.la-marque` |
| Livraison | `livraison` | `page.livraison` |
| Paiement | `paiement` | `page.paiement` |
| Échanges et retours | `politique-de-retour` | `page.politique-de-retour` |
| Mentions légales | `mentions-legales` | `page.mentions-legales` |
| Conditions générales de vente | `cgv` | `page.cgv` |
| Politique de confidentialité | `confidentialite` | `page.confidentialite` |
| Questions fréquentes | `faq` | `page.faq` |
| Contact | `contact` | `page.contact` |
| Club Maman | `club-maman` | `page.club-maman` |

Tant qu'une page n'existe pas, le lien correspondant **n'apparaît pas** (menu, pied de page, boutons) : aucun lien ne mène à une page vide.

**Étape 6 — Créer le menu principal.** Navigation → *Main menu* → ajouter : Maternité → *Collections / Maternité*, Bébé → *Collections / Bébé*, Nouveautés → *Collections / Nouveautés*, Allaitement → *Collections / Allaitement*, Accessoires et pièces détachées → *Collections / Accessoires*. C'est ce menu qu'affiche l'en-tête (ligne sous le logo) et le menu mobile.

**Étape 7 — Le journal (facultatif).** Boutique en ligne → Blog → Ajouter un article : créer les 3 articles du fichier `LLUFAN-DEMO-journal-a-publier.md` (titre, adresse et texte à coller), puis ajouter l'illustration. Le thème affiche la liste des articles et la page de chaque article.

**Étape 8 — Le compte client (facultatif).** Paramètres → Comptes clients → activer. Sans cela, décocher « Afficher le lien Compte » dans l'en-tête (Éditeur → En-tête → section *En-tête*).

---

## 3. Où modifier quoi dans Shopify

| Ce que vous voulez changer | Où |
|---|---|
| Bandeau d'annonces, pré-bandeau, logo, logo (mobile), pastille CLUB MAMAN, lien Compte | Éditeur → **En-tête** (et ses sections Bandeau / Pré-bandeau / En-tête) |
| Diaporama d'accueil (texte, bouton, visuel) | Éditeur → **Accueil** → section *Héros (diaporama)* |
| Bandeau de réassurance (3 engagements) | Éditeur → **Accueil** → section *Icônes + texte* |
| Les 4 cartes d'univers | Éditeur → **Accueil** → *Cartes de collection* (choisir une collection = le visuel et le lien suivent) |
| La sélection « Nos coups de cœur » | Éditeur → **Accueil** → *Produits d'une collection* |
| Les avis (fictifs) | Éditeur → **Accueil** → *Avis clients* → remplacer par de vrais avis, ou vider les blocs |
| Le bloc éditorial (« Chaque détail compte ») | Éditeur → **Accueil** → *Médias et texte* |
| FAQ (accueil, collection, fiche produit, page FAQ) | Éditeur → la section *Questions fréquentes* de chaque modèle |
| Fiche produit : badges, sous-titre, accordéons, réassurance, éditorial, questions | Éditeur → Produits → ouvrir un produit → *Modèle de thème* → sections et blocs |
| Formulaire de commande (titre, bouton, barre mobile) | Éditeur → modèle produit / panier → bloc ou section *Commander* |
| Titre « Description » de la fiche produit (masquable) | Éditeur → Produits → ouvrir un produit → bloc *Description* |
| Club Maman (texte d'accueil, espaces, discussions, ressources, inscription) | Éditeur → Pages → *Club Maman* → section *Club Maman* |
| Pages d'information (La marque, Livraison, Paiement, Échanges et retours, Mentions légales, CGV, Confidentialité) | Éditeur → Pages → la page → section *Page d'information* (sur-titre, titre, intro, blocs, note) + onglet **Contenu** de la page pour le texte libre |
| Pied de page : colonnes, liens, contact, mentions, copyright | Éditeur → **Pied de page** (chaque colonne et chaque adresse se règlent dans la section *Pied de page*) |
| Numéro WhatsApp et e-mail (repris partout : pied de page, contact, Club, boutons) | Réglages du thème → *Contact et identité LLUFAN* |
| Couleurs, polices, largeur, gouttières, coins | Réglages du thème (rubriques *Couleurs*, *Typographie*, *Mise en page*) |
| Visuels de démonstration | Réglages du thème → *Identité* → **Mode démonstration** (voir §5) |
| Articles du journal | Boutique en ligne → Blog |
| Produits, prix, variantes, stocks, descriptions | Produits |
| Collections et leurs produits | Produits → Collections |
| Livraison : 69 wilayas, communes, tarifs domicile / stop-desk | **fichier du thème** `assets/llufan-livraison-dz.json` (un tarif par wilaya) |

---

## 4. Ce qui est fictif (à remplacer avant la mise en ligne)

- **Les 9 produits ajoutés** (Luna, Amira, Cocon, Nid, Bavoirs, Coussinets, Nour, Sahara, Housse) : noms, prix, descriptions, compositions. Le **coussin Nomad** conserve, quant à lui, la fiche fournie par LLUFAN (seule la mention « composition à confirmer » reste à valider).
- **Les prix** (900 à 5 500 DA) et **tous les visuels** : les 10 visuels produits **et** les 8 visuels d'ambiance du thème (`assets/demo-*.jpg` : diaporama, cartes d'univers, bandeau de collection, bloc éditorial) sont des images générées pour la démonstration. Ils sont remplaçables un par un dans l'éditeur, et le réglage *Mode démonstration* les coupe d'un coup.
- **Les 3 avis clients** de l'accueil : ils portent la mention « Avis de démonstration ».
- **Les 3 discussions du Club Maman** et leurs compteurs (réponses, j'aime) : fictifs.
- **Les textes des pages Aide et Informations** : La marque, Livraison, Paiement, Échanges et retours, Mentions légales, CGV, Politique de confidentialité. Chaque page affiche en haut le bandeau **« Contenu de démonstration — à remplacer avant la mise en ligne »** : il se vide dans le réglage *Bandeau d'avertissement* de la section.
- **Les délais « 2 à 5 jours ouvrés »** et **les tarifs de livraison** : provisoires, comme indiqué dans les textes.
- **La vidéo de l'accueil** : aucun visuel n'a été inventé. Tant qu'aucun lien n'est saisi, la section ne s'affiche
  pas dans la boutique (elle reste visible dans l'éditeur, avec un texte d'attente). Elle réapparaîtra dès que
  vous collerez un lien YouTube / Vimeo ou déposerez un fichier : Éditeur → Accueil → *Vidéo*.
- **Le bandeau d'annonces**, le pré-bandeau et la pastille : contenus LLUFAN, mais à valider (les liens pointent vers les pages et collections, pas vers des adresses inventées).

---

## 5. Mode démonstration (visuels)

Réglages du thème → *Identité* → **Mode démonstration (visuels fictifs)** :

- **activé** (par défaut dans cette livraison) : partout où aucun visuel n'a été choisi, le thème affiche un visuel de démonstration fourni avec le thème (diaporama, cartes d'univers, bandeau de collection, bloc éditorial, liste des collections). Ces visuels sont reconnaissables : leurs fichiers s'appellent `demo-*.jpg` dans `assets/`.
- **désactivé** : dès qu'une image est choisie dans une section, elle prend la main ; les emplacements restés vides affichent le cadre neutre « visuel à fournir ». À décocher avant la mise en ligne.

Aucun réglage de texte ne dépend de ce mode : les textes de démonstration sont **dans les champs de l'éditeur**, donc modifiables directement, sans code.

---

## 6. Après la démonstration : passer en réel

1. Remplacer les textes de chaque section (ils sont tous dans l'éditeur, aux emplacements listés au §3) et vider les bandeaux « Contenu de démonstration ».
2. Remplacer les 9 produits fictifs (supprimer ou réécrire) et les prix ; conserver le coussin Nomad.
3. Supprimer les avis et les discussions fictifs, ou les remplacer par de vrais contenus.
4. Faire rédiger/valider Mentions légales, CGV, politique de confidentialité et politique de retour.
5. Confirmer les tarifs et délais de livraison dans `assets/llufan-livraison-dz.json` (tarifs) et dans les textes (délais).
6. Décocher **Mode démonstration** et supprimer les fichiers `assets/demo-*.jpg` depuis l'éditeur de code du thème, si vous voulez alléger le thème.
7. Renseigner les réseaux sociaux (Réglages du thème → *Réseaux sociaux*) : les emplacements du pied de page n'apparaissent que si un lien est saisi.

---

## 7. Ce que la démonstration ne peut pas faire

- **Passer une vraie commande depuis l'aperçu HTML** : l'aperçu est statique (le formulaire de commande y est montré à titre de vérification). Dans la boutique Shopify, ce même formulaire envoie réellement la commande (message de contact Shopify + récapitulatif WhatsApp).
- **Créer un compte client depuis l'aperçu** : le lien « Compte » dépend des comptes clients activés dans Shopify.
- **Ajouter des images aux produits par CSV** : Shopify n'accepte dans un CSV que des adresses d'images accessibles en ligne ; les visuels sont donc à glisser à la main (étape 4).
- **Importer les articles du journal par CSV** : Shopify n'importe pas les articles de blog par fichier. Les 3 articles de démonstration sont livrés prêts à coller dans `LLUFAN-DEMO-journal-a-publier.md` (Boutique en ligne → Blog → Ajouter un article). Le thème contient les modèles de liste et d'article.
