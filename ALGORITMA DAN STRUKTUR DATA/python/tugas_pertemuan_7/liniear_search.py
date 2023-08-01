def linear_search(a, n, k):
    # a: array yang akan dicari
    # n: ukuran array
    # k: elemen yang akan dicari
    for i in range(n):
        if a[i] == k:
            return i
    return -1

# penggunaan teknik linear search
arr = [2, 5, 6, 8, 10, 13, 15, 17, 18, 19, 21]
n = len(arr)
k = int(input("Masukkan elemen yang akan dicari: "))
r = linear_search(arr, n, k)
if r == -1:
    print("Elemen tidak ditemukan")
else:
    print("Elemen ditemukan pada indeks ", r)
