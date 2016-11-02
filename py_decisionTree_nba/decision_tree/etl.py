#-*- coding: utf-8 -*-

import pandas as pd

data_filename = '../data/nbaMini.csv'
dataset = pd.read_csv(data_filename)

print dataset.ix[:5]