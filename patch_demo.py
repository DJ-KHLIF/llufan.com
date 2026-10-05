#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passe unique : branche le mode démonstration sur le thème.

1. Réglage « mode_demo » (réglages du thème) + visuels de démonstration là où
   aucun visuel n'a encore été choisi.
2. Résolution des adresses saisies (« pages/… », « collections/… ») via le
   snippet « lien » : un lien dont la cible n'existe pas encore est masqué.

Script idempotent : chaque remplacement est vérifié ; si le texte est déjà
présent, l'étape est ignorée.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(ROOT, 'theme')
faits = 0
deja = 0


def patch(chemin, avant, apres, etiquette):
    global faits, deja
    p = os.path.join(THEME, chemin)
    s = open(p, encoding='utf-8').read()
    if apres in s and avant not in s:
        deja += 1
        print('  = déjà en place :', etiquette)
        return
    if s.count(avant) != 1:
        print('  ! INTROUVABLE (%d occurrence) : %s — %s' % (s.count(avant), chemin, etiquette))
        sys.exit(1)
    open(p, 'w', encoding='utf-8').write(s.replace(avant, apres))
    faits += 1
    print('  + %s — %s' % (chemin, etiquette))


def patch_n(chemin, avant, apres, n, etiquette):
    global faits, deja
    p = os.path.join(THEME, chemin)
    s = open(p, encoding='utf-8').read()
    if s.count(avant) != n:
        if apres in s:
            deja += 1
            print('  = déjà en place :', etiquette)
            return
        print('  ! %d occurrences de « %s » au lieu de %d dans %s' % (s.count(avant), etiquette, n, chemin))
        sys.exit(1)
    open(p, 'w', encoding='utf-8').write(s.replace(avant, apres))
    faits += 1
    print('  + %s — %s (%d)' % (chemin, etiquette, n))


