#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aperçu HTML de la vitrine LLUFAN — version DÉMONSTRATION.

Produit un fichier HTML autonome par page (CSS et polices en ligne, images en
données, aucune ressource externe) : toutes les pages de la boutique sont
accessibles depuis l'aperçu, y compris par les liens du menu, du pied de page
et des cartes produit.

Les contenus, les produits, les prix, les avis et les discussions sont FICTIFS :
ils viennent de demo/contenu_demo.py, la même source que celle qui alimente les
modèles JSON du thème Shopify. Ils servent à tester la boutique de bout en bout.

Usage : python3 build_preview.py
"""
import base64
import json
import os
import sys
from io import BytesIO

from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(ROOT, 'theme')
OUT = os.path.join(ROOT, 'preview')
sys.path.insert(0, os.path.join(ROOT, 'demo'))
import contenu_demo as D  # noqa: E402

# ---------------------------------------------------------------------------
# Feuilles de style, scripts, polices
# ---------------------------------------------------------------------------
css = open(os.path.join(THEME, 'assets', 'theme.css'), encoding='utf-8').read()
theme_js = open(os.path.join(THEME, 'assets', 'theme.js'), encoding='utf-8').read()
livraison_js = open(os.path.join(THEME, 'assets', 'llufan-livraison.js'), encoding='utf-8').read()
livraison_data = open(os.path.join(THEME, 'assets', 'llufan-livraison-dz.json'), encoding='utf-8').read()


def inline_font(fname):
    chemin = os.path.join(THEME, 'assets', fname)
    data = base64.b64encode(open(chemin, 'rb').read()).decode()
    return "url(data:font/woff2;base64,%s) format('woff2')" % data


# Seules les variantes latine sont intégrées (les accents français y sont) :
# l'aperçu reste léger, les fichiers « latin-ext » sont remplacés par la police
# locale du poste de lecture.
css = css.replace("url('jost-latin.woff2')", inline_font('jost-latin.woff2'))
css = css.replace("url('fraunces-latin.woff2')", inline_font('fraunces-latin.woff2'))
css = css.replace("url('jost-latin-ext.woff2')", "local('Jost')")
css = css.replace("url('fraunces-latin-ext.woff2')", "local('Fraunces')")

css += """
/* --- Aperçu uniquement ---------------------------------------------------- */
.preview-note { background: #EB735B; color: #fff; font-family: var(--heading-font-family);
  font-size: .6875rem; letter-spacing: .1em; text-transform: uppercase; text-align: center; padding: .5rem 1rem; }
.preview-note strong { font-weight: 600; }
.field-empty { display: inline-block; border: 1px dashed currentColor; border-radius: .25rem;
  padding: .1rem .5rem; opacity: .55; font-style: italic; font-size: .8125em; font-family: var(--heading-font-family); }
.visuel { width: 100%; height: 100%; display: grid; place-items: center; background: #EAE6E1; color: #183264;
  font-family: var(--heading-font-family); font-size: .6875rem; letter-spacing: .08em; text-transform: uppercase; text-align: center; }
.visuel span { max-width: 70%; opacity: .75; }
/* Reproduit le « position: sticky » que les sections appliquent dans Shopify. */
.announcement-bar { position: sticky; top: 0; z-index: 5; }
.header { position: sticky; top: var(--announcement-bar-height, 38px); z-index: 4; }
.footer__secondaire { display: grid; gap: 1.5rem; padding-block-start: 1.75rem; border-block-start: 1px solid rgb(var(--border-color) / .45); }
@media screen and (min-width: 1000px) { .footer__secondaire { grid-template-columns: 1fr auto; align-items: center; } }
.footer__secondaire .footer__reassurance { display: flex; flex-wrap: wrap; gap: .5rem 1.75rem; }
@media screen and (max-width: 999px) { .footer__secondaire .footer__reassurance { display: grid; } }
.footer__contact-lien .footer__contact-icone { grid-row: span 2; }
.footer__reseau-vide { display: inline-flex; align-items: center; justify-content: center; width: 2.25rem; height: 2.25rem;
  border: 1px dashed rgb(var(--text-color) / .45); border-radius: var(--rounded-full); opacity: .75; }
:root { --announcement-bar-is-sticky: 1; --header-is-sticky: 1; }
"""

HEAD = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — aperçu LLUFAN</title>
<style>{css}</style></head>
<body class="features--button-transition features--zoom-image color-scheme color-scheme--scheme-1">
<loading-bar class="loading-bar" role="progressbar" aria-hidden="true"></loading-bar>
<div class="preview-note">Aperçu de démonstration — <strong>contenus, produits, prix, avis et visuels fictifs</strong>, créés pour tester la boutique</div>
<a class="skip-to-content sr-only" href="#main">Aller au contenu</a>
"""


# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------
def data_uri(chemin, largeur=None, qualite=80):
    im = Image.open(chemin).convert('RGB')
    if largeur and im.width > largeur:
        im = im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS)
    tampon = BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(tampon.getvalue()).decode()


ASSETS = os.path.join(THEME, 'assets')
IMG = {
    'hero-1': data_uri(os.path.join(ASSETS, 'demo-hero-1.jpg'), 1400),
    'hero-2': data_uri(os.path.join(ASSETS, 'demo-hero-2.jpg'), 1400),
    'univers-1': data_uri(os.path.join(ASSETS, 'demo-univers-1.jpg'), 800),
    'univers-2': data_uri(os.path.join(ASSETS, 'demo-univers-2.jpg'), 800),
    'univers-3': data_uri(os.path.join(ASSETS, 'demo-univers-3.jpg'), 800),
    'univers-4': data_uri(os.path.join(ASSETS, 'demo-univers-4.jpg'), 800),
    'editorial': data_uri(os.path.join(ASSETS, 'demo-editorial.jpg'), 700),
    'banniere': data_uri(os.path.join(ASSETS, 'demo-collection-banner.jpg'), 1600),
    'nomad': data_uri(os.path.join(ASSETS, 'llufan-nomad-coussin.jpg'), 500),
}
PRODUITS_IMG = {}
for _p in D.PRODUITS:
    _chemin = os.path.join(ROOT, 'demo', 'produits', _p['image'])
    PRODUITS_IMG[_p['handle']] = {
        'carte': data_uri(_chemin, 460, 76),
        'fiche': data_uri(_chemin, 620, 80),
        'vignette': data_uri(_chemin, 180, 70),
    }


