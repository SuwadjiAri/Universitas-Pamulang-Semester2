def binery_search(a, n, k):
    # a: array yang akan dicari
    # n: ukuran array
    # k: elemen yang akan dicari
    # r: indeks terakhir
    # l: indeks awal
    # m: indeks tengah
    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2
        print(f"l={l}, m={m}, r={r}")
        if a[m] == k:
            return m
        elif a[m] < k:
            l = m + 1
        else:
            r = m - 1
    return -1

a = [2, 5, 6, 8, 10, 13, 15, 17, 18, 19, 21]
n = len(a)
k = int(input("Masukkan elemen yang akan dicari: "))

res = binery_search(a, n, k)
if res == -1:
    print("Elemen tidak ditemukan")
else :
    print("Elemen ditemukan pada indeks ", res)