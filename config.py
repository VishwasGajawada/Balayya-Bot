#!/usr/bin/python3
'''
config.py

Configuration files for running the bot
'''

import pandas as pd 
import numpy as np 

DELIMITER = "<::>"
NEWLINE_REPL = '<:NEWLINE:>'

TRIGGER_WORDS_DF = pd.read_csv('./resources/triggers.csv', delimiter=DELIMITER, engine='python')
