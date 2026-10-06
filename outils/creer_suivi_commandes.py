# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
#  LLUFAN — le tableau de suivi des commandes (paiement à la livraison).
#
#  POURQUOI
#  Une commande LLUFAN n'arrive pas comme une « commande Shopify » : le client
#  remplit le formulaire de la fiche produit, et le message part dans votre
#  boîte (Formulaires de contact / l'e-mail de la boutique). Shopify comptera
#  donc toujours 0 commande et 0 DZD, même quand vous vendez tous les jours.
#  C'est la raison pour laquelle il faut un tableau : c'est lui qui dit combien
#  de commandes sont confirmées, expédiées, livrées, refusées, encaissées — et
#  combien il reste vraiment en poche après la livraison.
#
#  CE QUE FAIT CE FICHIER : un classeur avec deux feuilles.
#    1. « Commandes » : une ligne par commande, avec les listes déroulantes de
#       statut et de mode, et le calcul automatique du net.
#    2. « Comment s'en servir » : la marche à suivre, écrite dans la feuille.
#
#  Usage : python3 creer_suivi_commandes.py
# ---------------------------------------------------------------------------
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, 'LLUFAN-suivi-commandes-COD.xlsx')

NUIT = '1F1B2E'
IVOIRE = 'F6F1E7'
CORAL = 'D96A55'
LIGNE = 'D8CFC0'

# (titre, largeur, aide en commentaire d'en-tête)
COLONNES = [
    ('N° de commande', 16, 'Votre numéro, à reporter sur le bon de livraison : ex. LFN-2026-001'),
    ('Date de réception', 15, 'La date où le message est arrivé dans votre boîte.'),
    ('Nom du client', 20, 'Tel qu’écrit dans le formulaire.'),
    ('Téléphone', 16, 'Le numéro est indispensable : c’est lui qui sert à confirmer la commande.'),
    ('Wilaya', 16, 'Pour le transporteur.'),
    ('Commune', 18, 'Pour le transporteur.'),
    ('Mode', 12, 'À domicile ou en stop-desk.'),
    ('Articles', 30, 'Le détail : « Coussin Nomad — bleu × 1 », etc.'),
    ('Prix des articles', 15, 'Ce que le client doit pour les produits, hors livraison.'),
    ('Frais annoncés', 14, 'Le tarif de livraison annoncé par le site au moment de la commande.'),
    ('Total à encaisser', 16, 'Ce que le livreur doit rapporter. Se calcule tout seul.'),
    ('Statut', 16, 'Reçue → confirmée → expédiée → livrée, ou refusée.'),
    ('Transporteur', 16, 'La société à qui vous confiez le colis.'),
    ('N° de suivi', 16, 'Le numéro du bordereau, pour retrouver le colis.'),
    ('Frais réels', 13, 'Ce que le transporteur vous facture réellement. À comparer aux frais annoncés.'),
    ('Coût des articles', 15, 'Votre coût d’achat + emballage pour cette ligne.'),
    ('Net encaissé', 14, 'Total encaissé − frais réels − coût des articles. Se calcule tout seul.'),
    ('Payé le', 13, 'La date à laquelle le transporteur vous a versé l’argent.'),
    ('Remarques', 34, 'Refus, absence, deuxième passage, retour… tout ce qui explique la ligne.'),
]

STATUTS = ['Reçue', 'Confirmée', 'Expédiée', 'Livrée', 'Refusée', 'Encaissée']


