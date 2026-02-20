import pandas as pd

df = pd.read_csv("/datasets/music_log_chpt_11.csv")

result = df.loc[7, "track"]
print(result)

"""Result"""

# Riviera
