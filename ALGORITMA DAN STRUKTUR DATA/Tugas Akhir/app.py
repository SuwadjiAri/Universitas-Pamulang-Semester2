from flask import Flask, render_template, request
from mysql_connector import create_connection, close_connection, get_mobil

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk hasil pencarian
@app.route('/search', methods=['GET'])
def search():
    brand = request.args.get('brand')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    
    # Membuat koneksi ke database
    connection = create_connection()

    # Mendapatkan data mobil dari database
    mobil = get_mobil(connection)
    
    #dump data mobil
    print(mobil)

    # Menutup koneksi
    close_connection(connection)

    # Render template HTML dan kirimkan data mobil ke template
    return render_template('result.html', mobils=mobil)

# Route untuk halaman input mobil
@app.route('/input', methods=['GET', 'POST'])
def input_mobil():
    if request.method == 'POST':
        # Ambil data dari form input
        nama = request.form['nama']
        tahun = int(request.form['tahun'])
        harga = int(request.form['harga'])
        merk = request.form['merk']
        jenis = request.form['jenis']
        nopol = request.form['nopol']

        # Membuat koneksi ke database
        connection = create_connection()

        # Memasukkan data mobil ke database
        insert_mobil(connection, nama, tahun, harga, merk, jenis, nopol)

        # Menutup koneksi
        connection.close()

        # Redirect ke halaman utama setelah berhasil memasukkan data
        return redirect('/')
    else:
        return render_template('input.html')

@app.route('/konsumen')
def konsumen():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM konsumen"
    cursor.execute(query)
    result = cursor.fetchall()
    data_konsumen = result
    close_connection(connection)
    return render_template('konsumen.html', data_konsumen=data_konsumen)

@app.route('/pegawai')
def pegawai():
    # Mengambil data pegawai dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM pegawai"
    cursor.execute(query)
    result = cursor.fetchall()
    data_pegawai = result
    close_connection(connection)
    return render_template('pegawai.html', data_pegawai=data_pegawai)

@app.route('/divisi')
def divisi():
    # Mengambil data divisi dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM divisi"
    cursor.execute(query)
    result = cursor.fetchall()
    data_divisi = result
    close_connection(connection)
    return render_template('divisi.html', data_divisi=data_divisi)

@app.route('/jabatan')
def jabatan():
    # Mengambil data jabatan dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM jabatan"
    cursor.execute(query)
    result = cursor.fetchall()
    data_jabatan = result
    close_connection(connection)
    return render_template('jabatan.html', data_jabatan=data_jabatan)

@app.route('/transaksi')
def transaksi():
    # Mengambil data transaksi dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM transaksi"
    cursor.execute(query)
    result = cursor.fetchall()
    data_transaksi = result
    close_connection(connection)
    return render_template('transaksi.html', data_transaksi=data_transaksi)

@app.route('/status_transaksi')
def status_transaksi():
    # Mengambil data status transaksi dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM status_transaksi"
    cursor.execute(query)
    result = cursor.fetchall()
    data_status_transaksi = result
    close_connection(connection)
    return render_template('status_transaksi.html', data_status_transaksi=data_status_transaksi)

@app.route('/detail_status_transaksi')
def detail_status_transaksi():
    # Mengambil data detail status transaksi dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM detail_status_transaksi"
    cursor.execute(query)
    result = cursor.fetchall()
    data_detail_status_transaksi = result
    close_connection(connection)
    return render_template('detail_status_transaksi.html', data_detail_status_transaksi=data_detail_status_transaksi)

@app.route('/detail_pembayaran')
def detail_pembayaran():
    # Mengambil data detail pembayaran dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM detail_pembayaran"
    cursor.execute(query)
    result = cursor.fetchall()
    data_detail_pembayaran = result
    close_connection(connection)
    return render_template('detail_pembayaran.html', data_detail_pembayaran=data_detail_pembayaran)

@app.route('/jenis_pembayaran')
def jenis_pembayaran():
    # Mengambil data jenis pembayaran dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM jenis_pembayaran"
    cursor.execute(query)
    result = cursor.fetchall()
    data_jenis_pembayaran = result
    close_connection(connection)
    return render_template('jenis_pembayaran.html', data_jenis_pembayaran=data_jenis_pembayaran)

@app.route('/pembayaran')
def pembayaran():
    # Mengambil data pembayaran dari database
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM pembayaran"
    cursor.execute(query)
    result = cursor.fetchall()
    data_pembayaran = result
    close_connection(connection)
    return render_template('pembayaran.html', data_pembayaran=data_pembayaran)

if __name__ == '__main__':
    app.run(debug=True)
