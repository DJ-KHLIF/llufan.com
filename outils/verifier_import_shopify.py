#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle « prêt pour Shopify » : vérifie l'ARCHIVE, pas le dossier.

Les autres contrôles regardent `theme/`. Celui-ci regarde exactement ce qu'on
téléverse dans Shopify : `LLUFAN-theme-Shopify.zip`. Il l'ouvre, l'extrait
dans un dossier temporaire et vérifie ce qui ferait échouer — ou rendrait une
page vide — à l'import :

  1. la structure attendue (les sept dossiers, `layout/theme.liquid`,
     `config/settings_schema.json`, la langue par défaut) ;
  2. chaque `{% render %}` a bien son snippet, chaque `{% section %}` sa
     section, chaque groupe de sections ses sections ;
  3. chaque fichier d'`assets/` cité en toutes lettres existe bien dans
     l'archive (police, feuille de style, script, visuel de démonstration) ;
  4. tous les fichiers JSON sont lisibles ;
  5. aucun chemin absolu de la machine de travail (`/home/user`, `file://`) :
     dans Shopify, un tel chemin ne mène nulle part ;
  6. les fichiers d'import qui accompagnent le thème (produits, collections,
     traductions) sont présents et ont les bonnes colonnes ;
  7. rien de superflu (dossier `__MACOSX`, `.DS_Store`, `node_modules`).

Usage : python3 verifier_import_shopify.py
"""
import csv
import io
import json
import os
import re
import sys
import tempfile
import zipfile

RACINE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(RACINE, 'LLUFAN-theme-Shopify.zip')

DOSSIERS = ('assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates')
EXTENSIONS_ASSET = ('.css', '.js', '.json', '.jpg', '.jpeg', '.png', '.webp', '.svg',
                    '.woff2', '.woff', '.ttf', '.gif', '.mp4', '.webm')
# Adresses externes qui ont une raison d'être dans le thème. Tout autre domaine
# est signalé : c'est ainsi qu'on repère un chemin laissé par la machine de
# travail ou une dépendance oubliée.
DOMAINES_ATTENDUS = ('youtube.com', 'youtu.be', 'vimeo.com', 'facebook.com', 'pinterest.com',
                     'wa.me', 'shopify.dev', 'shopify.com',
                     'schema.org')   # le vocabulaire des données structurées :
                                     # il est exigé, ce n'est pas un lien sortant

# Fichiers d'import livrés avec le thème : entête attendue (les premières colonnes).
IMPORTS = {
    'LLUFAN-DEMO-produits.csv': ['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags'],
    'LLUFAN-DEMO-collections.csv': ['Handle', 'Title', 'Body (HTML)', 'Published'],
    'LLUFAN-DEMO-traductions-ar.csv': ['Type', 'Ressource (handle)', 'Champ'],
    'LLUFAN-produit-Nomad-a-importer.csv': ['Handle', 'Title'],
}


def lire_texte(chemin):
    """Le texte d'un fichier. Les fichiers de langue de Shopify commencent par un
    commentaire « auto-generated » : json.loads le refuse, alors on le retire
    (voir audit_conformite_shopify.py, même raison)."""
    texte = io.open(chemin, encoding='utf-8', errors='replace').read()
    if texte.startswith('/*'):
        fin = texte.find('*/')
        if fin != -1:
            return texte[fin + 2:].lstrip()
    return texte


def controler_arborescence(tmp, problemes):
    for d in DOSSIERS:
        if not os.path.isdir(os.path.join(tmp, d)):
            problemes.append('dossier absent : %s/' % d)
    for f, quoi in (('layout/theme.liquid', 'le gabarit principal'),
                    ('config/settings_schema.json', 'les réglages du thème'),
                    ('config/settings_data.json', 'les réglages enregistrés')):
        if not os.path.isfile(os.path.join(tmp, f)):
            problemes.append('%s (%s) est absent de l\'archive' % (f, quoi))
    locales = [f for f in os.listdir(os.path.join(tmp, 'locales')) if f.endswith('.json')]
    if not any(f.endswith('.default.json') for f in locales):
        problemes.append('aucune langue par défaut (*.default.json) dans locales/')
    return locales


def controler_references(tmp, problemes):
    """Chaque snippet, section et asset cité doit exister dans l'archive."""
    liquides, json_fichiers = [], []
    for base, _d, fichiers in os.walk(tmp):
        for f in fichiers:
            chemin = os.path.join(base, f)
            if f.endswith('.liquid'):
                liquides.append(chemin)
            elif f.endswith('.json'):
                json_fichiers.append(chemin)

    snippets = {f[:-len('.liquid')] for f in os.listdir(os.path.join(tmp, 'snippets'))
                if f.endswith('.liquid')}
    sections = {f.split('.')[0] for f in os.listdir(os.path.join(tmp, 'sections'))}
    assets = set(os.listdir(os.path.join(tmp, 'assets')))

    for chemin in liquides + json_fichiers:
        texte = lire_texte(chemin)
        relatif = os.path.relpath(chemin, tmp)
        for nom in re.findall(r"{%-?\s*(?:render|include)\s+'([^']+)'", texte):
            if nom not in snippets:
                problemes.append('%s : snippet « %s » introuvable' % (relatif, nom))
        for nom in re.findall(r"{%-?\s*section\s+'([^']+)'", texte):
            if nom not in sections:
                problemes.append('%s : section « %s » introuvable' % (relatif, nom))
        for nom in re.findall(r"{%-?\s*sections\s+'([^']+)'", texte):
            if nom not in sections:
                problemes.append('%s : groupe de sections « %s » introuvable' % (relatif, nom))

    # Fichiers d'assets cités en toutes lettres. Le thème les appelle de deux
    # façons : par un filtre (« 'theme.css' | asset_url ») ou directement dans
    # une balise (src="{{ 'llufan-nomad-coussin.jpg' | asset_img_url: '1200x' }}").
    # Dans les deux cas, le fichier doit être dans assets/ — sinon la page
    # s'affiche sans style, sans police ou sans image, sans message d'erreur.
    motif = re.compile(r"'([A-Za-z0-9._-]+\.(?:css|js|jpeg|jpg|png|webp|svg|woff2|woff|json))'"
                       r"(\s*\|\s*asset[_a-z]*_?url[^}]*)?")
    for chemin in liquides + json_fichiers:
        texte = lire_texte(chemin)
        relatif = os.path.relpath(chemin, tmp)
        for nom, filtre in motif.findall(texte):
            est_appele_comme_asset = bool(filtre) or nom in assets or nom.startswith('llufan-') \
                or nom.startswith('demo-') or nom in (
                    'theme.css', 'theme.js', 'fraunces-latin.woff2', 'jost-latin.woff2',
                    'fraunces-latin-ext.woff2', 'jost-latin-ext.woff2')
            if est_appele_comme_asset and nom not in assets:
                problemes.append('%s : asset « %s » absent de l\'archive' % (relatif, nom))


