import pandas as pd

df = pd.read_csv("/datasets/music_log_chpt_11.csv")  # Lee el archivo CSV

zodiac_total = df[df["Artist"] == "Zodiac"][
    "total play"
].sum()  # Suma las duraciones de las canciones de Zodiac

print(zodiac_total)  # Muestra el resultado