def V(w, h, label='Visuel LLUFAN à fournir', tint='#EAE6E1'):
    """Visuel de remplacement, pour les seuls emplacements encore vides."""
    svg = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 %d %d\" width=\"%d\" height=\"%d\">"
           "<rect width=\"100%%\" height=\"100%%\" fill=\"%s\"/>"
           "<text x=\"50%%\" y=\"50%%\" text-anchor=\"middle\" font-family=\"Jost, sans-serif\" font-size=\"%d\""
           " fill=\"#183264\" fill-opacity=\".7\">%s</text></svg>") % (
        w, h, w, h, tint, max(11, min(w, h) // 20), label)
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


# ---------------------------------------------------------------------------
# Icônes
# ---------------------------------------------------------------------------
ICON = {
    'chevron-down': '<svg viewBox="0 0 12 12" style="width:10px;height:10px"><path d="m2 4 4 4 4-4" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'flower': '<svg class="ic" viewBox="0 0 24 24" fill="none"><path d="M12 21c0-3 0-6 0-7.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/><path d="M12 13.5c-2.6 0-4.6-1.7-4.6-4S9.4 5 12 5s4.6 2.2 4.6 4.5-2 4-4.6 4Z" stroke="currentColor" stroke-width="1.3"/><path d="M12 9.6c1.3 0 2.4-1 2.4-2.3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>',
    'sparkle': '<svg class="ic" viewBox="0 0 24 24" fill="none"><path d="M12 3.5c.9 3.8 1.7 4.6 5.5 5.5-3.8.9-4.6 1.7-5.5 5.5-.9-3.8-1.7-4.6-5.5-5.5 3.8-.9 4.6-1.7 5.5-5.5Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><path d="M17.5 15.5c.4 1.7.8 2.1 2.5 2.5-1.7.4-2.1.8-2.5 2.5-.4-1.7-.8-2.1-2.5-2.5 1.7-.4 2.1-.8 2.5-2.5Z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/></svg>',
    'heart': '<svg viewBox="0 0 24 24" class="ic"><path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9Z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    'star': '<svg viewBox="0 0 24 24" class="ic"><path d="M12 3l2.5 5 5.5.8-4 3.8 1 5.4L12 15l-5 3 1-5.4-4-3.8 5.5-.8L12 3Z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    'lock': '<svg class="ic" viewBox="0 0 24 24" fill="none"><rect x="5" y="10.5" width="14" height="9.5" rx="2" stroke="currentColor" stroke-width="1.3"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>',
    'locker': '<svg class="ic" viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="16" height="16" rx="2.5" stroke="currentColor" stroke-width="1.3"/><path d="M12 4v16" stroke="currentColor" stroke-width="1.3"/><path d="M8 10.5h1.5M14.5 10.5H16" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>',
    'shipping': '<svg class="ic" viewBox="0 0 24 24" fill="none"><path d="M2.5 15.5c0-3.4 2.3-5.7 5.7-5.7s5.7 2.3 5.7 5.7" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/><path d="M13.9 15.5h6.6v-3.2h-2.6l-1.6-2.5h-2.4" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><circle cx="6.4" cy="17.6" r="1.6" stroke="currentColor" stroke-width="1.3"/><circle cx="17.6" cy="17.6" r="1.6" stroke="currentColor" stroke-width="1.3"/><path d="M8 17.6h7.9" stroke="currentColor" stroke-width="1.3"/></svg>',
    'payment': '<svg class="ic" viewBox="0 0 24 24" fill="none"><rect x="2.5" y="6" width="19" height="12" rx="2.5" stroke="currentColor" stroke-width="1.3"/><path d="M2.5 10h19" stroke="currentColor" stroke-width="1.3"/><path d="M6 14h4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>',
    'tag': '<svg viewBox="0 0 24 24" class="ic"><path d="M20.6 13.4 13 21a2 2 0 0 1-2.8 0L3 13.8V4h9.8l7.8 7.8a2 2 0 0 1 0 1.6Z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" class="ic"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="m3 7 9 6 9-6" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    'whatsapp': '<svg viewBox="0 0 24 24" class="ic"><path d="M12 3.6a8.4 8.4 0 0 0-7.2 12.7L3.6 20.4l4.2-1.1A8.4 8.4 0 1 0 12 3.6Z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M8.9 8.6c.3-.6.6-.6.9-.6h.6c.2 0 .5 0 .7.6l.7 1.7c.1.3 0 .5-.2.7l-.6.7c-.2.2-.2.4-.1.6.4.8 1.3 1.8 2.2 2.3.3.2.5.1.7-.1l.6-.7c.2-.2.4-.2.7-.1l1.6.8c.3.2.5.4.4.7-.1.7-.5 1.4-1.4 1.5-1.1.1-2.7-.5-4.3-1.9-1.5-1.3-2.3-2.8-2.4-3.9 0-1 .4-1.6.9-2Z" fill="currentColor"/></svg>',
    'account': '<svg viewBox="0 0 24 24" class="ic"><circle cx="12" cy="8" r="4" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    'gift': '<svg viewBox="0 0 24 24" class="ic"><rect x="4" y="9" width="16" height="11" rx="1.6" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M3 6h18v3H3zM12 6v14" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    'search': '<svg viewBox="0 0 24 24" class="ic"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="m21 21-4.3-4.3" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>',
    'bag': '<svg viewBox="0 0 24 24" class="ic"><path d="M6 8h12l-1 12H7L6 8Z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M9 8a3 3 0 0 1 6 0" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    'burger': '<svg viewBox="0 0 24 24" class="ic"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>',
}
ICON_WHATSAPP = ICON['whatsapp']
ICON_MAIL = ICON['mail']
ICON_FACEBOOK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.2h2.4l.4-2.8h-2.8V9.2c0-.8.2-1.4 1.4-1.4h1.5V5.3c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9V11H8v2.8h2.3V21h3.2Z"/></svg>'
ICON_INSTAGRAM = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="4.5" stroke="currentColor" stroke-width="1.3"/><circle cx="12" cy="12" r="3.6" stroke="currentColor" stroke-width="1.3"/><circle cx="16.6" cy="7.4" r="1" fill="currentColor"/></svg>'
ICON_TIKTOK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M15.5 3h-2.4v11.2a2.4 2.4 0 1 1-2.4-2.4c.2 0 .5 0 .7.1V9.4a4.9 4.9 0 1 0 4.1 4.8V8.6c1 .8 2.2 1.3 3.5 1.3V7.4a3.4 3.4 0 0 1-3.5-3.4V3Z"/></svg>'
LOGO_ENCR = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(ASSETS, 'llufan-logo-navy.png'), 'rb').read()).decode()
LOGO_BLANC = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(ASSETS, 'llufan-logo-footer.png'), 'rb').read()).decode()

COULEURS_VARIANTES = {
    'bleu': '#8FB4D9', 'bleu poudré': '#8FB4D9', 'bleu marine': '#1F3462', 'rose': '#E8A6B8',
    'rose poudré': '#E8A6B8', 'gris': '#9A9A9A', 'gris perle': '#C9C9C4', 'sauge': '#A9CBB6',
    'crème': '#F2EAD9', 'écru': '#F2EAD9', 'sable': '#DCC8A8', 'beige': '#DCC8A8',
    'duo sauge': '#A9CBB6', 'duo lilas': '#DCC8ED', 'lilas': '#DCC8ED', 'noir': '#2B2B2B',
}


def prix(valeur):
    return ("{:,}".format(int(valeur)).replace(',', ' ')) + ' DA'


def combinaisons(options):
    resultat = [[]]
    for _, valeurs in options:
        resultat = [c + [v] for c in resultat for v in valeurs]
    return resultat


# ---------------------------------------------------------------------------
# Résolution des adresses (mêmes valeurs que dans les modèles du thème)
# ---------------------------------------------------------------------------
def lien(valeur):
    """Transforme « pages/la-marque », « collections/bebe », « products/… » en
    fichier d'aperçu. Une cible absente renvoie None, comme dans la boutique."""
    if not valeur:
        return None
    v = valeur.replace('shopify://', '')
    if v.startswith('pages/'):
        cle = v.split('/', 1)[1]
        return 'contact.html' if cle == 'contact' else '%s.html' % cle
    if v.startswith('collections/'):
        cle = v.split('/', 1)[1]
        return 'collection-%s.html' % (cle if cle != 'all' else 'allaitement')
    if v.startswith('products/'):
        return 'produit-%s.html' % v.split('/', 1)[1]
    if v == 'all':
        return 'collection-allaitement.html'
    return v


def href(valeur):
    cible = lien(valeur)
    return cible if cible else '#'


