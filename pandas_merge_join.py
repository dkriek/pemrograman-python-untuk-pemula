import pandas as pd


# Dataset transaksi penjualan
transaksi = pd.DataFrame(
    {
        "id_transaksi": [101, 102, 103, 104],
        "id_produk": [1, 2, 1, 3],
        "jumlah": [2, 1, 3, 2],
    }
)

# Dataset master produk
produk = pd.DataFrame(
    {
        "id_produk": [1, 2, 3],
        "nama_produk": ["Kopi", "Roti", "Teh"],
        "harga_satuan": [15000, 12000, 8000],
    }
)

# MERGE: gabungkan dengan mencocokkan kolom id_produk di kedua dataset.
# how="left" memastikan semua transaksi tetap muncul.
hasil_merge = pd.merge(
    transaksi,
    produk,
    on="id_produk",
    how="left",
)
hasil_merge["total"] = hasil_merge["jumlah"] * hasil_merge["harga_satuan"]

print("Hasil merge:")
print(hasil_merge)

# JOIN: cara lain menggabungkan data; id_produk di transaksi dicocokkan
# dengan index produk.
produk_berdasarkan_id = produk.set_index("id_produk")
hasil_join = transaksi.join(produk_berdasarkan_id, on="id_produk")

print("\nHasil join:")
print(hasil_join)
