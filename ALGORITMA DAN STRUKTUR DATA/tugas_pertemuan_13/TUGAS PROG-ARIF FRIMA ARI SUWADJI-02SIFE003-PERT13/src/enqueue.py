# Fungsi enqueue
def enqueue(antrian, kapasitas_antrian, data):
    if len(antrian) < kapasitas_antrian:
        antrian.append(data)
        print("Elemen", data, "berhasil ditambahkan ke antrian.")
    else:
        print("Antrian penuh, tidak dapat menambahkan elemen.")
    return antrian