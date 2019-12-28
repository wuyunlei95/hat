import pandas as pd

data = pd.read_csv('..//data//add_user_fields.csv',nrows = 5)
# nrows = 5 是读取去掉标题栏之后的5行
print(data)