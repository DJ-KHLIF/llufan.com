#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle français ↔ arabe : les deux langues doivent raconter la même chose.

Pourquoi ce script existe
--------------------------------------------------------------------------
Le 5 octobre 2026, les contrôles automatiques (arabe, miroir RTL, mobile,
chargement) étaient tous verts — et pourtant cinq vrais défauts se cachaient
dans la version arabe : une section sans son enveloppe, la bande du haut qui
montrait les liens du menu au lieu des promesses, un carrousel transformé en
grille, un bandeau éditorial manquant sur les fiches produit, et trois produits
rangés dans des collections différentes selon la langue.

Aucun de ces défauts n'empêche une page de s'afficher : ils ne se voient qu'en
comparant les deux langues. C'est ce que fait ce script.

Ce qu'il vérifie
--------------------------------------------------------------------------
  1. les collections de chaque produit : le CSV Shopify (qui fait foi) doit
     dire la même chose que la page française et que la page arabe ;
  2. la structure, page contre page, des 40 paires françaises/arabes :
     nombre de sections, présence de la grille « univers », nombre de cartes
     produit, présence des bandeaux éditoriaux ;
  3. les réglages communs aux deux langues : hauteur de la première image,
     bande de promesses de l'accueil arabe.

Usage :  python3 audit_contenu_fr_ar.py
Sortie : une ligne de verdict (lire cette ligne, pas le code de sortie).
"""
import csv
import importlib.util
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PREVIEW = os.path.join(ICI, 'preview')
DEMO = os.path.join(ICI, 'demo')
COLLECTIONS = ['maternite', 'allaitement', 'bebe', 'nouveautes', 'accessoires']

problemes = []


def charge(nom):
    """Charge un module du dossier demo/ (contenu_demo, contenu_demo_ar)."""
    chemin = os.path.join(DEMO, nom + '.py')
    spec = importlib.util.spec_from_file_location(nom, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tags_du_csv():
    """Les collections déclarées dans le CSV destiné à Shopify, par produit."""
    tags = {}
    chemin = os.path.join(ICI, 'LLUFAN-DEMO-produits.csv')
    with open(chemin, encoding='utf-8-sig') as f:
        for ligne in csv.DictReader(f):
            if ligne.get('Tags'):
                tags.setdefault(ligne['Handle'], set()).update(
                    t.strip() for t in ligne['Tags'].split(',') if t.strip())
    return tags


# ---------------------------------------------------------------------------
# 1. Les collections : CSV = français = arabe
# ---------------------------------------------------------------------------
def controle_collections(fr, ar):
    tags = tags_du_csv()
    for p in fr.PRODUITS:
        handle = p['handle']
        attendu = sorted(tags.get(handle, set()) & set(COLLECTIONS))
        cote_fr = sorted(x for x in p['collections'].split(', ') if x in COLLECTIONS)
        jumeau = next((x for x in ar.PRODUITS if x['handle'] == handle), None)
        if jumeau is None:
            problemes.append('collection : %s n\'existe pas en arabe' % handle)
            continue
        cote_ar = sorted(x for x in jumeau['collections'].split(', ') if x in COLLECTIONS)
        if not (attendu == cote_fr == cote_ar):
            problemes.append(
                'collections de %s : CSV %s · FR %s · AR %s'
                % (handle, attendu, cote_fr, cote_ar))
        # l'étiquette affichée dans l'aperçu doit elle aussi concorder
        etiquette_fr = p.get('tags', '')
        if etiquette_fr:
            trouvees = sorted({t.strip() for t in etiquette_fr.split(',')} & set(COLLECTIONS))
            if trouvees != cote_fr:
                problemes.append(
                    'étiquette/collection incohérentes pour %s : étiquettes %s, '
                    'collection %s (FR)' % (handle, trouvees, cote_fr))


# ---------------------------------------------------------------------------
# 2. La structure, page contre page
# ---------------------------------------------------------------------------
def empreinte_structure(chemin, langue):
    """Ce qui doit être identique entre une page et sa jumelle."""
    with open(chemin, encoding='utf-8') as f:
        h = f.read()
    liens = set(re.findall(r'class="product-card__media" href="([^"]+)"', h))
    if langue == 'ar':                       # les liens arabes portent le préfixe
        liens = {l[3:] if l.startswith('ar-') else l for l in liens}
    return (h.count('<div class="section-spacing'),      # sections
            h.count('class="collection-cards"'),         # grille « univers »
            len(liens),                                  # cartes produit distinctes
            h.count('media-with-text__image-main'))      # bandeaux éditoriaux


def controle_pages():
    if not os.path.isdir(PREVIEW):
        problemes.append('le dossier preview/ est absent : pages non générées')
        return 0
    pages_fr = sorted(f for f in os.listdir(PREVIEW)
                      if f.endswith('.html') and not f.startswith(('ar-', 'comment-'))
                      and f != 'apercu.html')
    paires = 0
    for f in pages_fr:
        jumelle = 'ar-' + f
        if not os.path.exists(os.path.join(PREVIEW, jumelle)):
            problemes.append('pas de jumelle arabe pour %s' % f)
            continue
        paires += 1
        a = empreinte_structure(os.path.join(PREVIEW, f), 'fr')
        b = empreinte_structure(os.path.join(PREVIEW, jumelle), 'ar')
        if a != b:
            noms = ['sections', 'grille univers', 'cartes produit', 'bandeaux édit.']
            detail = ', '.join('%s %s→%s' % (n, x, y) for n, x, y in zip(noms, a, b) if x != y)
            problemes.append('structure de %s : %s' % (f, detail))
    return paires


# ---------------------------------------------------------------------------
# 3. Les réglages communs
# ---------------------------------------------------------------------------
def controle_reglages(ar):
    for reglage, fichier in [('--hero-height:78vh', 'accueil.html')]:
        for langue, prefixe in (('FR', ''), ('AR', 'ar-')):
            chemin = os.path.join(PREVIEW, prefixe + fichier)
            if os.path.exists(chemin):
                with open(chemin, encoding='utf-8') as f:
                    if reglage not in f.read():
                        problemes.append(
                            '%s : %s ne porte pas %s' % (langue, fichier, reglage))
    texte_ar = getattr(ar, 'ICONES_ACCUEIL', None)
    if not texte_ar or len(texte_ar) != 3:
        problemes.append('la bande de promesses arabe (ICONES_ACCUEIL) est incomplète')
    chemin = os.path.join(PREVIEW, 'ar-accueil.html')
    if texte_ar and os.path.exists(chemin):
        with open(chemin, encoding='utf-8') as f:
            h = f.read()
        for promesse in texte_ar:
            if promesse['text'] not in h:
                problemes.append('accueil arabe : la promesse « %s » n\'est pas affichée'
                                 % promesse['text'])


def main():
    print('LLUFAN — contrôle français ↔ arabe\n')
    fr, ar = charge('contenu_demo'), charge('contenu_demo_ar')

    controle_collections(fr, ar)
    print('  1. collections des %d produits (CSV = FR = AR) ....... %s'
          % (len(fr.PRODUITS), 'conforme' if not problemes else 'à revoir'))

    avant = len(problemes)
    paires = controle_pages()
    print('  2. structure de %d paires de pages ................... %s'
          % (paires, 'conforme' if len(problemes) == avant else 'à revoir'))

    avant = len(problemes)
    controle_reglages(ar)
    print('  3. réglages communs (hauteur d\'accueil, promesses) .. %s'
          % ('conforme' if len(problemes) == avant else 'à revoir'))

    print()
    if problemes:
        for p in problemes:
            print('  ✗', p)
        print()
        print('  ✗ %d problème(s) : les deux langues ne racontent pas la même chose.'
              % len(problemes))
    else:
        print('  ✓ Aucun écart : la version arabe et la version française se')
        print('    répondent section par section.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
