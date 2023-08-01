daftar_belanja = []

jumlah_barang = int(input("Masukkan jumlah barang yang akan dibeli: "))

for i in range(jumlah_barang):
    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    barang = {'Nama': nama_barang, 'Jumlah': jumlah_barang}
    daftar_belanja.append(barang)

print("Daftar Belanja:")
for barang in daftar_belanja:
    print(barang['Nama'], "-", barang['Jumlah'])
