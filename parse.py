#!/usr/bin/env python3

import pandas as pd
import numpy as np
from datetime import datetime
import glob
import yaml

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

pd.set_option('max_columns', None)
print(df[0:10])

