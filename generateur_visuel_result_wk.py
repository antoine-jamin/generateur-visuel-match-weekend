from utils import *

template_img = Image.open('doc/template_resultats.png')
visuel = ImageDraw.Draw(template_img)

dateDeb = date_jour1
dateFin = date_jour1 + datetime.timedelta(days=len(jours) - 1)
msg = dateDeb.strftime("Weekend du %d au") + dateFin.strftime(" %d %B")
w, h = visuel.textsize(msg, font_jour)
visuel.text(((1080 - w) / 2, y), msg, font=font_jour, fill=color_jour, align='center', stroke_width=2,
            stroke_fill=color_jour)
y += h + delta_h_jour

for i, match in xl_matchs.iterrows():
    c = color_nul
    if match["Score PDC"] > match["Score Adv"]:
        c = color_win
    elif match["Score PDC"] < match["Score Adv"]:
        c = color_def
    # à domicile PdC
    if match["LIEU"] in salles_club or (
            match["LIEU"] in salles_equipes_conventions and match["EQUIPE"] in salles_equipes_conventions[
        match["LIEU"]]):
        msg = match["EQUIPE"] + " vs. " + match["ADVERSAIRE"] + "    (" + str(int(match["Score PDC"])) + "-" + str(
            int(match["Score Adv"])) + ")"
    # à l'exterieur
    else:
        msg = match["ADVERSAIRE"] + " vs. " + match["EQUIPE"] + "    ("+ str(int(match["Score Adv"])) + "-" + str(
            int(match["Score PDC"]))+")"
    w, h = visuel.textsize(msg.expandtabs(), font_match)
    visuel.text((y_match, y), msg.expandtabs(), font=font_match, fill=c, stroke_width=1, stroke_fill=color_jour)
    y += h + delta_h_lieu

name_file = "visuel_rwk_" + date_jour1.strftime("%Y%m")
for n, j in enumerate(jours):
    name_file += (date_jour1 + datetime.timedelta(days=n)).strftime(
        "%d-")
name_file = name_file[:-1] + ".png"
template_img.save('gen/' + name_file)
