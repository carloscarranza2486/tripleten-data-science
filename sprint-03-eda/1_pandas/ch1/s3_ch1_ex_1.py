import pandas as pd

df = pd.read_csv("/dataset/music_log_chpt_11.csv")

data_types = df.dtypes
column_names = df.columns
data_shape = df.shape
df.info()

print(data_types)
print(column_names)
print(data_shape)
