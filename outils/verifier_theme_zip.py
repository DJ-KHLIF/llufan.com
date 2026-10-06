#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare le thème du dossier `theme/` avec l'archive `LLUFAN-theme-Shopify.zip`.

L'archive est l'état **livré** du thème : c'est elle qu'on importe dans Shopify.
Quand les deux divergent, c'est le plus souvent qu'un fichier a été modifié d'un
seul côté. Deux causes possibles, opposées :

  * le DOSSIER a reculé (une remise en place de l'espace de travail a rétabli
    des fichiers anciens) → il faut restaurer depuis l'archive ;
  * l'ARCHIVE a pris du retard (on a travaillé sur le thème sans refaire
    l'archive) → il faut refaire l'archive, surtout PAS restaurer.

Pour trancher sans se tromper, le script tient un **journal des états** du thème
(`etat-theme.json`, une empreinte par fichier, écrit à chaque reconstruction de
l'archive). Si les fichiers du dossier correspondent exactement à un état plus
ANCIEN que celui de l'archive, le dossier a reculé : la restauration est sûre.

Usage :
    python3 verifier_theme_zip.py                montre les différences et conclut
    python3 verifier_theme_zip.py --restaurer    remet le disque dans l'état de
                                                 l'archive — REFUSÉ si l'archive a
                                                 elle-même reculé (voir reference/)
    python3 verifier_theme_zip.py --archive-saine  l'archive est-elle conforme ?
    python3 verifier_theme_zip.py --forcer       restaure même si le journal n'est pas formel
    python3 verifier_theme_zip.py --enregistrer  inscrit l'archive au journal (après reconstruction)
    python3 verifier_theme_zip.py --journal      montre le journal des états
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import zipfile

RACINE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(RACINE, 'theme')
ARCHIVE = os.path.join(RACINE, 'LLUFAN-theme-Shopify.zip')
JOURNAL = os.path.join(RACINE, 'etat-theme.json')
ETATS_CONSERVES = 12


def empreintes_disque():
    resultat = {}
    for base, dossiers, fichiers in os.walk(THEME):
        dossiers[:] = [d for d in dossiers if not d.startswith('.')]
        for f in fichiers:
            if f.startswith('.'):
                continue
            chemin = os.path.join(base, f)
            resultat[os.path.relpath(chemin, THEME)] = hashlib.md5(
                open(chemin, 'rb').read()).hexdigest()
    return resultat


def empreintes_archive():
    with zipfile.ZipFile(ARCHIVE) as z:
        return {i.filename: hashlib.md5(z.read(i)).hexdigest()
                for i in z.infolist() if not i.is_dir()}


# ---------------------------------------------------------------------------
#  Journal des états du thème
# ---------------------------------------------------------------------------
def lire_journal():
    if not os.path.exists(JOURNAL):
        return []
    try:
        return json.load(open(JOURNAL, encoding='utf-8')).get('etats', [])
    except (ValueError, OSError):
        return []


APERCU = os.path.join(RACINE, 'preview')


def empreintes_apercu():
    """Les empreintes de l'aperçu : le témoin indépendant du thème.

    L'aperçu est produit à partir des mêmes sources mais vit dans un autre
    dossier. Quand une remise en place de l'espace de travail rétablit
    d'anciens fichiers du thème, l'aperçu, lui, reste presque toujours intact :
    en comparant les deux, on sait de quel côté est le retard.
    """
    resultat = {}
    if not os.path.isdir(APERCU):
        return resultat
    for f in sorted(os.listdir(APERCU)):
        if f.endswith('.html'):
            resultat[f] = hashlib.md5(open(os.path.join(APERCU, f), 'rb').read()).hexdigest()
    return resultat


def rang_apercu(empreintes):
    """Numéro du plus récent état du journal dont l'aperçu est celui du disque."""
    etats = lire_journal()
    for rang in range(len(etats) - 1, -1, -1):
        temoin = etats[rang].get('apercu')
        if temoin and all(temoin.get(k) == v for k, v in empreintes.items()):
            return rang, etats[rang].get('date', '?')
    return None, None


def ecrire_journal(etats):
    json.dump({'etats': etats[-ETATS_CONSERVES:]},
              open(JOURNAL, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def enregistrer_etat():
    """Inscrit l'archive au journal — appelé par refaire_archives.sh."""
    empreintes = empreintes_archive()
    etats = lire_journal()
    if etats and etats[-1]['empreintes'] == empreintes:
        print('journal des états : inchangé (%d état(s))' % len(etats))
        return 0
    etats.append({'date': datetime.datetime.now().strftime('%d/%m/%Y %H:%M'),
                  'empreintes': empreintes,
                  'apercu': empreintes_apercu()})
    ecrire_journal(etats)
    print('journal des états : état n°%d inscrit (%d fichiers)'
          % (len(etats[-ETATS_CONSERVES:]), len(empreintes)))
    return 0


def rangs_journal(empreintes):
    """Pour chaque état du journal, le plus ancien → le plus récent.

    Renvoie la liste [(date, empreintes), …] du plus ancien au plus récent.
    """
    return [(e.get('date', '?'), e['empreintes']) for e in lire_journal()]


def journal_correspond(etat, empreintes):
    return etat.get('empreintes') == empreintes


def etat_le_plus_proche(empreintes, concernes):
    """Numéro du journal dont l'état correspond EXACTEMENT aux fichiers concernés.

    Renvoie (rang, date) du plus récent état qui reproduit, pour chacun des
    fichiers divergents, l'empreinte présente sur le disque — ou (None, None).
    C'est ce qui permet de dire « ce dossier est l'état d'avant ».
    """
    etats = rangs_journal(empreintes)
    for rang in range(len(etats) - 1, -1, -1):
        date, emp = etats[rang]
        if all(emp.get(k) == empreintes.get(k) for k in concernes):
            return rang, date
    return None, None


def ecart_dates():
    """Écart entre la plus ancienne et la plus récente date des fichiers du thème.

    Après une remise en place de l'espace de travail, TOUS les fichiers portent
    la même date : les dates ne disent alors plus rien, et s'y fier mènerait à
    la mauvaise décision.
    """
    dates = [os.path.getmtime(os.path.join(base, f))
             for base, dossiers, fichiers in os.walk(THEME)
             for f in fichiers if not f.startswith('.')]
    if len(dates) < 2:
        return 0
    return max(dates) - min(dates)


def archive_saine():
    """L'archive sert-elle bien les fichiers de référence ?

    POURQUOI CE CONTRÔLE EXISTE — 6 octobre 2026. Restaurer le dossier depuis
    l'archive est le bon geste... À CONDITION que l'archive soit saine. Or le
    6 octobre, l'archive avait été construite pendant un recul : elle servait
    elle aussi l'ancienne feuille de style. `--restaurer` a donc écrasé le bon
    fichier par le mauvais. Le contrôle ci-dessous l'interdit désormais : la
    seule source de vérité pour un fichier surveillé est
    `llufan/reference/`, jamais l'archive.

    Retourne (vrai, []) ou (faux, [(membre, trouvé, attendu)]).
    """
    import hashlib
    import json
    import zipfile

    fichier = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'empreintes-reference.json')
    if not os.path.exists(fichier):
        return True, []
    with open(fichier, encoding='utf-8') as f:
        ref = json.load(f)
    surveilles = {c: v for c, v in ref.items() if not c.startswith('_')}
    if not os.path.exists(ARCHIVE):
        return True, []

    ecarts = []
    with zipfile.ZipFile(ARCHIVE) as z:
        noms = z.namelist()
        for chemin, attendu in surveilles.items():
            membre = chemin.split('/', 1)[1] if chemin.startswith('theme/') else chemin
            candidat = next((n for n in noms if n == membre), None)
            if candidat is None:
                continue
            trouve = hashlib.md5(z.read(candidat)).hexdigest()
            if trouve != attendu:
                ecarts.append((candidat, trouve, attendu))
    return (not ecarts), ecarts


def main():
    if '--archive-saine' in sys.argv:
        saine, ecarts = archive_saine()
        if saine:
            print("  ✓ l'archive sert bien les fichiers de référence")
            return 0
        print("  ✗ l'archive a reculé :")
        for membre, trouve, attendu in ecarts:
            print('     %s : %s (attendu %s)' % (membre, trouve, attendu))
        return 1

    if '--enregistrer' in sys.argv:
        return enregistrer_etat()

    if '--journal' in sys.argv:
        etats = rangs_journal({})
        if not etats:
            print('journal des états : vide (il se remplit à chaque reconstruction de l\'archive)')
        for i, (date, emp) in enumerate(etats, 1):
            print('%2d. %s — %d fichiers' % (i, date, len(emp)))
        return 0

    disque, archive = empreintes_disque(), empreintes_archive()
    manquants = sorted(set(archive) - set(disque))
    en_trop = sorted(set(disque) - set(archive))
    differents = sorted(k for k in set(disque) & set(archive) if disque[k] != archive[k])

    print('thème : %d fichiers · archive : %d fichiers' % (len(disque), len(archive)))
    if not (manquants or en_trop or differents):
        print('✓ le dossier et l\'archive sont identiques — rien à faire.')
        return 0

    for titre, liste in (('absents du dossier', manquants),
                         ('absents de l\'archive', en_trop),
                         ('contenus différents', differents)):
        if liste:
            print('\n%s : %d' % (titre, len(liste)))
            for k in liste:
                print('   ', k)

    concernes = manquants + differents
    rang_disque, date_disque = etat_le_plus_proche(disque, concernes)
    rang_archive, date_archive = etat_le_plus_proche(archive, concernes)
    ecart = ecart_dates()

    print()
    if rang_disque is not None and rang_archive is not None and rang_disque < rang_archive:
        verdict = 'recul'
        print('➜ LE DOSSIER A RECULÉ : ces fichiers sont exactement l\'état du %s,'
              % date_disque)
        print('  alors que l\'archive est l\'état du %s. Une remise en place de' % date_archive)
        print('  l\'espace de travail a rétabli d\'anciens fichiers.')
        print('  → la restauration depuis l\'archive est sûre, elle ne perd rien.')
    elif rang_disque is not None and rang_disque < len(lire_journal()) - 1:
        # Le dossier correspond à un état ancien du journal, mais pas à l'archive.
        verdict = 'recul'
        print('➜ LE DOSSIER A RECULÉ : ces fichiers reproduisent l\'état du %s,'
              % date_disque)
        print('  alors que l\'archive est plus récente. La restauration est sûre.')
    else:
        # Témoin : l'aperçu. S'il correspond à l'état de l'archive, le dossier est en retard.
        temoin_disque, date_temoin = rang_apercu(empreintes_apercu())
        etats = lire_journal()
        if temoin_disque is not None and journal_correspond(etats[temoin_disque], archive):
            verdict = 'recul'
            print('➜ LE DOSSIER A RECULÉ : l\'aperçu est celui de l\'état du %s et'
                  % date_temoin)
            print('  correspond à l\'archive, alors que les fichiers du thème (ci-dessus)')
            print('  sont d\'anciennes versions. La restauration est sûre.')
        else:
            verdict = None
    if verdict is not None:
        pass                                  # un verdict a déjà été rendu : on n'y touche plus
    elif ecart < 300:
        verdict = 'douteux'
        print('➜ JE NE PEUX PAS TRANCHER. Tous les fichiers du thème portent la même')
        print('  date (%.0f s d\'écart) : l\'espace de travail a été remis en place, les' % ecart)
        print('  dates ne veulent plus rien dire. Ces fichiers ne correspondent à aucun')
        print('  état connu du journal.')
        print('  → comparer à la main (ci-dessus), puis --restaurer ou --forcer.')
    else:
        verdict = 'travail'
        print('➜ L\'ARCHIVE A PRIS DU RETARD : les fichiers du dossier ont été modifiés')
        print('  après elle et ne correspondent à aucun état du journal.')
        print('  → ne pas restaurer : refaire l\'archive (`bash refaire_archives.sh`).')

    restaurer = '--restaurer' in sys.argv
    if restaurer and verdict == 'douteux' and '--forcer' not in sys.argv:
        print('\n  Rien n\'a été touché. (--forcer restaure quand même.)')
        return 2
    if restaurer and verdict == 'travail' and '--forcer' not in sys.argv:
        print('\n  Rien n\'a été touché. (--forcer restaure quand même.)')
        return 2

    if restaurer:
        saine, ecarts_archive = archive_saine()
        if not saine:
            print('\n⛔ RESTAURATION REFUSÉE : l\'archive elle-même a reculé.')
            for membre, trouve, attendu in ecarts_archive:
                print('     %s' % membre)
                print('       dans l\'archive : %s' % trouve)
                print('       attendu        : %s' % attendu)
            print('  Restaurer depuis la copie de référence, puis refaire l\'archive :')
            print('     python3 verifier_empreintes.py --restaurer')
            print('     bash refaire_archives.sh')
            return 3
        a_restaurer = concernes
        if a_restaurer:
            subprocess.run(['unzip', '-o', '-q', ARCHIVE, '-d', THEME] + a_restaurer, check=True)
            print('\n✓ %d fichier(s) restauré(s) depuis l\'archive.' % len(a_restaurer))
        if en_trop:
            print('  (les %d fichiers en trop n\'ont pas été touchés : à regarder à la main.)'
                  % len(en_trop))
        return 0

    print('\nPour remettre le dossier dans l\'état de l\'archive :')
    print('   python3 verifier_theme_zip.py --restaurer')
    return 1


if __name__ == '__main__':
    sys.exit(main())
