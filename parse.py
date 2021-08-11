#!/usr/bin/env python3

import pandas as pd
import numpy as np
from datetime import datetime
import glob
import yaml
import csv

def get_bank_config(bank='pko'):
    # TODO: allow changing the default bank
    with open(f'bank_configs/{bank}.yml') as bank_config_file:
        return yaml.safe_load(bank_config_file)

def get_history(encoding):
    data_filenames = glob.glob('./history/*.csv')
    return pd.concat([pd.read_csv(dfn, encoding=encoding) for dfn in data_filenames])


def parse_history(df, bank_config):
    field_names = bank_config['field_names']
    # reverse the dict since we're mapping the other way than in config file
    field_names = {field_names[k]:k for k in field_names}

    df.rename(columns=field_names, inplace=True)
    df.fillna('', inplace=True)

    if bank_config.get('unnamed_are_desc', False):
        for column in df.filter(regex="Unname"):
            df['description'] += " " + df[column]

    return df

def apply_names_and_categories(df):
    df['category'] = ''
    df['name'] = ''
    with open('assignments.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            df.loc[df['description'].str.contains(row[0]), 'name'] = row[1]
            df.loc[df['description'].str.contains(row[0]), 'category'] = row[2]
    return df

def main():
    bank_config = get_bank_config()
    df = get_history(bank_config.get('encoding', 'utf-8'))
    df = parse_history(df, bank_config)
    df = apply_names_and_categories(df)
    return df

if __name__ == "__main__":
    main()
