# Njord

Parse bank data and group the spendings using Pandas.

Njord uses two types of categorization based on loose criteria - a human-friendly name (e.g. garage) as well as more general category to aggregate similar types of payments (e.g. bills).

All data (bank configuration, categorization data) is read from files:

* `history` - put bank transcript exports in csv files here
* `bank_configs/{bank}.yml` - bank config files, see example to tweak to your
  bank
* `assignments.csv` - put categorization assignments here as string-filter,friendly-name,category

Filters are relaxed, with (future) warnings on things that fall under more than one category.

## Install

```
pipenv install
```

## Run

```
pipenv run ./parse.py
```