# ---------------------------------------------------------------------------
# En-tête
# ---------------------------------------------------------------------------
def header_html(active='accueil', h1_logo=False):
    messages = ''.join(
        (f'<a class="announcement-bar__link prose heading{" is-selected" if i == 0 else ""}" href="{href(m["link"])}">{m["text"]}</a>'
         if lien(m['link']) else
         f'<p class="announcement-bar__link prose heading{" is-selected" if i == 0 else ""}">{m["text"]}</p>')
        for i, m in enumerate(D.BANDEAU))
    raccourcis = ''
    for p in D.PREHEADER:
        cible = lien(p['link']) or ('club-maman.html' if p['vers_le_club'] else None)
        dedans = f'{ICON.get(p["icon"], ICON["heart"])}<span>{p["label"]}</span>'
        raccourcis += (f'<a class="preheader__item" href="{cible}">{dedans}</a>' if cible
                       else f'<span class="preheader__item">{dedans}</span>')
    nav = [('Maternité', 'collection-maternite.html'), ('Bébé', 'collection-bebe.html'),
           ('Nouveautés', 'collection-nouveautes.html')]
    subnav = ''.join(f'<a href="{u}">{t}</a>' for t, u in nav)
    pastille = (f'<a class="header__pill" href="{href(D.PILL["link"])}">{D.PILL["label"]}</a>'
                if lien(D.PILL['link']) else f'<span class="header__pill">{D.PILL["label"]}</span>')
    menu = ''
    for titre, cible in nav + [('Allaitement', 'collection-allaitement.html'),
                               ('Accessoires et pièces détachées', 'collection-accessoires.html')]:
        menu += (f'<details class="drawer-header__accordion" style="border-bottom:1px solid rgb(var(--border-color) / .6)">'
                 f'<summary style="display:flex;justify-content:space-between;align-items:center;padding-block:1.1rem;text-transform:uppercase;letter-spacing:.06em">'
                 f'<span class="h6">{titre}</span><span aria-hidden="true">›</span></summary>'
                 f'<div class="drawer-header__submenu" style="display:grid;gap:.75rem;padding-block:0 1.1rem">'
                 f'<a class="h6" href="{cible}">Voir la collection</a>'
                 f'<a class="h6" href="collection-allaitement.html">Tous les produits</a></div></details>')
    balise = 'h1' if h1_logo else 'div'
    marque_logo = (f'<{balise} class="header__logo"><a href="accueil.html" aria-label="LLUFAN">'
                   f'<img class="header__logo-image" src="{LOGO_ENCR}" alt="LLUFAN"></a></{balise}>')
    return f'''
<aside class="announcement-bar color-scheme color-scheme--scheme-2">
  <div class="announcement-bar__inner announcement-bar__inner--sans-fleches">
    <announcement-bar-carousel class="announcement-bar__carousel" data-autoplay="true" data-speed="3500">{messages}</announcement-bar-carousel>
  </div>
</aside>
<div class="preheader"><div class="container"><div class="preheader__inner" data-preheader>{raccourcis}</div></div></div>
<header class="header color-scheme color-scheme--scheme-1" data-header-behavior="shadow">
  <div class="container">
    <div class="header__row">
      <button type="button" class="header__burger tap-area" data-drawer-open="header-menu-drawer" aria-label="Menu">{ICON['burger']}</button>
      {marque_logo}

      <div class="header__icons">
        <details class="header__locale"><summary><span>Français</span>{ICON['chevron-down']}</summary>
          <div class="header__locale-popover"><button type="button">Français</button><button type="button">العربية</button></div></details>
        <a href="compte.html" class="tap-area" aria-label="Compte">{ICON['account']}</a>
        <a href="recherche.html" class="tap-area" aria-label="Recherche">{ICON['search']}</a>
        <a href="panier.html" class="tap-area header__cart" aria-label="Panier"><span class="header__cart-count is-visible" data-cart-count data-cart-dot>1</span>{ICON['bag']}</a>
      </div>
    </div>
  </div>
  <div class="header__subnav-row">
    <div class="container"><nav class="header__subnav">{subnav}</nav>{pastille}</div>
  </div>
</header>

<div class="drawer drawer--menu color-scheme color-scheme--scheme-1" id="header-menu-drawer" aria-hidden="true">
  <div class="drawer__header">
    <p class="h4">Menu</p>
    <button type="button" class="tap-area" data-drawer-close aria-label="Fermer">✕</button>
  </div>
  <div class="drawer__body drawer__stagger">
    {menu}
    <div style="padding-block:1.5rem"><a class="button button--coral button--full" href="collection-allaitement.html">Tous les produits</a></div>
    <a class="h6" href="club-maman.html" style="display:flex;gap:.75rem;align-items:center;padding-block:1rem;border-top:1px solid rgb(var(--border-color) / .6);text-transform:uppercase">{ICON['flower']} Club Maman</a>
    <a class="h6" href="faq.html" style="display:flex;gap:.75rem;align-items:center;padding-block:1rem;border-top:1px solid rgb(var(--border-color) / .6);text-transform:uppercase">Aide / FAQ</a>
  </div>
</div>
'''


# ---------------------------------------------------------------------------
# Pied de page
# ---------------------------------------------------------------------------
def colonne(titre, liens):
    items = ''.join(
        (f'<a href="{href(v)}">{t}</a>' if lien(v) else f'<span class="field-empty">{t} — adresse à renseigner</span>')
        for t, v in liens)
    liens_html = f'<div class="footer__block-links">{items}</div>'
    return (f'<div class="footer__block">'
            f'<div class="footer__colonne footer__desktop-only"><p class="footer__block-title">{titre}</p>{liens_html}</div>'
            f'<details class="footer__colonne footer__mobile-only"><summary class="footer__block-title">{titre}</summary>{liens_html}</details>'
            f'</div>')


FOOTER = f'''
<div class="section-spacing section-spacing--tight color-scheme color-scheme--scheme-1 bordered-section">
  <div class="container"><div class="text-with-icons">
    <div class="text-with-icons__item"><span class="text-with-icons__icon">{ICON['shipping']}</span><div class="v-stack gap-1">
      <p class="text-with-icons__label">Livraison dans les 69 wilayas</p></div></div>
    <div class="text-with-icons__item"><span class="text-with-icons__icon">{ICON['payment']}</span><div class="v-stack gap-1">
      <p class="text-with-icons__label">Paiement à la livraison</p></div></div>
    <div class="text-with-icons__item"><span class="text-with-icons__icon">{ICON['heart']}</span><div class="v-stack gap-1">
      <p class="text-with-icons__label">Conçu pour l'allaitement</p></div></div>
  </div></div>
</div>
<div class="footer color-scheme color-scheme--scheme-2">
  <div class="container"><div class="footer__inner">
    <div class="footer__blocks">
      <div class="footer__block footer__block--marque">
        <a href="accueil.html" class="footer__marque" aria-label="LLUFAN"><img class="footer__logo" src="{LOGO_BLANC}" alt="LLUFAN" width="700" height="687"></a>
        <p class="footer__marque-phrase">Une marque algérienne dédiée au confort de la maman et du bébé.</p>
      </div>
      {colonne('LLUFAN', D.PIED['llufan'])}
      {colonne('Nos univers', D.PIED['univers'])}
      {colonne('Aide', D.PIED['aide'])}
      <div class="footer__block footer__block--contact">
        <p class="footer__block-title">Contact</p>
        <div class="footer__contact">
          <a href="https://wa.me/213772415120" class="footer__contact-lien" target="_blank" rel="noopener"><span class="footer__contact-icone">{ICON_WHATSAPP}</span><span>Contactez-nous sur WhatsApp</span><strong>0772 415 120</strong></a>
          <a href="mailto:contact@llufan.com" class="footer__contact-lien"><span class="footer__contact-icone">{ICON_MAIL}</span><span>contact@llufan.com</span></a>
        </div>
      </div>
    </div>
    <div class="footer__secondaire">
      <div class="footer__block--reassurance">
        <p class="footer__reassurance-titre sr-only">Nos engagements</p>
        <ul class="footer__reassurance"><li>Livraison partout en Algérie</li><li>Paiement à la livraison</li><li>Service client LLUFAN</li></ul>
      </div>
      <div class="footer__reseaux">
        <span class="footer__reseau-vide" title="Emplacement Facebook — lien à renseigner">{ICON_FACEBOOK}</span>
        <span class="footer__reseau-vide" title="Emplacement Instagram — lien à renseigner">{ICON_INSTAGRAM}</span>
        <span class="footer__reseau-vide" title="Emplacement TikTok — lien à renseigner">{ICON_TIKTOK}</span>
        <span class="eyebrow" style="align-self:center;opacity:.7">Réseaux sociaux LLUFAN — liens à renseigner</span>
      </div>
    </div>
    <div class="footer__aside">
      <div class="footer__legal">
        <a href="{href(D.PIED['legal']['mentions'])}">Mentions légales</a>
        <a href="{href(D.PIED['legal']['cgv'])}">Conditions générales de vente</a>
        <a href="{href(D.PIED['legal']['confidentialite'])}">Politique de confidentialité</a>
        <a href="{href(D.PIED['legal']['retours'])}">Politique de retour / échange</a>
      </div>
      <div class="footer__copyright">
        <span>© 2026 LLUFAN. Tous droits réservés.</span>
        <span>Algérie · llufan.com</span>
      </div>
      <div class="footer__locales">
        <span class="eyebrow" style="opacity:.7">Devise DZD · Algérie</span>
        <span class="footer__shopify"><a href="#">Propulsé par Shopify</a></span>
      </div>
    </div>
  </div></div>
</div>
<script>{theme_js}</script>
</body></html>'''

