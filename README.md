# 💰 KAWI-Kas: Catatan Kas Digital Berbasis Konsol
 KAWI-Kas adalah solusi fintech minimalis berbasis terminal yang dirancang untuk melacak dan mengelola keuangan pribadi harian secara aman. Proyek ini dibangun dengan Python murni, berfokus pada integritas data dan pengalaman pengguna di lingkungan command line interface (CLI).

## ✨ Fitur Kunci & Arsitektur
**Fungsionalitas Inti**
- **Dukungan Multi-Akun:** Sistem memungkinkan pembuatan dan pengelolaan akun pengguna yang terpisah, dengan saldo dan riwayat transaksi yang terisolasi per individu.

- **Akses Terkunci:** Sistem Daftar/Masuk dengan autentikasi PIN dan Password.

- **Keamanan:** Fitur cooldown 10 detik setelah 3 kali salah memasukkan PIN (seperti real-world banking).

- **Pencatatan Detail:** Mencatat Pemasukan dan Pengeluaran lengkap dengan Nominal dan Keterangan.

- **Audit Riwayat:** Tampilan riwayat transaksi yang rapi menggunakan string formatting (.ljust()).

- **Data Immutability:** Memungkinkan Edit dan Hapus transaksi dengan logika yang menjamin Saldo Akhir selalu akurat (self-correcting balance).

**Struktur Data (Senior View)**  
Data pengguna (`nama`, `pin`, `password`, `saldo`) disimpan secara independen. Riwayat transaksi diatur menggunakan List Bersarang (`Nested Lists`) (`jenis_transaksi`, `nominal_transaksi`, `keterangan_transaksi`) untuk memetakan setiap transaksi ke index pengguna yang benar, memastikan data tetap disinkronkan antar akun.  

## 🛠️ Persyaratan & Instalasi
Proyek ini dirancang untuk dijalankan di lingkungan Python 3.11 atau yang lebih baru.

1. **Persiapan Lokal**
    - **Clone Repositori:**
    ``` bash
    git clone [ALAMAT REPO ANDA]
    cd [NAMA FOLDER PROYEK]
    ```
    - **Jalankan Script**
    ``` bash
    python catatan_kas.py
    ```

2. **Deployment dengan Docker (Direkomendasikan) 🐳**
Untuk memastikan konsistensi lingkungan, containerize aplikasi dengan Docker.

    - **Build Image:** (Gunakan base image `python:3.11-slim` seperti yang didefinisikan di `Dockerfile`).
    ``` bash
    docker build -t kawi-kas .
    ```
    - **Jalankan Aplikasi:** Gunakan flag -it untuk mode interaktif (memungkinkan input terminal).
    ``` bash
    docker run --rm -it kawi-kas
    ```
(Flag --rm secara otomatis menghapus container setelah selesai)

## 💡 Panduan Penggunaan
Aplikasi akan memandu Anda melalui menu utama.  
|Menu|Keterangan|Catatan Penting|
|-----|--------|---------|
|Daftar|Buat akun baru dengan Nama Pengguna, Password, PIN 4 digit, dan Saldo Awal.| Pastikan pin hanya 4 digit|
|Catat Pemasukan/Pengeluaran|Menambahkan data ke riwayat dan memperbarui saldo.|Nominal 0 akan membatalkan input.|
|Edit Riwayat|Memungkinkan koreksi typo pada Nominal atau Keterangan.|Logika ini secara otomatis membalikkan transaksi lama dan menghitung ulang saldo.|
|Hapus Transaksi|Menghapus entri dari riwayat dan mengembalikan saldo ke keadaan sebelum transaksi itu.|

## 👤 Kontributor
Proyek ini dikembangkan oleh:
- Kahfi Athohillah
- Wisanggeni Cahya Manggalar

## 📜 Lisensi
Proyek ini berada di bawah Lisensi MIT. Silakan merujuk pada file `LICENSE` untuk detail lengkap