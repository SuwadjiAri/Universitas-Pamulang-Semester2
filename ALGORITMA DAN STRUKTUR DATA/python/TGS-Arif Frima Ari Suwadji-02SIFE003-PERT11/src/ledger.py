# Fungsi untuk menampilkan ledger
def tampil_ledger(data_siswa):
    print("Tampilan Ledger Siswa")
    print("============")

    for siswa in data_siswa:
        nama_siswa = siswa[0]
        nilai_siswa = siswa[1]

        print("Nama siswa: {}".format(nama_siswa))
        print("Nilai:")

        for nilai in nilai_siswa:
            mata_pelajaran = nilai[0]
            nilai_pelajaran = nilai[1]
            print("{}: {}".format(mata_pelajaran, nilai_pelajaran))

    print("============")
