import pandas as pd


# Membuat DataFrame dari data sederhana
data = {
    "nama": ["Andi", "Budi", "Citra"],
    "nilai": [85, 90, 78],
}

df = pd.DataFrame(data)

print("Data siswa:")
print(df)

# Menghitung rata-rata nilai
rata_rata = df["nilai"].mean()
print("\nRata-rata nilai:", rata_rata)
