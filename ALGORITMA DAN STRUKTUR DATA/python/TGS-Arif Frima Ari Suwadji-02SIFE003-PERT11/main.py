from src.input_siswa import input_data_siswa
from src.ledger import tampil_ledger
from src.hitung_nilai import jumlah_nilai_dan_banyak_nilai_kurang_70
from src.quick_sort import quick_sort


# panggil fungsi input_siswa
data_siswa = input_data_siswa()

# tampilkan ledger
tampil_ledger(data_siswa)

# menghitung jumlah nilai dan banyaknya nilai kurang dari 70 per siswa
print("Mehitung jumlah nilai dan banyaknya nilai kurang dari 70")
for siswa in data_siswa:
    nama_siswa = siswa[0]
    nilai_siswa = siswa[1]
    total_nilai, banyak_nilai_kurang_70 = jumlah_nilai_dan_banyak_nilai_kurang_70(nilai_siswa)
    print("Nama siswa: {}".format(nama_siswa))
    print("Jumlah nilai: {}".format(total_nilai))
    print("Banyaknya nilai kurang dari 70: {}".format(banyak_nilai_kurang_70))
    print("============")
    
# perankingan siswa
data_siswa_sorted = quick_sort(data_siswa)

# daftar sebelum perankingan
print("\nDaftar sebelum perankingan:")
n = 0
for siswa in data_siswa:
    n += 1
    print("{}. {}".format(n, siswa[0]))

# daftar sesudah perankingan descending
print("\nDaftar sesudah perankingan (descending):")

i = 0
for siswa in data_siswa_sorted:
    i += 1
    print("{}. {}".format(i, siswa[0]))