SCRIPTS_FIN = (f'<script>window.LLUFAN_LIVRAISON_DATA = {livraison_data};</script>\n'
               f'<script>{livraison_js}</script>\n')


def page(titre, contenu, avec_entete=True, avec_scripts=True):
    html = HEAD.format(title=titre, css=css)
    if avec_entete:
        html += header_html(h1_logo=(titre == 'Accueil — démonstration'))
    html += '<main id="main">' + contenu + '</main>' + FOOTER
    if avec_scripts:
        html = html.replace('</body></html>', SCRIPTS_FIN + '</body></html>')
    return html


# ---------------------------------------------------------------------------
# Composants
# ---------------------------------------------------------------------------
def carte_produit(p, reveal=False):
    images = PRODUITS_IMG[p['handle']]
    badges = ''
    if p['handle'] == 'coussin-allaitement-nomad':
        badges = '<div class="product-card__badges"><span class="badge badge--peach">Nouveauté</span></div>'
    return f'''<product-card class="product-card"{' reveal-on-scroll="true"' if reveal else ''}>
  <div class="product-card__figure">
    {badges}
    <a class="product-card__media" href="produit-{p['handle']}.html"><img class="product-card__image" src="{images['carte']}" alt="{p['title']}"></a>
  </div>
  <div class="product-card__info">
    <a class="product-card__title h6" href="produit-{p['handle']}.html">{p['title']}</a>
    <span class="product-card__price">{prix(p['price'])}</span>
    <div class="rating"><div class="rating__stars">★★★★★</div><span class="rating__value">4,8 · 12 avis (démo)</span></div>
  </div></product-card>'''


def commande(mode, cle, sous_total, produit_titre='', variantes=None, ligne_panier=''):
    jeu = ''
    if mode == 'produit':
        jeu = ('<script type="application/json" data-llufan-variantes>'
               + json.dumps(variantes, ensure_ascii=False).replace('</', '<\\/')
               + '</script>')
    encart = ' commande-encart--produit' if mode == 'produit' else ''
    return f'''{jeu}
<span id="commander" class="commande__ancre" aria-hidden="true"></span>
<div class="commande-wrapper" id="commande-{cle}" data-llufan-commande data-mode-section="{mode}"
     data-src="" data-devise="DA" data-sous-total="{sous_total}" data-produit="{produit_titre}"
     data-lignes="{ligne_panier}" data-mode="apercu">
  <div class="commande-encart{encart}">
    <p class="commande__titre">Commander — Paiement à la livraison</p>
    <form class="commande" novalidate>
      <p class="commande__confirmation" data-llufan-confirmation role="status" hidden>Merci ! Commande enregistrée. On vous rappelle pour confirmer.</p>
      <p class="commande__avertissement" data-llufan-avertissement role="alert" hidden></p>
      <textarea name="contact[body]" data-llufan-recapitulatif hidden></textarea>
      <div class="commande__champs">
        <label class="field"><span class="field__label">Nom complet *</span><input class="input" type="text" name="contact[Nom complet]" placeholder="Nom et prénom" required></label>
        <label class="field"><span class="field__label">Téléphone *</span><input class="input" type="tel" name="contact[Téléphone]" inputmode="tel" placeholder="05 / 06 / 07 …" required></label>
        <label class="field"><span class="field__label">Wilaya *</span><select class="select" name="contact[Wilaya]" data-llufan-wilaya required><option value="">Choisir…</option></select></label>
        <label class="field"><span class="field__label">Commune *</span><select class="select" name="contact[Commune]" data-llufan-commune required disabled><option value="">Wilaya d'abord…</option></select></label>
      </div>
      <fieldset class="commande__livraison" data-llufan-type>
        <legend class="field__label">Livraison</legend>
        <label class="commande__option" data-llufan-type-item><input type="radio" name="contact[Type de livraison]" value="domicile" checked><span>À domicile</span><span class="commande__option-prix" data-llufan-prix-domicile>—</span></label>
        <label class="commande__option" data-llufan-type-item><input type="radio" name="contact[Type de livraison]" value="stop-desk"><span>Stop-desk</span><span class="commande__option-prix" data-llufan-prix-stop-desk>—</span></label>
      </fieldset>
      <div class="commande__totaux">
        <div class="commande__total-ligne"><span>Sous-total</span><span data-llufan-sous-total>{prix(sous_total // 100)}</span></div>
        <div class="commande__total-ligne"><span>Livraison</span><span data-llufan-frais>À calculer</span></div>
        <div class="commande__total-ligne commande__total-ligne--total"><span>Total</span><span data-llufan-total>—</span></div>
      </div>
      <button type="submit" class="button button--coral button--lg commande__bouton" data-llufan-bouton>Commander maintenant</button>
      <div class="commande__reassurance"><span>Sans paiement en ligne</span><span>Commande protégée</span></div>
    </form>
    <div class="commande__infos"><p>Livraison 2 à 5 jours ouvrés</p><p class="text-subdued">Partout en Algérie · Paiement à la livraison</p></div>
  </div>
  <div class="commande__barre-espace" aria-hidden="true"></div>
  <div class="commande__barre">
    <span class="commande__barre-montant" data-llufan-sticky-total>—</span>
    <a href="#commande-{cle}" class="button button--navy" data-llufan-sticky>Commander</a>
  </div>
</div>
'''


def accordeons(items):
    return ''.join(
        f'<details class="accordion"><summary class="accordion__toggle"><span>{a["titre"]}</span>'
        f'<span class="animated-plus" aria-hidden="true"></span></summary>'
        f'<div class="accordion__content prose">{a["texte"]}</div></details>'
        for a in items if a.get('titre'))


def bloc_faq(items, titre='Questions fréquentes', eyebrow='', contact_label='', contact_href=None):
    corps = ''.join(
        f'<details class="accordion"><summary class="accordion__toggle"><span>{q["q"]}</span>'
        f'<span class="animated-plus" aria-hidden="true"></span></summary>'
        f'<div class="accordion__content prose">{q["a"]}</div></details>' for q in items)
    lien = (f'<div><a class="button button--outline" href="{contact_href}">{contact_label}</a></div>'
            if contact_label and contact_href else '')
    return f'''
<div class="section-spacing color-scheme color-scheme--scheme-1 bordered-section">
  <div class="container container--md"><div class="v-stack gap-6">
    <div class="v-stack gap-2">
      {f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}
      <h2 class="h3">{titre}</h2>
    </div>
    <div>{corps}</div>
    {lien}
  </div></div>
</div>'''


# ---------------------------------------------------------------------------
# ACCUEIL
# ---------------------------------------------------------------------------
def section_hero():
    slides = ''
    for i, s in enumerate(D.ACCUEIL['hero']['slides']):
        visuel = IMG['hero-1'] if i == 0 else IMG['hero-2']
        slides += f'''<div class="slideshow__slide{' is-selected' if i == 0 else ''}" media-type="image">
    <img class="slideshow__slide-media" src="{visuel}" alt="">
    <div class="container"><div class="slideshow__slide-content">
      {f'<p class="hero__kicker">{s["kicker"]}</p>' if s.get('kicker') else ''}
      <h2 class="hero__title h1">{s['heading']}</h2>
      {f'<a class="button button--coral" href="{href(s["button_link"])}">{s["button_label"]}</a>' if s.get('button_label') else ''}
    </div></div>
  </div>'''
    return f'''<slideshow-carousel id="slideshow-accueil" class="slideshow color-scheme color-scheme--scheme-3"
  allow-swipe data-autoplay="true" data-speed="5"
  style="--hero-height:78vh; --slideshow-progress-duration:5000ms">
  {slides}
  <div class="hero__scroll"><span class="circle-button hover\\:animate-icon-block">⌄</span></div>
</slideshow-carousel>
<span id="section-after-hero"></span>'''


def section_icons():
    items = ''.join(
        f'<div class="text-with-icons__item text-with-icons__item--stacked"><span class="text-with-icons__icon">{ICON[i["icon"]]}</span>'
        f'<div class="v-stack gap-1"><p class="text-with-icons__label">{i["text"]}</p></div></div>'
        for i in D.ACCUEIL['icons'])
    return f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="text-with-icons text-with-icons--stacked">{items}</div></div>
</div>'''


def section_univers():
    cartes = ''
    for i, c in enumerate(D.ACCUEIL['univers']['cards']):
        visuel = IMG['univers-%d' % (i + 1)]
        badge = (f'<span class="collection-card__badge badge badge--{c["badge_color"]}">{c["badge"]}</span>'
                 if c.get('badge') else '')
        bouton = (f'<span class="button button--navy">{c["button_label"]}</span>'
                  if c.get('button_label') else '')
        cartes += f'''<a class="collection-card" href="{href(c['link'])}">
          <img src="{visuel}" alt="{c['title']}">
          <span class="collection-card__overlay"></span>{badge}
          <div class="collection-card__content"><span class="collection-card__title">{c['title']}</span>{bouton}</div></a>'''
    return f'''
<div class="section-spacing color-scheme color-scheme--scheme-4">
  <div class="container"><div class="section-stack">
    <div class="v-stack gap-4 text-center justify-self-center"><h2 class="h2--serif">{D.ACCUEIL['univers']['heading']}</h2></div>
    <div class="collection-cards">{cartes}</div>
  </div></div>
</div>'''


def section_selection():
    S = D.ACCUEIL['selection']
    produits = [p for p in D.PRODUITS if S['collection'] in p['collections'].split(', ')]
    # reveal=False : dans le thème, ce carrousel ne passe pas par l'apparition au défilement
    cartes = ''.join(carte_produit(p) for p in produits[:S['products_count']])
    return f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="section-stack">
    <div class="v-stack gap-4 text-center justify-self-center">
      <h2 class="h2">{S['heading']}</h2></div>
    <div class="carousel-wrapper relative">
      <scroll-carousel class="product-list product-list--carousel scroll-area">{cartes}</scroll-carousel>
      <div class="carousel-nav" style="position:absolute;top:-3.25rem;right:0">
        <span class="circle-button circle-button--sm">←</span><span class="circle-button circle-button--sm">→</span></div>
    </div>
    <div class="justify-self-center"><a class="button" href="{href(S['button_link'])}">{S['button_label']}</a></div>
  </div></div>
</div>'''


def section_avis():
    A = D.ACCUEIL['avis']
    blocs = ''.join(
        f'''<div class="testimonial{' is-selected' if i == 0 else ''}">
        <div class="testimonial__rating" role="img" aria-label="{a['stars']} / 5">{ICON['star'] * a['stars']}</div>
        <blockquote class="testimonial__quote">{a['quote']}</blockquote>
        <p class="testimonial__author">{a['author']}</p></div>''' for i, a in enumerate(A['items']))
    points = ''.join(f'<button type="button" aria-current="{"true" if i == 0 else "false"}" aria-label="Avis {i + 1}"></button>'
                     for i in range(len(A['items'])))
    return f'''
<style>#apercu-avis {{ --testimonials-font-size: {A['text_size']}px; }}</style>
<div class="section-spacing color-scheme color-scheme--scheme-2" id="apercu-avis">
  <div class="container"><div class="section-stack testimonials">
    <div class="section-header"><div class="prose"><h2 class="h2">{A['heading']}</h2></div></div>
    <testimonial-carousel class="testimonial-list" id="testimonials-apercu" allow-swipe data-autoplay="true" data-speed="7000">{blocs}</testimonial-carousel>
    <carousel-navigation class="page-dots" data-carousel-dots="testimonials-apercu">{points}</carousel-navigation>
  </div></div>
</div>'''


def section_editorial(ed=None, images=('editorial', 'nomad')):
    E = ed or D.ACCUEIL['editorial']
    secondaire = IMG[images[1]]
    return f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--md">
    <div class="media-with-text">
      <div class="media-with-text__media">
        <div class="media-with-text__image-main"><img src="{IMG[images[0]]}" alt=""></div>
        <div class="media-with-text__image-secondary"><img src="{secondaire}" alt=""></div>
      </div>
      <div class="media-with-text__content">
        {f'<p class="eyebrow">{E["eyebrow"]}</p>' if E.get('eyebrow') else ''}
        <h2 class="h2 media-with-text__title">{E['heading']}</h2>
        <div class="prose text-subdued">{E['text']}</div>
        {f'<a class="button button--navy media-with-text__button" href="{href(E["button_link"])}">{E["button_label"]}</a>' if E.get('button_label') else ''}
      </div>
    </div>
  </div>
</div>'''


def page_accueil():
    contenu = (section_hero() + section_icons() + section_univers() + section_selection()
               + section_avis() + section_editorial())
    return page('Accueil — démonstration', contenu)


# ---------------------------------------------------------------------------
# COLLECTION
# ---------------------------------------------------------------------------
def page_collection(col):
    produits = [p for p in D.PRODUITS if col['handle'] in p['collections'].split(', ')]
    cartes = ''.join(carte_produit(p, reveal=True) for p in produits)
    return page(col['title'], f'''
<div class="collection-banner color-scheme color-scheme--scheme-3">
  <img class="collection-banner__image" src="{IMG['banniere']}" alt="{col['title']}">
  <div class="collection-banner__content"><div class="prose text-center">
    <h1 class="h1--serif">{col['title']}</h1>
    <div class="collection-description">{col['body']}</div>
  </div></div>
