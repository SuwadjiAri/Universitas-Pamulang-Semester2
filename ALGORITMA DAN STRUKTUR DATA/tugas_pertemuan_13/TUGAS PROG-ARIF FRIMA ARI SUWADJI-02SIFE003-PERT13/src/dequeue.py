# Fungsi dequeue()
def dequeue(antrian):
    if not antrian:
        print("Antrian kosong, tidak ada elemen yang dihapus.")
    else:
        elemen_dihapus = antrian.pop(0)
        print("Elemen", elemen_dihapus, "dihapus dari antrian.")
    return antrian