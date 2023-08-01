daftar_barang = [{"Kode": "BR"}, {"Nama_Barang": "Beras"}, {"Harga_Satuan": 300000}, {"Kode": "GL"}, {"Nama_Barang": "Gula"}, {"Harga_Satuan": 12000}, {"Kode":"MY", "Nama_Barang":"Minyak","Harga_Satuan":56000}]

daftar_penjualan = []
for barang in daftar_barang :
    print("Kode ", barang["Kode"], " - ", barang["Nama_Barang"])
    jumlah_unit = int(input("Masukkan jumlah Unit : "))
    daftar_penjualan.append({"Kode" : barang["Kode"], "Nama_Barang": barang["Nama_Barang"], "Harga_Satuan": barang["Harga_Satuan"], "Jumlah Unit": jumlah_unit})
    # 081213357600

for jual in daftar_penjualan:
    print("Kode,     Nama Barang,    Harga Barang,     Jumlah Beli,     Kartu,       Diskon,      PPN,     Bayar")
    print( jual["kode"], jual["Nama_barang"], jual["Harga_Satuan"], jual["jumlah_unit"])
    
    