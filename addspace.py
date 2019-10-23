import pandas as pd
import re

tourney_heroes = ["Brigand Lucca", "Doge Monteferro","Dowager Anibaldo","Sang Ashkar","Shofet Daru","Xalia","Vexillius III",
          "Countess Aline"]
heroes = [""]

def addspace(csv):
    df = pd.read_csv(csv)
    for index, row in df.iterrows():
        name = row[df.columns[0]]
        twoword = re.search("([A-Z][a-z]+)([A-Z][A-Z|a-z]*)", name)
        if twoword:
            name = twoword.groups()[0] + " " + twoword.groups()[1]
        ofexception = re.search("([a-z|A-Z]+)(of|the) ([A-Z][a-z]+)", name)
        if ofexception:
            name = ofexception.groups()[0] + " " + ofexception.groups()[1] + " " + ofexception.groups()[2]
        df.at[index, df.columns[0]] = name
        #df.to_csv("paste_into_doc.csv")
    return df


def merge(csvs):
    main_df = pd.DataFrame
    i = 1
    for csv in csvs:
        df = addspace(csv)
        df.rename(columns={df.columns[0]: "Card"}, inplace=True)
        print(df.head(1))
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.merge(right=df, on="Card")

    return main_df

print(merge(["design_winningcards_pvp_all_value.csv", "woo_pvp_cards.csv"]).head(200))



#TODO: Plan of attack
#
#TODO: Grab 2 csvs, add space to both
#TODO: Merge csvs
#TODO: Delta
#TODO: filter out heroes