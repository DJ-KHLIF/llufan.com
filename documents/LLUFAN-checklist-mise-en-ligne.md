# LLUFAN — Liste de contrôle avant mise en ligne

À suivre dans l'ordre, en cochant au fur et à mesure. Chaque étape indique
**ce qu'on fait**, **où** dans Shopify, et **ce qu'on doit voir** pour pouvoir
cocher. Le détail de chaque manipulation est dans `LLUFAN-DEMO-mode-emploi.md` ;
l'aperçu montre le résultat attendu — il se reconstruit d'abord, il n'est plus
gardé sur le disque parce qu'il pèse 60 Mo et se refait en quelques secondes :

    bash llufan/refaire_apercu.sh      →  llufan/preview/apercu.html

Les mentions « démonstration » signalent les contenus fictifs livrés pour
tester : ils sont listés ensemble à la fin (§10).

---

## 0. Avant de commencer — ce qu'il faut avoir sous la main

- [ ] `LLUFAN-theme-Shopify.zip` (le thème)
- [ ] `LLUFAN-DEMO-produits.csv` et `LLUFAN-DEMO-collections.csv`
- [ ] `LLUFAN-DEMO-journal-a-publier.md` (3 articles)
- [ ] Les **visuels produits définitifs** (ou, pour tester, ceux de `demo/produits/`)
- [ ] Le **lien de la vidéo** de l'accueil (YouTube ou Vimeo) — facultatif
- [ ] Le **numéro WhatsApp** et l'**e-mail** à afficher : 0772 415 120 · contact@llufan.com
- [ ] Un accès administrateur à la boutique Shopify

---

## 1. Le thème

- [ ] Boutique en ligne → Thèmes → **Ajouter un thème** → Importer un fichier ZIP → `LLUFAN-theme-Shopify.zip`
- [ ] **Ce qu'on doit voir** : le thème s'ajoute sans message d'erreur, avec son aperçu
- [ ] Ne pas publier tout de suite (dernière étape seulement)

*L'archive livrée est déjà passée au contrôle d'import : 19 points vérifiés,
0 avertissement, 0 point bloquant — fichiers obligatoires, modèles, schémas de
section, réglages, Liquid obsolète, traductions, appels d'images, poids. Pour le
repasser après une modification du thème : `python3 audit_conformite_shopify.py`,
et pour le rapport complet (conformité + vitesse) :
`python3 build_rapport_vitesse.py` → `LLUFAN-conformite-et-vitesse.html`
(README §30).*

## 2. Les produits

- [ ] Produits → **Importer** → `LLUFAN-DEMO-produits.csv` (10 produits, 28 variantes, créés en brouillon)
- [ ] **Ce qu'on doit voir** : 10 produits listés, chacun avec ses couleurs ou tailles
- [ ] Ouvrir chaque produit → **Médias** → ajouter les photos définitives (glisser, ou « Ajouter à partir d'une URL »)
- [ ] **Reprendre chaque prix** : les prix livrés (900 à 5 500 DA) sont fictifs sauf le coussin Nomad (3 200 DA)
- [ ] Vérifier les **descriptions** sur 2 ou 3 produits : elles sont de démonstration
- [ ] Décider du **coussin de grossesse Luna** et des 8 autres produits inventés : à garder, renommer ou supprimer
- [ ] Passer les produits retenus en **Actif** (les CSV les créent en brouillon, volontairement)

## 3. Les collections

- [ ] Produits → Collections → **Importer** → `LLUFAN-DEMO-collections.csv` (5 collections)
- [ ] Rattacher les produits : chaque produit porte déjà son **type** dans le CSV ; créer les collections *automatiques* sur ce type, ou les remplir à la main
- [ ] **Ce qu'on doit voir** : Maternité (3), Allaitement (5), Bébé (4), Nouveautés (5), Accessoires et pièces détachées (3)
- [ ] Vérifier qu'aucune collection ne reste vide (une collection vide affiche un état vide)

## 4. Les pages d'information (10 pages à créer)

Pour chaque page : Boutique en ligne → **Pages** → Ajouter une page, puis choisir le
modèle dans le menu de droite.

- [ ] `La marque` → modèle `page.la-marque`
- [ ] `Livraison` → `page.livraison`
- [ ] `Paiement` → `page.paiement`
- [ ] `Échanges et retours` → `page.politique-de-retour`
- [ ] `Mentions légales` → `page.mentions-legales`
- [ ] `Conditions générales de vente` → `page.cgv`
- [ ] `Politique de confidentialité` → `page.confidentialite`
- [ ] `FAQ` → `page.faq`
- [ ] `Contact` → `page.contact`
- [ ] `Club Maman` → `page.club-maman`
- [ ] **Ce qu'on doit voir** : chaque page s'affiche **habillée** (en-tête, pied de page, styles), pas en texte brut
- [ ] Le lien du pied de page s'affiche **dès que la page existe** (avant, il reste masqué : c'est voulu)

