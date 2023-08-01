from mysql.connector import connect

# Buat koneksi ke database
connection = connect(
    host='localhost',
    user='root',
    password='',
    database='sim_app'
)

# Buat cursor
cursor = connection.cursor()

# Daftar mobil
mobil_list = [
    {'id': 1, 'nama': 'Avanza', 'tahun': 2019, 'harga': 150000000, 'merk': 'Toyota', 'jenis': 'MPV', 'nopol': 'B 1234 AB'},
    {'id': 2, 'nama': 'Xenia', 'tahun': 2020, 'harga': 160000000, 'merk': 'Daihatsu', 'jenis': 'MPV', 'nopol': 'B 5678 CD'},
    {'id': 3, 'nama': 'Innova', 'tahun': 2018, 'harga': 180000000, 'merk': 'Toyota', 'jenis': 'MPV', 'nopol': 'B 9012 EF'}
]

# Query untuk memasukkan data mobil ke tabel mobil
query = "INSERT INTO mobil (id, nama, tahun, harga, merk, jenis, nopol) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# Loop melalui daftar mobil dan jalankan query untuk setiap mobil
for mobil in mobil_list:
    values = (mobil['id'], mobil['nama'], mobil['tahun'], mobil['harga'], mobil['merk'], mobil['jenis'], mobil['nopol'])
    cursor.execute(query, values)

# Commit perubahan ke database
connection.commit()

# Tutup cursor dan koneksi
cursor.close()
connection.close()
