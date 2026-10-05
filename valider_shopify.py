#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle « comme à l'import Shopify » du thème LLUFAN.

Vérifie ce que le validateur de balises ne regarde pas :
  1. chaque type de section utilisé dans un modèle ou un groupe de sections
     existe bien dans sections/ (et un groupe n'utilise pas une section prévue
     pour un autre emplacement) ;
  2. chaque type de bloc existe dans le schéma de sa section ;
  3. chaque réglage écrit dans un modèle (section ou bloc) est déclaré dans le
     schéma correspondant ;
  4. les clés de config/settings_data.json existent dans le schéma des réglages ;
  5. chaque clé de traduction « ... | t » existe dans locales/fr.default.json.

Ce sont les cinq causes d'avertissement ou de rendu vide à l'import.

Usage : python3 valider_shopify.py
"""
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent / 'theme'
TYPES_SHOPIFY = {'@app'}          # types natifs : aucune section à fournir


def charger_schema(chemin):
    """Schéma d'une section Liquid (ou None si absent/illisible)."""
    src = chemin.read_text(encoding='utf-8')
    m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}', src, flags=re.S)
    if not m:
        return None
    return json.loads(m.group(1))


def ids_reglages(liste):
    return {s.get('id') for s in liste or [] if s.get('id')}


def main():
    problemes = []
    infos = []

    # --- schémas de toutes les sections -----------------------------------
    schemas = {}
    for p in sorted((RACINE / 'sections').glob('*.liquid')):
        s = charger_schema(p)
        if s is None:
            problemes.append('%s : pas de schéma lisible' % p.name)
            continue
        schemas[p.stem] = s

    # --- 1. modèles et groupes --------------------------------------------
    modeles = sorted((RACINE / 'templates').rglob('*.json')) + sorted((RACINE / 'sections').glob('*-group.json'))
    for p in modeles:
        try:
            donnees = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            problemes.append('%s : JSON illisible (%s)' % (p.name, e))
            continue
        sections = donnees.get('sections', {})
        for cle, section in sections.items():
            typ = section.get('type')
            nom = p.relative_to(RACINE).as_posix()
            if typ not in schemas:
                if typ not in TYPES_SHOPIFY:
                    problemes.append('%s → section « %s » : type « %s » sans fichier sections/%s.liquid'
                                     % (nom, cle, typ, typ))
                continue
            schema = schemas[typ]
            # emplacement déclaré
            if schema.get('enabled_on'):
                groupes = schema['enabled_on'].get('groups') or []
                if groupes and not nom.endswith('-group.json'):
                    problemes.append('%s → « %s » (%s) est réservé aux groupes %s'
                                     % (nom, cle, typ, groupes))
                if not groupes and nom.endswith('-group.json'):
                    problemes.append('%s → « %s » (%s) n\'est pas prévu pour un groupe'
                                     % (nom, cle, typ))
            # --- 3a. réglages de section
            declares = ids_reglages(schema.get('settings'))
            for r in (section.get('settings') or {}):
                if r not in declares and r != 'color_scheme':
                    problemes.append('%s → %s : réglage « %s » absent du schéma' % (nom, typ, r))
            # --- 2/3b. blocs
            types_blocs = {b.get('type'): b for b in schema.get('blocks') or []}
            for icle, bloc in (section.get('blocks') or {}).items():
                tb = bloc.get('type')
                if tb not in types_blocs:
                    if types_blocs:
                        problemes.append('%s → %s, bloc « %s » : type « %s » non déclaré'
                                         % (nom, typ, icle, tb))
                    continue
                declares_bloc = ids_reglages(types_blocs[tb].get('settings'))
                for r in (bloc.get('settings') or {}):
                    if r not in declares_bloc:
                        problemes.append('%s → %s, bloc « %s » (%s) : réglage « %s » absent du schéma'
                                         % (nom, typ, icle, tb, r))
            # ordre des blocs : toutes les clés présentes ?
            for k in (section.get('block_order') or []):
                if k not in (section.get('blocks') or {}):
                    problemes.append('%s → %s : block_order cite « %s » qui n\'existe pas' % (nom, typ, k))
            for k in (section.get('blocks') or {}):
                if section.get('block_order') and k not in section['block_order']:
                    problemes.append('%s → %s : bloc « %s » absent de block_order' % (nom, typ, k))
        infos.append('%s : %d section(s)' % (p.relative_to(RACINE).as_posix(), len(sections)))

    # --- 1b. {{ section '…' }} dans le Liquid -----------------------------
    for p in sorted(RACINE.rglob('*.liquid')):
        for m in re.finditer(r"\{%-?\s*section\s+'([^']+)'", p.read_text(encoding='utf-8')):
            if not (RACINE / 'sections' / ('%s.liquid' % m.group(1))).exists():
                problemes.append('%s : {{ section \'%s\' }} sans fichier correspondant'
                                 % (p.relative_to(RACINE).as_posix(), m.group(1)))

    # --- 4. réglages généraux --------------------------------------------
    schema_global = json.loads((RACINE / 'config' / 'settings_schema.json').read_text(encoding='utf-8'))
    globales = set()
    for groupe in schema_global:
        globales |= ids_reglages(groupe.get('settings'))
    donnees = json.loads((RACINE / 'config' / 'settings_data.json').read_text(encoding='utf-8'))
    for cle in donnees.get('current', {}):
        if cle not in globales:
            problemes.append('settings_data.json : « %s » absent du schéma des réglages' % cle)

    # --- 5. clés de traduction -------------------------------------------
    locale = json.loads((RACINE / 'locales' / 'fr.default.json').read_text(encoding='utf-8'))

    def existe(cle):
        noeud = locale
        for partie in cle.split('.'):
            if not isinstance(noeud, dict) or partie not in noeud:
                return False
            noeud = noeud[partie]
        return True

    utilisees = {}
    for p in sorted(RACINE.rglob('*.liquid')):
        src = p.read_text(encoding='utf-8')
        for m in re.finditer(r"'([a-z0-9_]+(?:\.[a-z0-9_]+)+)'\s*\|\s*t\b", src):
            utilisees.setdefault(m.group(1), set()).add(p.relative_to(RACINE).as_posix())
    manquantes = {c: v for c, v in utilisees.items() if not existe(c)}
    for c, fichiers in sorted(manquantes.items()):
        problemes.append('traduction manquante : « %s » (utilisée dans %s)'
                         % (c, ', '.join(sorted(fichiers))))

    # --- 6. layout --------------------------------------------------------
    layout = (RACINE / 'layout' / 'theme.liquid').read_text(encoding='utf-8')
    for attendu in ('{{ content_for_header }}', '{{ content_for_layout }}'):
        if attendu not in layout:
            problemes.append('layout/theme.liquid : %s absent' % attendu)

    # --- bilan ------------------------------------------------------------
    print('• Sections : %d fichiers de schéma' % len(schemas))
    print('• Modèles et groupes contrôlés : %d' % len(modeles))
    print('• Clés de traduction utilisées : %d (présentes : %d)'
          % (len(utilisees), len(utilisees) - len(manquantes)))
    print('• Anomalies : %d' % len(problemes))
    for x in problemes[:40]:
        print('    -', x)
    return 1 if problemes else 0


if __name__ == '__main__':
    sys.exit(main())
