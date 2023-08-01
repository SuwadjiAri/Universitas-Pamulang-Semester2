
# antrian = ["hallo", "perknalkan", "nama", "saya", "arif", "suwadji"]
antrian = []

len = len(antrian)

if len == 0:
    print("Antrian kosong.")
else:
    print("Antrian saat ini:")
    for elemen in antrian:
        print(elemen)