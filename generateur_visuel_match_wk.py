from utils import *

template_img = Image.open('doc/template_programme.png')
visuel = ImageDraw.Draw(template_img)

for ij, jour in enumerate(jours):
    if not xl_matchs.loc[(xl_matchs['JOUR'] == jour)].empty:
        date = date_jour1 + datetime.timedelta(days=ij)
        msg = date.strftime("%A %d %B")
        w, h = visuel.textsize(msg, font_jour)
        visuel.text(((1080 - w) / 2, y), msg, font=font_jour, fill=color_jour, align='center', stroke_width=2,
                    stroke_fill=color_jour)
        y += h + delta_h_jour

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
                y += h + delta_h_lieu
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
            y += h + delta_h_lieu
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
                y += h + delta_h_lieu
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
            y += h + delta_h_lieu
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
                y += h + delta_h_lieu
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
        y += h + delta_h_lieu

name_file = "visuel_pwk_" + date_jour1.strftime("%Y%m")
for n, j in enumerate(jours):
    name_file += (date_jour1 + datetime.timedelta(days=n)).strftime(
        "%d-")
name_file = name_file[:-1] + ".png"
template_img.save('gen/' + name_file)
