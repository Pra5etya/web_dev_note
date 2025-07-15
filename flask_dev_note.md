# Log

1. Install library core yang dibutuhkan terlebih dahulu:
    ```bash
        pip install Flask Flask-SQLAlchemy python-dotenv
    ```

2. Buat terlebih dahulu folder struktur:
    ```graphql
    <!-- aplikasi utama -->
    app
        models
            __init__.py         ->  register models agar lebih mudah di maintenance
            name_db.py

        middleware
            __init__.py         ->  register middleware agar lebih mudah di maintenance
            auth.py
            log.py
            secutiy.py

        private
            image
                sample.jpg

            animation
                sample.gif

        routes
            __init__.py         ->  register routes agar lebih mudah di maintenance
            main_routes.py
            api_routes.py

        static
            css
                main.css        ->  kumpulan dari beberapa file .css
                style.css

            js
                main.js         ->  kumpulan dari beberapa file .js
                detect.js

            polyfill
                minified.js     ->  biasanya file jadi yang telah di download agar bisa menyesuaikan browser

        templates
            base.html           ->  base jinja menggunakan {% extends base.html %} ke tampilan halaman html lain (misal: index.html, dsb)
            index.html          ->  tampilan halaman index.html dengan menggunakan {% include tujuan_file/sample.html %}
            index               ->  tempat penyimpanan {% include tujuan_file/sample.html %}, untuk tampilan halaman web

        shell.py                ->  Menyiapkan variabel agar langsung tersedia saat kamu menjalankan **flask shell** di terminal

    <!-- penyimpanan config -->
    config
        __init__.py             ->  register config agar lebih mudah di maintenance
        default.py
        development.py
        staging.py
        production.py
        testing.py

    instance                    ->  folder menyimpan file sensitive
    migration                   ->  folder untuk migrasi data (database)
    test                        ->  folder untuk melakukan testing
    ```

3. setelah membuat struktur folder tersebut, maka berikutnya terapkan fungsi sederhana web terlebih dahulu, yakni:
    1. pembuatan isi folder **static (css, js, dan polyfill)** beserta dengan **templates** nya agar bisa support pada semua browser
    2. pembuatan **route beserta inisialisasi nya**
    3. penerapan inisialisasi pada folder app **(folder aplikasi utama)**
    4. uji coba dengan pembuatan file untuk runninf script **(misal -> run.py pada root project)**

4. jika hal tersebut sudah diterapkan, maka langkah berikutnya adalah pembuatan konfigurasi **(config)**, yakni:
    1. pembuatan folder **config di root project** beserta **file dan inisialisasinya**
    2. pembuatan environment berdasarkan kebutuhan dan bisa disimpan di **instance di root project**, misal:
        * .env.development
        * .env.staging
        * .env.production
        * .env.testing
        * .env.default

5. jika sudah jalankan scriptnya kembali dan pastikan configurasinya sesuai berdasarkan task, yakni pada terminal:
    ```bash
    python run.py            # -> development
    python run.py staging    # -> staging
    python run.py production # -> production

    ```

6. setelah penerapan **config**, beriuktnya menerapkan **database**: 
    1. buat folder **models di aplikasi utama** beserta dengan **file dan inisialisasinya**
    2. buat terlebih dahulu file yang ada di **models**, kemudian **forms / tampilan untuk keluar masuk data** kemudian file yang ada di **forms**
    3. s


# ✅ Relational Database Engines yang Didukung SQLAlchemy (dan Flask-SQLAlchemy):

| Engine                    | URI Format Contoh                                      |
| ------------------------- | ------------------------------------------------------ |
| **SQLite**                | `sqlite:///storage/dev.db`                             |
| **PostgreSQL**            | `postgresql://user:password@localhost/dbname`          |
| **PostgreSQL + psycopg2** | `postgresql+psycopg2://user:password@localhost/dbname` |
| **MySQL**                 | `mysql://user:password@localhost/dbname`               |
| **MySQL + pymysql**       | `mysql+pymysql://user:password@localhost/dbname`       |
| **MariaDB**               | `mariadb://user:password@localhost/dbname`             |
| **Oracle**                | `oracle://user:password@localhost:1521/dbname`         |
| **Microsoft SQL Server**  | `mssql+pyodbc://user:password@dsn_name`                |
| **Firebird**              | `firebird://user:password@localhost/dbname`            |
| **Sybase**                | `sybase://user:password@localhost/dbname`              |


## Note

* SQLite: pakai sqlite:/// untuk path lokal.
* PostgreSQL/MySQL: harus pakai :// dua slash, bukan tiga.
* Tidak bisa menulis postgresql:///user:..., karena itu akan disalahartikan sebagai localhost atau socket.

* APScheduler menjadwalkan backup database secara otomatis (misal mingguan) dalam Flask, yakni scheduler berbasis Python yang ringan, powerful, dan bisa dijalankan di dalam proses Flask tanpa proses eksternal seperti cron., berikut folder strukturnya:
    ```arduino
    project_root/
    ├── app/
    ├── config/
    │   ├── backup.py
    │   ├── ...
    ├── scheduler/
    │   └── backup_job.py         ⬅️ Job penjadwalan mingguan
    ├── run.py                    ⬅️ Start app + scheduler
    ```
    * Berikut Cara install APScheduler
    ```bash
    pip install APScheduler
    ```

# RAW CODE:

