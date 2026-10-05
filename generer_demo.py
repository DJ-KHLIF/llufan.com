#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit les modèles JSON du thème Shopify à partir du contenu de démonstration.

Source unique : demo/contenu_demo.py
Sorties :
  theme/templates/index.json, collection.json, product.json, page.*.json
  theme/sections/header-group.json, footer-group.json

Usage : python3 generer_demo.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(ROOT, 'theme')
sys.path.insert(0, os.path.join(ROOT, 'demo'))
import contenu_demo as D  # noqa: E402


def ecrire(chemin, data):
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('  écrit', os.path.relpath(chemin, ROOT))


def bloc(typ, settings):
    return {"type": typ, "settings": settings}


def ordonner(blocks, type_section):
    """Assemble une section de modèle : type + blocs + ordre des blocs.
    Le type est indispensable : sans lui, Shopify ne sait pas quelle section
    rendre et la section n'apparaît pas dans la boutique."""
    return {"type": type_section, "blocks": blocks[0], "block_order": list(blocks[0].keys())}


# ---------------------------------------------------------------------------
# 1. ACCUEIL
# ---------------------------------------------------------------------------
def index_json():
    A = D.ACCUEIL
    slides = {}
    for i, s in enumerate(A['hero']['slides'], start=1):
        slides['s%d' % i] = bloc('slide', {
            "image": None,
            "kicker": s['kicker'],
            "heading": s['heading'],
            "button_label": s['button_label'],
            "button_link": s['button_link'],
        })
    hero = ordonner((slides,), 'hero')

    icones = {}
    for i, it in enumerate(A['icons'], start=1):
        icones['i%d' % i] = bloc('item', {
            "icon": it['icon'], "heading": it['heading'], "text": it['text']})
    icons = ordonner((icones,), 'text-with-icons')
    icons['settings'] = {"tight": False, "border": False, "stacked": True}

    cartes = {}
    for i, c in enumerate(A['univers']['cards'], start=1):
        cartes['c%d' % i] = bloc('collection_card', {
            "collection": c['link'].split('/', 1)[1],
            "image": None,
            "title": c['title'],
            "link": c['link'],
            "badge": c['badge'],
            "badge_color": c['badge_color'],
            "button_label": c['button_label'],
        })
    univers = ordonner((cartes,), 'featured-collections')
    univers['settings'] = {"heading": A['univers']['heading']}

    S = A['selection']
    selection = {
        "type": "featured-collection-products",
        "blocks": {"badge": bloc('badge', {
            "label": S['badge_label'], "color": S['badge_color'], "products": []})},
        "block_order": ["badge"],
        "settings": {
            "heading": S['heading'],
            "collection": S['collection'],
            "products_count": S['products_count'],
            "button_label": S['button_label'],
            "button_link": S['button_link'],
        },
    }

    avis = {}
    for i, a in enumerate(A['avis']['items'], start=1):
        avis['t%d' % i] = bloc('testimonial', {
            "stars": a['stars'], "quote": a['quote'], "author": a['author']})
    avis_section = ordonner((avis,), 'testimonials')
    avis_section['settings'] = {
        "heading": A['avis']['heading'], "text_size": A['avis']['text_size'],
        "autoplay": True, "speed": 7}

    E = A['editorial']
    editorial = {
        "type": "media-with-text",
        "settings": {
            "image_main": None, "image_secondary": None, "image_tertiary": None,
            "eyebrow": E['eyebrow'], "heading": E['heading'], "text": E['text'],
            "button_label": E['button_label'], "button_link": E['button_link'],
        },
    }

    return {
        "sections": {
            "hero": dict({"settings": {
                "height": 78, "autoplay": True, "speed": 5,
                "overlay": False, "show_scroll_button": True}}, **hero),
            "icons": icons,
            "univers": univers,
            "selection": selection,
            "video": {"type": "video", "settings": {
                "heading": A['video']['heading'], "video_url": A['video']['video_url'], "video": None}},
            "avis": avis_section,
            "editorial": editorial,
        },
        "order": ["hero", "icons", "univers", "selection", "video", "avis", "editorial"],
    }


