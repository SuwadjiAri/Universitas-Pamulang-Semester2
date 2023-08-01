nilai = input("masukkan nilai=")

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)

nilai = int(nilai)
print(faktorial(nilai))