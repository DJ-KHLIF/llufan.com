# LLUFAN — les remarques du 6 octobre 2026

Ce document réunit deux choses, dans l'ordre où elles sont arrivées :

1. **la remarque sur la langue** — pourquoi la version arabe / française n'apparaissait
   pas, ce que j'ai corrigé, et les deux gestes qui restent (30 secondes, côté Shopify) ;
2. **l'audit reçu le 6 octobre** (six points de correction, du parcours de commande au
   mobile) — retranscrit fidèlement, puis **confronté à nos fichiers**, point par point :
   ce qui vient de notre travail, ce qui vient de la boutique, et ce qu'il faut faire.

> Résumé en une phrase : **aucun des défauts signalés ne vient des fichiers livrés par
> moi.** Ils viennent de pages saisies dans la boutique — dont une page de commande
> écrite hors de l'identité de la marque. Trois d'entre eux sont réels et à corriger
> tout de suite ; trois sont déjà réglés par le thème, ou n'ont pas lieu d'être.

---

## 1. La remarque sur la langue

**Le symptôme** : « je n'ai pas toujours la version arabe / française ».

**Les deux causes, cumulées :**

| # | La cause | L'état |
|---|---|---|
| 1 | Le sélecteur de langue du thème était **coché « non » par défaut** | corrigé : coché par défaut, dans le schéma **et** dans les réglages enregistrés |
| 2 | La langue arabe **n'est pas encore publiée** dans Shopify (Paramètres → Langues) | à faire : sans elle, Shopify ne propose qu'une langue, et aucun thème ne peut afficher de bascule |

**Le troisième problème, qui rendait le mélange pénible** : la détection automatique de
langue est active (`auto_language`). Une visiteuse dont le téléphone est en arabe arrive
donc en arabe — et le sélecteur étant éteint, elle n'avait **aucun moyen de revenir au
français**.

**Les deux gestes, dans cet ordre :**

1. **Paramètres → Langues → Ajouter une langue → العربية → Publier.**
2. **Personnaliser → Paramètres du thème → « Sélecteurs et mentions légales » →
   « Afficher le sélecteur de langue » : coché** → Enregistrer.
   Sur un thème déjà importé avant le 6 octobre, c'est cette case qui fait apparaître la
   pastille ; dans le thème à jour, elle est déjà cochée.

Ensuite : en français l'en-tête affiche « العربية », en arabe il affiche « Français », et
**jamais les deux à la fois**.

---

## 2. L'audit reçu le 6 octobre — ce qu'il dit

*(retranscription fidèle ; l'auditeur précise d'emblée qu'il a lu « le catalogue, les pages
et les menus enregistrés » et qu'il n'a pas pu afficher le site public ni son rendu mobile)*

1. **Fiabiliser le parcours de commande.** La page « Nomad — Commander » annonce une
   livraison à **1 500 DA** et la gratuité pour les trois articles, alors que le dernier
   tarif provisoire convenu est de **700 DA** (configuration à vérifier). Son bouton
   « **Confirmer ma commande** » redirige vers un panier puis le checkout au lieu de
   confirmer directement. *Priorité n° 1 : « aucune surprise au moment de payer ».*
2. **Terminer les pages de confiance.** « La marque », « Nos engagements », « Pièces
   détachées » et « Aide / FAQ » contiennent encore des mentions « **À compléter** ».
   Le contenu enregistré de « Livraison & retours » se limite à « **s** ». La FAQ annonce
   **2 à 5 jours**, contre **3 à 5 jours** dans la politique d'expédition. Les pages
   Contact et Club Maman ont un corps vide, mais le thème peut les alimenter : à
   contrôler avant de les juger vides.
3. **Cohérence catalogue / stocks.** Nomad à **3 200 DA**, 15 unités sur trois variantes ;
   **poncho (2 200 DA) et housse (1 200 DA) : 0 unité**. La **housse n'a aucun média**
   produit : une vraie photo est indispensable avant de la mettre en avant.
4. **Simplifier la navigation.** Dans le menu principal enregistré, « Maternité », «
   Bébé » et « Nouveautés » pointent **tous vers `/collections/all`** — trois intitulés
   pour une même sélection. Recommandation : « Boutique », « La marque », « Aide » ;
   garder le bouton **MAMA'S CLUB** existant.
5. **Renforcer les fiches produits.** Nomad est une bonne base (usage, dimensions, housse
   lavable) ; poncho et housse sont plus maigres : préciser dimensions, entretien,
   compatibilité, options réelles. Photos : une démonstration d'usage, une vue entière,
   un détail du tissu.