# ---------------------------------------------------------------------------
# 2. COLLECTION
# ---------------------------------------------------------------------------
def collection_json():
    F = D.COLLECTION['faq']
    faq = {}
    for i, it in enumerate(F['items'], start=1):
        faq['q%d' % i] = bloc('item', {"question": it['q'], "answer": it['a']})
    faq_section = ordonner((faq,), 'faq')
    faq_section['settings'] = {
        "eyebrow": F['eyebrow'], "heading": F['heading'],
        "contact_label": F['contact_label'], "contact_link": F['contact_link']}
    return {
        "sections": {
            "banner": {"type": "collection-banner", "settings": {"image": None, "show_description": True}},
            "grid": {"type": "main-collection", "settings": {"show_toolbar": True, "products_per_page": 24}},
            "faq": faq_section,
        },
        "order": ["banner", "grid", "faq"],
    }


# ---------------------------------------------------------------------------
# 3. PRODUIT
# ---------------------------------------------------------------------------
def product_json():
    P = D.PRODUIT
    B = P['badges']
    accordeons = {}
    for i, a in enumerate(P['accordeons'], start=1):
        accordeons['acc-%d' % i] = bloc('accordion', {"title": a['titre'], "content": a['texte']})
    T = P['trust']
    E = P['editorial']
    F = D.FAQ_COURTE
    faq = {}
    for i, it in enumerate(F['items'], start=1):
        faq['q%d' % i] = bloc('item', {"question": it['q'], "answer": it['a']})
    faq_section = ordonner((faq,), 'faq')
    faq_section['settings'] = {
        "eyebrow": F['eyebrow'], "heading": F['heading'],
        "contact_label": F['contact_label'], "contact_link": F['contact_link']}

    blocks = {
        "badges": bloc('badges', {
            "label_1": B['label_1'], "color_1": B['color_1'],
            "label_2": B['label_2'], "color_2": B['color_2'],
            "label_3": B['label_3'], "color_3": B['color_3'],
            "label_4": B['label_4'], "color_4": B['color_4']}),
        "title": bloc('title', {}),
        "subtitle": bloc('subtitle', {"text": P['subtitle']}),
        "price": bloc('price', {}),
        "rating": bloc('rating', {}),
        "variants": bloc('variant_picker', {}),
        "buy": bloc('buy_buttons', {}),
        "commande": bloc('commande', {
            "heading": "Commander — Paiement à la livraison",
            "cta": "Commander maintenant",
            "barre_mobile": True}),
        "acc-utilisation": accordeons['acc-1'],
        "acc-entretien": accordeons['acc-2'],
        "acc-composition": accordeons['acc-3'],
        "trust": bloc('trust', {
            "icon_1": T[0]['icon'], "label_1": T[0]['label'],
            "icon_2": T[1]['icon'], "label_2": T[1]['label'],
            "icon_3": T[2]['icon'], "label_3": T[2]['label']}),
        "description": bloc('description', {"heading": "Description"}),
        "reviews": bloc('reviews', {"heading": ""}),
    }
    ordre = ["badges", "title", "subtitle", "price", "rating", "variants", "buy",
             "commande", "acc-utilisation", "acc-entretien", "acc-composition",
             "trust", "description", "reviews"]

    return {
        "sections": {
            "main": {"type": "main-product", "settings": {}, "blocks": blocks, "block_order": ordre},
            "editorial": {"type": "media-with-text", "settings": {
                "image_main": None, "image_secondary": None, "image_tertiary": None,
                "eyebrow": E['eyebrow'], "heading": E['heading'], "text": E['text'],
                "button_label": E['button_label'], "button_link": E['button_link']}},
            "faq": faq_section,
            "related": {"type": "related-products", "settings": {"heading": P['related_heading']}},
            "recent": {"type": "recently-viewed", "settings": {"heading": P['recent_heading']}},
        },
        "order": ["main", "editorial", "faq", "related", "recent"],
    }


# ---------------------------------------------------------------------------
# 4. PAGE FAQ
# ---------------------------------------------------------------------------
def faq_json():
    F = D.FAQ_PAGE
    faq = {}
    for i, it in enumerate(F['items'], start=1):
        faq['q%d' % i] = bloc('item', {"question": it['q'], "answer": it['a']})
    faq_section = ordonner((faq,), 'faq')
    faq_section['settings'] = {
        "eyebrow": F['eyebrow'], "heading": F['heading'],
        "contact_label": F['contact_label'], "contact_link": F['contact_link']}
    return {
        "sections": {
            "main": {"type": "main-page", "settings": {}},
            "faq": faq_section,
        },
        "order": ["main", "faq"],
    }


