def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    barang = {'Nama': nama_barang, 'Jumlah': jumlah_barang}
    daftar_belanja.append(barang)
    
    tambah_lagi = input("Tambah barang lagi? (y/t): ")
    if tambah_lagi.lower() == 'y':
        tambah_barang()

daftar_belanja = []
total_barang = 0
total_qty = 0

tambah_barang()

print("Daftar Belanja:")
for barang in daftar_belanja:
    print(barang['Nama'], "-", barang['Jumlah'])
    total_barang += 1
    total_qty = total_qty + barang['Jumlah']

print("Total barang:", total_barang)
print("Total qty:", total_qty)

