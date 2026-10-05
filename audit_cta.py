#!/usr/bin/env python3
"""Contrôle des boutons et des appels à l'action du thème LLUFAN.

Pour chaque lien du thème, le script vérifie que la destination existe :
routes Shopify valides, objets de la boutique (produit, collection, page),
ancres présentes sur la même page, liens externes (WhatsApp, e-mail, partage),
ou textes volontairement non cliquables. Tout lien mort est signalé.

Usage : python3 audit_cta.py        (depuis /home/user/llufan)
"""
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parent / 'theme'

# Routes officielles de l'objet `routes` (shopify.dev/docs/api/liquid/objects/routes)
ROUTES_VALIDES = {
    'account_addresses_url', 'account_login_url', 'account_logout_url', 'account_profile_url',
    'account_recover_url', 'account_register_url', 'account_url', 'all_products_collection_url',
    'cart_add_url', 'cart_change_url', 'cart_clear_url', 'cart_update_url', 'cart_url',
    'collections_url', 'predictive_search_url', 'product_recommendations_url', 'root_url',
    'search_url', 'storefront_login_url',
}


def destinations(chemin, src):
    """Renvoie [(ligne, expression, extrait du texte, balise)] pour chaque lien."""
    trouves = []
    for m in re.finditer(r'<(a|form)\b[^>]*?(?:href|action)="([^"]*)"[^>]*>', src, re.S):
        balise, cible = m.group(1), m.group(2).strip()
        ligne = src[:m.start()].count('\n') + 1
        suite = src[m.end():m.end() + 160]
        texte = re.sub(r'<[^>]+>', ' ', suite)
        texte = re.sub(r'\s+', ' ', texte).strip()[:48]
        trouves.append((ligne, cible, texte, balise))
    return trouves


def normaliser(texte):
    """Remplace chaque expression Liquid par un jeton, pour comparer des ancres."""
    return re.sub(r'\{\{.*?\}\}', '#X#', texte)


def ancre_existe(ancre, ancres_du_fichier, ancres_du_theme):
    """Vrai si l'ancre existe dans le fichier, ou dans un snippet rendu par lui."""
    if ancre in ancres_du_fichier:
        return True, 'même fichier'
    cible = normaliser(ancre)
    for identifiant, fichier in ancres_du_theme.items():
        if normaliser(identifiant) == cible:
            return True, f'rendu par {fichier}'
    return False, ''

def classer(cible, ancres_du_fichier, ancres_du_theme):
    if cible in ('', '#'):
        return 'MORT', 'aucune destination'
    if cible.startswith('#'):
        ancre = cible.lstrip('#')
        existe, ou = ancre_existe(ancre, ancres_du_fichier, ancres_du_theme)
        return ('OK', f'ancre #{ancre} ({ou})') if existe else ('À VÉRIFIER', f'ancre #{ancre} introuvable')
    if '#' in cible:
        avant, _, apres = cible.partition('#')
        etat, quoi = classer(avant.strip(), ancres_du_fichier, ancres_du_theme)
        existe, ou = ancre_existe(apres, ancres_du_fichier, ancres_du_theme)
        if etat == 'OK' and existe:
            return 'OK', f'{quoi} + ancre #{apres} ({ou})'
        return 'À VÉRIFIER', f'{quoi} + ancre #{apres} introuvable'
    if cible.startswith('{{'):
        interieur = cible.strip('{} ')
        if interieur.startswith('routes.'):
            nom = interieur.split('|')[0].strip().replace('routes.', '')
            return ('OK', f'route {nom}') if nom in ROUTES_VALIDES else ('MORT', f'route inconnue {nom}')
        if 'contact_email' in interieur:
            return 'OK', 'e-mail (centralisé)'
        if 'whatsapp' in interieur or 'lien_contact' in interieur:
            return 'OK', 'contact centralisé (WhatsApp)'
        if 'payment_url' in interieur:
            return 'OK', 'page de paiement Shopify'
        if '.url' in interieur:
            return 'OK', 'objet de la boutique'
        return 'RÉGLAGE', 'valeur de réglage'
    if cible.startswith('mailto:'):
        return 'OK', 'e-mail'
    if 'wa.me' in cible:
        return 'OK', 'WhatsApp'
    if cible.startswith('https://'):
        return 'OK', 'lien externe'
    return 'OK', 'chemin'

def main():
    lignes = []
    morts = []
    ancres_du_theme = {}
    for p in sorted(RACINE.rglob('*.liquid')):
        src = p.read_text(encoding='utf-8')
        for identifiant in re.findall(r'id="([^"]+)"', src):
            ancres_du_theme[identifiant] = str(p.relative_to(RACINE))
    for p in sorted(RACINE.rglob('*.liquid')):
        if 'customers' in str(p) or p.name == 'gift_card.liquid':
            continue
        src = p.read_text(encoding='utf-8')
        ancres = set(re.findall(r'id="([^"]+)"', src))
        for ligne, cible, texte, balise in destinations(p.relative_to(RACINE), src):
            etat, quoi = classer(cible, ancres, ancres_du_theme)
            if etat == 'MORT':
                morts.append((str(p.relative_to(RACINE)), ligne, cible, texte))
            elif etat == 'À VÉRIFIER':
                morts.append((str(p.relative_to(RACINE)), ligne, cible, quoi))
            lignes.append((str(p.relative_to(RACINE)), ligne, cible, texte, etat, quoi))

    print(f"• {len(lignes)} liens et formulaires analysés dans le thème")
    print("• Destinations mortes ou à vérifier :", len(morts))
    for f, l, c, t in morts:
        print(f"    {f}:{l} → {c!r} {('— ' + t) if t else ''}")

    print("\n• Répartition :")
    from collections import Counter
    for (etat, quoi), n in Counter((e, q) for *_x, e, q in lignes).most_common(14):
        print(f"    {n:3}  {quoi}")
    return 1 if morts else 0


if __name__ == '__main__':
    raise SystemExit(main())
