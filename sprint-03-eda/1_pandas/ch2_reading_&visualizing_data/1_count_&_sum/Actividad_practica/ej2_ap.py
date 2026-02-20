import pandas as pd

df = pd.read_csv("/datasets/music_log_chpt_11.csv")

# Filtrar por géneros clásicos y pop
classical_df = df[df["genre"] == "classical"]
pop_df = df[df["genre"] == "pop"]

# Calcular el conteo de canciones clásicas y el tiempo total de pop
classical_count = df[df["genre"] == "classical"]["track"].count()
pop_total_time = df[df["genre"] == "pop"]["total play"].sum()

print("Número de canciones clásicas:", classical_count)
print("Tiempo total pop:", pop_total_time)
