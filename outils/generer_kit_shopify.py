#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deux fichiers pour remplir Shopify sans recopier à la main.

Ce script écrit :

  1. `LLUFAN-DEMO-contenus-a-coller.md`
     Les pages, les collections et le journal, en français ET en arabe,
     assemblés : un bloc à copier pour le titre, un bloc à copier pour le
     corps de page. On colle le français dans Shopify (Boutique en ligne →
     Pages), puis l'arabe dans « Traduire et adapter ». Aucun texte à
     retaper, aucun HTML à reconstituer.

  2. `LLUFAN-DEMO-traductions-ar.csv`
     La version réalignée du fichier de traduction : **une ligne = un champ
     tel que Shopify l'exporte** (Paramètres → Langues → Exporter). C'est ce
     qui rend le collage direct possible : dans l'ancienne version, une page
     était découpée en 11 lignes (« bloc 1 », « bloc 2 »…) alors que Shopify
     n'a qu'une seule ligne `body_html` — il fallait recoller les morceaux
     soi-même. Les corps de page sont désormais assemblés, en HTML.

Pourquoi les corps en HTML : Shopify conserve le HTML du corps de page
(titres, listes, gras). L'ancienne version retirait les balises, ce qui
faisait perdre la mise en forme à l'import.

Usage : python3 generer_kit_shopify.py
"""
import csv
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, 'demo'))

import contenu_demo as FR          # noqa: E402
import contenu_demo_ar as AR       # noqa: E402

# Les textes arabes des gabarits du thème (accueil, fiche produit, pages
# d'information, FAQ). Un texte français du thème absent de ce dictionnaire
# arrête la génération : aucun trou silencieux.
sys.path.insert(0, ICI)
from theme_textes_ar import TEXTES_AR  # noqa: E402

SORTIE_CSV = os.path.join(ICI, 'LLUFAN-DEMO-traductions-ar.csv')
SORTIE_KIT = os.path.join(ICI, 'LLUFAN-DEMO-contenus-a-coller.md')
THEME = os.path.join(ICI, 'theme')

# Les textes que l'on saisit à la main dans l'éditeur du thème (réglages de
# sections). Ils n'ont pas de fichier de contenu : ils se traduisent depuis
# « Contenu du thème », et on les repère par leur texte français.
TEXTES_DES_SECTIONS = {
    'sections/cart-drawer.liquid': {'cta_label': 'إتمام الطلب'},
    'sections/club-maman.liquid': {
        'heading': AR.CLUB['heading'],
        'espaces_titre': AR.CLUB['espaces_titre'],
        'discussions_titre': AR.CLUB['discussions_titre'],
        'rejoindre_titre': AR.CLUB['rejoindre_titre'],
        'rejoindre_bouton': 'أشترك',
        'rejoindre_confirmation': 'شكرًا، تم تسجيل اشتراكك.',
        'rejoindre_compte_label': 'إنشاء حسابي',
    },
    'sections/commande-livraison.liquid': {
        'heading': 'اطلبي — الدفع عند الاستلام',
        'cta': 'اطلبي الآن',
    },
    'sections/footer.liquid': {
        'copyright_text': 'جميع الحقوق محفوظة.',
        'copyright_line': 'الجزائر · llufan.com',
        'legal_mentions_label': AR.PAGES_TITRES['mentions-legales'],
        'legal_cgv_label': AR.PAGES_TITRES['cgv'],
        'legal_confidentialite_label': AR.PAGES_TITRES['confidentialite'],
        'legal_retours_label': AR.PAGES_TITRES['politique-de-retour'],
    },
    'sections/information.liquid': {'bandeau_demo': AR.BANDEAU_DEMO_INFO},
}


def reglages_du_schema(chemin):
    """{id du réglage: texte par défaut} d'un fichier de section du thème."""
    fichier = os.path.join(THEME, chemin)
    if not os.path.exists(fichier):
        return {}
    s = open(fichier, encoding='utf-8').read()
    m = re.search(r'(?s)\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}', s)
    if not m:
        return {}
    try:
        schema = json.loads(m.group(1))
    except ValueError:
        return {}
    return {st.get('id'): st.get('default', '')
            for st in schema.get('settings', []) if st.get('id')}


