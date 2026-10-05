#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  LLUFAN — LE CONTRÔLE À PASSER AVANT TOUT ENVOI.
#
#  Usage :  bash llufan/verifier_avant_envoi.sh
#
#  Pourquoi cette commande existe
#  ---------------------------------------------------------------------------
#  Le 5 octobre 2026, le dossier du thème (llufan/theme/) a reculé DEUX FOIS à
#  l'état du 16h48, alors que l'archive, elle, restait bonne : une remise en
#  place de l'espace de travail rétablissait d'anciens fichiers. Un envoi fait
#  sans s'en apercevoir aurait publié une version dépassée — c'est exactement
#  ce qui s'était produit avant.
#
#  Cette commande fait donc quatre choses, dans l'ordre, et dit à la fin si
#  l'on peut envoyer :
#      1. si le dossier a reculé, elle le RESTAURE depuis l'archive (sans rien
#         perdre : l'archive est l'état livré) ;
#      2. elle relit les règles que Shopify applique à l'import ;
#      3. elle compare la version française et la version arabe ;
#      4. elle contrôle la conformité du thème (19 points).
#
#  Durée : quelques secondes. Aucun navigateur nécessaire.
# ---------------------------------------------------------------------------
cd "$(dirname "$0")" || exit 1
OK="✓ tout est prêt : on peut envoyer"
SOUCIS=""

echo "═══════════════════════════════════════════════════════════════════"
echo "  LLUFAN — contrôle avant envoi"
echo "═══════════════════════════════════════════════════════════════════"
echo

# ── 1. le dossier du thème face à l'archive ────────────────────────────────
echo "1/4  le dossier du thème est-il celui de l'archive ?"
ETAT="$(python3 verifier_theme_zip.py 2>&1)"
if echo "$ETAT" | grep -q "LE DOSSIER A RECULÉ"; then
  echo "     ! il a reculé : restauration depuis l'archive…"
  python3 verifier_theme_zip.py --restaurer 2>&1 | tail -1 | sed 's/^/     /'
  ETAT="$(python3 verifier_theme_zip.py 2>&1)"
fi
if echo "$ETAT" | grep -q "identiques — rien à faire"; then
  echo "     ✓ dossier et archive identiques (104 fichiers)"
else
  echo "     ✗ dossier et archive différents — à examiner avant d'envoyer :"
  echo "$ETAT" | grep -E "différent|~|◆" | head -6 | sed 's/^/       /'
  echo "       → si c'est un fichier que vous venez de modifier exprès :"
  echo "            bash llufan/refaire_archives.sh        (l'archive rattrape)"
  echo "       → si c'est un recul de l'espace de travail :"
  echo "            python3 llufan/verifier_theme_zip.py --restaurer --forcer"
  SOUCIS="$SOUCIS dossier/archive"
fi
echo

# ── 2. les règles de Shopify ───────────────────────────────────────────────
echo "2/4  les règles de validation de Shopify"
REG="$(python3 audit_erreurs_shopify.py 2>&1)"
if echo "$REG" | grep -q "Aucune erreur"; then
  echo "     ✓ filtres, noms, décimales, adresses : tout conforme"
else
  echo "     ✗ au moins une règle n'est pas respectée :"
  echo "$REG" | grep -E "✗" | head -6 | sed 's/^/       /'
  SOUCIS="$SOUCIS règles-shopify"
fi
echo

# ── 3. français ↔ arabe ───────────────────────────────────────────────────
echo "3/4  la version française et la version arabe"
FRAR="$(python3 audit_contenu_fr_ar.py 2>&1)"
if echo "$FRAR" | grep -q "Aucun écart"; then
  echo "$FRAR" | grep -E "^  [0-9]\." | sed 's/^/     /'
  echo "     ✓ les deux langues se répondent section par section"
else
  echo "$FRAR" | grep -E "✗" | head -8 | sed 's/^/       /'
  SOUCIS="$SOUCIS arabe"
fi
echo

# ── 4. la conformité du thème ─────────────────────────────────────────────
echo "4/4  la conformité du thème (19 points)"
CONF="$(python3 audit_conformite_shopify.py 2>&1)"
LIGNE="$(echo "$CONF" | grep -E "conforme\(s\)" | tail -1)"
echo "     ${LIGNE:-$(echo "$CONF" | tail -1)}"
if echo "$CONF" | grep -q "sans réserve bloquante"; then
  echo "     ✓ importable dans Shopify"
else
  SOUCIS="$SOUCIS conformité"
fi
echo

echo "═══════════════════════════════════════════════════════════════════"
if [ -z "$SOUCIS" ]; then
  echo "  $OK"
  echo
  echo "  Rappel : après un envoi, vérifier sur GitHub que les empreintes"
  echo "  correspondent, puis, dans Shopify, « ⋯ → journaux de thème »."
else
  echo "  ✗ NE PAS ENVOYER : à revoir →$SOUCIS"
fi
echo "═══════════════════════════════════════════════════════════════════"
