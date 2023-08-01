# Inisialisasi antrian sebagai list kosong
antrian = []

# Fungsi enqueue(data)
def enqueue(data):
    antrian.append(data)
    print("Elemen", data, "berhasil ditambahkan ke antrian.")

# Fungsi dequeue()
def dequeue():
    if not antrian:
        print("Antrian kosong, tidak ada elemen yang dihapus.")
    else:
        elemen_dihapus = antrian.pop(0)
        print("Elemen", elemen_dihapus, "dihapus dari antrian.")

# Fungsi display()
def display():
    if not antrian:
        print("Antrian kosong.")
    else:
        print("Antrian saat ini:")
        for elemen in antrian:
            print(elemen)

# Program Utama
while True:
    print("\nMenu Pilihan:")
    print("1. Enqueue (Tambah Elemen)")
    print("2. Dequeue (Hapus Elemen)")
    print("3. Tampilkan Antrian")
    print("4. Keluar")

    pilihan = input("Pilih operasi (1-4): ")

    if pilihan == "1":
        data = input("Masukkan elemen yang akan ditambahkan: ")
        enqueue(data)
    elif pilihan == "2":
        dequeue()
    elif pilihan == "3":
        display()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
