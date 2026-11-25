import json
from pathlib import Path

import pandas as pd


file_json = Path(__file__).resolve().parent / "pesanan_nested.json"

# Extract: baca respons JSON yang berisi objek bertingkat dan daftar items.
with file_json.open("r", encoding="utf-8") as file:
    data_pesanan = json.load(file)

# Transform: ratakan items menjadi baris, lalu salin informasi pesanan
# dan customer ke setiap baris item yang terkait.
df_items = pd.json_normalize(
    data_pesanan["orders"],
    record_path="items",
    meta=[
        "order_id",
        "tanggal",
        ["customer", "id"],
        ["customer", "nama"],
    ],
    record_prefix="item_",
    meta_prefix="order_",
)

# Hitung nilai penjualan setiap item.
df_items["item_total"] = df_items["item_jumlah"] * df_items["item_harga"]

print("DataFrame hasil normalisasi JSON:")
print(df_items)

print("\nJumlah baris dan kolom:", df_items.shape)
print("Nama kolom:", df_items.columns.tolist())
