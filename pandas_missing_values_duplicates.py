import pandas as pd


# Data contoh berisi satu transaksi duplikat dan beberapa nilai kosong.
data = {
    "id_transaksi": [101, 102, 102, 103, 104],
    "produk": ["Kopi", "Roti", "Roti", "Teh", None],
    "jumlah": [2, 1, 1, None, 3],
    "harga_satuan": [15000, 12000, 12000, 8000, 9000],
}

df = pd.DataFrame(data)

print("Data awal:")
print(df)

# Periksa jumlah nilai kosong di setiap kolom.
print("\nJumlah nilai kosong:")
print(df.isna().sum())

# Cari duplikat berdasarkan ID transaksi.
jumlah_duplikat = df.duplicated(subset="id_transaksi").sum()
print(f"\nJumlah transaksi duplikat: {jumlah_duplikat}")

# Hapus transaksi dengan ID yang sama, sisakan kemunculan pertama.
df_bersih = df.drop_duplicates(subset="id_transaksi", keep="first").copy()

# Isi nama produk yang kosong dengan label agar tetap terlihat saat dianalisis.
df_bersih["produk"] = df_bersih["produk"].fillna("Tidak diketahui")

# Jumlah atau harga yang kosong tidak dipakai untuk menghitung penjualan,
# jadi buang baris yang tidak memiliki kedua nilai tersebut.
df_bersih = df_bersih.dropna(subset=["jumlah", "harga_satuan"]).copy()

# Hitung total setelah data dibersihkan.
df_bersih["total"] = df_bersih["jumlah"] * df_bersih["harga_satuan"]

print("\nData setelah dibersihkan:")
print(df_bersih)
