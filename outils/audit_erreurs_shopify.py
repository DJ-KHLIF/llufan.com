#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLUFAN — contrôle des règles de validation de Shopify
====================================================

Ces règles ne sont PAS visibles à l'œil nu, mais Shopify refuse les fichiers
qui les enfreignent — et quand des fichiers sont refusés, les pages du thème
retombent sur le 404 dans l'éditeur. Apprises à nos dépens le 5 octobre 2026
(journal de l'intégration GitHub : 19 fichiers refusés, 36 échecs).

Ce contrôle vérifie, avant tout envoi :

  1. Liquid — aucun filtre à l'intérieur d'une balise
     ({% form 'contact', id: 'x' | append: y %} → refusé par Shopify) ;

  2. Noms — 25 caractères au maximum pour le nom d'une section, d'un bloc
     ou d'un préréglage ;

  3. Décimales — un réglage numérique (range) n'accepte qu'UNE décimale
     pour default, min, max et step ;

  4. Adresses — un réglage de type « url » doit être vide, ou commencer par
     / http shopify:// # mailto: tel: whatsapp:.

Usage :
    python3 llufan/audit_erreurs_shopify.py
Code de sortie : 0 si tout est conforme, 1 sinon.
"""

import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(ICI, 'theme')
NOM_LIMITE = 25

erreurs = []
avertissements = []


# ───────────────────────────────────────────────────────────────────────────
def fichiers_liquid():
    for dossier in ('layout', 'sections', 'snippets', 'templates'):
        base = os.path.join(THEME, dossier)
        for r, _, fs in os.walk(base):
            for f in fs:
                if f.endswith('.liquid'):
                    yield os.path.join(r, f)


def schema_de(chemin):
    s = io.open(chemin, encoding='utf-8').read()
    m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', s, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


# ── 1. filtres à l'intérieur d'une balise ──────────────────────────────────
BALISES_SANS_FILTRE = ('form', 'render', 'include', 'section', 'cycle', 'paginate')


def controle_1_liquid():
    for p in fichiers_liquid():
        for no, ligne in enumerate(io.open(p, encoding='utf-8'), 1):
            for m in re.finditer(r'{%-?\s*(form|render|include|section|cycle|paginate)\b(.*?)-?%}',
                                 ligne, re.S):
                balise, contenu = m.group(1), m.group(2)
                if '|' in contenu:
                    erreurs.append(
                        "1. %s ligne %d : filtre (|) à l'intérieur de {% %s … %} — Shopify refuse. "
                        "Calculer la valeur avant, avec {%% assign %%}."
                        % (os.path.relpath(p, THEME), no, balise))


# ── 2. noms trop longs ─────────────────────────────────────────────────────
def controle_2_noms():
    base = os.path.join(THEME, 'sections')
    for f in sorted(os.listdir(base)):
        if not f.endswith('.liquid'):
            continue
        schema = schema_de(os.path.join(base, f))
        if schema is None:
            continue
        for b in (schema if isinstance(schema, list) else [schema]):
            if not isinstance(b, dict):
                continue
            if isinstance(b.get('name'), str) and len(b['name']) > NOM_LIMITE:
                erreurs.append("2. sections/%s : nom de section « %s » = %d caractères (max 25)"
                               % (f, b['name'], len(b['name'])))
            for blk in (b.get('blocks') or []):
                if isinstance(blk, dict) and isinstance(blk.get('name'), str) \
                        and len(blk['name']) > NOM_LIMITE:
                    erreurs.append("2. sections/%s : nom du bloc « %s » (« %s ») = %d caractères (max 25)"
                                   % (f, blk.get('type'), blk['name'], len(blk['name'])))
            for pre in (b.get('presets') or []):
                if isinstance(pre, dict) and isinstance(pre.get('name'), str) \
                        and len(pre['name']) > NOM_LIMITE:
                    erreurs.append("2. sections/%s : nom de préréglage « %s » = %d caractères (max 25)"
                                   % (f, pre['name'], len(pre['name'])))


# ── 3. décimales ───────────────────────────────────────────────────────────
def controle_3_decimales():
    p = os.path.join(THEME, 'config', 'settings_schema.json')
    schema = json.load(io.open(p, encoding='utf-8'))
    for i, g in enumerate(schema, 1):
        if not isinstance(g, dict):
            continue
        for st in (g.get('settings') or []):
            if not isinstance(st, dict) or st.get('type') != 'range':
                continue
            for cle in ('default', 'min', 'max', 'step'):
                v = st.get(cle)
                if isinstance(v, float) and len(str(v).split('.')[-1]) > 1:
                    erreurs.append("3. settings_schema.json groupe %d : « %s » %s = %s "
                                   "(plus d'une décimale)" % (i, st.get('id'), cle, v))


# ── 4. adresses ────────────────────────────────────────────────────────────
def adresse_valide(v):
    return (not isinstance(v, str)) or v == '' or v.startswith(
        ('/', 'http', 'shopify://', '#', 'mailto:', 'tel:', 'whatsapp:'))


def controle_4_adresses():
    def types_url(chemin):
        schema = schema_de(chemin)
        section, blocs = {}, {}
        if schema is None:
            return section, blocs
        for b in (schema if isinstance(schema, list) else [schema]):
            if not isinstance(b, dict):
                continue
            for st in (b.get('settings') or []):
                if isinstance(st, dict) and st.get('id'):
                    section[st['id']] = st.get('type')
            for blk in (b.get('blocks') or []):
                if isinstance(blk, dict) and blk.get('type'):
                    blocs[blk['type']] = {st.get('id'): st.get('type')
                                          for st in (blk.get('settings') or [])
                                          if isinstance(st, dict) and st.get('id')}
        return section, blocs

    for dossier in ('templates', 'sections'):
        base = os.path.join(THEME, dossier)
        for r, _, fs in os.walk(base):
            for f in sorted(fs):
                if not f.endswith('.json'):
                    continue
                p = os.path.join(r, f)
                try:
                    d = json.load(io.open(p, encoding='utf-8'))
                except Exception:
                    continue
                if not isinstance(d, dict):
                    continue
                rel = os.path.relpath(p, THEME)

                def verifier(dictionnaire, types, ou):
                    for k, v in dictionnaire.items():
                        if types.get(k) == 'url' and not adresse_valide(v):
                            erreurs.append("4. %s · %s · « %s » = « %s » : adresse invalide"
                                           "(il manque le « / » ou le domaine)" % (rel, ou, k, v))

                for sid, sec in (d.get('sections') or {}).items():
                    if not isinstance(sec, dict):
                        continue
                    chemin = os.path.join(THEME, 'sections', '%s.liquid' % sec.get('type'))
                    if not os.path.exists(chemin):
                        continue
                    ts, tb = types_url(chemin)
                    verifier(sec.get('settings') or {}, ts, sid)
                    for _, blk in (sec.get('blocks') or {}).items():
                        if isinstance(blk, dict):
                            verifier(blk.get('settings') or {},
                                     tb.get(blk.get('type'), {}), sid)

    # réglages globaux
    p = os.path.join(THEME, 'config', 'settings_data.json')
    try:
        data = json.load(io.open(p, encoding='utf-8'))
        schema = json.load(io.open(os.path.join(THEME, 'config', 'settings_schema.json'),
                                  encoding='utf-8'))
    except Exception:
        return
    types = {}
    for g in schema:
        if isinstance(g, dict):
            for st in (g.get('settings') or []):
                if isinstance(st, dict) and st.get('id'):
                    types[st['id']] = st.get('type')
    cur = data.get('current')
    if isinstance(cur, dict):
        for k, v in cur.items():
            if types.get(k) == 'url' and not adresse_valide(v):
                erreurs.append("4. config/settings_data.json · « %s » = « %s » : adresse invalide"
                               % (k, v))


# ───────────────────────────────────────────────────────────────────────────
def main():
    print("LLUFAN — contrôle des règles de validation de Shopify")
    print("")
    controle_1_liquid()
    print("  1. filtres dans les balises           : %s" %
          ("aucun ✓" if not any(e.startswith('1.') for e in erreurs) else "PROBLÈMES"))
    controle_2_noms()
    print("  2. noms de 25 caractères maximum      : %s" %
          ("tous conformes ✓" if not any(e.startswith('2.') for e in erreurs) else "PROBLÈMES"))
    controle_3_decimales()
    print("  3. une décimale pour les nombres      : %s" %
          ("conforme ✓" if not any(e.startswith('3.') for e in erreurs) else "PROBLÈMES"))
    controle_4_adresses()
    print("  4. adresses valides (/ http shopify:) : %s" %
          ("toutes valides ✓" if not any(e.startswith('4.') for e in erreurs) else "PROBLÈMES"))
    print("")
    if erreurs:
        print("  %d point(s) à corriger :" % len(erreurs))
        for e in erreurs[:40]:
            print("   ✗", e)
        print("")
        print("  → lancer : python3 llufan/corriger_validation_shopify.py")
        return 1
    print("  ✓ Aucune erreur : le thème passe les règles que Shopify applique à l'envoi.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
