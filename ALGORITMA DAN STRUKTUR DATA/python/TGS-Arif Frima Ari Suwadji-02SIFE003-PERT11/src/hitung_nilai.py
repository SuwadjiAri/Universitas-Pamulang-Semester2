# menghitung jumlah nilai dan banyaknya nilai kurang dari 70 per siswa
def jumlah_nilai_dan_banyak_nilai_kurang_70(data_nilai):
    total_nilai = 0
    banyak_nilai_kurang_70 = 0

    for nilai in data_nilai:
        nilai_pelajaran = nilai[1]
        total_nilai += nilai_pelajaran

        if nilai_pelajaran < 70:
            banyak_nilai_kurang_70 += 1

    return total_nilai, banyak_nilai_kurang_70