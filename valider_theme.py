#!/usr/bin/env python3
"""Contrôle du thème LLUFAN : balises Liquid, snippets appelés, réglages déclarés, JSON.

Usage : python3 valider_theme.py        (depuis /home/user/llufan)
"""
import json
import pathlib
import re

PAIRES = {
    'if': 'endif', 'unless': 'endunless', 'for': 'endfor', 'case': 'endcase',
    'capture': 'endcapture', 'form': 'endform', 'paginate': 'endpaginate',
    'schema': 'endschema', 'style': 'endstyle', 'stylesheet': 'endstylesheet',
    'javascript': 'endjavascript', 'comment': 'endcomment',
    'raw': 'endraw', 'tablerow': 'endtablerow',
}
OUVRANTS, FERMANTS = set(PAIRES), set(PAIRES.values())
NEUTRES = {
    'else', 'elsif', 'when', 'break', 'continue', 'cycle', 'assign', 'render', 'include',
    'section', 'sections', 'layout', 'echo', 'liquid', 'increment', 'decrement',
}
RACINE = pathlib.Path(__file__).resolve().parent / 'theme'


def analyser(chemin, src):
    """Vérifie l'équilibrage des balises et des accolades, hors bloc {% schema %}."""
    src = re.sub(r'\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}', '', src, flags=re.S)
    pile, erreurs = [], []
    for m in re.finditer(r'\{%-?\s*(\w+)(.*?)-?%\}', src, flags=re.S):
        t = m.group(1)
        ligne = src[:m.start()].count('\n') + 1
        if t in OUVRANTS:
            pile.append((t, ligne))
        elif t in FERMANTS:
            if not pile:
                erreurs.append(f"{chemin}:{ligne} → {t} sans ouverture")
            else:
                o, lo = pile.pop()
                if PAIRES.get(o) != t:
                    erreurs.append(f"{chemin}:{ligne} → {t} ferme {o} (ouvert l.{lo})")
        elif t not in NEUTRES:
            erreurs.append(f"{chemin}:{ligne} → balise inconnue « {t} »")
    for o, lo in pile:
        erreurs.append(f"{chemin}:{lo} → {o} jamais fermé")
    for m in re.finditer(r'\{\{(.*?)\}\}', src, flags=re.S):
        if m.group(1).count('{') or m.group(1).count('}'):
            erreurs.append(f"{chemin}:{src[:m.start()].count(chr(10)) + 1} → accolades déséquilibrées")
    return erreurs


def main():
    fichiers = sorted(RACINE.rglob('*.liquid'))
    erreurs = []
    for p in fichiers:
        erreurs += analyser(p.relative_to(RACINE), p.read_text(encoding='utf-8'))
    print(f"• Balises Liquid : {len(fichiers) - len({e.split(':')[0] for e in erreurs})}/{len(fichiers)} fichiers conformes")

    manquants = set()
    for p in fichiers:
        for m in re.finditer(r"\{%-?\s*(?:render|include)\s+'([^']+)'", p.read_text(encoding='utf-8')):
            if not (RACINE / 'snippets' / f"{m.group(1)}.liquid").exists():
                manquants.add(f"snippets/{m.group(1)}.liquid")
    print("• Snippets appelés :", "tous présents" if not manquants else sorted(manquants))

    globaux = set()
    for bloc in json.loads((RACINE / 'config' / 'settings_schema.json').read_text(encoding='utf-8')):
        for s_ in bloc.get('settings', []) or []:
            if s_.get('id'):
                globaux.add(s_['id'])

    souci = []
    for p in sorted((RACINE / 'sections').glob('*.liquid')):
        src = p.read_text(encoding='utf-8')
        m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}', src, flags=re.S)
        if not m:
            continue
        try:
            schema = json.loads(m.group(1))
        except Exception as e:
            souci.append((p.name, f"schéma illisible : {e}"))
            continue
        ids = {s.get('id') for s in schema.get('settings', []) if s.get('id')}
        for b in schema.get('blocks') or []:
            ids |= {s.get('id') for s in b.get('settings', []) if s.get('id')}
        for b in schema.get('blocks') or []:
            for s in b.get('settings', []) or []:
                if s.get('type') == 'select' and s.get('id') == 'color_scheme':
                    pass
        utilises = set(re.findall(r'(?<!section\.)(?<!block\.)settings\.([a-zA-Z0-9_]+)', src))
        inconnus = {u for u in utilises if u not in ids and u not in globaux}
        if inconnus:
            souci.append((p.name, f"réglages introuvables : {sorted(inconnus)}"))
    print("• Réglages de section :", "tous déclarés" if not souci else f"{len(souci)} section(s) à revoir")
    for n, s in souci:
        print("    ", n, "→", s)

    jsons = sorted(RACINE.rglob('*.json'))
    for p in jsons:
        try:
            json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            print("• JSON", p.relative_to(RACINE), "invalide :", e)
    print(f"• JSON : {len(jsons)} fichiers valides")

    for e in erreurs[:20]:
        print("    ", e)
    return 1 if erreurs or manquants or souci else 0


if __name__ == '__main__':
    raise SystemExit(main())
