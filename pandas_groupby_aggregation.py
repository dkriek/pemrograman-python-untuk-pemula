import pandas as pd


# Data transaksi penjualan
data = {
    "produk": ["Kopi", "Roti", "Teh", "Kopi", "Roti", "Teh"],
    "kategori": ["Minuman", "Makanan", "Minuman", "Minuman", "Makanan", "Minuman"],
    "jumlah": [3, 2, 4, 5, 1, 2],
    "harga_satuan": [15000, 12000, 8000, 15000, 12000, 8000],
}

df = pd.DataFrame(data)

# Hitung nilai penjualan setiap baris transaksi
df["total_penjualan"] = df["jumlah"] * df["harga_satuan"]

print("Data transaksi:")
print(df)

# GroupBy: kelompokkan berdasarkan kategori, lalu hitung beberapa agregasi
ringkasan_kategori = df.groupby("kategori").agg(
    total_barang=("jumlah", "sum"),
    total_penjualan=("total_penjualan", "sum"),
    rata_rata_transaksi=("total_penjualan", "mean"),
)

print("\nRingkasan per kategori:")
print(ringkasan_kategori)

# Kelompokkan juga berdasarkan produk untuk mengetahui produk terlaris
ringkasan_produk = df.groupby("produk").agg(
    total_barang=("jumlah", "sum"),
    total_penjualan=("total_penjualan", "sum"),
)

print("\nRingkasan per produk:")
print(ringkasan_produk.sort_values("total_penjualan", ascending=False))
