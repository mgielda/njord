#!/usr/bin/env python3

import pandas as pd
import numpy as np
from datetime import datetime
import glob
import yaml
import csv

data_filenames = glob.glob('./history/*.csv')
df = pd.concat([pd.read_csv(dfn) for dfn in data_filenames])

default_bank = 'pko'
# TODO: allow changing the default bank
bank = default_bank

bank_config = {}
with open(f'bank_configs/{bank}.yml') as bank_config_file:
    bank_config = yaml.safe_load(bank_config_file)

field_names = bank_config['field_names']
# reverse the dict since we're mapping the other way than in config file
field_names = {field_names[k]:k for k in field_names}

df.rename(columns=field_names, inplace=True)
df.fillna('', inplace=True)

if bank_config.get('unnamed_are_desc', False):
    for column in df.filter(regex="Unname"):
        df['description'] += " " + df[column]

pd.set_option('max_columns', None)
print(df[0:10])

df['category'] = ''
df['name'] = ''
with open('assignments.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        df.loc[df['description'].str.contains(row[0]), 'name'] = row[1]
        df.loc[df['description'].str.contains(row[0]), 'category'] = row[2]

print(df[0:10])