# ---------------------------------------------------------------------------
# Petits assemblage : le corps de page, en HTML propre
# ---------------------------------------------------------------------------
def p(texte):
    """Un paragraphe, si le texte n'est pas déjà balisé."""
    texte = (texte or '').strip()
    if not texte:
        return ''
    return texte if texte.startswith('<') else '<p>%s</p>' % texte


def h(niveau, texte):
    return '<h%d>%s</h%d>' % (niveau, (texte or '').strip(), niveau)


def liens_pages(chemin):
    """`pages/faq` → l'adresse de la page dans la boutique."""
    if not chemin:
        return ''
    return '/' + chemin.lstrip('/') if chemin.startswith('pages/') else chemin


def corps_information(page, langue='fr'):
    """Corps d'une page d'information : intertitre, intro, blocs, note, bouton.

    Même ordre que la page de l'aperçu, pour que la boutique et la
    démonstration racontent la même chose.
    """
    morceaux = []
    if page.get('eyebrow'):
        morceaux.append('<p class="eyebrow">%s</p>' % page['eyebrow'])
    if page.get('heading'):
        morceaux.append(h(2, page['heading']))
    morceaux.append(p(page.get('intro')))
    for bloc in page.get('blocs') or []:
        morceaux.append(h(3, bloc.get('titre', '')))
        morceaux.append(p(bloc.get('texte')))
        if bloc.get('lien_label') and bloc.get('lien'):
            morceaux.append('<p><a href="%s">%s</a></p>'
                            % (liens_pages(bloc['lien']), bloc['lien_label']))
    if page.get('note'):
        morceaux.append(p(page['note']))
    if page.get('cta_label') and page.get('cta_lien'):
        morceaux.append('<p><a href="%s">%s</a></p>'
                        % (liens_pages(page['cta_lien']), page['cta_label']))
    return '\n'.join(m for m in morceaux if m)


def corps_faq(faq):
    morceaux = ['<p class="eyebrow">%s</p>' % faq['eyebrow'], h(2, faq['heading'])]
    for item in faq['items']:
        morceaux.append(h(3, item.get('q', '')))
        morceaux.append(p(item.get('a')))
    if faq.get('contact_label'):
        morceaux.append('<p><a href="%s">%s</a></p>'
                        % (liens_pages(faq.get('contact_link', 'pages/contact')),
                           faq['contact_label']))
    return '\n'.join(m for m in morceaux if m)


def corps_club(club):
    morceaux = ['<p class="eyebrow">%s</p>' % club['eyebrow'], h(2, club['heading']),
                p(club.get('intro'))]
    if club.get('espaces_titre'):
        morceaux.append(h(3, club['espaces_titre']))
    for e in club.get('espaces') or []:
        morceaux.append('<p><strong>%s</strong><br>%s</p>'
                        % (e.get('titre', ''), e.get('texte', '')))
    if club.get('discussions_titre'):
        morceaux.append(h(3, club['discussions_titre']))
    for d in club.get('discussions') or []:
        morceaux.append(h(3, d.get('titre', '')))
        morceaux.append(p(d.get('extrait')))
        morceaux.append('<p><em>%s · %s</em></p>'
                        % (d.get('autrice', ''), d.get('date', '')) if d.get('date')
                        else '<p><em>%s</em></p>' % d.get('autrice', ''))
    for cle, niveau in (('ressources_titre', 3), ('ressources_texte', 2),
                        ('rejoindre_titre', 3), ('rejoindre_texte', 2),
                        ('rejoindre_note', 2)):
        if club.get(cle):
            morceaux.append(h(niveau, club[cle]) if niveau == 3 else p(club[cle]))
    return '\n'.join(m for m in morceaux if m)


def page_du_kit(cle, titre_fr, corps_fr, titre_ar, corps_ar):
    return {
        'cle': cle, 'titre_fr': titre_fr, 'corps_fr': corps_fr,
        'titre_ar': titre_ar, 'corps_ar': corps_ar,
    }


