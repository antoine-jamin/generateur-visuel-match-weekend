import datetime
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

jours = ["JEUDI", "VENDREDI","SAMEDI", "DIMANCHE"]
# jours = ["SAMEDI", "DIMANCHE"]
salles_club = ["LIGERIA", "SALLE B", "ATHLÉTIS", "LIGERIA (CLUB HOUSE)"]
salles_equipes_conventions = {'JEAN MONNET': ['S1F', 'S2F', 'S3F', 'U20F', 'U17F N', 'U17F D'],
                              'JEAN LEHAY': ['S1F', 'S2F', 'S3F', 'U20F', 'U17F N', 'U17F D'],
                              'BELLE BEILLE': ['S1F', 'S2F', 'S3F', 'U20F', 'U17F N', 'U17F D'],
                              'MONTAIGNE': ['U15M']}

date_jour1 = datetime.date(2022, 5, 19)

xl_matchs = pd.read_excel('doc/template.xlsx').dropna().sort_values(by=['JOUR', 'HEURE'])

y_match = 90
y = 200
template_img = Image.open('doc/template.png')
visuel = ImageDraw.Draw(template_img)
font_jour = ImageFont.truetype("Chalkboard.ttc", 60)
font_salle = ImageFont.truetype("Chalkboard.ttc", 45)
font_match = ImageFont.truetype("Chalkboard.ttc", 40)
color_jour = (255, 255, 255, 255)
color_salle_conv = (43, 106, 188, 255)
color_salle_ext = (255, 60, 60, 255)
color_salle_pdc = (255, 255, 0, 255)
color_match = (255, 255, 255, 255)

for ij, jour in enumerate(jours):
    if not xl_matchs.loc[(xl_matchs['JOUR'] == jour)].empty:
        date = date_jour1 + datetime.timedelta(days=ij)
        msg = date.strftime("%A %d %B")
        w, h = visuel.textsize(msg, font_jour)
        visuel.text(((1080 - w) / 2, y), msg, font=font_jour, fill=color_jour, align='center', stroke_width=2,
                    stroke_fill=color_jour)
        y += h + 30

    # DOMICILE
    index_to_rm = []
    for salle in salles_club:
        msg = ""
        cpt = 0
        for i, row in xl_matchs.loc[(xl_matchs['JOUR'] == jour) & (xl_matchs['LIEU'] == salle)].iterrows():
            index_to_rm.append(i)
            if (cpt == 0):
                w, h = visuel.textsize(salle, font_salle)
                visuel.text(((1080 - w) / 2, y), salle, font=font_salle, fill=color_salle_pdc, stroke_width=1,
                            stroke_fill=color_salle_pdc)
                y += h + 25
            heure = row['HEURE'].split("H")[0]
            if row['HEURE'].upper().split("H")[1] != '':
                heure = row['HEURE'].upper()
            else:
                heure = row['HEURE'].split("H")[0] + "H00"
            if row["ADVERSAIRE"].upper() == "TOURNOI":
                msg += heure + "\tTOURNOI " + row["EQUIPE"] + "\n"
            elif row["EQUIPE"].upper() == "ANIMATION":
                msg += heure + "\t" + row["ADVERSAIRE"] + "\n"
            else:
                msg += heure + "\t" + row["EQUIPE"] + " vs. " + row["ADVERSAIRE"] + "\n"
            cpt += 1
        if msg != "":
            msg = msg[:-1]
            w, h = visuel.textsize(msg.expandtabs(), font_match)
            visuel.multiline_text((y_match, y), msg.expandtabs(), font=font_match, fill=color_match)
            y += h + 25
    # CONVENTION
    for i, salle in enumerate(salles_equipes_conventions):
        msg = ""
        cpt = 0
        for i, row in xl_matchs.loc[
            (xl_matchs['JOUR'] == jour) & (xl_matchs['LIEU'] == salle) & xl_matchs["EQUIPE"].isin(
                salles_equipes_conventions[salle])].iterrows():
            index_to_rm.append(i)
            if (cpt == 0):
                w, h = visuel.textsize(salle, font_salle)
                visuel.text(((1080 - w) / 2, y), salle, font=font_salle, fill=color_salle_conv, stroke_width=1,
                            stroke_fill=color_salle_conv)
                y += h + 25
            heure = row['HEURE'].split("H")[0]
            if row['HEURE'].upper().split("H")[1] != '':
                heure = row['HEURE'].upper()
            else:
                heure = row['HEURE'].split("H")[0] + "H00"
            if row["ADVERSAIRE"].upper() == "TOURNOI":
                msg += heure + "\tTOURNOI " + row["EQUIPE"] + "\n"
            else:
                msg += heure + "\t" + row["EQUIPE"] + " vs. " + row["ADVERSAIRE"] + "\n"
            cpt += 1
        if msg != "":
            msg = msg[:-1]
            w, h = visuel.textsize(msg.expandtabs(), font_match)
            visuel.multiline_text((y_match, y), msg.expandtabs(), font=font_match, fill=color_match)
            y += h + 25
        cpt += 1
    # EXTERIEUR
    msg = ""
    cpt = 0
    for i, row in xl_matchs.loc[(xl_matchs['JOUR'] == jour)].iterrows():
        if not i in index_to_rm:
            if (cpt == 0):
                w, h = visuel.textsize("EXTÉRIEUR", font_salle)
                visuel.text(((1080 - w) / 2, y), "EXTÉRIEUR", font=font_salle, fill=color_salle_ext, stroke_width=1,
                            stroke_fill=color_salle_ext)
                y += h + 25
            heure = row['HEURE'].split("H")[0]
            if row['HEURE'].upper().split("H")[1] != '':
                heure = row['HEURE'].upper()
            else:
                heure = row['HEURE'].split("H")[0] + "H00"
            if row["ADVERSAIRE"].upper() == "TOURNOI":
                msg += heure + "\tTOURNOI " + row["EQUIPE"] + " À " + row["LIEU"] + "\n"
            else:
                msg += heure + "\t" + row["ADVERSAIRE"] + " vs. " + row["EQUIPE"] + "\n"
            cpt += 1
    if msg != "":
        msg = msg[:-1]
        w, h = visuel.textsize(msg.expandtabs(), font_match)
        visuel.multiline_text((y_match, y), msg.expandtabs(), font=font_match, fill=color_match)
        y += h + 25

name_file = "visuel_wk_" + date_jour1.strftime("%Y%m")
for n, j in enumerate(jours):
    name_file += (date_jour1 + datetime.timedelta(days=n)).strftime(
        "%d-")
name_file = name_file[:-1] + ".png"
template_img.save('gen/' + name_file)
