import random

hm = int(7000)
ha = int(3500)
hj = int(2000)

# cetak data tanpa menggunakan print
nm = input("Nama Mahasiswa: ")
ub = int(input("Uang Bayar: "))
rd = input("Acak Jumlah Buah (y/t): ")

print("DATA PENJUALAN")
print(f'Toko Buah "Segar" - {nm}')
print("Data Harga Buah")
print(f'a. Mangga   : Rp {hm}/buah')
print(f'b. Apel     : Rp {ha}/buah')
print(f'c. Jeruk    : Rp {hj}/buah')
print(f'Uang yang dibelanjakan: Rp {ub}')
print("Mendapat:")

dictionary = {'mangga': hm, 'apel': ha, 'jeruk': hj}

if rd == 't':
    jm, ja, jj = 0, 0, 0

    jm = int(ub / hm)
    uk = ub - (hm*jm)
    print(f'Mangga  : {jm} buah')

    if (uk / ha) >= 1:
        ja = int(uk / ha)
        uk = uk - (ha*ja)

    print(f'Apel    : {ja} buah')
        
    if (uk / hj) >= 1:
        jj = int(uk / hj)
        uk = uk - (hj*jj)

    print(f'Jeruk   : {jj} buah')
    
    print(f'Uang kembalian: Rp {uk}')
    print("="*30)
else:
    keys = list(dictionary.keys())
    random.shuffle(keys)
    for key in keys:
        # print (key, dictionary[key])
        jb = int(ub / dictionary[key])
        uk = ub - (dictionary[key]*jb)
        ub = uk
        print(f'{key} : {jb} buah')
    print(f'Uang kembalian: Rp {uk}')
    print("="*30)