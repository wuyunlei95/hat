from common.util.csv_file import CSV_File

data = CSV_File().read_by_dict('../../src/data/module_title.csv')
for row in data:
    print(row)
    print((row['module']))