def pages_du_kit():
    """Les 10 pages à créer dans Shopify, français puis arabe."""
    out = []
    for cle, page in FR.PAGES.items():
        ar = AR.PAGES.get(cle)
        if not ar:
            continue
        out.append(page_du_kit(
            cle, page['titre_attendu'], corps_information(page),
            ar['titre_attendu'], corps_information(ar)))
    out.append(page_du_kit('faq', 'Questions fréquentes', corps_faq(FR.FAQ_PAGE),
                           AR.PAGES_TITRES.get('faq', 'الأسئلة الشائعة'), corps_faq(AR.FAQ_PAGE)))
    out.append(page_du_kit('club-maman', 'Club Maman', corps_club(FR.CLUB),
                           AR.PAGES_TITRES.get('club-maman', 'نادي الأمهات'), corps_club(AR.CLUB)))
    # La page Contact est presque entièrement faite par le thème : seul le
    # titre se traduit.
    out.append(page_du_kit('contact', 'Contact', '', AR.CONTACT.get('titre', 'اتصلي بنا'), ''))
    return out


# ---------------------------------------------------------------------------
# 1. Le kit « prêt à coller »
# ---------------------------------------------------------------------------
def ecrire_kit():
    pages = pages_du_kit()
    lignes = []
    a = lignes.append
    a('# LLUFAN — les contenus à coller dans Shopify')
    a('')
    a("Ce fichier évite de recopier quoi que ce soit à la main. Pour chaque")
    a("ressource : le texte **français** (à coller quand vous créez la ressource")
    a("dans Shopify) et le texte **arabe** (à coller ensuite dans")
    a("« Traduire et adapter »).")
    a('')
    a('Trois façons de coller un corps de page :')
    a('')
    a("1. dans l'éditeur de page, cliquez sur le bouton `</>` (afficher le code HTML),")
    a('   collez, puis revenez à la vue normale ;')
    a("2. ou dans « Traduire et adapter » → la ressource → le champ concerné ;")
    a("3. ou dans l'export des traductions, colonne `Translated content`.")
    a('')
    a('> Les textes sont ceux de la **démonstration** : remplacez-les par les vôtres')
    a('> quand vous voudrez, la structure reste la même.')
    a('')
    a('---')
    a('')
    a('## 1. Les 10 pages')
    a('')
    a('Boutique en ligne → **Pages** → Ajouter une page. Le « handle » indiqué est')
    a("l'adresse de la page : `llufan.com/pages/` + le handle.")
    a('')
    releve = []   # les « emplacements à compléter », page par page
    for n, page in enumerate(pages, 1):
        a('### 1.%d — %s' % (n, page['titre_fr']))
        a('')
        a('* handle : `%s` → adresse `/pages/%s`' % (page['cle'], page['cle']))
        a('')
        a('**Titre (français)** — à coller dans « Titre » :')
        a('')
        a('```text')
        a(page['titre_fr'])
        a('```')
        if page['corps_fr']:
            a('**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :')
            a('')
            a('```html')
            a(page['corps_fr'])
            a('```')
        else:
            a('*Cette page est construite par le thème : seul le titre se remplit.*')
            a('')
        a('**Titre (arabe)** — dans « Traduire et adapter » :')
        a('')
        a('```text')
        a(page['titre_ar'])
        a('```')
        if page['corps_ar']:
            a('**Corps (arabe)** :')
            a('')
            a('```html')
            a(page['corps_ar'])
            a('```')
        a('')
        # Ce qui, dans cette page, demande encore une décision de LLUFAN.
        for langue, corps in (('français', page['corps_fr']), ('arabe', page['corps_ar'])):
            for trouve in re.finditer(r'<em>(.*?)</em>', corps or '', re.S):
                texte = re.sub(r'<[^>]+>', '', trouve.group(1)).strip()
                if texte and ('compléter' in texte or 'remplacer' in texte
                              or 'يُستكمل' in texte or 'يُستبدل' in texte):
                    releve.append(('1.%d' % n, page['titre_fr'], langue, texte))

    a('---')
    a('')
    a('## 2. Les 5 collections')
    a('')
    a('Produits → **Collections** → Créer une collection. Le handle doit être')
    a("exactement celui-ci : c'est lui que le thème appelle.")
    a('')
    for c in FR.COLLECTIONS:
        ca = next((x for x in AR.COLLECTIONS if x['handle'] == c['handle']), None)
        a('### %s — `%s`' % (c['title'], c['handle']))
        a('')
        a('```text')
        a('Titre (français) : ' + c['title'])
        a('```')
        a('```html')
        a(c['body'].strip())
        a('```')
        if ca:
            a('```text')
            a('Titre (arabe) : ' + ca['title'])
            a('```')
            if ca.get('body'):
                a('```html')
                a(ca['body'].strip())
                a('```')
        a('')

    a('---')
    a('')
    a('## 3. Le journal et ses 3 articles')
    a('')
    a('Contenu → **Blog posts** → Gérer les blogs → Ajouter un blog (`%s`),'
      % FR.JOURNAL['titre'])
    a("puis les trois articles.")
    a('')
    a('```text')
    a('Nom du blog (français) : ' + FR.JOURNAL['titre'])
    a('Nom du blog (arabe)    : ' + AR.JOURNAL_TITRE)
    a('```')
    a('')
    for na, art in enumerate(FR.JOURNAL['articles'], 1):
        ara = next((x for x in AR.JOURNAL['articles'] if x['handle'] == art['handle']), None)
        a('### %s' % art['titre'])
        a('')
        a('* handle : `%s`' % art['handle'])
        a('')
        a('```text')
        a('Titre (français) : ' + art['titre'])
        a('Auteur : ' + art.get('auteur', ''))
        a('```')
        a('```html')
        a('<p><em>%s</em></p>' % art.get('chapeau', ''))
        a(art.get('contenu', '').strip())
        a('```')
        if ara:
            a('```text')
            a('Titre (arabe) : ' + ara['titre'])
            a('Auteur : ' + ara.get('auteur', ''))
            a('```')
            a('```html')
            a('<p><em>%s</em></p>' % ara.get('chapeau', ''))
            a(ara.get('contenu', '').strip())
            a('```')
        a('')
        # Les mêmes marqueurs, côté articles du journal.
        for langue, morceaux in (('français', [art.get('chapeau', ''), art.get('contenu', '')]),
                                 ('arabe', [ara.get('chapeau', ''), ara.get('contenu', '')] if ara else [])):
            for morceau in morceaux:
                for trouve in re.finditer(r'<em>(.*?)</em>', morceau or '', re.S):
                    texte = re.sub(r'<[^>]+>', '', trouve.group(1)).strip()
                    if texte and ('compléter' in texte or 'remplacer' in texte
                                  or 'يُستكمل' in texte or 'يُستبدل' in texte):
                        releve.append(('3.%d' % na, art['titre'], langue, texte))

    a('---')
    a('')
    a('## 4. Ce qui n\'est pas ici')
    a('')
    a('- **Les produits** : ils s\'importent par le fichier `LLUFAN-DEMO-produits.csv`')
    a('  (Produits → Importer), puis leurs traductions par le fichier')
    a('  `LLUFAN-DEMO-traductions-ar.csv`.')
    a('- **Les libellés de l\'interface** (Panier, Filtrer, Votre nom, les messages')
    a('  du formulaire de commande) : ils sont déjà traduits dans le thème, fichier')
    a('  `locales/ar.json`, et partent avec lui.')
    a('- **Les pages Recherche, Compte et Page introuvable** : ce sont des gabarits')
    a('  du thème, rien à créer.')
    a('')
    a('---')
    a('')
    a("## 5. Les emplacements à compléter — le seul reste à faire")
    a('')
    a('Ces mentions sont **volontaires** : elles marquent les informations que')
    a('seule LLUFAN peut fournir (raison sociale, hébergeur, qui paie le retour…).')
    a('Tout le reste des pages est complet et publiable tel quel.')
    a('')
    if releve:
        a('| Réf. | Page | Langue | Ce qui manque |')
        a('|---|---|---|---|')
        for reference, titre, langue, texte in releve:
            a('| %s | %s | %s | %s |' % (reference, titre, langue, texte.replace('|', '/')))
        a('')
        a('**Règle simple : une page qui contient encore une de ces mentions ne se')
        a('publie pas.** Le plus souvent, une phrase suffit — et si une information')
        a("manque encore, mieux vaut retirer la phrase que la laisser en l'état.")
    else:
        a('Aucun : tout est complet.')
    a("### Ce qu'il faut réunir pour les remplir (8 lignes)")
    a('')
    a('| Ce qu\'il faut | Où le trouver |')
    a('|---|---|')
    a('| Raison sociale exacte | extrait du registre de commerce |')
    a('| Adresse du siège social | idem |')
    a('| Numéro de registre de commerce (RC) | idem |')
    a('| NIF / NIS | vos documents fiscaux |')
    a("| Nom et adresse de l'hébergeur | **une boutique Shopify est hébergée par Shopify** : « Shopify Inc., 151 O'Connor Street, Ground floor, Ottawa, Ontario K2P 2L8, Canada » (à confirmer selon votre contrat) |")
    a('| Qui paie les frais de retour | votre décision — deux phrases possibles ci-dessous |')
    a('| Traitements de données réellement effectués | vos outils : WhatsApp, e-mail, transporteur |')
    a('| Droits sur les photos et les textes | vous (photos et textes LLUFAN) |')
    a('')
    a('**Les frais de retour** — choisissez une phrase, elle remplace la mention 1.4 :')
    a('')
    a('- à la charge de la cliente : *« Les frais de retour sont à la charge de la cliente,')
    a("  sauf si l'article est arrivé endommagé ou ne correspond pas à la commande ; dans")
    a('  ce cas, ils sont à notre charge. »*')
    a('- à la charge de LLUFAN : *« Les frais de retour sont à notre charge pour toute')
    a('  commande retournée dans les 7 jours suivant la réception. »*')
    a('')
    a('')
    with open(SORTIE_KIT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes) + '\n')
    return len(pages)


