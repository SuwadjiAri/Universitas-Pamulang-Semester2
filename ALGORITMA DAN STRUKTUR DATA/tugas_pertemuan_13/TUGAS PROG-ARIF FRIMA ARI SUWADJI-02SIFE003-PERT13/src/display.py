# Fungsi display()
def display(antrian):
    if not antrian:
        print("Antrian kosong.")
    else:
        print("Antrian saat ini:")
        for elemen in antrian:
            print(elemen)
    return antrian