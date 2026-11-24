from pathlib import Path

import pandas as pd

# File Excel diletakkan di folder yang sama dengan program ini.
file_excel = Path(__file__).resolve().parent / "data_penjualan.xlsx"

# Membaca sheet pertama dari file Excel.
data = pd.read_excel(file_excel)

print("Data dari Excel:")
print(data)