# ---------------------------------------------------------------------------
# 2. Le fichier de traductions, réaligné sur les lignes de Shopify
# ---------------------------------------------------------------------------
def lignes_traduction():
    """(Type, Ressource, Champ, Français, العربية) — une ligne = un champ Shopify.

    `vus` retient les textes français déjà donnés plus haut : quand un même
    texte apparaît deux fois (un réglage de section et le gabarit qui s'en
    sert), une seule ligne suffit — c'est le même champ chez Shopify.
    """
    vus = set()
    yield ('ENTÊTE', '—', '—',
           "Traduction arabe — boutique LLUFAN (contenu de démonstration). "
           "Une ligne = un champ tel que Shopify l'exporte (Paramètres → Langues → Exporter). "
           "Coller la dernière colonne dans « Translated content », ligne par ligne : "
           "les colonnes « Type », « Ressource » et « Champ » permettent de se repérer.",
           "ترجمة عربية — متجر LLUFAN (محتوى تجريبي)")

    # — Produits -------------------------------------------------------------
    for p in FR.PRODUITS:
        a = next((x for x in AR.PRODUITS if x['handle'] == p['handle']), None)
        if not a:
            continue
        yield ('PRODUCT', p['handle'], 'title', p['title'], a['title'])
        yield ('PRODUCT', p['handle'], 'body_html', p['body'].strip(), a['body'].strip())
        yield ('PRODUCT', p['handle'], 'product_type', p['type'], a['type'])
        for (nom_fr, valeurs_fr), (nom_ar, valeurs_ar) in zip(p['options'], a['options']):
            yield ('PRODUCT_OPTION', p['handle'], nom_fr, nom_fr, nom_ar)
            for vf, va in zip(valeurs_fr, valeurs_ar):
                yield ('PRODUCT_OPTION_VALUE', p['handle'], nom_fr, vf, va)

    # — Collections ----------------------------------------------------------
    for c in FR.COLLECTIONS:
        a = next((x for x in AR.COLLECTIONS if x['handle'] == c['handle']), None)
        if not a:
            continue
        yield ('COLLECTION', c['handle'], 'title', c['title'], a['title'])
        yield ('COLLECTION', c['handle'], 'body_html', c['body'].strip(), a['body'].strip())

    # — Pages : une seule ligne body_html, assemblée -------------------------
    for page in pages_du_kit():
        yield ('PAGE', page['cle'], 'title', page['titre_fr'], page['titre_ar'])
        if page['corps_fr']:
            yield ('PAGE', page['cle'], 'body_html', page['corps_fr'], page['corps_ar'])

    # — Journal et articles --------------------------------------------------
    yield ('BLOG', 'journal', 'title', FR.JOURNAL['titre'], AR.JOURNAL_TITRE)
    for art in FR.JOURNAL['articles']:
        ara = next((x for x in AR.JOURNAL['articles'] if x['handle'] == art['handle']), None)
        if not ara:
            continue
        yield ('ARTICLE', art['handle'], 'title', art['titre'], ara['titre'])
        yield ('ARTICLE', art['handle'], 'excerpt', art.get('chapeau', ''), ara.get('chapeau', ''))
        yield ('ARTICLE', art['handle'], 'body_html',
               art.get('contenu', '').strip(), ara.get('contenu', '').strip())

    # — Textes saisis dans les réglages des sections (Contenu du thème) ------
    # Ils n'ont pas de fichier de contenu : ils se saisissent dans l'éditeur du
    # thème, et se traduisent depuis « Contenu du thème ». On les repère par
    # leur texte français (colonne 4), que Shopify affiche aussi.
    vivantes = valeurs_vivantes()
    type_de = lambda c: os.path.basename(c).replace('.liquid', '').replace('.json', '')
    for chemin, reglages in TEXTES_DES_SECTIONS.items():
        defauts = reglages_du_schema(chemin)
        for identifiant, arabe in reglages.items():
            vivant = vivantes.get((type_de(chemin), identifiant))
            if vivant:
                texte, gabarit, chemin_gabarit = vivant
                yield ('ONLINE_STORE_THEME', gabarit,
                       '%s (réglage « %s »)' % (chemin_gabarit, identifiant), texte, arabe)
            else:
                yield ('ONLINE_STORE_THEME', chemin, 'réglage « %s »' % identifiant,
                       defauts.get(identifiant, ''), arabe)

    # — Bandeaux de l'en-tête ------------------------------------------------
    for i, message in enumerate(FR.BANDEAU, 1):
        arabe = AR.BANDEAU[i - 1] if i <= len(AR.BANDEAU) else ''
        yield ('ONLINE_STORE_THEME', 'sections/header-group.json',
               "bandeau d'annonce — message %d" % i, message['text'], arabe)
    for i, raccourci in enumerate(FR.PREHEADER, 1):
        arabe = AR.PREHEADER[i - 1][1] if i <= len(AR.PREHEADER) else ''
        yield ('ONLINE_STORE_THEME', 'sections/header-group.json',
               'pré-bandeau — raccourci %d' % i, raccourci['label'], arabe)

    # — Textes écrits dans les gabarits du thème ------------------------------
    # Accueil, fiche produit, collections, pages, FAQ, en-tête, pied de page :
    # ce sont les blocs que la cliente voit en arabe. Sans ces lignes, la page
    # reste à moitié française (relevé par l'audit du 6 octobre).
    sans_traduction = []
    for nom, chemin, francais in textes_des_gabarits():
        if francais in vus:
            continue          # déjà fourni plus haut : même champ, pas de doublon
        arabe = TEXTES_AR.get(francais)
        if arabe is None:
            sans_traduction.append('%s → %s' % (nom, francais[:60]))
            continue
        vus.add(francais)
        yield ('ONLINE_STORE_THEME', nom, chemin, francais, arabe)
    if sans_traduction:
        raise SystemExit(
            'ARRÊT : %d texte(s) du thème sans traduction arabe dans '
            'theme_textes_ar.py :\n  - %s'
            % (len(sans_traduction), '\n  - '.join(sans_traduction[:15])))

    yield ('RAPPEL', 'thème', 'locales/ar.json',
           "Libellés de l'interface (panier, filtres, formulaire de commande, recherche, "
           "compte, page introuvable)",
           "هذه العبارات مترجمة داخل القالب في ملف locales/ar.json — لا تُنسخ هنا")


