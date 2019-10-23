# This file is meant to make it easier for anyone to update this for new c
import pickle

# If a new faction gets released, add it to faction_list, and add its heroes to cards like below, then run Card_Soup.py
# If a new card gets released run Card_Soup.py
faction_list = ["Vespitole", "Daramek", "Metris", "Endazu"]
cards = {"Vespitole Heroes": ["Captain Listrata", "Sofocatro", "Cardinal Pocchi", "Sister Ysadora"],
         "Daramek Heroes": ["Liet", "Esra", "Mogesh", "Babarus"],
         "Metris Heroes": ["Valdorian", "Theodox", "Birondelle", "Gretta"],
         "Endazu Heroes": ["Raktaba'an", "Calipeth", "Jesmai", "Zalasair"],
         "Tourney Heroes": [], #
         "Vespitole": [], "Daramek": [], "Metris": [], "Endazu": {}}


class Global_Variables:
    def __init__(self):
        global cards
        self.faction_list = faction_list
        self.cards = cards

    def get_factions(self):
        return self.faction_list

    def get_list(self, key):
        return self.cards[key]

    def get_keys(self):
        return self.cards.keys()

    def update_list(self, key, card_list):
        self.cards[key] = card_list

    def cards_write(self):
        f = open("file.pkl", "wb")
        pickle.dump(self.cards, f)
        f.close()

    def cards_read(self):
        f = open("file.pkl", "rb")
        self.cards = pickle.load(f)
        f.close()