6. **Unifier le design, contrôler le mobile.** La page de commande a **sa propre
   identité** (Inter, Playfair Display, tons bruns) — différente de la direction « Ivoire
   & Nuit » — et contient un emplacement « **Photo du coussin Nomad, à remplacer** ».
   Une seule identité visuelle, puis un contrôle sur téléphone.

**Côté marketing et référencement**, l'auditeur recommande : Nomad en produit principal,
poncho et housse en compléments (une fois la disponibilité fiabilisée) ; une promesse
simple — « Allaitez confortablement, à la maison comme en déplacement » ; des intitulés
descriptifs et des textes propres à chaque produit.

---

## 3. La vérification, point par point

J'ai cherché chaque élément cité dans **nos** fichiers (thème, contenus, kit de saisie,
CSV produits) pour savoir de quel côté est le défaut.

| Ce que l'audit signale | Présent chez nous ? | Verdict |
|---|---|---|
| Page « Nomad — Commander », identité Inter + Playfair, tons bruns | **Non** — aucune trace dans le thème ni dans les contenus | **Vient de la boutique.** Aucun modèle du thème ne produit cette page. |
| Livraison à 1 500 DA / 700 DA, gratuité « pour les trois articles » | **Non** — ces montants n'existent nulle part chez nous | **Vient de la boutique.** Notre système calcule le tarif par wilaya et par mode (domicile / stop-desk) et l'affiche dans le formulaire. |
| Bouton « Confirmer ma commande » → panier → checkout | **Non** — notre formulaire **n'ouvre jamais de panier** : il envoie la commande directement (formulaire de contact) | **Vient de la boutique.** Le thème a déjà le parcours « 2 étapes au lieu de 4 ». |
| Pages « La marque », « Nos engagements », « Pièces détachées », « Aide / FAQ » avec « À compléter » | **Partiellement** : ces **intitulés** sont bien dans notre thème (pré-bandeau et pied de page), mais **pas les textes** décrits | Notre page « La marque » est **complète** ; aucune de nos pages de confiance ne contient « À compléter ». |
| « Livraison & retours » dont le contenu se limite à « s » | **Non** — nous avons deux pages distinctes : « Livraison » et « Échanges et retours », toutes deux rédigées | **Vient de la boutique** (page saisie à la main, restée vide). |
| FAQ 2 à 5 jours contre 3 à 5 jours dans la politique d'expédition | **Chez nous, tout dit « 2 à 5 jours ouvrés »** : la FAQ, la page Livraison, le bandeau d'icônes | **Vient de la boutique** : le « 3 à 5 » a été saisi ailleurs. Chez nous, aucune contradiction. |
| Contact et Club Maman « au corps vide » | **Conforme à notre conception** : ces deux pages sont **construites par le thème** (modèles `page.contact.json` et `page.club-maman.json`) ; seul le titre se remplit | **Rien à corriger** : l'auditeur le pressentait, c'est exactement ça. |
| Nomad 3 200 DA / 15 unités ; poncho et housse à **0 unité** | **Non** — notre CSV d'import **ne contient aucune quantité** (ni photo), volontairement | **Vient de la boutique** (saisie à la main après import). |
| Housse « sans aucun média » | **Non** — notre CSV ne livre **aucune photo** ; c'est dit dans la fiche des gestes : « il n'y a PAS de photos dans le fichier : vous ajouterez les vôtres » | **Rien à corriger côté fichiers** : il faut vos photos. |
| Menu : « Maternité », « Bébé », « Nouveautés » → tous `/collections/all` | **Non** — nos documents demandent 10 entrées, chacune vers sa propre collection (`maternite`, `allaitement`, `bebe`, `nouveautes`, `accessoires`) | **Vient de la boutique** : le menu a été créé autrement que demandé. |
| « Photo du coussin Nomad, à remplacer » | **Non** | **Vient de la boutique.** |

**Ce qui, chez nous, est déjà bon — et vérifié :**

- **Les délais : une seule valeur partout.** « 2 à 5 jours ouvrés » dans la FAQ, sur la
  page Livraison et dans le bandeau de promesses. Aucun « 3 à 5 ».
- **Le parcours de commande est déjà direct.** Le formulaire de commande (paiement à la
  livraison) est placé **sous les boutons d'achat de la fiche produit** : nom, téléphone,
  wilaya, commune, domicile ou stop-desk, **tarif affiché**, puis envoi de la commande.
  Pas de panier, pas de checkout, pas de surprise : le montant affiché est celui du
  transporteur, calculé pour la wilaya choisie (69 wilayas, 1 541 communes).
- **Notre kit de saisie est complet** : 10 pages, 5 collections, 3 articles, en français
  **et** en arabe, prêts à coller. Les seules mentions « à compléter » qui restent sont
  des **informations légales que vous seul pouvez fournir** (raison sociale, hébergeur,
  qui paie le retour) — et elles sont désormais **listées en clair** à la fin du kit
  (section 5, avec la référence de chaque ligne).
