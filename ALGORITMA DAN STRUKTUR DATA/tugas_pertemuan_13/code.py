# Inisialisasi antrian sebagai array kosong
antrian = []
indeks_awal = 0
indeks_akhir = -1

# Fungsi enqueue(data)
def enqueue(data):
    global indeks_akhir
    if indeks_akhir < len(antrian) - 1:
        antrian.append(data)
        indeks_akhir += 1
        print("Elemen", data, "berhasil ditambahkan ke antrian.")
    else:
        print("Antrian penuh, tidak dapat menambahkan elemen.")

# Fungsi dequeue()
def dequeue():
    global indeks_awal, indeks_akhir
    if indeks_awal <= indeks_akhir:
        elemen_dihapus = antrian[indeks_awal]
        indeks_awal += 1
        print("Elemen", elemen_dihapus, "dihapus dari antrian.")
    else:
        print("Antrian kosong, tidak ada elemen yang dihapus.")

# Fungsi display()
def display():
    if indeks_awal <= indeks_akhir:
        for i in range(indeks_awal, indeks_akhir + 1):
            print(antrian[i])
    else:
        print("Antrian kosong.")

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
