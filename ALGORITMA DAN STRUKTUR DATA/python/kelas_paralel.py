level_kelas=input("Masukkan level kelas: ")
jumlah_siswa=input("Masukkan jumlah siswa: ")
jumlah_kelas_paralel=input("Masukkan jumlah kelas paralel: ")

level_kelas = int(level_kelas)
jumlah_siswa = int(jumlah_siswa)
jumlah_kelas_paralel = int(jumlah_kelas_paralel)

print("level kelas ", level_kelas)
print("jumlah siswa ", jumlah_siswa)
print("jumlah kelas paralel ", jumlah_kelas_paralel)

kelas_paralel = int(jumlah_siswa / jumlah_kelas_paralel)
jumlah_siswa_per_kelas = int(jumlah_siswa % jumlah_kelas_paralel)
sisa_siswa = int(jumlah_siswa_per_kelas % kelas_paralel)

for i in range(1, jumlah_kelas_paralel + 1):
    if i == jumlah_kelas_paralel:
        print("Kelas ",level_kelas,"-",i, "jumlah siswa: ",kelas_paralel + sisa_siswa)
    else :
        print("Kelas ",level_kelas,"-",i, "jumlah siswa: ",kelas_paralel)
    
    