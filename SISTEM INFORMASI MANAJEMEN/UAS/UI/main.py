from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tentang')
def about():
    return render_template('tentang.html')

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='SI_Management',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Berhasil terhubung ke database")
            return connection

    except Error as e:
        print(f"Error: {e}")

    return connection

@app.route('/users')
def users():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data pengguna
    query = "SELECT * FROM Pengguna"
    cursor.execute(query)
    users = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('users.html', users=users)

@app.route('/companies')
def companies():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data perusahaan
    query = "SELECT * FROM Perusahaan"
    cursor.execute(query)
    companies = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('companies.html', companies=companies)

@app.route('/products')
def products():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data produk
    query = "SELECT * FROM Produk"
    cursor.execute(query)
    products = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('products.html', products=products)

@app.route('/applications')
def applications():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data aplikasi dengan join perusahaan
    query = """
    SELECT Aplikasi.ID_Aplikasi, Aplikasi.Nama_Aplikasi, Aplikasi.Jenis_Aplikasi,
           Aplikasi.Deskripsi, Aplikasi.Tanggal_Pengembangan, Aplikasi.Status_Pengembangan,
           Perusahaan.Nama_Perusahaan
    FROM Aplikasi
    JOIN Perusahaan ON Aplikasi.ID_Perusahaan = Perusahaan.ID_Perusahaan
    """
    cursor.execute(query)
    applications = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('applications.html', applications=applications)

@app.route('/customers')
def customers():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data pelanggan
    query = "SELECT * FROM Pelanggan"
    cursor.execute(query)
    customers = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('customers.html', customers=customers)

@app.route('/modules')
def modules():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data modul
    query = "SELECT * FROM Modul"
    cursor.execute(query)
    modules = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('modules.html', modules=modules)

@app.route('/transactions')
def transactions():
    # Koneksi ke database
    connection = create_connection()
    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query untuk mengambil data transaksi
    query = """
        SELECT T.ID_Transaksi, T.Tanggal_Transaksi, P.Nama_Pelanggan, T.Total_Harga
        FROM Transaksi T
        JOIN Pelanggan P ON T.ID_Pelanggan = P.ID_Pelanggan
        """
    cursor.execute(query)
    transactions = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('transactions.html', transactions=transactions)

@app.route('/access')
def access():
    # Koneksi ke database
    connection = create_connection()

    # Membuat kursor
    cursor = connection.cursor()

    # Eksekusi query dengan JOIN untuk mengambil data hak akses beserta informasi terkait
    query = """
        SELECT HA.ID_Hak_Akses, M.Nama_Modul, P.Nama_Pengguna
        FROM Hak_Akses HA
        JOIN Modul M ON HA.ID_Modul = M.ID_Modul
        JOIN Pengguna P ON HA.ID_Pengguna = P.ID_Pengguna
    """
    cursor.execute(query)
    accesses = cursor.fetchall()

    # Menutup koneksi
    cursor.close()
    connection.close()

    return render_template('access.html', accesses=accesses)

if __name__ == '__main__':
    app.run()