# ---------------------------------------------------------------------------
# 5. PAGE CLUB MAMAN
# ---------------------------------------------------------------------------
def club_json():
    C = D.CLUB
    blocks = {}
    for i, e in enumerate(C['espaces'], start=1):
        blocks['e%d' % i] = bloc('espace', {
            "icone": e['icone'], "titre": e['titre'], "texte": e['texte'], "lien": e['lien']})
    for i, d in enumerate(C['discussions'], start=1):
        blocks['d%d' % i] = bloc('discussion', {
            "titre": d['titre'], "extrait": d['extrait'], "autrice": d['autrice'],
            "reponses": d['reponses'], "likes": d['likes'], "lien": d['lien']})
    ordre = (['e%d' % i for i in range(1, len(C['espaces']) + 1)]
             + ['d%d' % i for i in range(1, len(C['discussions']) + 1)])
    return {
        "sections": {
            "club": {
                "type": "club-maman",
                "settings": {
                    "eyebrow": C['eyebrow'], "heading": C['heading'], "intro": C['intro'],
                    "espaces_titre": C['espaces_titre'],
                    "discussions_titre": C['discussions_titre'],
                    "discussions_vide": C['discussions_vide'],
                    "ressources_titre": C['ressources_titre'],
                    "ressources_texte": C['ressources_texte'],
                    "ressources_bouton": C['ressources_bouton'],
                    "ressources_lien": C['ressources_lien'],
                    "rejoindre_titre": C['rejoindre_titre'],
                    "rejoindre_texte": C['rejoindre_texte'],
                    "rejoindre_newsletter": True,
                    "rejoindre_bouton": "Je m'inscris",
                    "rejoindre_confirmation": "Merci, votre inscription est enregistrée.",
                    "rejoindre_note": C['rejoindre_note'],
                    "rejoindre_compte": True,
                    "rejoindre_compte_label": "Créer mon compte",
                    "rejoindre_whatsapp": True,
                },
                "blocks": blocks,
                "block_order": ordre,
            }
        },
        "order": ["club"],
    }


# ---------------------------------------------------------------------------
# 6. PAGES D'INFORMATION
# ---------------------------------------------------------------------------
def page_json(cle):
    P = D.PAGES[cle]
    blocks = {}
    for i, b in enumerate(P['blocs'], start=1):
        blocks['b%d' % i] = bloc('bloc', {
            "icone": b['icone'], "titre": b['titre'], "texte": b['texte'],
            "lien_label": b['lien_label'], "lien": b['lien']})
    info = ordonner((blocks,), 'information')
    info['settings'] = {
        "bandeau_demo": D.BANDEAU_DEMO_INFO,
        "eyebrow": P['eyebrow'], "heading": P['heading'], "intro": P['intro'],
        "note": P['note'], "cta_label": P['cta_label'], "cta_lien": P['cta_lien'],
    }
    return {
        "sections": {
            "main": {"type": "main-page", "settings": {}},
            "info": info,
        },
        "order": ["main", "info"],
    }


# ---------------------------------------------------------------------------
# 7. EN-TÊTE (bandeau, pré-bandeau, pastille)
# ---------------------------------------------------------------------------
def header_group():
    messages = {}
    for i, m in enumerate(D.BANDEAU, start=1):
        messages['message-%d' % i] = bloc('message', {"text": m['text'], "link": m['link']})
    raccourcis = {}
    for i, p in enumerate(D.PREHEADER, start=1):
        raccourcis['item-%d' % i] = bloc('item', {
            "label": p['label'], "link": p['link'],
            "vers_le_club": p['vers_le_club'], "icon": p['icon']})
    return {
        "type": "header",
        "name": "En-tête de page",
        "sections": {
            "announcement-bar": {
                "type": "announcement-bar",
                "blocks": messages,
                "block_order": list(messages.keys()),
                "settings": {"color_scheme": "2", "sticky": True, "autoplay": True, "speed": 3.5},
            },
            "preheader": {
                "type": "preheader",
                "blocks": raccourcis,
                "block_order": list(raccourcis.keys()),
                "settings": {},
            },
            "header": {
                "type": "header",
                "settings": {
                    "logo": None,
                    "menu": "main-menu",
                    "sticky": True,
                    "pill_label": D.PILL['label'],
                    "pill_link": D.PILL['link'],
                    "logo_height": 30,
                    "logo_height_mobile": 26,
                    "behavior": "shadow",
                    "show_account": True,
                },
            },
        },
        "order": ["announcement-bar", "preheader", "header"],
    }


