# + language="javascript"
#
# // allow to run all cells from current cell to end with a keyboard shortcut
# Jupyter.keyboard_manager.command_shortcuts.add_shortcut('f', {
#     help : 'run all cells',
#     help_index : 'zz',
#     handler : function (event) {
#         IPython.notebook.execute_all_cells();
#         return false;
#     }}
# );
# -

from parse import *

df = main()

pd.options.display.max_columns = None
pd.options.display.max_rows = 100
df[0:10]

csv_string = """

"""
df = apply_names_and_categories(df, csv_string)

# filter out positive transfers
df = df[df['amount'] < 0]
print(df.groupby(['category'])['amount'].sum())
len(df[df['category'] == ''])

pd.options.display.width = 5500
pd.options.display.max_rows = 500
pd.options.display.max_colwidth = None
df[df['category'] == ''].head(500)
