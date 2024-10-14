from flask import Flask, render_template
from config.db_config import init_db

app = Flask(__name__)

mysql = init_db(app)

@app.route('/')
def home():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")  # Ambil semua data dari tabel users
        data = cur.fetchall()  # Data yang diambil adalah list of tuples
        cur.close()
        return render_template('index.html', users=data)  # Kirim data ke template HTML
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