# ---------------------------------------------------------------------------
# 8. PIED DE PAGE
# ---------------------------------------------------------------------------
def footer_group():
    def colonne(titre, liens):
        s = {"title": titre}
        for i in range(1, 7):
            if i <= len(liens):
                s['label_%d' % i] = liens[i - 1][0]
                s['link_%d' % i] = liens[i - 1][1]
            else:
                s['label_%d' % i] = ''
                s['link_%d' % i] = ''
        return s

    L = D.PIED
    rebuild = ordonner(({
        "item-1": bloc('item', {"icon": "shipping", "heading": "", "text": "Livraison dans les 69 wilayas"}),
        "item-2": bloc('item', {"icon": "payment", "heading": "", "text": "Paiement à la livraison"}),
        "item-3": bloc('item', {"icon": "heart", "heading": "", "text": "Conçu pour l'allaitement"}),
    },), 'text-with-icons')
    rebuild['settings'] = {"tight": True, "border": True, "stacked": False}

    return {
        "type": "footer",
        "name": "Pied de page",
        "sections": {
            "reassurance": rebuild,
            "footer": {
                "type": "footer",
                "blocks": {
                    "marque": bloc('brand', {"logo": "", "tagline": "", "text": ""}),
                    "llufan": bloc('menu', colonne("LLUFAN", L['llufan'])),
                    "univers": bloc('menu', colonne("Nos univers", L['univers'])),
                    "aide": bloc('menu', colonne("Aide", L['aide'])),
                    "contact": bloc('contact', {"title": "Contact", "note": ""}),
                    "engagements": bloc('reassurance', {
                        "title": "Nos engagements",
                        "line_1": "Livraison partout en Algérie",
                        "line_2": "Paiement à la livraison",
                        "line_3": "Service client LLUFAN"}),
                },
                "block_order": ["marque", "llufan", "univers", "aide", "contact", "engagements"],
                "settings": {
                    "copyright_text": "Tous droits réservés.",
                    "copyright_line": "Algérie · llufan.com",
                    "legal_mentions_label": "Mentions légales",
                    "legal_mentions": L['legal']['mentions'],
                    "legal_cgv_label": "Conditions générales de vente",
                    "legal_cgv": L['legal']['cgv'],
                    "legal_confidentialite_label": "Politique de confidentialité",
                    "legal_confidentialite": L['legal']['confidentialite'],
                    "legal_retours_label": "Politique de retour / échange",
                    "legal_retours": L['legal']['retours'],
                },
            },
        },
        "order": ["reassurance", "footer"],
    }


def main():
    print('Modèles du thème :')
    ecrire(os.path.join(THEME, 'templates', 'index.json'), index_json())
    ecrire(os.path.join(THEME, 'templates', 'collection.json'), collection_json())
    ecrire(os.path.join(THEME, 'templates', 'product.json'), product_json())
    ecrire(os.path.join(THEME, 'templates', 'page.faq.json'), faq_json())
    ecrire(os.path.join(THEME, 'templates', 'page.club-maman.json'), club_json())
    for cle in D.PAGES:
        ecrire(os.path.join(THEME, 'templates', 'page.%s.json' % cle), page_json(cle))
    print('Groupes de sections :')
    ecrire(os.path.join(THEME, 'sections', 'header-group.json'), header_group())
    ecrire(os.path.join(THEME, 'sections', 'footer-group.json'), footer_group())
    print('OK — %d fichiers.' % (6 + len(D.PAGES) + 2))


if __name__ == '__main__':
    main()
