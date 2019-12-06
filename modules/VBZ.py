# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:25:25 2019

@author: Dr-Nuke & 

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


# # read in one file
# path = 'C://data//fahrzeiten_soll_ist_20171231_20180106.csv'
# data=pd.read_csv(path)

# path_halt='C://data//haltepunkt.csv'
# halt=pd.read_csv(path_halt)


def Second_to_timeStr(seconds):
    """
    converts the seconds-from-midnight (VBZ-format) into a readable string of time hh:mm:ss
    """
    return '00:00:00'

 
if __name__ == "__main__":
    # execute only if run as a script
    print('nothing executed on calling VBZ')