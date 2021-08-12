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

pd.set_option('max_columns', None)
pd.set_option('max_rows', 100)
print(df[0:10])

csv_string = """

"""
df = apply_names_and_categories(df, csv_string)

print(df.groupby(['category'])['amount'].sum())
len(df[(df['category'] == '')])

# +
pd.set_option('display.width', 5500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', None)

df[(df['category'] == '')].head(500)
# -
