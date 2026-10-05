# LLUFAN — la boutique (copie de démonstration)

Boutique **LLUFAN** (maternité, allaitement, confort mère-bébé — Algérie), 
transposée en thème Shopify, avec sa version arabe complète.

**Voir la boutique :** ouvrez [`docs/index.html`](docs/index.html) — aucune installation,
aucune connexion requise. La page [`docs/apercu.html`](docs/apercu.html) montre les
81 pages d'un coup d'œil. La version arabe commence à
[`docs/ar-accueil.html`](docs/ar-accueil.html).

| Dossier | Ce qu'il contient |
|---|---|
| `docs/` | La boutique hors ligne : 41 pages françaises + 40 arabes, chacune autonome |
| `theme/` | `LLUFAN-theme-Shopify.zip` — le thème à importer dans Shopify |
| `contenus/` | Les CSV d'import (produits, collections), le journal, les traductions arabes |
| `documents/` | Liste de contrôle avant mise en ligne, pas à pas, méthode, conformité et vitesse mesurée, comparaison avec la référence `doomoo.com` |
| `outils/` | Les contrôles automatiques du projet, dont la commande à passer avant tout envoi (`verifier_avant_envoi.sh`) — voir `outils/LIRE-MOI.txt` |

**État vérifié le 5 octobre 2026 :** import Shopify sans réserve (19 points conformes,
0 avertissement, 0 bloquant) · accueil ≈ 1,3 s, fiche produit ≈ 2,0 s sur réseau bridé ·
aucun déplacement sous le doigt (0,008) · 246 + 82 + 729 contrôles de mise en page,
d'arabe et de téléphone, tous verts.

**Tout télécharger d'un clic :** le bouton vert **Code → Download ZIP** donne
cette archive telle quelle. Si le fichier `llufan.com.zip` est présent à la racine
du dépôt, il contient exactement les mêmes fichiers, prêts à décompresser.

**Ce n'est pas la boutique en ligne.** Les photos, prix et textes sont des contenus de
**démonstration**, à remplacer. La boutique qui vend (panier, paiement à la livraison,
stock, e-mails) vit dans **Shopify** ; cette copie sert à regarder, montrer et partager.

*Pages de preuve : `documents/LLUFAN-conformite-et-vitesse.html` (conformité et vitesse),
`documents/comparaison-doomoo-llufan.html` (la comparaison avec la référence, point par
point : ce qui est identique, ce qui clochait, ce qui a été corrigé) et
`documents/README.md` (la méthode complète, chapitre par chapitre).*
