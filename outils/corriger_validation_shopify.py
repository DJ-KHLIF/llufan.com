#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLUFAN — corrige les erreurs que Shopify a signalées à l'envoi du thème
=======================================================================

Source : journal de l'intégration GitHub du 5 octobre 2026, 17h31
(« 127 réussite, 0 avertissement, 36 échec — 19 fichiers n'ont pas été
enregistrés »). Un thème dont des fichiers sont refusés retombe sur la page
404 dans l'éditeur : c'est ce qui donnait l'impression que « rien ne se
charge ».

Les quatre familles d'erreurs, et ce que fait ce script :

  1. Liquid — un filtre était utilisé à l'intérieur d'une balise :
        {% form 'contact', id: 'commande-formulaire-' | append: cle %}
     Shopify refuse (ligne 77 de forme-commande.liquid). → on calcule la
     valeur AVANT, avec {% assign %}, puis on la passe telle quelle.

  2. Noms trop longs — la limite de Shopify est de 25 caractères pour le
     nom d'une section et d'un bloc :
        « Quantité et ajout au panier » (27), « Commande (paiement à la
        livraison) » (34), « Contact (WhatsApp et e-mail) » (28). → renommés.

  3. Décimales — un réglage de type « range » n'accepte qu'une décimale :
        step 0.05, min 0.75, max 1.125, step 0.0625, default 0.875.
     → arrondis à une décimale, dans le schéma ET dans les valeurs
     enregistrées (settings_data.json), sans changer le rendu.

  4. Adresses — un réglage de type « url » exige une adresse valide :
        « collections/allaitement », « pages/faq »… (sans « / » initial).
     → toutes préfixées par « / ». (Une adresse vide reste acceptée.)

Le script est sans danger : il n'écrit que ce qu'il annonce, et se relance
sans rien casser (idempotent). Après lui, lancer :
    python3 llufan/audit_erreurs_shopify.py     (contrôle)
    bash llufan/refaire_archives.sh             (nouvelles archives)