def controler_json_et_chemins(tmp, problemes):
    for base, _d, fichiers in os.walk(tmp):
        for f in fichiers:
            chemin = os.path.join(base, f)
            relatif = os.path.relpath(chemin, tmp)
            if f.endswith('.json'):
                try:
                    json.loads(lire_texte(chemin))
                except ValueError as e:
                    problemes.append('%s : JSON illisible (%s)' % (relatif, str(e)[:60]))
            if f.endswith(('.liquid', '.json', '.js', '.css')):
                texte = lire_texte(chemin)
                for motif, quoi in (('/home/user', 'chemin de la machine de travail'),
                                    ('file://', 'adresse de fichier local')):
                    if motif in texte:
                        problemes.append('%s : %s (« %s »)' % (relatif, quoi, motif))
                for domaine in set(re.findall(r'https?://([a-z0-9.-]+\.[a-z]{2,})', texte)):
                    if not any(domaine.endswith(a) for a in DOMAINES_ATTENDUS):
                        problemes.append('%s : adresse externe inattendue (%s)' % (relatif, domaine))


def controler_imports(problemes, avertissements):
    print('\n  Fichiers d\'import livrés avec le thème :')
    for nom, entete in IMPORTS.items():
        chemin = os.path.join(RACINE, nom)
        if not os.path.isfile(chemin):
            problemes.append('fichier d\'import absent : %s' % nom)
            continue
        with io.open(chemin, encoding='utf-8-sig', newline='') as f:
            lignes = list(csv.reader(f))
        trouvee, nombre = lignes[0] if lignes else [], len(lignes) - 1
        manquantes = [c for c in entete if c not in trouvee]
        if manquantes:
            problemes.append('%s : colonnes manquantes (%s)' % (nom, ', '.join(manquantes)))
        vides = sum(1 for l in lignes[1:] if l and not l[0].strip())
        if vides:
            avertissements.append('%s : %d ligne(s) sans identifiant' % (nom, vides))
        print('     %-42s %5d lignes · colonnes %s' % (
            nom, nombre, 'conformes' if not manquantes else 'À REVOIR'))


def controler_superflu(tmp, avertissements):
    with zipfile.ZipFile(ARCHIVE) as z:
        noms = z.namelist()
    for nom in noms:
        if '__MACOSX' in nom or nom.endswith('.DS_Store') or 'node_modules' in nom:
            avertissements.append('élément superflu dans l\'archive : %s' % nom)
    return noms


def main():
    if not os.path.isfile(ARCHIVE):
        print('Archive absente : %s' % ARCHIVE)
        return 1
    print('Archive : %s (%.1f Mo, %d entrées)'
          % (os.path.basename(ARCHIVE), os.path.getsize(ARCHIVE) / 1048576,
             len(zipfile.ZipFile(ARCHIVE).namelist())))
    problemes, avertissements = [], []
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(ARCHIVE) as z:
            z.extractall(tmp)
        locales = controler_arborescence(tmp, problemes)
        controler_references(tmp, problemes)
        controler_json_et_chemins(tmp, problemes)
        print('  Langues : %s' % ', '.join(locales))
        for d in DOSSIERS:
            chemin = os.path.join(tmp, d)
            nombre = len(os.listdir(chemin)) if os.path.isdir(chemin) else 0
            print('  %-11s %3d fichier(s)' % (d + '/', nombre))
    controler_imports(problemes, avertissements)
    controler_superflu(None, avertissements)

    if avertissements:
        print('\n  À savoir (sans conséquence à l\'import) :')
        for a in avertissements:
            print('     · %s' % a)
    if problemes:
        print('\n  ✗ %d problème(s) — à corriger avant de téléverser :' % len(problemes))
        for p in problemes:
            print('     · %s' % p)
        return 1
    print('\n  ✓ Le thème est prêt à être téléversé dans Shopify, tel quel.')
    print('    Boutique en ligne → Thèmes → Ajouter un thème → Importer un fichier ZIP.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