def valeurs_vivantes():
    """{(type de section, nom du réglage): (texte affiché, gabarit, chemin)}.

    Sert à citer, dans le kit, le texte RÉELLEMENT affiché sur la page et non la
    valeur par défaut écrite dans le schéma de la section : un gabarit peut
    remplacer un réglage (« Commander — Paiement à la livraison » devient
    « Paiement à la livraison » sur la fiche produit). Citer la valeur du schéma
    ferait chercher la cliente pour rien dans « Contenu du thème ».
    """
    table = {}
    dossier = os.path.join(THEME, 'templates')
    fichiers = [os.path.join(dossier, x) for x in sorted(os.listdir(dossier)) if x.endswith('.json')]
    fichiers += [os.path.join(THEME, 'sections', x)
                 for x in ('header-group.json', 'footer-group.json')]
    for chemin in fichiers:
        if not os.path.exists(chemin):
            continue
        donnees = json.load(open(chemin, encoding='utf-8'))
        for sid, section in (donnees.get('sections') or {}).items():
            type_section = section.get('type')
            for cle, valeur in (section.get('settings') or {}).items():
                if isinstance(valeur, str) and valeur.strip():
                    table.setdefault((type_section, cle),
                                     (valeur, os.path.basename(chemin), '%s › %s' % (sid, cle)))
    return table


