import numpy as np


# Data penjualan beberapa produk
produk = np.array(["Kopi", "Roti", "Teh", "Susu"])
jumlah = np.array([3, 2, 4, 1])
harga_satuan = np.array([15000, 12000, 8000, 18000])

# Hitung pendapatan untuk setiap produk
pendapatan = jumlah * harga_satuan

# Filtering: pilih produk dengan pendapatan minimal Rp30.000
mask = pendapatan >= 30000
produk_terpilih = produk[mask]
pendapatan_terpilih = pendapatan[mask]

# Sorting: urutkan produk terpilih dari pendapatan tertinggi
urutan = np.argsort(pendapatan_terpilih)[::-1]

print("Produk dengan pendapatan minimal Rp30.000,")
print("diurutkan dari pendapatan tertinggi:")

for nama_produk, total in zip(produk_terpilih[urutan], pendapatan_terpilih[urutan]):
    print(f"{nama_produk}: Rp{total:,.0f}")
