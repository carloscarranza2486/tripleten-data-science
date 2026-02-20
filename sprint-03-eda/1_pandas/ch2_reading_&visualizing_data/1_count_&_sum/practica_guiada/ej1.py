import pandas as pd

df = pd.read_csv("/datasets/music_log_chpt_11.csv")

user_mean_dur = df[df["user_id"] == "5D9AAD37"]["total play"].mean()

print(user_mean_dur)
