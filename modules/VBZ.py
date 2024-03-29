# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:25:25 2019

@author: Dr-Nuke & Gilles P.

Explorative exploration of the VBZ 2018 data
"""

# this is the module for toying with the VBZ data

# 1 load in (parts of the) data
# 2 vizualize
# 3 ??


import numpy as np
import csv
import pandas as pd
import datetime as dt

def datetime_from_date_and_seconds(date_str,seconds):
    """Transforms a date in stringform and seconds since midnight into a datetime
    date_str: string of the form 'dd.mm.yy'
    seconds: int for seconds since midnight (can be negative or larger than
    number of seconds in a day)
    """
    date_lst = [int(d) for d in date_str.split('.')[::-1]];
    date = dt.datetime(date_lst[0]+2000,date_lst[1],date_lst[2]);
    return date + dt.timedelta(seconds = seconds)


if __name__ == "__main__":
    # execute only if run as a script
    print('nothing executed on calling VBZ')
# evil troll edit
