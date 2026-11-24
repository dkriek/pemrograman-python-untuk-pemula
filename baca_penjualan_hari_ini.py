from datetime import date
from pathlib import Path

import pandas as pd

# Membaca data penjualan dari file CSV di folder yang sama dengan program ini.
file_csv = Path(__file__).resolve().parent / "penjualan.csv"
data = pd.read_csv(file_csv)

# Ambil transaksi yang tanggalnya sama dengan tanggal hari ini.
hari_ini = date.today().isoformat()
penjualan_hari_ini = data[data["tanggal"] == hari_ini].copy()

print(f"Data penjualan tanggal {hari_ini}:")

if penjualan_hari_ini.empty:
    print("Belum ada penjualan hari ini.")
else:
    penjualan_hari_ini["total"] = (
        penjualan_hari_ini["jumlah"] * penjualan_hari_ini["harga_satuan"]
    )
    print(penjualan_hari_ini)

    total_penjualan = penjualan_hari_ini["total"].sum()
    print(f"\nTotal pemasukan hari ini: Rp{total_penjualan:,.0f}")
