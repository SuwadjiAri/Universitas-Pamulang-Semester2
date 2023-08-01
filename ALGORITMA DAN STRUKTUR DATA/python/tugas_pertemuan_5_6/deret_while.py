na=int(input("Nilai Awal:"))
nb=int(input("Nilai Akhir:"))
nk=int(input("Nilai Kelipatan:"))

i = na
while i >= na and i<=nb:
    print(i)
    if i % 2 != 0:
        ng = i
        print(f'Nilai {i} adalah bilangan ganjil')
    if i % nk == 0:
        hk = i
        print(f'Nilai {i} adalah kelipatan {nk}')
    i+=1
