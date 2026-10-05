#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  LLUFAN — publier cette copie de la boutique sur GitHub.
#
#  Usage, depuis CE dossier (celui qui contient docs/, theme/, contenus/) :
#
#      bash publier-sur-github.sh https://github.com/<compte>/<depot>.git
#
#  Avant : créez le dépôt sur github.com (« New repository »), SANS rien
#  cocher — il doit être vide. Le dépôt peut être public ou privé.
#
#  Le script : vérifie git, fait le premier commit, relie le dépôt et envoie.
#  C'est git, sur VOTRE machine, qui demandera l'autorisation (fenêtre de
#  connexion, ou identifiants déjà enregistrés).
# ---------------------------------------------------------------------------
set -e
URL="$1"
if [ -z "$URL" ]; then
  echo "Usage : bash publier-sur-github.sh https://github.com/<compte>/<depot>.git"
  exit 1
fi
case "$URL" in
  *github.com*) ;;
  *) echo "✗ cette adresse ne ressemble pas à un dépôt GitHub : $URL"; exit 1 ;;
esac
command -v git >/dev/null || { echo "✗ git n'est pas installé (git-scm.com)."; exit 1; }

if [ ! -d .git ]; then
  git init -q -b main
  echo "· dépôt local initialisé"
fi
# Le paquet lui-même, s'il est rangé juste à côté du dossier décompressé :
# il part dans le dépôt, téléchargeable d'un clic depuis GitHub.
case " $* " in
  *" --sans-paquet "*)
    echo "· (--sans-paquet : le zip du paquet n'est pas déposé dans le dépôt)" ;;
  *)
    if [ -f ../llufan.com.zip ] && [ ! -f llufan.com.zip ]; then
      cp ../llufan.com.zip ./llufan.com.zip
      echo "· llufan.com.zip (le paquet, juste à côté) ajouté au dépôt"
    fi ;;
esac

git config user.name  >/dev/null 2>&1 || git config user.name  "LLUFAN"
git config user.email >/dev/null 2>&1 || git config user.email "contact@llufan.com"

git add .
if git diff --cached --quiet; then
  echo "· rien de nouveau à enregistrer"
else
  git commit -q -m "Boutique LLUFAN — site hors ligne, thème, contenus et documents"
  echo "· premier commit fait ($(git ls-files | wc -l) fichiers)"
fi

if git remote | grep -qx origin; then
  git remote set-url origin "$URL"
else
  git remote add origin "$URL"
fi

echo "· envoi vers $URL — git va demander l'autorisation…"
git push -u origin main

echo
echo "✓ envoyé. Les trois dernières étapes, dans le navigateur :"
echo "  1. dépôt → Settings → Pages → Source : « Deploy from a branch »"
echo "     branche « main », dossier « /docs » → Save"
echo "  2. au bout d'une à deux minutes, la copie est en ligne à"
echo "     https://<compte>.github.io/<depot>/"
echo "  3. (facultatif) champ « Custom domain » pour un autre nom de domaine."
echo
echo "  Rappel : cette copie MONTRE la boutique. Le domaine llufan.com doit"
echo "  pointer vers la boutique Shopify, qui vend (panier, stock, paiement)."