def construire():
    wb = Workbook()
    f = wb.active
    f.title = 'Commandes'

    # ── 1. Les titres ────────────────────────────────────────────────────────
    for i, (titre, largeur, aide) in enumerate(COLONNES, 1):
        c = f.cell(row=1, column=i, value=titre)
        c.font = Font(bold=True, color='FFFFFF', size=11)
        c.fill = PatternFill('solid', fgColor=NUIT)
        c.alignment = Alignment(vertical='center', horizontal='center', wrap_text=True)
        if aide:
            c.comment = None
        f.column_dimensions[get_column_letter(i)].width = largeur
    f.row_dimensions[1].height = 30

    # ── 2. Dix lignes d'exemple, effaçables, pour montrer le calcul ──────────
    exemples = [
        ('LFN-2026-001', '2026-10-07', 'Amina B.', '0555 12 34 56', 'Alger', 'Bab El Oued',
         'domicile', 'Coussin Nomad — bleu × 1', 3200, 400, None, 'Livrée', 'Yalidine', 'YL-88231',
         400, 1500, None, '2026-10-12', 'Livrée en 2 jours, encaissée.'),
        ('LFN-2026-002', '2026-10-08', 'Nour K.', '0661 98 76 54', 'Constantine', 'El Khroub',
         'stop-desk', 'Coussin Nomad — terracotta × 1 + Housse × 1', 4400, 300, None, 'Refusée',
         'ZR Express', 'ZR-40771', 300, 2100, None, '', 'Client injoignable, colis revenu.'),
    ]
    for r, ligne in enumerate(exemples, start=2):
        for i, valeur in enumerate(ligne[:8], 1):
            f.cell(row=r, column=i, value=valeur)
        f.cell(row=r, column=9, value=ligne[8]).number_format = '#,##0 "DA"'
        f.cell(row=r, column=10, value=ligne[9]).number_format = '#,##0 "DA"'
        f.cell(row=r, column=11, value='=IF(COUNT(I%d:J%d)=2,I%d+J%d,"")' % (r, r, r, r)).number_format = '#,##0 "DA"'
        f.cell(row=r, column=12, value=ligne[11])
        f.cell(row=r, column=13, value=ligne[12])
        f.cell(row=r, column=14, value=ligne[13])
        f.cell(row=r, column=15, value=ligne[14]).number_format = '#,##0 "DA"'
        f.cell(row=r, column=16, value=ligne[15]).number_format = '#,##0 "DA"'
        f.cell(row=r, column=17, value='=IF(AND(K%d<>"",O%d<>"",P%d<>""),K%d-O%d-P%d,IF(AND(K%d<>"",L%d="Refusée"),0,""))'
               % (r, r, r, r, r, r, r, r)).number_format = '#,##0 "DA"'
        f.cell(row=r, column=18, value=ligne[17])
        f.cell(row=r, column=19, value=ligne[18])

    # ── 3. Les lignes vides, déjà calculées : on n'a plus qu'à remplir ───────
    for r in range(len(exemples) + 2, len(exemples) + 202):
        f.cell(row=r, column=11, value='=IF(COUNT(I%d:J%d)=2,I%d+J%d,"")' % (r, r, r, r)).number_format = '#,##0 "DA"'
        f.cell(row=r, column=17,
               value='=IF(AND(K%d<>"",O%d<>"",P%d<>""),K%d-O%d-P%d,"")' % (r, r, r, r, r, r)).number_format = '#,##0 "DA"'
        for c in (15, 16, 9, 10):
            f.cell(row=r, column=c).number_format = '#,##0 "DA"'

    # ── 4. Listes déroulantes : statut, mode ────────────────────────────────
    dv = DataValidation(type='list', formula1='"%s"' % ','.join(STATUTS), allow_blank=True,
                        promptTitle='Statut', prompt='Choisissez le statut dans la liste.')
    f.add_data_validation(dv)
    dv.add('L2:L201')
    dv2 = DataValidation(type='list', formula1='"domicile,stop-desk"', allow_blank=True,
                         promptTitle='Mode de livraison', prompt='À domicile ou en stop-desk.')
    f.add_data_validation(dv2)
    dv2.add('G2:G201')

    # ── 5. Mise en forme : bordures, total en bas ───────────────────────────
    fin = Side(style='thin', color=LIGNE)
    for r in range(1, 202):
        for c in range(1, len(COLONNES) + 1):
            f.cell(row=r, column=c).border = Border(bottom=fin)
    for c in range(1, len(COLONNES) + 1):
        cel = f.cell(row=1, column=c)
        cel.fill = PatternFill('solid', fgColor=NUIT)
    # une bande ivoire une ligne sur deux : plus facile à lire
    for r in range(2, 202):
        if r % 2 == 0:
            for c in range(1, len(COLONNES) + 1):
                f.cell(row=r, column=c).fill = PatternFill('solid', fgColor=IVOIRE)
    f.cell(row=203, column=8, value='Total').font = Font(bold=True, color=NUIT)
    for c in (9, 10, 11, 15, 16, 17):
        cel = f.cell(row=203, column=c, value='=SUM(%s2:%s201)' % (get_column_letter(c), get_column_letter(c)))
        cel.font = Font(bold=True, color=NUIT)
        cel.number_format = '#,##0 "DA"'
    # Les trois compteurs du bas : ce sont eux qu'on regarde une fois par mois.
    f.cell(row=205, column=8, value='Commandes').font = Font(bold=True, color=NUIT)
    f.cell(row=205, column=9,
           value='=COUNTIF(L2:L201,"Livrée")+COUNTIF(L2:L201,"Encaissée")').font = Font(bold=True, color=CORAL)
    f.cell(row=205, column=10, value='livrées ou encaissées')
    f.cell(row=206, column=9,
           value='=COUNTIF(L2:L201,"Refusée")').font = Font(bold=True, color=CORAL)
    f.cell(row=206, column=10, value='refusées')
    f.cell(row=207, column=9,
           value='=COUNTA(B2:B201)').font = Font(bold=True, color=NUIT)
    f.cell(row=207, column=10, value='commandes reçues au total')
    for r in (205, 206, 207):
        f.cell(row=r, column=10).font = Font(italic=True, color=NUIT)

    f.freeze_panes = 'C2'

    # ── 6. La feuille « Comment s'en servir » ───────────────────────────────
    g = wb.create_sheet("Comment s'en servir")
    g.column_dimensions['A'].width = 4
    g.column_dimensions['B'].width = 104
    texte = [
        ('t', "LLUFAN — suivi des commandes payées à la livraison"),
        ('s', "Pourquoi ce tableau existe"),
        ('p', "Une commande LLUFAN n'arrive pas comme une « commande Shopify ». Le client remplit le "
              "formulaire de la fiche produit, et le message part dans votre boîte (Formulaires de "
              "contact, l'e-mail de la boutique). Shopify comptera donc toujours 0 commande et 0 DZD, "
              "même quand vous vendez tous les jours."),
        ('p', "Ce tableau est donc votre registre : c'est lui qui dit combien de commandes sont "
              "confirmées, expédiées, livrées, refusées, encaissées — et ce qu'il reste réellement "
              "après la livraison. C'est aussi lui qui vous dira si la publicité est rentable : "
              "comparez « Net encaissé » (colonnes O et P remplies) au budget publicitaire de la "
              "période."),
        ('s', "Les huit gestes, dans l'ordre"),
        ('n', "À chaque nouvelle commande : ouvrez le message, copiez le nom, le téléphone, la "
              "wilaya, la commune, le mode, les articles et les deux montants dans une nouvelle "
              "ligne. Le total à encaisser se calcule tout seul."),
        ('n', "Téléphonez ou écrivez sur WhatsApp pour confirmer la commande. C'est à ce moment-là "
              "que le statut passe de « Reçue » à « Confirmée »."),
        ('n', "Remettez le colis au transporteur : statut « Expédiée », avec le nom du transporteur "
              "et le numéro de suivi."),
        ('n', "À la livraison : « Livrée » si le client a payé, « Refusée » sinon — notez le motif "
              "en remarque (injoignable, absence, changement d'avis)."),
        ('n', "Quand le transporteur vous verse l'argent : statut « Encaissée » et date dans "
              "« Payé le »."),
        ('n', "Remplissez « Frais réels » avec ce que le transporteur vous a facturé : c'est la "
              "seule façon de savoir si les tarifs de livraison affichés sur le site sont justes. "
              "Tant que cette colonne est vide, ne baissez pas les frais et ne promettez pas la "
              "livraison gratuite."),
        ('n', "Remplissez « Coût des articles » (achat + emballage) : la colonne « Net encaissé » "
              "donne alors votre marge réelle par commande."),
        ('n', "Une fois par mois, regardez les trois compteurs du bas, et comparez le net total au "
              "budget publicitaire. C'est ce chiffre qui décide si l'on augmente la publicité — pas "
              "le nombre de visites."),
        ('s', "Trois conseils qui évitent des pertes"),
        ('p', "Un colis refusé coûte deux fois : le transport (aller et retour) et l'immobilisation. "
              "C'est pour cela qu'un appel de confirmation avant expédition vaut toujours mieux "
              "qu'une vente expédiée à l'aveugle."),
        ('p', "Notez toujours le numéro de téléphone exactement comme le client l'a écrit : c'est "
              "lui qui permet de rattraper une adresse incomplète."),
        ('p', "Gardez le message d'origine : en cas de litige, c'est la preuve de ce que le client "
              "a commandé."),
    ]
    r = 1
    for genre, contenu in texte:
        if genre == 't':
            c = g.cell(row=r, column=2, value=contenu)
            c.font = Font(bold=True, size=15, color=NUIT)
            r += 1
        elif genre == 's':
            c = g.cell(row=r, column=2, value=contenu)
            c.font = Font(bold=True, size=12, color=CORAL)
            r += 1
        elif genre == 'p':
            c = g.cell(row=r, column=2, value=contenu)
            c.alignment = Alignment(wrap_text=True, vertical='top')
            g.row_dimensions[r].height = 46
            r += 2
        elif genre == 'n':
            g.cell(row=r, column=1, value='•').font = Font(color=CORAL, bold=True)
            c = g.cell(row=r, column=2, value=contenu)
            c.alignment = Alignment(wrap_text=True, vertical='top')
            g.row_dimensions[r].height = 46
            r += 2
    wb.save(SORTIE)
    return SORTIE


if __name__ == '__main__':
    chemin = construire()
    print('✓ %s' % os.path.basename(chemin))
    print('   feuille « Commandes » : %d colonnes, 200 lignes prêtes, 2 exemples à effacer'
          % len(COLONNES))
    print('   feuille « Comment s\'en servir » : 8 gestes, 3 conseils')