</div>
<div class="section-spacing section-spacing--no-top">
  <div class="container"><div class="v-stack gap-6">
    <div class="collection-toolbar">
      <div class="collection-toolbar__buttons">
        <span class="collection-toolbar__button">≡ Filtrer</span>
        <span class="collection-toolbar__button">↕ Trier par</span>
      </div>
      <p class="collection-toolbar__count">{len(produits)} produits</p>
    </div>
    <product-list class="product-list">{cartes}</product-list>
  </div></div>
</div>''' + bloc_faq(D.FAQ_COURTE['items'], eyebrow='', contact_label='',
                     contact_href=None))


# ---------------------------------------------------------------------------
# PRODUIT
# ---------------------------------------------------------------------------
def page_produit(p):
    images = PRODUITS_IMG[p['handle']]
    options_html = ''
    for nom, valeurs in p['options']:
        est_couleur = nom.lower() in ('couleur', 'coloris')
        if est_couleur:
            valeurs_html = ''.join(
                f'<button type="button" class="color-swatch{" is-selected" if i == 0 else ""}" '
                f'style="background:{COULEURS_VARIANTES.get(v.lower(), "#DDE1E7")}" data-variante="{i + 1}" '
                f'data-couleur="{v}" title="{v}" aria-label="{v}"></button>' for i, v in enumerate(valeurs))
        else:
            valeurs_html = ''.join(
                f'<button type="button" class="variant-picker__value{" is-selected" if i == 0 else ""}" '
                f'data-variante="{i + 1}">{v}</button>' for i, v in enumerate(valeurs))
        options_html += f'''<fieldset class="variant-picker__option" data-apercu-options>
          <legend class="variant-picker__option-label">{nom} : <span class="text-subdued" data-couleur-choisie>{valeurs[0]}</span></legend>
          <div class="variant-picker__values">{valeurs_html}</div>
        </fieldset>'''

    variantes = [{"id": i + 1, "titre": ' / '.join(c), "prix": int(p['price']) * 100, "dispo": True}
                 for i, c in enumerate(combinaisons(p['options']))]
    B = D.PRODUIT['badges']
    badges = ''.join(f'<span class="badge badge--{B["color_%d" % i]}">{B["label_%d" % i]}</span>'
                     for i in range(1, 5) if B['label_%d' % i])
    trust = ''.join(f'<div class="text-with-icons__item"><span class="text-with-icons__icon">{ICON[t["icon"]]}</span>'
                    f'<span class="text-with-icons__label" style="font-size:var(--text-base)">{t["label"]}</span></div>'
                    for t in D.PRODUIT['trust'])
    autres = [q for q in D.PRODUITS if q['handle'] != p['handle']][:4]
    contenu = f'''
<div class="section-spacing section-spacing--tight">
  <div class="container"><div class="product">
    <div class="product-gallery">
      <div class="product-gallery__carousel"><div class="product-gallery__media">
        <img src="{images['fiche']}" alt="{p['title']}"></div></div>
    </div>
    <div class="product-info">
      <div class="badge-list">{badges}</div>
      <h1 class="product-info__title h1">{p['title']}</h1>
      <div class="product-info__price">{prix(p['price'])}</div>
      <div class="product-info__rating"><div class="rating__stars">★★★★★</div><span class="rating__value">4,8 · 12 avis (démo)</span></div>
      <variant-picker class="variant-picker">{options_html}</variant-picker>
      <form class="shopify-product-form" onsubmit="return false">
        <input type="hidden" name="id" value="1">
        <div class="h-stack gap-4 items-center">
          <div class="quantity-selector">
            <button type="button" class="quantity-selector__button" data-quantity-button="minus">−</button>
            <input class="quantity-selector__input" type="number" name="quantity" value="1" min="1" aria-label="Quantité">
            <button type="button" class="quantity-selector__button" data-quantity-button="plus">+</button>
          </div>
        </div>
        <div class="buy-buttons"><a class="button button--outline button--full button--lg" href="panier.html">Ajouter au panier</a></div>
      </form>
      {commande('produit', 'produit', int(p['price']) * 100, produit_titre=p['title'], variantes=variantes)}
      {accordeons(D.PRODUIT['accordeons'])}
      <div class="text-with-icons" style="gap:1rem 2rem">{trust}</div>
      <div class="v-stack gap-3"><h2 class="h4">Description</h2><div class="prose">{p['body']}</div></div>
    </div>
  </div></div>
</div>''' + section_editorial(D.PRODUIT['editorial']) \
        + bloc_faq(D.FAQ_COURTE['items'], contact_label='', contact_href=None) + f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="section-stack">
    <h2 class="h2 text-center">{D.PRODUIT['related_heading']}</h2>
    <div class="product-list">{''.join(carte_produit(q) for q in autres)}</div>
  </div></div>
</div>'''
    return page(p['title'], contenu)


# ---------------------------------------------------------------------------
# PANIER
# ---------------------------------------------------------------------------
def ligne_panier(p, couleur, qty=1):
    images = PRODUITS_IMG[p['handle']]
    return f'''<div class="line-item">
  <a class="line-item__image" href="produit-{p['handle']}.html"><img src="{images['vignette']}" alt="{p['title']}"></a>
  <div class="v-stack gap-1">
    <a class="line-item__title" href="produit-{p['handle']}.html">{p['title']}</a>
    <span class="line-item__properties">Couleur : {couleur}</span>
    <div class="h-stack gap-4 items-center">
      <div class="quantity-selector"><span class="quantity-selector__button">−</span><span class="quantity-selector__input">{qty}</span><span class="quantity-selector__button">+</span></div>
      <span class="line-item__price">{prix(p['price'])}</span>
    </div>
  </div>
  <span class="tap-area">🗑</span>
</div>'''


def page_panier():
    nomad = D.PRODUITS[0]
    housse = D.PRODUITS[3]
    lignes = ligne_panier(nomad, 'Bleu', 1) + ligne_panier(housse, 'Rose', 1)
    total = (int(nomad['price']) + int(housse['price'])) * 100
    drawer = f'''
<div class="drawer color-scheme color-scheme--scheme-1" style="transform:none;visibility:visible;position:static;width:100%;max-width:26rem;margin:0 auto 4rem;box-shadow:var(--shadow-md);height:34rem">
  <div class="drawer__header"><p class="h4">Panier</p><span class="tap-area">✕</span></div>
  <div class="drawer__body"><div class="line-items">{ligne_panier(nomad, 'Bleu', 1)}</div></div>
  <div class="drawer__footer">
    <div class="cart-totals"><div class="cart-totals__row cart-totals__row--total"><span>Sous-total</span><span>{prix(nomad['price'])}</span></div></div>
    <a href="panier.html#commander" class="button button--navy button--full">Commander</a>
    <a href="panier.html" class="text-center" style="font-size:var(--text-sm);text-decoration:underline">Voir le panier</a>
  </div>
</div>
<div class="container text-center" style="margin-block-end:3rem"><span class="eyebrow">Aperçu du tiroir panier (affiché ouvert ici pour la vérification)</span></div>'''
    contenu = f'''
<div class="section-spacing">
  <div class="container container--md"><div class="section-stack">
    <h1 class="h2 text-center">Panier</h1>
    <div class="line-items">{lignes}</div>
    <p class="cart-update"><button class="cart-update__button">Mettre à jour</button></p>
  </div></div>
</div>
{commande('panier', 'panier', total, ligne_panier='1 × ' + nomad['title'] + ' : ' + prix(nomad['price']))}
{drawer}'''
    return page('Panier', contenu, avec_entete=False)


def page_panier_vide():
    return page('Panier', '''
<div class="section-spacing">
  <div class="container container--xs">
    <div class="empty-state">
      <div class="prose">
        <h1 class="h4">Panier</h1>
        <p>Votre panier est vide</p>
        <a href="collection-allaitement.html" class="button">Continuer mes achats</a>
      </div>
    </div>
  </div>
</div>''')


