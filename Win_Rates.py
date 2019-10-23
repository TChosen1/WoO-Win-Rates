from global_vars import Global_Variables
import pandas as pd
from os import listdir
from os.path import join, isfile


global_vars = Global_Variables()
global_vars.cards_read()
onlyfiles = [f for f in listdir("csvs") if isfile(join("csvs", f))]
# TODO: make DF
# TODO: DF headers are headers of files
# TODO: check for cards against cards