> Les quatre pages juridiques (CGV, mentions, confidentialité, retours) sont des
> **gabarits à trous** : les parties entre crochets sont à faire rédiger ou
> valider. Aucun texte juridique n'a été inventé.

## 5. Les menus

- [ ] Boutique en ligne → **Navigation** → menu principal : Maternité · Bébé · Nouveautés (puis Allaitement, Accessoires)
- [ ] Ajouter au menu les quatre entrées du pré-bandeau : Espace maman · La marque · Pièces détachées · Aide / FAQ
- [ ] Remplir les quatre colonnes du pied de page (La marque, Nos univers, Aide, Contact) avec les pages créées à l'étape 4

## 6. Le journal

- [ ] Boutique en ligne → **Blog** → Ajouter un article × 3, en collant les textes de `LLUFAN-DEMO-journal-a-publier.md`
- [ ] Ajouter une illustration à chaque article
- [ ] **Ce qu'on doit voir** : la liste des articles et la page de chaque article s'affichent avec le modèle du thème

## 7. Le compte client

- [ ] Paramètres → **Comptes clients** → activer (facultatif)
- [ ] **Ce qu'on doit voir** : le lien « Compte » de l'en-tête ouvre la page de connexion habillée

## 8. Les réglages de la boutique

- [ ] Éditeur → **Identité** : logo, couleurs de la charte, police (déjà en place)
- [ ] Éditeur → **Mode démonstration** : le passer sur **non** quand vos contenus sont prêts (il masque le bandeau « contenu de démonstration »)
- [ ] **Contact WhatsApp** : vérifier que le numéro affiché et le lien sont bien synchronisés
- [ ] **Devise** : DZD (Paramètres → Boutique → Devise)
- [ ] **Livraison** : les 69 wilayas et leurs tarifs sont dans le thème ; vérifier qu'ils correspondent à vos tarifs transporteur réels
- [ ] **Paiement** : paiement à la livraison, aucune passerelle à activer

## 9. Les réglages du thème, section par section

- [ ] Accueil : diaporama (2 visuels + textes), cartes d'univers (4), sélection produits, avis, bloc éditorial
- [ ] Accueil → **Vidéo** : coller le lien YouTube / Vimeo (voir `preview/comment-ajouter-une-video.html`)
- [ ] Pied de page : phrase de marque, contacts, mentions, réseaux sociaux (emplacements sans lien fictif)
- [ ] Vérifier que le pré-bandeau et le bandeau d'annonce affichent le bon message

## 10. Ce qui est fictif et ne doit pas partir en ligne tel quel

- [ ] **3 avis** de l'accueil (auteur « Amina — Alger »)
- [ ] **3 discussions** du Club Maman
- [ ] **8 produits sur 10** et **9 prix sur 10** (seul le coussin Nomad est réel)
- [ ] Les **10 visuels produits** et les **8 visuels d'ambiance** (images générées)
- [ ] Les **textes** des pages d'information, les **3 articles** du journal, les **8 questions** de la FAQ
- [ ] Les **délais « 2 à 5 jours ouvrés »** et les **tarifs de livraison** : provisoires
- [ ] Les **réseaux sociaux** du pied de page : emplacements vides, à relier à vos comptes
- [ ] Les **textes arabes** des pages `preview/ar-*.html` et des fichiers `LLUFAN-DEMO-contenus-a-coller.md` (pages, collections, articles) et `LLUFAN-DEMO-traductions-ar.csv` (133 lignes) : propositions de traduction, à valider par un arabophone

