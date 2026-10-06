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
AVERTISSEMENT=""

echo "═══════════════════════════════════════════════════════════════════"
echo "  LLUFAN — contrôle avant envoi"
echo "═══════════════════════════════════════════════════════════════════"
echo

# ── 1. le dossier du thème face à l'archive ────────────────────────────────
echo "1/5  les fichiers qui ont déjà reculé (feuille de style) sont-ils intacts ?"
RECUL=""
EMP=$(python3 verifier_empreintes.py)
echo "$EMP"
if echo "$EMP" | grep -q "FICHIER DE RÉFÉRENCE MODIFIÉ"; then
  RECUL="feuille-de-style"
  echo "     ! la feuille de style n'est pas celle attendue."
  # LA COPIE DE RÉFÉRENCE D'ABORD. C'est la seule source qui ne peut pas mentir :
  # le 6 octobre, une archive construite pendant un recul servait elle aussi
  # l'ancienne feuille, et « --restaurer » a écrasé le bon fichier par le mauvais.
  # Depuis, on restaure d'abord depuis llufan/reference/.
  echo "       → restauration depuis la copie de référence…"
  python3 verifier_empreintes.py --restaurer | sed 's/^/       /'
  if python3 verifier_empreintes.py | grep -q "sont intacts"; then
    RECUL=""
    AVERTISSEMENT="la feuille de style avait reculé ; elle a été restaurée depuis la copie de référence"
  else
    echo "       ⛔ restauration impossible : ne pas reconstruire l'archive dans cet état."
  fi
fi
echo

echo "2/5  le dossier du thème est-il celui de l'archive ?"
REPARE=""
ETAT="$(python3 verifier_theme_zip.py 2>&1)"
if echo "$ETAT" | grep -q "LE DOSSIER A RECULÉ"; then
  echo "     ! il a reculé : restauration depuis l'archive…"
  python3 verifier_theme_zip.py --restaurer 2>&1 | tail -1 | sed 's/^/     /'
  ETAT="$(python3 verifier_theme_zip.py 2>&1)"
  REPARE="oui"
  if [ -n "$RECUL" ] && python3 verifier_empreintes.py | grep -q "sont intacts"; then
    RECUL=""
    AVERTISSEMENT="le dossier du thème avait reculé ; il a été restauré depuis l'archive"
  fi
fi
if echo "$ETAT" | grep -q "identiques — rien à faire"; then
  echo "     ✓ dossier et archive identiques (104 fichiers)"
else
  echo "     ✗ dossier et archive différents — à examiner avant d'envoyer :"
  echo "$ETAT" | grep -E "différent|~|◆" | head -6 | sed 's/^/       /'
  echo "       → si le DOSSIER est le bon (fichier modifié exprès) :"
  echo "            bash llufan/refaire_archives.sh       (l'archive rattrape)"
  echo "       → si l'ARCHIVE est la bonne (le dossier a reculé) :"
  echo "            python3 llufan/verifier_empreintes.py --restaurer"
  echo "            bash llufan/refaire_archives.sh"
  echo "       (ne jamais « --forcer » : le 6 octobre, cette restauration a écrasé"
  echo "        une copie saine du dossier par une archive qui avait reculé)"
  SOUCIS="$SOUCIS dossier-vs-archive"
fi
if [ -n "$RECUL" ]; then SOUCIS="$SOUCIS $RECUL"; fi
echo

# ── 2. les règles de Shopify ───────────────────────────────────────────────
echo "3/5  les règles de validation de Shopify"
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
echo "4/5  la version française et la version arabe"
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
echo "5/5  la conformité du thème (19 points)"
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
if [ -n "$AVERTISSEMENT" ]; then
  echo "  ⚠ À NOTER : $AVERTISSEMENT."
  echo "     L'état est bon (c'est celui de l'archive livrée) : on peut envoyer."
  echo "     Simplement, l'espace de travail recule parfois tout seul — gardez"
  echo "     cette commande en réflexe avant chaque envoi."
  echo
fi
if [ -z "$SOUCIS" ]; then
  echo "  $OK"
  echo
  echo "  Rappel : après un envoi, vérifier sur GitHub que les empreintes"
  echo "  correspondent, puis, dans Shopify, « ⋯ → journaux de thème »."
else
  echo "  ✗ NE PAS ENVOYER : à revoir →$SOUCIS"
fi
echo "═══════════════════════════════════════════════════════════════════"