"""

import io
import json
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'theme')
NOM_LIMITE = 25

rapport = []


def dire(txt):
    print(txt)
    rapport.append(txt)


# ───────────────────────────────────────────────────────────────────────────
#  1. Liquid : filtre à l'intérieur d'une balise
# ───────────────────────────────────────────────────────────────────────────
def corriger_liquid():
    p = os.path.join(RACINE, 'snippets', 'forme-commande.liquid')
    s = io.open(p, encoding='utf-8').read()
    avant = "{%- form 'contact', class: 'commande', id: 'commande-formulaire-' | append: cle -%}"
    apres = ("{%- assign id_formulaire_commande = 'commande-formulaire-' | append: cle -%}\n"
             "    {%- form 'contact', class: 'commande', id: id_formulaire_commande -%}")
    if avant in s:
        s = s.replace(avant, apres, 1)
        io.open(p, 'w', encoding='utf-8').write(s)
        dire("  ✓ forme-commande.liquid : le filtre est calculé avant la balise (ligne 77)")
    else:
        dire("  · forme-commande.liquid : déjà corrigé")


# ───────────────────────────────────────────────────────────────────────────
#  2. Noms de sections et de blocs : 25 caractères au maximum
# ───────────────────────────────────────────────────────────────────────────
RENOMMAGES = {
    "Quantité et ajout au panier": "Quantité et achat",
    "Commande (paiement à la livraison)": "Commande à la livraison",
    "Contact (WhatsApp et e-mail)": "Contact et WhatsApp",
}


def schema_de(chemin):
    s = io.open(chemin, encoding='utf-8').read()
    m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', s, re.S)
    if not m:
        return None, None
    try:
        return json.loads(m.group(1)), s
    except Exception:
        return None, s


def noms_trop_longs(schema):
    """renvoie les noms de plus de 25 caractères (section, blocs, préréglages)"""
    trouves = []
    for b in (schema if isinstance(schema, list) else [schema]):
        if not isinstance(b, dict):
            continue
        if isinstance(b.get('name'), str) and len(b['name']) > NOM_LIMITE:
            trouves.append(b['name'])
        for blk in (b.get('blocks') or []):
            if isinstance(blk, dict) and isinstance(blk.get('name'), str) and len(blk['name']) > NOM_LIMITE:
                trouves.append(blk['name'])
        for pre in (b.get('presets') or []):
            if isinstance(pre, dict) and isinstance(pre.get('name'), str) and len(pre['name']) > NOM_LIMITE:
                trouves.append(pre['name'])
    return trouves


def raccourcir(nom):
    """renommage choisi si connu, sinon coupe propre au mot"""
    if nom in RENOMMAGES:
        return RENOMMAGES[nom]
    court = nom[:NOM_LIMITE].rstrip()
    if ' ' in court:
        court = court[:court.rfind(' ')].rstrip()
    return court or nom[:NOM_LIMITE]


def corriger_noms():
    for nom_fichier in sorted(os.listdir(os.path.join(RACINE, 'sections'))):
        if not nom_fichier.endswith('.liquid'):
            continue
        p = os.path.join(RACINE, 'sections', nom_fichier)
        schema, texte = schema_de(p)
        if schema is None:
            continue
        trop = noms_trop_longs(schema)
        if not trop:
            continue
        for ancien in sorted(set(trop), key=len, reverse=True):
            nouveau = raccourcir(ancien)
            texte = texte.replace('"%s"' % ancien, '"%s"' % nouveau)
            dire("  ✓ %-32s « %s » → « %s »" % (nom_fichier, ancien, nouveau))
        io.open(p, 'w', encoding='utf-8').write(texte)


# ───────────────────────────────────────────────────────────────────────────
#  3. Décimales : une seule pour un réglage de type range
# ───────────────────────────────────────────────────────────────────────────
def une_decimale(v):
    return round(float(v), 1)


def corriger_decimales():
    p = os.path.join(RACINE, 'config', 'settings_schema.json')
    schema = json.load(io.open(p, encoding='utf-8'))
    change = False
    for g in schema:
        if not isinstance(g, dict):
            continue
        for st in (g.get('settings') or []):
            if not isinstance(st, dict):
                continue
            for cle in ('default', 'min', 'max', 'step'):
                v = st.get(cle)
                if isinstance(v, float) and len(str(v).split('.')[-1]) > 1:
                    neuf = une_decimale(v)
                    dire("  ✓ schéma · %-22s %-8s %s → %s" % (st.get('id'), cle, v, neuf))
                    st[cle] = neuf
                    change = True
    if change:
        with io.open(p, 'w', encoding='utf-8') as f:
            f.write(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')

    # les valeurs enregistrées doivent rester dans les bornes, avec 1 décimale
    p = os.path.join(RACINE, 'config', 'settings_data.json')
    data = json.load(io.open(p, encoding='utf-8'))
    courant = data.get('current')
    if isinstance(courant, dict):
        bornes = {}
        for g in schema:
            if isinstance(g, dict):
                for st in (g.get('settings') or []):
                    if isinstance(st, dict) and st.get('type') == 'range':
                        bornes[st['id']] = (st.get('min'), st.get('max'), st.get('default'))
        change = False
        for k, v in list(courant.items()):
            if k in bornes and isinstance(v, float) and len(str(v).split('.')[-1]) > 1:
                mn, mx, df = bornes[k]
                neuf = une_decimale(v)
                if mn is not None:
                    neuf = max(neuf, une_decimale(mn))
                if mx is not None:
                    neuf = min(neuf, une_decimale(mx))
                dire("  ✓ valeurs · %-22s %s → %s" % (k, v, neuf))
                courant[k] = neuf
                change = True
        if change:
            with io.open(p, 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


# ───────────────────────────────────────────────────────────────────────────
#  4. Adresses : une valeur vide, ou qui commence par / http shopify:// #
# ───────────────────────────────────────────────────────────────────────────
def types_url_du_schema(chemin):
    schema, _ = schema_de(chemin)
    if schema is None:
        return {}, {}
    section, blocs = {}, {}
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


def adresse_valide(v):
    return (not isinstance(v, str)) or v == '' or v.startswith(('/',
            'http', 'shopify://', '#', 'mailto:', 'tel:', 'whatsapp:'))


def corriger_adresses():
    fichiers = []
    for dossier in ('templates', 'sections'):
        base = os.path.join(RACINE, dossier)
        for r, _, fs in os.walk(base):
            for f in fs:
                if f.endswith('.json'):
                    fichiers.append(os.path.join(r, f))
    fichiers.append(os.path.join(RACINE, 'config', 'settings_data.json'))

    total = 0
    for p in sorted(fichiers):
        try:
            d = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        modifs = 0

        def corriger(dictionnaire, types):
            nonlocal modifs
            for k, v in list(dictionnaire.items()):
                if types.get(k) == 'url' and isinstance(v, str) and v and not adresse_valide(v):
                    dictionnaire[k] = '/' + v.lstrip('/')
                    modifs += 1

        # modèles et groupes de sections
        for _, sec in (d.get('sections') or {}).items():
            if not isinstance(sec, dict):
                continue
            t = sec.get('type')
            chemin_section = os.path.join(RACINE, 'sections', '%s.liquid' % t)
            if not os.path.exists(chemin_section):
                continue
            types_section, types_blocs = types_url_du_schema(chemin_section)
            corriger(sec.setdefault('settings', {}), types_section)
            for _, blk in (sec.get('blocks') or {}).items():
                if isinstance(blk, dict):
                    corriger(blk.setdefault('settings', {}),
                             types_blocs.get(blk.get('type'), {}))

        # réglages globaux (settings_data.json)
        if p.endswith('settings_data.json'):
            schema = json.load(io.open(os.path.join(RACINE, 'config', 'settings_schema.json'),
                                       encoding='utf-8'))
            types = {}
            for g in schema:
                if isinstance(g, dict):
                    for st in (g.get('settings') or []):
                        if isinstance(st, dict) and st.get('id'):
                            types[st['id']] = st.get('type')
            cur = d.get('current')
            if isinstance(cur, dict):
                corriger(cur, types)

        if modifs:
            with io.open(p, 'w', encoding='utf-8') as f:
                f.write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
            rel = os.path.relpath(p, RACINE)
            dire("  ✓ %-52s %d adresse(s) préfixée(s) par « / »" % (rel, modifs))
            total += modifs
    if total:
        dire("  → %d adresses corrigées au total" % total)


# ───────────────────────────────────────────────────────────────────────────
def main():
    dire("LLUFAN — correction des erreurs signalées par Shopify (5 octobre 2026)")
    dire("")
    dire("1. Liquid : filtre à l'intérieur d'une balise")
    corriger_liquid()
    dire("2. Noms de sections et de blocs (25 caractères maximum)")
    corriger_noms()
    dire("3. Décimales des réglages numériques")
    corriger_decimales()
    dire("4. Adresses des réglages de type « url »")
    corriger_adresses()
    dire("")
    dire("Terminé. Contrôle : python3 llufan/audit_erreurs_shopify.py")


if __name__ == '__main__':
    sys.exit(main())