## 11. Le test de bout en bout, avant de publier

- [ ] Sur ordinateur **et** sur téléphone, faire une commande complète : produit → couleur → quantité → Nom, Téléphone → Wilaya → Commune → À domicile / Stop-desk
- [ ] Vérifier que le **total** = sous-total du panier + frais affichés, et que la **barre mobile** affiche le même montant
- [ ] Choisir 3 wilayas différentes (dont une éloignée) et vérifier les tarifs
- [ ] Cliquer **tous** les liens du pied de page et du menu : aucune page vide, aucun lien mort
- [ ] Ouvrir le panier vide, le tiroir panier et le tiroir menu sur téléphone
- [ ] Vérifier les e-mails de commande (notification, confirmation) dans Paramètres → Notifications

## 12. La version arabe (facultatif)

- [ ] Paramètres → **Langues** → *Ajouter une langue* → **العربية** → **Publier**
- [ ] Éditeur → Réglages du thème → **Sélecteurs et mentions légales** : « Afficher le sélecteur de langue » coché, « Choisir la langue d'après celle du navigateur » coché (ou décoché, si le choix doit toujours venir de la cliente)
- [ ] Applications → **Traduire et adapter** : traduire les **produits**, **collections**, **pages**, **articles** et **politiques** — les libellés de l'interface, eux, sont déjà traduits dans le thème (`locales/ar.json` — 136 clés, les 123 utilisées
  toutes présentes)
- [ ] **Texte arabe déjà écrit** : `LLUFAN-DEMO-traductions-ar.csv` — **133 lignes, une par champ** tel que Shopify l'exporte (les corps de page sont assemblés en HTML, le collage se fait donc ligne à ligne sans rien reconstituer). Exporter les traductions depuis Shopify, coller la colonne « العربية » dans « Translated content », réimporter. Les textes français à créer d'abord : `LLUFAN-DEMO-contenus-a-coller.md`. Détail : README §16.2
- [ ] **Contenu du thème** (Traduire et adapter → *Contenu du thème*, type `ONLINE_STORE_THEME`) : les 17 textes saisis dans les réglages de sections — titre du Club Maman, formulaire de commande, pied de page, bandeau de démonstration. On les repère par leur texte français
- [ ] **Faire relire les textes arabes** par un locuteur avant publication (ils sont marqués « تجريبي »)
- [ ] **Bascule de langue** : en français, l'en-tête affiche « العربية » et un clic passe en arabe ; en arabe, il affiche « Français » et ramène au français. **Les deux langues ne doivent jamais apparaître en même temps**
      - Elle est **cochée par défaut** (« Afficher le sélecteur de langue », groupe « Sélecteurs et mentions légales »). Si vous ne la voyez pas dans l'en-tête : vérifiez d'abord que l'**arabe est publié** (Paramètres → Langues) — le sélecteur ne peut apparaître qu'à partir de deux langues publiées — puis que la case est bien cochée dans les réglages du thème.
- [ ] Ouvrir `llufan.com/ar` : en-tête, une fiche produit, le formulaire de commande (les prix doivent s'afficher « 3 200 DA », jamais « DA 200 3 »)
- [ ] Sur téléphone : vérifier que le **panier** s'ouvre par la gauche, et le **menu** et les **filtres** par la droite
- [ ] Ouvrir le **tri** d'une collection en arabe : le panneau doit rester dans la page (deux défauts de ce genre ont été corrigés le 4 octobre, README §17)
- [ ] **Aucune page à moitié traduite** : parcourir les 40 pages arabes de l'aperçu (reconstruit d'abord) (elles sont toutes dans `preview/ar-*.html`) — sur une page arabe, aucun mot français ne doit apparaître, à trois exceptions près : le mot **« Français »** de la bascule de langue, le nom **LLUFAN** et les chiffres des prix
- [ ] **Wilayas en arabe** : dans le formulaire de commande arabe, la liste des wilayas doit s'afficher en arabe (`الجزائر`, `وهران`…). La commande reçue garde, elle, la valeur d'origine
- [ ] Vérifier que la **bascule de langue** mène bien à la même page dans l'autre langue : fiche produit → fiche produit, FAQ → FAQ, Club Maman → Club Maman