def textes_des_gabarits():
    """Les textes écrits DANS les gabarits du thème (templates/*.json et
    sections/*-group.json) : accueil, fiche produit, collections, pages
    d'information, FAQ, en-tête, pied de page.

    On ne retient que ce qui s'affiche : les couleurs, les icônes, les liens
    et les noms de menus en sont écartés (ce ne sont pas des phrases).
    """
    MORTS = ('link', 'menu', 'behavior', 'color_scheme', 'icon', 'url',
             'handle', 'collection', 'color', 'page', 'position')
    IDENTIFIANTS = {'peach', 'navy', 'sage', 'lilac', 'coral', 'gold', 'mist',
                    'DA', 'LLUFAN', 'maternite', 'allaitement', 'bebe',
                    'nouveautes', 'accessoires', 'main-menu', 'shadow'}

    def visible(cle, valeur):
        if any(x in cle for x in MORTS):
            return False
        if valeur.startswith('/') or valeur.strip() in IDENTIFIANTS:
            return False
        return True

    a_faire = []
    fichiers = [os.path.join(THEME, 'templates', x)
                for x in sorted(os.listdir(os.path.join(THEME, 'templates')))
                if x.endswith('.json')]
    fichiers += [os.path.join(THEME, 'sections', x)
                 for x in ('header-group.json', 'footer-group.json')]

    for chemin in fichiers:
        if not os.path.exists(chemin):
            continue
        donnees = json.load(open(chemin, encoding='utf-8'))
        nom = os.path.basename(chemin)
        for sid, section in (donnees.get('sections') or {}).items():
            for bid, bloc in (section.get('blocks') or {}).items():
                for cle, valeur in (bloc.get('settings') or {}).items():
                    if isinstance(valeur, str) and valeur.strip() and visible(cle, valeur):
                        a_faire.append((nom, '%s › %s › %s' % (sid, bid, cle), valeur))
            for cle, valeur in (section.get('settings') or {}).items():
                if isinstance(valeur, str) and valeur.strip() and visible(cle, valeur):
                    a_faire.append((nom, '%s › %s' % (sid, cle), valeur))
    return a_faire