- **Le mobile et le rendu ont été contrôlés** : 9 largeurs de téléphone (320 → 480 px) sur
  81 pages, 0 débordement, 0 zone tactile trop petite ; 82 pages arabes en écriture de
  droite à gauche ; vitesses mesurées (≈ 1,3 s sur l'accueil, ≈ 2 s sur une fiche).

---

## 4. Les corrections, dans l'ordre — la liste des gestes

### A. Dans Shopify, à faire d'abord (les trois qui coûtent de l'argent ou la confiance)

1. **Le prix de livraison : trancher.** 700 DA ou 1 500 DA ? Une valeur, une seule, et
   partout. Notre thème n'affiche pas un prix fixe : il affiche le tarif **de la wilaya**
   (domicile / stop-desk) — c'est ce tarif-là qu'il faut renseigner, pas un forfait.
   Si ces deux pages annoncent un forfait, **supprimez-les** : la fiche produit contient
   déjà le bon formulaire.
2. **Supprimer la page « Nomad — Commander »** (intervention n° 1 et n° 6 de l'audit).
   Elle a sa propre identité visuelle (Inter, Playfair, bruns) et un emplacement photo
   « à remplacer ». Le thème fait déjà ce travail, dans la bonne identité, sans panier ni
   checkout. Si vous tenez à garder une page dédiée, dites-le moi : je la reconstruis avec
   les sections du thème.
3. **Les pages « à compléter » et la page vide.** Recoller les pages depuis
   `LLUFAN-DEMO-contenus-a-coller.md` (elles sont complètes), et remplacer la page
   « Livraison & retours » vide par les deux nôtres : **Livraison** (`/pages/livraison`)
   et **Échanges et retours**. Les huit informations légales qui manquent vraiment sont
   listées en **section 5 du kit** — une phrase chacune, et c'est réglé.

### B. Ensuite (catalogue, menu, photos)

4. **Stocks** : vérifier le poncho et la housse avant de les mettre en avant. À savoir :
   notre CSV les importe avec la règle « **continuer à vendre même à zéro** » — donc un
   article à 0 unité reste commandable. Si vous ne voulez pas cela, passez la règle à
   « refuser la vente quand il n'y a plus de stock » (Produits → l'article → Stock).
5. **Photos** : la housse n'a aucune image. Trois prises suffisent, et c'est aussi la
   recommandation de l'audit : une démonstration d'usage, une vue entière, un détail du
   tissu. Rappel : le CSV ne livre **aucune** photo — elles viennent de vous.
6. **Menu principal** : avec trois produits, une navigation courte est très bien. Si vous
   gardez les cinq rubriques, **chacune doit pointer vers sa collection** :
   `maternite`, `allaitement`, `bebe`, `nouveautes`, `accessoires` — jamais toutes vers
   `/collections/all`. Le bouton **MAMA'S CLUB** de l'en-tête reste tel quel.
7. **Fiches produits** : pour le poncho et la housse, reprendre la structure de Nomad —
   usage, dimensions, entretien, compatibilité, options. Les textes de démonstration sont
   dans le CSV produits ; ils se remplacent dans Shopify par les vôtres.
8. **Mobile** : après ces changements, un tour sur téléphone (lisibilité, espaces, choix
   des coloris, accès au bouton d'achat). Nos contrôles portent sur le thème ; ils ne
   peuvent pas juger des pages ajoutées à la main.

### C. Le référencement, si vous voulez le soigner

Les intitulés descriptifs et des textes propres à chaque produit suffisent pour commencer.
Le thème pose déjà les données structurées, les partages (WhatsApp, Facebook) et les
liens `hreflang` entre le français et l'arabe — la preuve est dans
`preuve-referencement.html` et `LLUFAN-conformite-et-vitesse.html`.

---

## 5. Ce qui a été ajouté à cette occasion

- **Le kit `LLUFAN-DEMO-contenus-a-coller.md` porte désormais une section 5** :
  « Les emplacements à compléter — le seul reste à faire », avec un tableau **Réf. / Page /
  Langue / Ce qui manque**. 8 mentions en français, 1 en arabe, 6 dans les articles du
  journal. La règle y est écrite noir sur blanc : *une page qui contient encore une de ces
  mentions ne se publie pas.*
- Le reste (verrou de la feuille de style, bascule de langue, contrôles) est décrit dans
  `GITHUB.txt`, à la suite de la remarque sur la langue.

---

## 6. Les deux rappels

- **Les deux jetons GitHub sont encore vivants** (contrôle du 6 octobre) : à révoquer.
- **Les textes arabes sont des propositions de démonstration** : à faire relire par un
  arabophone avant publication.
