#!/usr/bin/env python3
# ---------------------------------------------------------------------------
#  LLUFAN — les fichiers qui ont déjà reculé.

#  POURQUOI CE CONTRÔLE EXISTE
#  Le dossier `llufan/theme/` a reculé trois fois (5 et 6 octobre 2026) : sans
#  crier gare, `assets/theme.css` revenait à la version d'AVANT le correctif
#  d'« air » (marges de page de 2 et 3 rem, rythme de 4 rem sur ordinateur).
#  Le dossier paraissait normal, la boutique aussi — seule la feuille de style
#  avait changé, et 1 510 octets manquaient.

#  Le danger n'est pas le recul en lui-même : c'est la RECONSTRUCTION. Si on
#  refait l'archive pendant le recul, le recul se fige dans le fichier .zip,
#  et c'est cette version-là qui part sur GitHub puis dans Shopify. C'est
#  exactement ce qui a failli se produire le 6 octobre 2026.

#  D'où ce verrou : `refaire_archives.sh` et `verifier_avant_envoi.sh` refusent
#  de continuer si un fichier surveillé n'est plus identique à sa référence.

#  Il sait lire les deux formes du thème :
#     • le dossier `theme/assets/theme.css` (espace de travail) ;
#     • l'archive `theme/LLUFAN-theme-Shopify.zip` (paquet livré, dépôt).

#      python3 verifier_empreintes.py              contrôle (code 0 = bon)
#      python3 verifier_empreintes.py --restaurer  remet la copie de secours
#                                                  (dossier seulement)
# ---------------------------------------------------------------------------
import hashlib
import io
import json
import os
import shutil
import sys
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(ICI, 'empreintes-reference.json')


def md5_de(donnees):
    return hashlib.md5(donnees).hexdigest()


def lire_dans_zip(chemin, membre):
    """Le contenu d'un fichier rangé dans une archive, ou None."""
    try:
        with zipfile.ZipFile(chemin) as z:
            for nom in z.namelist():
                if nom == membre or nom.endswith('/' + membre):
                    return z.read(nom)
    except (zipfile.BadZipFile, OSError):
        return None
    return None


def chercher(chemin):
    """Où vit le fichier surveillé ? → (md5, étiquette, fichier sur disque|None)

    Ordre : le dossier du thème, puis l'archive du paquet, puis l'archive
    posée à côté du script."""
    bases = [ICI, os.path.dirname(ICI)]
    for base in bases:                       # 1. le dossier du thème
        complet = os.path.join(base, chemin)
        if os.path.exists(complet):
            with open(complet, 'rb') as f:
                return md5_de(f.read()), complet, complet
    nom_archive = 'LLUFAN-theme-Shopify.zip'
    for base in bases:                       # 2. l'archive livrée
        for dossier in ('theme', ''):
            archive = os.path.join(base, dossier, nom_archive)
            if os.path.exists(archive):
                # Dans l'archive du thème, les fichiers sont à la racine :
                # « theme/assets/theme.css » y devient « assets/theme.css ».
                donnees = lire_dans_zip(archive, chemin)
                if donnees is None and '/' in chemin:
                    donnees = lire_dans_zip(archive, chemin.split('/', 1)[1])
                if donnees is not None:
                    return md5_de(donnees), "%s (%s)" % (chemin, os.path.relpath(archive, base)), None
    return None, None, None


def main():
    restaurer = '--restaurer' in sys.argv
    if not os.path.exists(FICHIER):
        print("  · pas de fichier d'empreintes : contrôle passé (rien à surveiller)")
        return 0
    ref = json.load(io.open(FICHIER, encoding='utf-8'))
    surveilles = {c: v for c, v in ref.items() if not c.startswith('_')}

    ecarts, repares, introuvables, verifies = [], [], [], []
    for chemin, attendu in surveilles.items():
        actuel, etiquette, sur_disque = chercher(chemin)
        if actuel is None:
            introuvables.append(chemin)
            continue
        if actuel == attendu:
            verifies.append(etiquette)
            continue
        secours = os.path.join(ICI, 'reference', os.path.basename(chemin))
        if not os.path.exists(secours):
            secours = os.path.join(os.path.dirname(ICI), 'reference', os.path.basename(chemin))
        if restaurer and sur_disque and os.path.exists(secours) and \
                md5_de(open(secours, 'rb').read()) == attendu:
            shutil.copy2(secours, sur_disque)
            repares.append(chemin)
            continue
        ecarts.append((etiquette, actuel, attendu, bool(sur_disque)))

    if repares and not ecarts:
        print("  ✓ %d fichier(s) restauré(s) depuis reference/ : %s"
              % (len(repares), ', '.join(repares)))
        return 0

    if ecarts:
        print("  ✗ FICHIER DE RÉFÉRENCE MODIFIÉ : le dossier a reculé.")
        for etiquette, actuel, attendu, restaurable in ecarts:
            print("       %s" % etiquette)
            print("         trouvé  : %s" % actuel)
            print("         attendu : %s" % attendu)
            if restaurable:
                print("         → python3 verifier_empreintes.py --restaurer")
            else:
                print("         → la feuille est DANS l'archive : la remplacer par l'archive vérifiée")
        return 1

    if introuvables and not verifies:
        print("  · thème non livré ici (ni dossier ni archive) : rien à surveiller")
        return 0

    print("  ✓ les %d fichier(s) surveillé(s) sont intacts : %s"
          % (len(verifies), ', '.join(verifies)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
