from urllib.request import urlopen
from bs4 import BeautifulSoup
from global_vars import Global_Variables

global_vars = Global_Variables()
factions = global_vars.get_factions()
for faction in factions:
    cards = []
    html = urlopen("https://war-of-omens.fandom.com/wiki/" + faction)
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")
    tables.remove(tables[0])  # table of heroes, useless to us
    for table in tables:
        all_boxes = table.find_all("a")
        for box in all_boxes:
            if not box.has_attr("class"):
                cards.append(box['title'])
    cards = [c for c in cards if c not in global_vars.get_list(faction + " Heroes")]
    global_vars.update_list(faction, cards)
global_vars.cards_write()
