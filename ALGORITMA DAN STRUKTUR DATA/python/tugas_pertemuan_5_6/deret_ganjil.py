na=int(input("Nilai Awal:"))
nb=int(input("Nilai Akhir:"))

i = na
while i >= na and i<=nb:
    print(i)
    if i % 2 != 0:
        ng = i
        print(f'Nilai {i} adalah bilangan ganjil')
    i+=1