# ---------------------------------------------------------------------------
# CLUB MAMAN
# ---------------------------------------------------------------------------
def page_club():
    C = D.CLUB
    espaces = ''.join(
        (f'<a class="club__espace" href="{href(e["lien"])}">' if lien(e['lien']) else '<div class="club__espace">')
        + f'<span class="club__espace-icone">{ICON.get(e["icone"], ICON["flower"])}</span>'
        + f'<span class="club__espace-titre">{e["titre"]}</span><span class="club__espace-texte">{e["texte"]}</span>'
        + ('</a>' if lien(e['lien']) else '</div>')
        for e in C['espaces'])
    discussions = ''.join(
        (f'<a class="club__discussion" href="{href(d["lien"])}">' if lien(d['lien']) else '<div class="club__discussion">')
        + f'<span class="club__discussion-titre">{d["titre"]}</span>'
        + f'<span class="club__discussion-extrait">{d["extrait"]}</span>'
        + f'<span class="club__discussion-meta"><span>{d["autrice"]}</span>'
        + f'<span>{d["reponses"]} réponses</span><span>{d["likes"]} j\'aime</span></span>'
        + ('</a>' if lien(d['lien']) else '</div>')
        for d in C['discussions'])
    contenu = f'''
<div class="section-spacing">
  <div class="container"><div class="section-stack">
    <div class="club__accueil">
      <p class="eyebrow">{C['eyebrow']}</p>
      <h1 class="h2--serif">{C['heading']}</h1>
      <div class="prose club__intro">{C['intro']}</div>
    </div>
    <div class="v-stack gap-5">
      <h2 class="h5 text-center">{C['espaces_titre']}</h2>
      <div class="club__espaces">{espaces}</div>
    </div>
    <div class="v-stack gap-5">
      <h2 class="h5 text-center">{C['discussions_titre']}</h2>
      <div class="club__discussions">{discussions}</div>
    </div>
    <div class="club__ressources">
      <div class="v-stack gap-3">
        <h2 class="h5">{C['ressources_titre']}</h2>
        <div class="prose">{C['ressources_texte']}</div>
      </div>
      <a href="{href(C['ressources_lien'])}" class="button button--navy">{C['ressources_bouton']}</a>
    </div>
    <div class="club__rejoindre" id="rejoindre-le-club">
      <h2 class="h5">{C['rejoindre_titre']}</h2>
      <div class="prose club__intro">{C['rejoindre_texte']}</div>
      <form class="club__formulaire" onsubmit="return false">
        <label class="sr-only" for="club-email">Votre e-mail</label>
        <input id="club-email" class="input" type="email" placeholder="Votre e-mail" style="padding:.65rem .8rem;border:1px solid rgb(var(--border-color))">
        <button type="submit" class="button button--coral">Je m'inscris</button>
      </form>
      <p class="club__note">{C['rejoindre_note']}</p>
      <div class="club__rejoindre-liens">
        <a class="link" href="compte.html">Créer mon compte</a>
        <a class="button button--outline whatsapp-bouton" href="https://wa.me/213772415120" target="_blank" rel="noopener">{ICON_WHATSAPP}<span>Contactez-nous sur WhatsApp</span></a>
      </div>
    </div>
  </div></div>
</div>'''
    return page('Club Maman', contenu)


# ---------------------------------------------------------------------------
# PAGES D'INFORMATION, FAQ, CONTACT, RECHERCHE
# ---------------------------------------------------------------------------
def page_information(cle):
    P = D.PAGES[cle]
    blocs = ''
    for b in P['blocs']:
        l = lien(b.get('lien'))
        lien_html = (f'<a class="link info-page__lien" href="{l}">{b["lien_label"]}</a>'
                     if b.get('lien_label') and l else '')
        blocs += f'''<div class="info-page__bloc">
          <span class="info-page__icone">{ICON.get(b['icone'], ICON['heart'])}</span>
          <div class="v-stack gap-2">
            <h3 class="h6">{b['titre']}</h3>
            <div class="prose info-page__texte">{b['texte']}</div>
            {lien_html}
          </div></div>'''
    cta = lien(P.get('cta_lien'))
    cta_html = (f'<div><a class="button" href="{cta}">{P["cta_label"]}</a></div>'
                if P.get('cta_label') and cta else '')
    contenu = f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--md">
    <div class="section-stack">
      <div class="section-header"><h1 class="h1">{P['titre_attendu']}</h1></div>
      <p class="info-page__demo">{D.BANDEAU_DEMO_INFO}</p>
      <div class="v-stack gap-2">
        {f'<p class="eyebrow">{P["eyebrow"]}</p>' if P.get('eyebrow') else ''}
        <h2 class="h3">{P['heading']}</h2>
      </div>
      <div class="prose">{P['intro']}</div>
      <div class="info-page__blocs">{blocs}</div>
      {f'<div class="prose info-page__note">{P["note"]}</div>' if P.get('note') else ''}
      {cta_html}
    </div>
  </div>
</div>'''
    return page(P['titre_attendu'], contenu)


def page_faq():
    F = D.FAQ_PAGE
    contenu = f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--md">
    <div class="section-header"><h1 class="h1">Questions fréquentes</h1></div>
  </div>
</div>''' + bloc_faq(F['items'], titre=F['heading'], eyebrow=F['eyebrow'],
                     contact_label=F['contact_label'], contact_href=lien(F['contact_link']))
    return page('Questions fréquentes', contenu)


def page_contact():
    contenu = f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--md"><div class="section-stack">
    <div class="section-header">
      <h1 class="h1">Contact</h1>
      <div class="prose"><p>Une question sur un produit, une commande en cours ou un échange ?
      Écrivez-nous sur WhatsApp : c'est le moyen le plus rapide de nous joindre.</p></div>
    </div>
    <div class="contact-whatsapp">
      <a class="button button--coral whatsapp-bouton" href="https://wa.me/213772415120" target="_blank" rel="noopener">{ICON_WHATSAPP}<span>Contactez-nous sur WhatsApp — 0772 415 120</span></a>
      <a class="footer__contact-lien" href="mailto:contact@llufan.com">{ICON_MAIL}<span>contact@llufan.com</span></a>
    </div>
    <form class="v-stack gap-4" onsubmit="return false">
      <div class="h-stack gap-4 wrap">
        <label class="field" style="flex:1"><span class="field__label">Nom</span><input class="input" type="text"></label>
        <label class="field" style="flex:1"><span class="field__label">E-mail</span><input class="input" type="email"></label>
      </div>
      <label class="field"><span class="field__label">Sujet</span><input class="input" type="text"></label>
      <label class="field"><span class="field__label">Message</span><textarea class="textarea" rows="6"></textarea></label>
      <button type="submit" class="button button--navy">Envoyer</button>
    </form>
  </div></div>
</div>'''
    return page('Contact', contenu)


def page_recherche():
    resultats = [p for p in D.PRODUITS if 'coussin' in p['handle'] or 'coussin' in p['title'].lower()][:3]
    contenu = f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="v-stack gap-6">
    <div class="section-header"><h1 class="h2">Recherche</h1></div>
    <label class="field" style="max-width:32rem">
      <span class="field__label">Que cherchez-vous ?</span>
      <input class="input" type="search" value="coussin" placeholder="Coussin, gigoteuse, poncho…">
    </label>
    <p class="text-subdued">{len(resultats)} résultats pour « coussin »</p>
    <product-list class="product-list">{''.join(carte_produit(p) for p in resultats)}</product-list>
  </div></div>
</div>'''
    return page('Recherche', contenu)


