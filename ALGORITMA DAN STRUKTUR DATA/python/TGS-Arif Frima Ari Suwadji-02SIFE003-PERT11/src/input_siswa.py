# Fungsi untuk menginput data siswa
# public array

def input_data_siswa():
    data_siswa = []
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    if jumlah_siswa < 20:
        print("Jumlah siswa minimal 20")
        return input_data_siswa()

    for i in range(jumlah_siswa):
        nama = input("Nama siswa: ")
        nilai = []

        for mata_pelajaran in ["Matematika", "Bahasa Inggris", "Agama", "Kimia", "Bahasa Indonesia", "Sejarah"]:
            nilai_pelajaran = float(input("Nilai {} siswa {}: ".format(mata_pelajaran, nama)))
            nilai.append((mata_pelajaran, nilai_pelajaran))

        data_siswa.append((nama, nilai))

    return data_siswa