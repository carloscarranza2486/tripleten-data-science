import pandas as pd

df = pd.read_csv("/datasets/music_log_chpt_11.csv")

aura_count = df[df["Artist"] == "Aura"]["Artist"].count()

print(aura_count)
