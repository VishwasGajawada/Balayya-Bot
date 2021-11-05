#!/usr/bin/python3
'''
utils.py
Functions:
    [] scrape comments
    [x] get trigger words
    [] reply to comment
    [] append to log files
    [] delete from log files
'''

import re 
from config import *
from datetime import datetime 
import praw 


# I know it sounds weird. But, it gets human readable timestamp format: Year_Month_Day_Hour_Min_Sec
get_human_timestamp = lambda : datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


def scrape_comments(start_time_utc, end_time_utc):
    '''
    [] Scrapes all comments from the posts in a subreddit, which were posted after start_time_utc
    and before end_time_utc.
    [] Generates a temporary file that contains all the scraped comments.
        - format: UTC_TIMESTAMP | POST_ID | COMMENT_ID | REDDITOR | COMMENT_BODY

    start_time_utc: (float) UTC timestamp to begin comment scraping
    end_time_utc: (flaot) UTC timestamp to end comment scraping
    '''
    pass


def get_trigger_words(raw_comment):
    '''
    Gets number of times a trigger word is used in a sentence.

    raw_comment: (str) raw comment directly parsed from scraped comments
    returns a (dict) with no. of matches with resp. trigger word types.
    '''
    global NEWLINE_REPL
    global TRIGGER_WORDS_DF

    raw_comment = ' '.join(raw_comment.split(NEWLINE_REPL))
    cleaned_comment = ' '.join([word for word in raw_comment.split(' ') if word])
    trigger_score_dict = {}

    trigger_types = sorted(list(set(TRIGGER_WORDS_DF['trigger_types'].to_numpy())))
    for trigger_type in trigger_types:
        trigger_score_dict[trigger_type] = 0
        triggers = TRIGGER_WORDS_DF[TRIGGER_WORDS_DF['trigger_types'] == trigger_type]['re_triggers']
        for trigger in triggers:
            for match in re.compile(fr"{trigger}", re.IGNORECASE).finditer(cleaned_comment):
                trigger_score_dict[trigger_type] += 1
    return trigger_score_dict


target = '!balayya pata padu'
print(get_trigger_words(target))
