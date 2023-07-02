import datetime
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

# jours = ["VENDREDI","SAMEDI", "DIMANCHE"]
# jours = ["SAMEDI", "DIMANCHE", "LUNDI"]
jours = ["SAMEDI", "DIMANCHE"]
salles_club = ["LIGERIA", "SALLE B", "ATHLÉTIS", "LIGERIA (CLUB HOUSE)", "COMPLEXE SPORTIF F. BERNARD", "VAL DE LOUET"]
salles_equipes_conventions = {'JEAN MONNET': ['S1F', 'S2F', 'S3F', 'S4F', 'U17F'],
                              'JEAN LEHAY': ['S1F', 'S2F', 'S3F', 'S4F', 'U17F'],
                              'BELLE BEILLE': ['S1F', 'S2F', 'S3F', 'S4F', 'U17F'],
                              'MONTAIGNE': ['U15M', 'U16M1']}

date_jour1 = datetime.date(2023, 6, 24)

xl_matchs = pd.read_excel('doc/template.xlsx').dropna().sort_values(by=['JOUR', 'HEURE'])

y_match = 90
y = 200
# FONTS
font_jour = ImageFont.truetype("Chalkboard.ttc", 60)
# font_jour = ImageFont.truetype("Chalkboard.ttc", 50)
font_salle = ImageFont.truetype("Chalkboard.ttc", 45)
# font_salle = ImageFont.truetype("Chalkboard.ttc", 40)
font_match = ImageFont.truetype("Chalkboard.ttc", 40)
# font_match = ImageFont.truetype("Chalkboard.ttc", 35)
# ESPACEMENTS
delta_h_jour = 30
# delta_h_jour = 22
delta_h_lieu = 25
# delta_h_lieu = 17
# COULEURS
color_jour = (254, 253, 26, 255)
color_salle_conv = (0, 176, 240, 255)
color_salle_ext = (255, 11, 172, 255)
color_salle_pdc = (254, 253, 26, 255)
color_match = (255, 255, 255, 255)

color_win = (36, 210, 109, 255)
color_nul = (153,153,153, 255)
color_def = (254, 75, 75, 255)
