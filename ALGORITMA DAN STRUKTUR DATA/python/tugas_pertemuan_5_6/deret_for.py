na=int(input("Nilai Awal:"))
nb=int(input("Nilai Akhir:"))
nk=int(input("Nilai Kelipatan:"))

i = na
for i in range(na,nb+1):
    if i >= na and i<=nb:
        print(i)
        if i % 2 != 0:
            ng = i
            print(f'Nilai {ng} adalah bilangan ganjil')
        if i % nk == 0:
            hk = i
            print(f'Nilai {hk} adalah kelipatan {nk}')
        i+=1