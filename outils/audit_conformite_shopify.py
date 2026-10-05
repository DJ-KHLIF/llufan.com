#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle de conformité du thème LLUFAN avec la plateforme Shopify.

Ce que ce script vérifie, et pourquoi :

  structure      les fichiers qu'un thème Shopify doit avoir, et ceux qu'il ne
                 doit plus avoir (checkout.liquid, obsolète depuis 2024) ;
  modèles        chaque modèle JSON est lisible, ses sections existent, il n'y
                 en a pas plus de 25 (limite imposée par l'éditeur) ;
  schémas        chaque {% schema %} est un JSON valide, avec des identifiants
                 uniques et des types de réglages que Shopify reconnaît ;
  réglages       chaque clé écrite dans settings_data.json existe dans
                 settings_schema.json — une clé inconnue est refusée à l'import ;
  Liquid         aucune balise ni filtre obsolète (include, img_url,
                 money_without_currency), qui produisent des avertissements ;
  traductions    la locale par défaut est bien fr.default.json, et les deux
                 langues portent le même jeu de clés (sinon l'une des deux
                 affiche des libellés techniques) ;
  assets         chaque asset appelé existe, aucune adresse locale ne traîne,
                 aucun fichier trop lourd pour Shopify ;
  images         les images passent par le CDN Shopify avec une largeur
                 demandée (sinon la photo d'origine est servie en pleine
                 taille : c'est le premier poste de lenteur) ;
  éditeur        les sections et blocs portent shopify_attributes, sinon
                 l'éditeur ne peut pas les sélectionner.

Usage : python3 audit_conformite_shopify.py     (depuis /home/user/llufan)
Sortie : un rapport lisible, et un code de sortie 1 si un point bloquant existe.
"""
import io
import json
import os
import re
import sys
import zipfile

RACINE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(RACINE, 'theme')
ZIP = os.path.join(RACINE, 'LLUFAN-theme-Shopify.zip')

# Types de réglages reconnus par Shopify (documentation « Input settings »).
TYPES_REGLAGES = {
    'text', 'textarea', 'richtext', 'html', 'liquid', 'inline_richtext',
    'number', 'range', 'checkbox', 'radio', 'select', 'color', 'color_background',
    'color_scheme', 'color_scheme_group', 'font_picker', 'image_picker',
    'video', 'video_url', 'url', 'product', 'product_list', 'collection',
    'collection_list', 'blog', 'page', 'article', 'link_list', 'header',
    'paragraph', 'email', 'text_alignment', 'html_heading', 'metaobject',
    'metaobject_list', 'range', 'date', 'header',
}

# Fichiers qu'un thème publié doit contenir.
REQUIS = [
    'layout/theme.liquid',
    'config/settings_schema.json',
    'locales/fr.default.json',
    'templates/index.json', 'templates/product.json', 'templates/collection.json',
    'templates/list-collections.json', 'templates/cart.json', 'templates/blog.json',
    'templates/article.json', 'templates/page.json', 'templates/search.json',
    'templates/404.json', 'templates/password.liquid', 'templates/gift_card.liquid',
    'templates/customers/account.liquid', 'templates/customers/login.liquid',
    'templates/customers/register.liquid', 'templates/customers/addresses.liquid',
    'templates/customers/order.liquid', 'templates/customers/reset_password.liquid',
    'templates/customers/activate_account.liquid',
]

# Ce qu'un thème ne doit PLUS contenir.
INTERDITS = {
    'templates/checkout.liquid': 'obsolète depuis 2024 : Shopify refuse de le charger, '
                                 'La caisse est gérée par la plateforme',
}

normal, bloquants, avertissements = [], [], []


def ok(titre, detail=''):
    normal.append((titre, detail))


def bloque(titre, detail):
    bloquants.append((titre, detail))


def attention(titre, detail):
    avertissements.append((titre, detail))


def lire(chemin):
    return io.open(chemin, encoding='utf-8', errors='replace').read()


def fichiers_du_theme():
    trouves = []
    for base, _d, fs in os.walk(THEME):
        for f in fs:
            trouves.append(os.path.relpath(os.path.join(base, f), THEME))
    return sorted(trouves)


# ── 1. structure ────────────────────────────────────────────────────────────
def controler_structure(fichiers):
    manquants = [f for f in REQUIS if f not in fichiers]
    if manquants:
        bloque('Fichiers obligatoires', 'absents : ' + ', '.join(manquants))
    else:
        ok('Fichiers obligatoires', '%d fichiers présents (modèles, langues, compte, caisse-cadeau)' % len(REQUIS))

    for chemin, raison in INTERDITS.items():
        if chemin in fichiers:
            bloque('Fichier obsolète', '%s — %s' % (chemin, raison))
    ok('Aucun fichier obsolète', 'pas de checkout.liquid ni de gabarit de caisse')

    parasites = [f for f in fichiers if os.path.basename(f).startswith(('.DS_Store', '__MACOSX'))
                 or f.endswith(('.zip', '.psd', '.ai'))]
    if parasites:
        attention('Fichiers parasites', ', '.join(parasites[:5]))
    else:
        ok('Aucun fichier parasite', 'ni .DS_Store, ni archive, ni fichier de travail')
    return [f for f in fichiers if f.endswith('.liquid')]


# ── 2. le gabarit principal ─────────────────────────────────────────────────
def controler_gabarit():
    texte = lire(os.path.join(THEME, 'layout', 'theme.liquid'))
    for element, quoi in (('{{ content_for_header }}', 'les scripts de Shopify (panier, statistiques, éditeur)'),
                          ('{{ content_for_layout }}', 'le contenu des pages'),
                          ('{% sections ', 'les sections de l\'éditeur')):
        if element in texte:
            ok('Gabarit principal', 'contient %s — %s' % (element, quoi))
        else:
            bloque('Gabarit principal', 'il manque %s (%s)' % (element, quoi))
    if 'viewport' in texte and 'width=device-width' in texte:
        ok('Affichage téléphone déclaré', 'balise viewport présente')
    else:
        bloque('Affichage téléphone déclaré', 'viewport absent')


# ── 3. modèles JSON ─────────────────────────────────────────────────────────
def types_de_blocs(type_section):
    """Les types de blocs d'une section sont déclarés dans SON schéma — pas dans
    la liste des fichiers. Un bloc « variant_picker » n'a de sens que si la
    section « main-product » le déclare."""
    chemin = os.path.join(THEME, 'sections', type_section + '.liquid')
    if not os.path.isfile(chemin):
        return None
    m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}',
                  lire(chemin), re.S)
    if not m:
        return set()
    try:
        schema = json.loads(m.group(1))
    except ValueError:
        return set()
    return {b.get('type') for b in (schema.get('blocks') or []) if b.get('type')}


def controler_modeles(fichiers):
    sections_dispo = {f.split('/')[-1][:-7] for f in fichiers if f.startswith('sections/')}
    modeles = [f for f in fichiers if f.startswith('templates/') and f.endswith('.json')]
    soucis, total_sections = [], 0
    for modele in sorted(modeles):
        try:
            donnees = json.loads(lire(os.path.join(THEME, modele)))
        except ValueError as e:
            soucis.append('%s : JSON illisible (%s)' % (modele, str(e)[:50]))
            continue
        sections = donnees.get('sections') or {}
        total_sections += len(sections)
        if len(sections) > 25:
            soucis.append('%s : %d sections (limite de l\'éditeur : 25)' % (modele, len(sections)))
        for ident, contenu in sections.items():
            type_section = contenu.get('type')
            if type_section not in sections_dispo:
                soucis.append('%s : section « %s » introuvable' % (modele, type_section))
                continue
            declares = types_de_blocs(type_section)
            if declares is None:
                continue
            for bloc in (contenu.get('blocks') or {}).values():
                type_bloc = bloc.get('type')
                if type_bloc and type_bloc not in declares:
                    soucis.append('%s : le bloc « %s » n\'est pas déclaré par la section « %s »'
                                  % (modele, type_bloc, type_section))
    if soucis:
        for s in soucis:
            bloque('Modèles de page', s)
    else:
        ok('Modèles de page', '%d modèles lisibles, %d sections posées au total, aucune section inconnue'
           % (len(modeles), total_sections))


# ── 4. schémas de section ───────────────────────────────────────────────────
def controler_schemas(fichiers):
    soucis, nb = [], 0
    types_inconnus = set()
    for f in fichiers:
        if not (f.startswith('sections/') and f.endswith('.liquid')):
            continue   # les *-group.json sont des groupes de sections, sans schéma
        texte = lire(os.path.join(THEME, f))
        m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}', texte, re.S)
        if not m:
            soucis.append('%s : aucun schéma (la section n\'apparaîtrait pas dans l\'éditeur)' % f)
            continue
        nb += 1
        try:
            schema = json.loads(m.group(1))
        except ValueError as e:
            soucis.append('%s : schéma illisible (%s)' % (f, str(e)[:50]))
            continue
        if not schema.get('name'):
            soucis.append('%s : nom manquant' % f)
        portees = [('la section', list(schema.get('settings') or []))]
        for bloc in schema.get('blocks') or []:
            portees.append(('le bloc « %s »' % bloc.get('type'), list(bloc.get('settings') or [])))
        for nom_portee, reglages in portees:
            identifiants = [r.get('id') for r in reglages if r.get('id')]
            doublons = {i for i in identifiants if identifiants.count(i) > 1}
            if doublons:
                soucis.append('%s : identifiants en double dans %s : %s' % (f, nom_portee, sorted(doublons)))
        for _nom, reglages in portees:
            for r in reglages:
                if r.get('type') and r['type'] not in TYPES_REGLAGES:
                    types_inconnus.add(r['type'])
    if soucis:
        for s in soucis:
            bloque('Schémas de section', s)
    else:
        ok('Schémas de section', '%d schémas lisibles, identifiants uniques' % nb)
    if types_inconnus:
        attention('Types de réglages', 'à confirmer : ' + ', '.join(sorted(types_inconnus)))


# ── 5. réglages globaux ─────────────────────────────────────────────────────
def controler_reglages():
    schema = json.loads(lire(os.path.join(THEME, 'config', 'settings_schema.json')))
    identifiants = set()
    for groupe in schema:
        for r in groupe.get('settings') or []:
            if r.get('id'):
                identifiants.add(r['id'])
        if not groupe.get('name'):
            attention('Réglages globaux', 'un groupe sans nom')
    donnees = json.loads(lire(os.path.join(THEME, 'config', 'settings_data.json')))
    valeurs = donnees.get('current') or {}
    inconnues = sorted(set(valeurs) - identifiants)
    if inconnues:
        bloque('Réglages globaux', 'clés absentes du schéma : ' + ', '.join(inconnues))
    else:
        ok('Réglages globaux', '%d groupes, %d réglages, %d valeurs enregistrées — toutes déclarées'
           % (len(schema), len(identifiants), len(valeurs)))
    theme_info = next((g for g in schema if 'theme_info' in (g.get('name', '').lower(), g.get('name', ''))), None)
    if theme_info or any('theme_info' in str(g) for g in schema):
        ok('Fiche du thème', 'bloc theme_info présent (nom, version, auteur)')


# ── 6. Liquid : balises et filtres obsolètes ────────────────────────────────
def controler_liquid(fichiers):
    obsoletes = {
        r'\{%-?\s*include\s': 'balise « include » (remplacée par « render »)',
        r'\|\s*img_url\b': 'filtre « img_url » (remplacé par « image_url »)',
        r'\|\s*money_without_currency\b': 'filtre « money_without_currency » '
                                          '(espaces insécables : cassent les prix lus par Google)',
        r'\{\{\s*product\.featured_image\b': 'product.featured_image (remplacé par featured_media)',
    }
    trouves = []
    for f in fichiers:
        texte = lire(os.path.join(THEME, f))
        texte = re.sub(r'\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}', '', texte, flags=re.S)
        for motif, quoi in obsoletes.items():
            for m in re.finditer(motif, texte):
                trouves.append('%s:%d → %s' % (f, texte[:m.start()].count('\n') + 1, quoi))
    if trouves:
        for t in trouves:
            attention('Liquid obsolète', t)
    else:
        ok('Liquid obsolète', 'aucune balise ni filtre déprécié dans les %d fichiers' % len(fichiers))


# ── 7. images : largeur demandée et CDN ─────────────────────────────────────
def controler_images(fichiers):
    soucis, nb, sans_largeur = [], 0, []
    for f in fichiers:
        texte = lire(os.path.join(THEME, f))
        for m in re.finditer(r'\|\s*image_url\s*:?([^|}\n]*)', texte):
            nb += 1
            if 'width' not in m.group(1):
                sans_largeur.append('%s:%d' % (f, texte[:m.start()].count('\n') + 1))
    if sans_largeur:
        attention('Images du CDN Shopify', 'appelées sans largeur (photo d\'origine servie en pleine '
                                           'taille) : ' + ', '.join(sans_largeur[:6]))
    else:
        ok('Images du CDN Shopify', '%d appels, tous avec une largeur demandée' % nb)


# ── 8. éditeur : shopify_attributes ─────────────────────────────────────────
def controler_editeur(fichiers):
    sections_avec_blocs, sans = 0, []
    for f in fichiers:
        if not f.startswith('sections/'):
            continue
        texte = lire(os.path.join(THEME, f))
        if '{%- for block in section.blocks' in texte or '{% for block in section.blocks' in texte:
            sections_avec_blocs += 1
            if 'shopify_attributes' not in texte:
                sans.append(f)
    if sans:
        attention('Sélection dans l\'éditeur', 'sections à blocs sans shopify_attributes : ' + ', '.join(sans))
    else:
        ok('Sélection dans l\'éditeur', '%d sections à blocs portent shopify_attributes' % sections_avec_blocs)


# ── 9. traductions ──────────────────────────────────────────────────────────
def controler_traductions():
    locale_par_defaut = [f for f in os.listdir(os.path.join(THEME, 'locales')) if f.endswith('.default.json')]
    if locale_par_defaut == ['fr.default.json']:
        ok('Langue par défaut', 'fr.default.json — le français est la référence')
    else:
        attention('Langue par défaut', 'locales marquées par défaut : %s' % locale_par_defaut)

    fr = json.loads(lire(os.path.join(THEME, 'locales', 'fr.default.json')))
    ar = json.loads(lire(os.path.join(THEME, 'locales', 'ar.json')))

    def aplatir(d, prefixe=''):
        """Toutes les clés valides : les feuilles, ET les branches plurielles.

        Shopify range les pluriels sous la même clé — search.results contient
        {\"one\": …, \"other\": …} — et « {{ 'search.results' | t: count: n }} »
        est l'usage correct. Ne compter que les feuilles ferait croire à des
        clés manquantes (faux positif corrigé le 5 octobre 2026).
        """
        cles = set()
        for k, v in d.items():
            if isinstance(v, dict):
                if 'one' in v or 'other' in v:
                    cles.add(prefixe + k)
                cles |= aplatir(v, prefixe + k + '.')
            else:
                cles.add(prefixe + k)
        return cles

    cles_fr, cles_ar = aplatir(fr), aplatir(ar)
    manquantes = sorted(cles_fr - cles_ar)
    if manquantes:
        attention('Traductions', '%d clé(s) absentes en arabe : %s'
                  % (len(manquantes), ', '.join(manquantes[:6])))
    else:
        ok('Traductions', '%d clés, présentes dans les deux langues' % len(cles_fr))
    return cles_fr


# ── 10. clés utilisées dans les fichiers ────────────────────────────────────
def controler_cles(fichiers, cles_fr):
    utilisees, manquantes = set(), set()
    for f in fichiers:
        for m in re.finditer(r"'([a-z0-9_]+\.[a-z0-9_.]+)'\s*\|\s*t\b", lire(os.path.join(THEME, f))):
            utilisees.add(m.group(1))
    for cle in utilisees:
        if cle not in cles_fr:
            manquantes.add(cle)
    if manquantes:
        bloque('Clés de traduction', 'utilisées mais absentes du français : ' + ', '.join(sorted(manquantes)))
    else:
        ok('Clés de traduction', '%d clés utilisées, toutes définies' % len(utilisees))


# ── 11. poids et limites Shopify ────────────────────────────────────────────
def controler_poids():
    total = 0
    plus_gros = []
    for base, _d, fs in os.walk(THEME):
        for f in fs:
            p = os.path.join(base, f)
            t = os.path.getsize(p)
            total += t
            plus_gros.append((t, os.path.relpath(p, THEME)))
    plus_gros.sort(reverse=True)
    if os.path.isfile(ZIP):
        taille_zip = os.path.getsize(ZIP)
        if taille_zip > 50 * 1048576:
            bloque('Poids du fichier ZIP', '%.1f Mo — la limite de Shopify est de 50 Mo' % (taille_zip / 1048576))
        else:
            ok('Poids du fichier ZIP', '%.1f Mo (limite Shopify : 50 Mo)' % (taille_zip / 1048576))
    trop_gros = [(t, p) for t, p in plus_gros if t > 20 * 1048576]
    if trop_gros:
        bloque('Fichier trop lourd', ', '.join('%s (%.1f Mo)' % (p, t / 1048576) for t, p in trop_gros))
    else:
        ok('Aucun fichier trop lourd', 'le plus gros : %s (%.0f Ko), limite Shopify : 20 Mo'
           % (plus_gros[0][1], plus_gros[0][0] / 1024))
    return total, plus_gros


# ── rapport ─────────────────────────────────────────────────────────────────
def main():
    fichiers = fichiers_du_theme()
    liquides = controler_structure(fichiers)
    controler_gabarit()
    controler_modeles(fichiers)
    controler_schemas(fichiers)
    controler_reglages()
    controler_liquid(liquides)
    controler_images(liquides)
    controler_editeur(liquides)
    cles = controler_traductions()
    controler_cles(liquides, cles)
    total, plus_gros = controler_poids()

    print('\n' + '═' * 74)
    print('  CONFORMITÉ SHOPIFY — %d fichiers, %.1f Mo' % (len(fichiers), total / 1048576))
    print('═' * 74)
    for titre, detail in normal:
        print('  ✓ %-30s %s' % (titre, detail))
    for titre, detail in avertissements:
        print('  ! %-30s %s' % (titre, detail))
    for titre, detail in bloquants:
        print('  ✗ %-30s %s' % (titre, detail))

    print('\n  Les 6 plus gros fichiers :')
    for t, p in plus_gros[:6]:
        print('     %7.0f Ko  %s' % (t / 1024, p))

    print('\n  %d point(s) conforme(s) · %d avertissement(s) · %d point(s) bloquant(s)'
          % (len(normal), len(avertissements), len(bloquants)))
    if not bloquants:
        print('\n  ✓ Le thème peut être importé dans Shopify sans réserve bloquante.')
    return 1 if bloquants else 0


if __name__ == '__main__':
    if '--json' in sys.argv:
        # même contrôle, mais lisible par un autre programme (le rapport)
        sortie = sys.stdout
        sys.stdout = io.StringIO()
        main()
        sys.stdout = sortie
        print(json.dumps({'conformes': [{'titre': t, 'detail': d} for t, d in normal],
                          'avertissements': [{'titre': t, 'detail': d} for t, d in avertissements],
                          'bloquants': [{'titre': t, 'detail': d} for t, d in bloquants]},
                         ensure_ascii=False))
        sys.exit(0)
    sys.exit(main())