*À savoir : les intitulés de champs transmis à la commande (`Nom complet`, `Téléphone`, `Wilaya`, `Commune`) restent en français — ce sont vos étiquettes côté administration, invisibles pour la cliente. Le détail est au §19 du README.*

---

## 12bis. Le téléphone (à vérifier avant publication)

- [ ] Ouvrir la boutique sur un **vrai téléphone**, pas seulement dans une fenêtre réduite
- [ ] L'**en-tête** : le bouton menu s'ouvre, les icônes compte / recherche / panier se touchent du premier coup (44 px), et rien ne passe sous le logo
- [ ] La **grille de collection** : deux colonnes, images entières, prix lisibles, pastilles de couleur assez grosses
- [ ] Sur une **fiche produit** : choisir une couleur, monter la quantité, commander — sans zoomer
- [ ] Le **formulaire de commande** : wilaya, commune, domicile / stop-desk ; les cartes de livraison font toute la ligne
- [ ] La **barre du bas** (prix + « Commander ») ne recouvre pas le pied de page
- [ ] Les bandeaux du haut ne prennent pas plus de deux lignes
- [ ] Contrôle automatique, si vous avez Python et un navigateur sur l'ordinateur :
      `python3 verifier_mobile.py` → doit finir sur « tout tient, sur toutes les largeurs »

*À savoir : les trois vérifications automatiques (`verifier_pages.py`,
`verifier_arabe.py`, `verifier_mobile.py`) ont besoin de Chromium installé sur
l'ordinateur — c'est ce qui a permis de trouver, le 4 octobre, sept défauts
invisibles sur les captures d'ordinateur : icônes d'en-tête écrasées à 0 px
sous 430 px, boutons à 20 px, panneau de tri hors écran. Détail : README §21.*

---

## 13. La publication

- [ ] Boutique en ligne → Thèmes → **Publier** le thème LLUFAN
- [ ] Vérifier l'accueil publiée sur téléphone (le bandeau de démonstration doit être absent)
- [ ] Passer commande **une fois pour de vrai**, puis annuler la commande de test
- [ ] Garder la version précédente du thème sous la main, en cas de retour arrière

### Mesurer la vitesse une fois en ligne

- [ ] Ouvrir **PageSpeed Insights** (Google) sur l'adresse de l'accueil, puis sur
      une fiche produit, en mode **téléphone** : c'est le seul chiffre qui compte
      vraiment, parce qu'il vient de la vraie boutique, servie par le CDN de
      Shopify — pas de notre banc d'essai
- [ ] Repères de notre mesure de laboratoire (README §30) : accueil ≈ 1,3 s,
      fiche produit ≈ 2,0 s, rien ne bouge sous le doigt (0,008). En ligne, viser
      **moins de 2,5 s** sur téléphone en 4G
- [ ] Si le score chute après l'installation d'une application : la désactiver et
      remesurer. Chaque application ajoute ses propres scripts ; c'est la première
      cause de lenteur sur une boutique Shopify
- [ ] Les images pèsent les trois quarts de la page : envoyer des photos déjà
      redimensionnées (**1600 px de large suffisent** pour une bannière)

---

*Documents liés : `LLUFAN-DEMO-mode-emploi.md` (les manipulations en détail) ·
`README.md` (méthode, mesures, décisions) · `preview/apercu.html` (les 81 pages
de l'aperçu, dont 40 en arabe) · `preview/comment-ajouter-une-video.html` (la vidéo).*
