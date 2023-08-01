import mysql.connector
from mysql.connector import Error

# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sim_app',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Berhasil terhubung ke database")
            return connection

    except Error as e:
        print(f"Error: {e}")

    return connection

# Fungsi untuk menutup koneksi ke database
def close_connection(connection):
    if connection:
        connection.close()
        print("Koneksi database ditutup")

# Fungsi untuk menambahkan data mobil ke tabel
def insert_mobil(connection, data):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO mobil (nama, tahun, harga, merk, jenis, nopol) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        connection.commit()
        print("Data mobil berhasil ditambahkan")

    except Error as e:
        print(f"Error: {e}")

# Fungsi untuk membaca data mobil dari tabel
def get_mobil(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM mobil"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data mobil berhasil didapatkan")
        print(result)
        return result

    except Error as e:
        print(f"Error: {e}")
        return []

# Fungsi untuk mengupdate data mobil di tabel berdasarkan ID
def update_mobil(connection, id, data):
    try:
        cursor = connection.cursor()
        query = "UPDATE mobil SET nama=%s, tahun=%s, harga=%s, merk=%s, jenis=%s, nopol=%s WHERE id=%s"
        cursor.execute(query, data + (id,))
        connection.commit()
        print("Data mobil berhasil diupdate")

    except Error as e:
        print(f"Error: {e}")

# Fungsi untuk menghapus data mobil dari tabel berdasarkan ID
def delete_mobil(connection, id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM mobil WHERE id=%s"
        cursor.execute(query, (id,))
        connection.commit()
        print("Data mobil berhasil dihapus")

    except Error as e:
        print(f"Error: {e}")
        
# fungsi untuk data konsumen
def get_konsumen(connection, id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM konsumen WHERE id=%s"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        print("Data konsumen berhasil didapatkan")
        print(result)
        return result
    except Error as e:
        print(f"Error: {e}")
        return []
    
