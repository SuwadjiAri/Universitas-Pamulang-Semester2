from src.enqueue import enqueue
from src.dequeue import dequeue
from src.display import display

# Inisialisasi antrian sebagai list kosong
antrian = []

# Batas maksimum antrian
kapasitas_antrian = 3

#main program
while True:
    print("\nMenu Pilihan:")
    print("1. Enqueue (Tambah Elemen)")
    print("2. Dequeue (Hapus Elemen)")
    print("3. Tampilkan Antrian")
    print("4. Keluar")

    pilihan = input("Pilih operasi (1-4): ")

    if pilihan == "1":
        data = input("Masukkan elemen yang akan ditambahkan: ")
        enqueue(antrian, kapasitas_antrian, data)
    elif pilihan == "2":
        dequeue(antrian)
    elif pilihan == "3":
        display(antrian)
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    # hitung jumlah antrian
    jumlah_antrian = len(antrian)
    print("Jumlah antrian saat ini:", jumlah_antrian)