# ---------------------------------------------------------------------------
# 1. Réglages du thème : case « mode démonstration »
# ---------------------------------------------------------------------------
def reglages():
    p = os.path.join(THEME, 'config', 'settings_schema.json')
    s = json.load(open(p, encoding='utf-8'))
    for groupe in s:
        if groupe.get('name') == 'Identité':
            ids = [x.get('id') for x in groupe['settings']]
            if 'mode_demo' not in ids:
                groupe['settings'].append({
                    "type": "checkbox",
                    "id": "mode_demo",
                    "label": "Mode démonstration (visuels fictifs)",
                    "default": False,
                    "info": ("Utilise les visuels de démonstration livrés avec le thème partout où "
                             "aucun visuel n'a encore été choisi (diaporama, cartes d'univers, bandeau "
                             "de collection, bloc éditorial). À décocher avant la mise en ligne : "
                             "les visuels LLUFAN choisis dans les sections reprennent alors la main.")
                })
                json.dump(s, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
                print('  + config/settings_schema.json — réglage mode_demo')
            else:
                print('  = réglage mode_demo déjà déclaré')
    p = os.path.join(THEME, 'config', 'settings_data.json')
    d = json.load(open(p, encoding='utf-8'))
    if 'mode_demo' not in d['current']:
        d['current']['mode_demo'] = True
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('  + config/settings_data.json — mode_demo actif')


# ---------------------------------------------------------------------------
# 2. Résolution des adresses + visuels de démonstration
# ---------------------------------------------------------------------------
def sections():
    # --- hero -------------------------------------------------------------
    patch('sections/hero.liquid',
          "{%- assign destination = block.settings.button_link | default: routes.all_products_collection_url -%}",
          "{%- capture lien_bouton -%}{%- render 'lien', valeur: block.settings.button_link -%}{%- endcapture -%}\n"
          "              {%- assign destination = lien_bouton | strip | default: routes.all_products_collection_url -%}",
          'héros : bouton résolu')
    patch('sections/hero.liquid',
          "        {%- elsif forloop.first -%}",
          "        {%- elsif settings.mode_demo -%}\n"
          "          {%- assign numero_visuel = forloop.index | minus: 1 | modulo: 2 | plus: 1 -%}\n"
          "          <img src=\"{{ 'demo-hero-' | append: numero_visuel | append: '.jpg' | asset_img_url: '1600x' }}\" class=\"slideshow__slide-media\" alt=\"\" loading=\"eager\" fetchpriority=\"high\">\n"
          "        {%- elsif forloop.first -%}",
          'héros : visuel de démonstration')

    # --- médias et texte --------------------------------------------------
    patch('sections/media-with-text.liquid',
          "      <div class=\"media-with-text__media\">",
          "      <div class=\"media-with-text__media\">\n"
          "        {%- if section.settings.image_main == blank and section.settings.image_secondary == blank and settings.mode_demo -%}\n"
          "          <div class=\"media-with-text__image-main\"><img src=\"{{ 'demo-editorial.jpg' | asset_img_url: '1200x' }}\" alt=\"\" loading=\"lazy\"></div>\n"
          "          <div class=\"media-with-text__image-secondary\"><img src=\"{{ 'llufan-nomad-coussin.jpg' | asset_img_url: '800x' }}\" alt=\"\" loading=\"lazy\"></div>\n"
          "        {%- endif -%}",
          'éditorial : visuels de démonstration')
    patch('sections/media-with-text.liquid',
          "{%- assign destination = section.settings.button_link | default: routes.all_products_collection_url -%}",
          "{%- capture lien_bouton -%}{%- render 'lien', valeur: section.settings.button_link -%}{%- endcapture -%}\n"
          "          {%- assign destination = lien_bouton | strip | default: routes.all_products_collection_url -%}",
          'éditorial : bouton résolu')

    # --- cartes d'univers -------------------------------------------------
    patch('sections/featured-collections.liquid',
          "          {%- assign destination = col.url | default: block.settings.link | default: routes.all_products_collection_url -%}",
          "          {%- capture lien_carte -%}{%- render 'lien', valeur: block.settings.link -%}{%- endcapture -%}\n"
          "          {%- assign destination = col.url | default: lien_carte | strip | default: routes.all_products_collection_url -%}",
          'cartes d\'univers : lien résolu')
    patch('sections/featured-collections.liquid',
          "            {%- else -%}\n"
          "              {{ 'collection-1' | placeholder_svg_tag: 'collection-card__placeholder' }}\n"
          "            {%- endif -%}",
          "            {%- elsif settings.mode_demo -%}\n"
          "              {%- assign numero_univers = forloop.index | minus: 1 | modulo: 4 | plus: 1 -%}\n"
          "              <img src=\"{{ 'demo-univers-' | append: numero_univers | append: '.jpg' | asset_img_url: '1000x' }}\" alt=\"\" loading=\"lazy\">\n"
          "            {%- else -%}\n"
          "              {{ 'collection-1' | placeholder_svg_tag: 'collection-card__placeholder' }}\n"
          "            {%- endif -%}",
          'cartes d\'univers : visuels de démonstration')

    # --- produits d'une collection ---------------------------------------
    patch('sections/featured-collection-products.liquid',
          "{%- assign destination = section.settings.button_link | default: section.settings.collection.url | default: routes.all_products_collection_url -%}",
          "{%- capture lien_bouton -%}{%- render 'lien', valeur: section.settings.button_link -%}{%- endcapture -%}\n"
          "      {%- assign destination = lien_bouton | strip | default: section.settings.collection.url | default: routes.all_products_collection_url -%}",
          'produits en avant : bouton résolu')

    # --- questions fréquentes --------------------------------------------
    patch('sections/faq.liquid',
          "      {%- assign lien_contact = section.settings.contact_link -%}",
          "      {%- capture lien_contact_resolu -%}{%- render 'lien', valeur: section.settings.contact_link -%}{%- endcapture -%}\n"
          "      {%- assign lien_contact = lien_contact_resolu | strip -%}",
          'FAQ : lien de contact résolu')

    # --- bandeau de collection -------------------------------------------
    patch('sections/collection-banner.liquid',
          "  {%- elsif collection.image != blank -%}",
          "  {%- elsif collection.image != blank -%}",
          'bandeau de collection (contrôle)')
    patch('sections/collection-banner.liquid',
          "  {%- else -%}\n    <div class=\"collection-banner__placeholder\">",
          "  {%- elsif settings.mode_demo -%}\n"
          "    <img src=\"{{ 'demo-collection-banner.jpg' | asset_img_url: '2400x' }}\" class=\"collection-banner__image\" alt=\"\" loading=\"eager\">\n"
          "  {%- else -%}\n    <div class=\"collection-banner__placeholder\">",
          'bandeau de collection : visuel de démonstration')

    # --- liste des collections -------------------------------------------
    patch('sections/main-list-collections.liquid',
          "              {{ 'collection-1' | placeholder_svg_tag }}",
          "              <img src=\"{{ 'demo-univers-' | append: forloop.index | minus: 1 | modulo: 4 | plus: 1 | append: '.jpg' | asset_img_url: '1000x' }}\" alt=\"\" loading=\"lazy\">",
          'liste des collections : visuels de démonstration')

    # --- bandeau d'annonces ----------------------------------------------
    patch('sections/announcement-bar.liquid',
          "              {%- if block.settings.link != blank -%}\n"
          "                <a href=\"{{ block.settings.link }}\"",
          "              {%- capture lien_message -%}{%- render 'lien', valeur: block.settings.link -%}{%- endcapture -%}\n"
          "              {%- assign lien_message = lien_message | strip -%}\n"
          "              {%- if lien_message != blank -%}\n"
          "                <a href=\"{{ lien_message }}\"",
          'bandeau : lien résolu')

    # --- pré-bandeau ------------------------------------------------------
    patch('sections/preheader.liquid',
          "            {%- assign lien_raccourci = block.settings.link -%}",
          "            {%- capture lien_raccourci_resolu -%}{%- render 'lien', valeur: block.settings.link -%}{%- endcapture -%}\n"
          "            {%- assign lien_raccourci = lien_raccourci_resolu | strip -%}",
          'pré-bandeau : lien résolu')

    # --- pastille d'en-tête ----------------------------------------------
    patch('sections/header.liquid',
          "        {%- assign lien_pastille = section.settings.pill_link -%}",
          "        {%- capture lien_pastille_resolu -%}{%- render 'lien', valeur: section.settings.pill_link -%}{%- endcapture -%}\n"
          "        {%- assign lien_pastille = lien_pastille_resolu | strip -%}",
          'en-tête : pastille résolue')

    # --- pied de page -----------------------------------------------------
    patch('sections/footer.liquid',
          "              {%- for i in (1..6) -%}\n"
          "                {%- assign cle_lien = 'link_' | append: i -%}\n"
          "                {%- if block.settings[cle_lien] != blank -%}{%- assign visibles = visibles | plus: 1 -%}{%- endif -%}\n"
          "              {%- endfor -%}",
          "              {%- for i in (1..6) -%}\n"
          "                {%- assign cle_lien = 'link_' | append: i -%}\n"
          "                {%- capture lien_compte -%}{%- render 'lien', valeur: block.settings[cle_lien] -%}{%- endcapture -%}\n"
          "                {%- if block.settings[cle_lien] != blank and lien_compte != blank -%}{%- assign visibles = visibles | plus: 1 -%}{%- endif -%}\n"
          "              {%- endfor -%}",
          'pied de page : comptage des liens visibles')
    patch_n('sections/footer.liquid',
            "                        {%- if block.settings[cle_lien] != blank -%}\n"
            "                          <a href=\"{{ block.settings[cle_lien] }}\">{{ block.settings[cle_label] }}</a>\n"
            "                        {%- endif -%}",
            "                        {%- capture lien_colonne -%}{%- render 'lien', valeur: block.settings[cle_lien] -%}{%- endcapture -%}\n"
            "                        {%- assign lien_colonne = lien_colonne | strip -%}\n"
            "                        {%- if block.settings[cle_label] != blank and lien_colonne != blank -%}\n"
            "                          <a href=\"{{ lien_colonne }}\">{{ block.settings[cle_label] }}</a>\n"
            "                        {%- endif -%}",
            2, 'pied de page : liens de colonne résolus')
    for cle, label in [('mentions', 'Mentions légales'), ('cgv', 'CGV'),
                       ('confidentialite', 'Confidentialité'), ('retours', 'Retour / échange')]:
        avant = ("          {%- if section.settings.legal_" + cle
                 + " != blank -%}<a href=\"{{ section.settings.legal_" + cle + " }}\">")
        apres = ("          {%- capture lien_legal -%}{%- render 'lien', valeur: section.settings.legal_"
                 + cle + " -%}{%- endcapture -%}\n"
                 "          {%- if lien_legal != blank -%}<a href=\"{{ lien_legal | strip }}\">")
        patch('sections/footer.liquid', avant, apres,
              'pied de page : lien légal ' + label)

    # --- club maman -------------------------------------------------------
    patch('sections/club-maman.liquid',
          "              {%- if block.settings.lien != blank -%}\n"
          "                <a class=\"club__espace\" href=\"{{ block.settings.lien }}\" {{ block.shopify_attributes }}>",
          "              {%- capture lien_espace -%}{%- render 'lien', valeur: block.settings.lien -%}{%- endcapture -%}\n"
          "              {%- assign lien_espace = lien_espace | strip -%}\n"
          "              {%- if lien_espace != blank -%}\n"
          "                <a class=\"club__espace\" href=\"{{ lien_espace }}\" {{ block.shopify_attributes }}>",
          'club : lien d\'espace')
    patch('sections/club-maman.liquid',
          "              {%- if block.settings.lien != blank -%}</a>{%- else -%}</div>{%- endif -%}",
          "              {%- if lien_espace != blank -%}</a>{%- else -%}</div>{%- endif -%}",
          'club : fermeture du lien d\'espace')
    patch('sections/club-maman.liquid',
          "                {%- if block.settings.lien != blank -%}\n"
          "                  <a class=\"club__discussion\" href=\"{{ block.settings.lien }}\" {{ block.shopify_attributes }}>",
          "                {%- capture lien_discussion -%}{%- render 'lien', valeur: block.settings.lien -%}{%- endcapture -%}\n"
          "                {%- assign lien_discussion = lien_discussion | strip -%}\n"
          "                {%- if lien_discussion != blank -%}\n"
          "                  <a class=\"club__discussion\" href=\"{{ lien_discussion }}\" {{ block.shopify_attributes }}>",
          'club : lien de discussion')
    patch('sections/club-maman.liquid',
          "                {%- if block.settings.lien != blank -%}</a>{%- else -%}</div>{%- endif -%}",
          "                {%- if lien_discussion != blank -%}</a>{%- else -%}</div>{%- endif -%}",
          'club : fermeture du lien de discussion')
    patch('sections/club-maman.liquid',
          "          {%- if section.settings.ressources_bouton != blank and section.settings.ressources_lien != blank -%}\n"
          "            <a href=\"{{ section.settings.ressources_lien }}\" class=\"button button--navy\">{{ section.settings.ressources_bouton }}</a>",
          "          {%- capture lien_ressources -%}{%- render 'lien', valeur: section.settings.ressources_lien -%}{%- endcapture -%}\n"
          "          {%- if section.settings.ressources_bouton != blank and lien_ressources != blank -%}\n"
          "            <a href=\"{{ lien_ressources | strip }}\" class=\"button button--navy\">{{ section.settings.ressources_bouton }}</a>",
          'club : lien du bandeau ressources')


if __name__ == '__main__':
    print('Réglages :')
    reglages()
    print('Sections :')
    sections()
    print('\n%d remplacement(s) effectué(s), %d déjà en place.' % (faits, deja))