# ---------------------------------------------------------------------------
# Génération
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# JOURNAL (blog) ET PAGE INTROUVABLE
# ---------------------------------------------------------------------------
def page_journal():
    cartes = ''
    for i, a in enumerate(D.JOURNAL['articles']):
        visuel = IMG['univers-%d' % (i % 4 + 1)]
        cartes += f'''<article class="product-card">
      <div class="product-card__figure">
        <a class="product-card__media" href="article-{a['handle']}.html"><img class="product-card__image" src="{visuel}" alt="{a['titre']}"></a>
      </div>
      <div class="product-card__info">
        <a class="product-card__title h6" href="article-{a['handle']}.html">{a['titre']}</a>
        <span class="text-subdued" style="font-size:var(--text-sm)">{a['date']}</span>
        <span class="text-subdued" style="font-size:var(--text-sm)">{a['chapeau']}</span>
      </div></article>'''
    return page(D.JOURNAL['titre'], f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="section-stack">
    <div class="section-header"><h1 class="h2">{D.JOURNAL['titre']}</h1></div>
    <div class="product-list">{cartes}</div>
  </div></div>
</div>''')


def page_article(a):
    return page(a['titre'], f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--md">
    <article class="v-stack gap-6">
      <header class="v-stack gap-3 text-center">
        <h1 class="h1--serif">{a['titre']}</h1>
        <p class="text-subdued">{a['date']} · {a['auteur']}</p>
      </header>
      <img src="{IMG[a['image']]}" alt="{a['titre']}">
      <div class="prose page-content">{a['contenu']}</div>
    </article>
  </div>
</div>''')


def page_404():
    return page('Page introuvable', '''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container">
    <div class="main-404">
      <h1 class="h1">Page introuvable</h1>
      <p class="text-subdued">La page demandée n'existe pas ou a été déplacée.</p>
      <a href="collection-allaitement.html" class="button">Continuer mes achats</a>
    </div>
  </div>
</div>''')



def page_collections():
    """Liste des collections de la boutique (modèle `list-collections.json`).
    Cette adresse existe toujours dans Shopify (/collections) : la page est
    générée pour que l'aperçu couvre tous les modèles du thème."""
    cartes = ''
    for i, col in enumerate(D.COLLECTIONS):
        visuel = IMG['univers-%d' % (i % 4 + 1)]
        cartes += f'''<a class="collection-card" href="collection-{col['handle']}.html" style="--card-ratio: 4 / 3">
        <img src="{visuel}" alt="{col['title']}">
        <span class="collection-card__overlay"></span>
        <div class="collection-card__content"><span class="collection-card__title">{col['title']}</span>
        <span class="button button--navy">Découvrir</span></div></a>'''
    return page('Nos collections', f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container"><div class="section-stack">
    <div class="section-header"><h1 class="h2">Nos collections</h1></div>
    <div class="collection-cards">{cartes}</div>
  </div></div>
</div>''')



def page_compte():
    """Connexion et création de compte — reprend les classes des modèles
    templates/customers/login.liquid et register.liquid du thème. Dans la
    boutique, ces formulaires sont rendus par Shopify ; l'aperçu en montre la
    mise en forme et les champs."""
    return page('Compte', f'''
<div class="section-spacing color-scheme color-scheme--scheme-1">
  <div class="container container--narrow">
    <div class="section-stack">
      <div class="section-header">
        <h1 class="h2">Votre compte</h1>
        <p class="text-subdued">Connectez-vous pour suivre vos commandes, ou créez un compte en quelques secondes.</p>
      </div>

      <div class="v-stack gap-4">
        <h2 class="h4">Connexion</h2>
        <form class="v-stack gap-4" onsubmit="return false">
          <label class="field"><span class="field__label">E-mail</span><input class="input" type="email" autocomplete="email"></label>
          <label class="field"><span class="field__label">Mot de passe</span><input class="input" type="password" autocomplete="current-password"></label>
          <div class="h-stack gap-4 wrap items-center justify-between">
            <label class="h-stack gap-2 items-center" style="font-size:var(--text-sm)"><input type="checkbox"> <span>Se souvenir de moi</span></label>
            <a class="link-faded" href="#" style="font-size:var(--text-sm);text-decoration:underline">Mot de passe oublié ?</a>
          </div>
          <div><button type="submit" class="button button--navy">Se connecter</button></div>
        </form>
      </div>

      <div class="v-stack gap-4" style="border-block-start:1px solid rgb(var(--border-color) / .6);padding-block-start:2rem">
        <h2 class="h4">Créer un compte</h2>
        <p class="text-subdued" style="font-size:var(--text-sm)">Un compte permet de retrouver vos commandes et de rejoindre le Club Maman.</p>
        <form class="v-stack gap-4" onsubmit="return false">
          <label class="field"><span class="field__label">Prénom</span><input class="input" type="text" autocomplete="given-name"></label>
          <label class="field"><span class="field__label">Nom</span><input class="input" type="text" autocomplete="family-name"></label>
          <label class="field"><span class="field__label">E-mail</span><input class="input" type="email" autocomplete="email"></label>
          <label class="field"><span class="field__label">Mot de passe</span><input class="input" type="password" autocomplete="new-password"></label>
          <div><button type="submit" class="button button--coral">Créer mon compte</button></div>
        </form>
      </div>

      <p class="text-subdued" style="font-size:var(--text-xs)">
        Ces formulaires fonctionnent dans la boutique dès que les comptes clients sont activés
        (Paramètres → Comptes clients). L'aperçu ne peut pas créer de compte : il n'y a pas de boutique derrière.
      </p>
    </div>
  </div>
</div>''')


def main():
    os.makedirs(OUT, exist_ok=True)
    pages = {
        'accueil.html': page_accueil(),
        'panier.html': page_panier(),
        'panier-vide.html': page_panier_vide(),
        'club-maman.html': page_club(),
        'faq.html': page_faq(),
        'contact.html': page_contact(),
        'recherche.html': page_recherche(),
    }
    for col in D.COLLECTIONS:
        pages['collection-%s.html' % col['handle']] = page_collection(col)
    for p in D.PRODUITS:
        pages['produit-%s.html' % p['handle']] = page_produit(p)
    for cle in D.PAGES:
        pages['%s.html' % cle] = page_information(cle)
    pages['journal.html'] = page_journal()
    for a in D.JOURNAL['articles']:
        pages['article-%s.html' % a['handle']] = page_article(a)
    pages['404.html'] = page_404()
    pages['collections.html'] = page_collections()
    pages['compte.html'] = page_compte()
    # Alias historiques : « collection.html » et « produit.html » restent valides.
    pages['collection.html'] = pages['collection-allaitement.html']
    pages['produit.html'] = pages['produit-coussin-allaitement-nomad.html']

    total = 0
    for nom, html in pages.items():
        with open(os.path.join(OUT, nom), 'w', encoding='utf-8') as f:
            f.write(html)
        total += len(html)
        print('  preview/%-46s %5d Ko' % (nom, len(html) // 1024))
    print('%d pages — %.1f Mo au total.' % (len(pages), total / 1048576))

    # Contrôle : aucun lien interne ne doit tomber dans le vide.
    import re
    noms = set(pages)
    morts = []
    for nom, html in pages.items():
        for cible in set(re.findall(r'href="([^"#][^"]*\.html)"', html)):
            if cible not in noms:
                morts.append((nom, cible))
    print('Liens internes morts : %d' % len(morts))
    for nom, cible in sorted(set(morts))[:20]:
        print('   %s → %s' % (nom, cible))
    return 0


if __name__ == '__main__':
    sys.exit(main())
