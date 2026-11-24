import json
from pathlib import Path


folder_project = Path(__file__).resolve().parent
file_input = folder_project / "penjualan.json"
file_output = folder_project / "hasil_penjualan.json"

# Extract: baca data JSON dari file.
with file_input.open("r", encoding="utf-8") as file:
    data_penjualan = json.load(file)

# Transform: hitung total untuk setiap transaksi dan total seluruh penjualan.
total_seluruh_penjualan = 0

for transaksi in data_penjualan["transaksi"]:
    transaksi["total"] = transaksi["jumlah"] * transaksi["harga_satuan"]
    total_seluruh_penjualan += transaksi["total"]

hasil = {
    "transaksi": data_penjualan["transaksi"],
    "total_seluruh_penjualan": total_seluruh_penjualan,
}

# Load: simpan hasil transformasi ke file JSON baru.
with file_output.open("w", encoding="utf-8") as file:
    json.dump(hasil, file, ensure_ascii=False, indent=4)

print("Data transaksi yang sudah diproses:")
for transaksi in hasil["transaksi"]:
    print(
        f"{transaksi['produk']}: {transaksi['jumlah']} x "
        f"Rp{transaksi['harga_satuan']:,} = Rp{transaksi['total']:,}"
    )

print(f"\nTotal seluruh penjualan: Rp{total_seluruh_penjualan:,}")
print(f"Hasil disimpan ke: {file_output.name}")
