#!/usr/bin/python3
'''
main.py
[] Log into operation logs.
[] Execute pending operations in the queue.
[] Delete executed operations from the queue.
[] Keep track of comments that have already been replied to by BalayyaBot.
'''
import time 
import pandas as pd 
import numpy as np 
import math import *
from utils import *
from secrets import balayya_keys


def execute_queue(comment_id, reply_content):
    '''
    comment_id: (str) the id of target comment.
    reply_content: (str) reply content 
    '''
