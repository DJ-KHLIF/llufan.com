#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les CSV d'import Shopify de la démonstration.

  • LLUFAN-DEMO-produits.csv     → Produits → Importer (10 produits, 27 variantes)
  • LLUFAN-DEMO-collections.csv  → Produits → Collections → Importer (5 collections)

Source : demo/contenu_demo.py. Les visuels produits sont livrés à part, dans
demo/produits/ (nom de fichier = handle du produit) : Shopify n'accepte dans le
CSV que des adresses d'images accessibles en ligne, on ne peut donc pas y
référencer des fichiers locaux.
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'demo'))
import contenu_demo as D  # noqa: E402

COLONNES = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value",
    "Option3 Name", "Option3 Value",
    "Variant SKU", "Variant Inventory Tracker", "Variant Inventory Qty",
    "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price",
    "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable",
    "Image Src", "Image Position", "Image Alt Text", "Variant Image",
    "SEO Title", "SEO Description", "Status",
]

COLONNES_COLLECTIONS = [
    "Handle", "Title", "Body (HTML)", "Published", "Sort Order", "Template Suffix",
]


def variantes(produit):
    """Énumère les combinaisons d'options — la dernière option varie le plus vite,
    comme dans les fichiers d'import Shopify."""
    combinaisons = [[]]
    for _, valeurs in produit['options']:
        combinaisons = [c + [v] for c in combinaisons for v in valeurs]
    return combinaisons


def lignes_produit(p):
    lignes = []
    for i, valeurs in enumerate(variantes(p)):
        ligne = {c: "" for c in COLONNES}
        ligne["Handle"] = p['handle']
        if i == 0:
            ligne["Title"] = p['title']
            ligne["Body (HTML)"] = p['body']
            ligne["Vendor"] = "LLUFAN"
            ligne["Type"] = p['type']
            ligne["Tags"] = p['tags']
            ligne["Published"] = "TRUE"
            ligne["SEO Title"] = p['seo_titre']
            ligne["SEO Description"] = p['seo_description']
        ligne["Variant SKU"] = ("LLUFAN-" + p['handle'].replace('-', ' ').title().replace(' ', '-')
                                + "".join("-" + v.replace(' ', '').replace('/', '') for v in valeurs))[:60]
        ligne["Variant Inventory Tracker"] = ""
        ligne["Variant Inventory Qty"] = ""
        ligne["Variant Inventory Policy"] = "continue"   # jamais en rupture pendant les tests
        ligne["Variant Fulfillment Service"] = "manual"
        ligne["Variant Price"] = p['price']
        ligne["Variant Requires Shipping"] = "TRUE"
        ligne["Variant Taxable"] = "TRUE"
        ligne["Status"] = "active"
        for j, (nom, _) in enumerate(p['options']):
            ligne["Option%d Name" % (j + 1)] = nom
            ligne["Option%d Value" % (j + 1)] = valeurs[j]
        lignes.append(ligne)
    return lignes


def main():
    chemin = os.path.join(ROOT, 'LLUFAN-DEMO-produits.csv')
    with open(chemin, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES)
        w.writeheader()
        total = 0
        for p in D.PRODUITS:
            lignes = lignes_produit(p)
            total += len(lignes)
            w.writerows(lignes)
    print('%s : %d produits, %d variantes' % (os.path.basename(chemin), len(D.PRODUITS), total))

    chemin = os.path.join(ROOT, 'LLUFAN-DEMO-collections.csv')
    with open(chemin, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES_COLLECTIONS)
        w.writeheader()
        for c in D.COLLECTIONS:
            w.writerow({
                "Handle": c['handle'], "Title": c['title'], "Body (HTML)": c['body'],
                "Published": "TRUE", "Sort Order": "manual", "Template Suffix": "",
            })
    print('%s : %d collections' % (os.path.basename(chemin), len(D.COLLECTIONS)))


if __name__ == '__main__':
    main()