def dedoublonner(donnees):
    """Une même phrase du thème ne doit pas apparaître deux fois dans le kit :
    c'est le même champ chez Shopify, et deux lignes feraient douter.

    On ne touche pas aux produits, collections, pages et articles : là, deux
    fiches peuvent porter le même libellé (une option « Couleur » sur plusieurs
    produits) et chaque ligne correspond à une fiche différente.
    """
    vus = set()
    propres = []
    for ligne in donnees:
        if ligne[0] != 'ONLINE_STORE_THEME':
            if ligne[3].strip():
                vus.add(ligne[3].strip())
            propres.append(ligne)
            continue
        texte = ligne[3].strip()
        if texte and texte in vus:
            continue
        if texte:
            vus.add(texte)
        propres.append(ligne)
    return propres


def ecrire_csv():
    donnees = dedoublonner(list(lignes_traduction()))
    with open(SORTIE_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        w.writerow(['Type', 'Ressource (handle)', 'Champ',
                    'Français (contenu par défaut)', 'العربية'])
        for ligne in donnees:
            w.writerow(list(ligne))
    return donnees


def main():
    n_pages = ecrire_kit()
    donnees = ecrire_csv()
    print('✓ %s' % os.path.basename(SORTIE_KIT))
    print('   %d pages, %d collections, %d articles — français et arabe assemblés'
          % (n_pages, len(FR.COLLECTIONS), len(FR.JOURNAL['articles'])))
    print('✓ %s' % os.path.basename(SORTIE_CSV))
    print('   %d lignes (une par champ Shopify)' % len(donnees))
    par_type = {}
    for l in donnees[1:]:
        par_type[l[0]] = par_type.get(l[0], 0) + 1
    for t, n in sorted(par_type.items()):
        print('     %-22s %3d' % (t, n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
