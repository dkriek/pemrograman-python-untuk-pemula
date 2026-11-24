import numpy as np


# Data penjualan beberapa produk
produk = np.array(["Kopi", "Roti", "Teh", "Susu"])
jumlah = np.array([3, 2, 4, 1])
harga_satuan = np.array([15000, 12000, 8000, 18000])

# Transformasi: hitung pendapatan untuk setiap produk
pendapatan = jumlah * harga_satuan

print("Pendapatan per produk:", pendapatan)
print("Total penjualan:", pendapatan.sum())
print("Rata-rata per produk:", pendapatan.mean())

# Analisis: cari produk dengan pendapatan di atas rata-rata
di_atas_rata_rata = pendapatan > pendapatan.mean()
print("Produk di atas rata-rata:", produk[di_atas_rata_rata])
print("Pendapatannya:", pendapatan[di_atas_rata_rata])
