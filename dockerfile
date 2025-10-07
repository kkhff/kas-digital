# 1. Base Image: Menggunakan image Python 3.11 slim sebagai dasar
FROM python:3.11-slim

# 2. Working Directory: Menetapkan direktori kerja di dalam container
WORKDIR /app

# 3. Copy Files: Menyalin semua file dari direktori lokal ke dalam direktori kerja di container
# Pastikan file catatan_kas.py ada di direktori yang sama dengan Dockerfile
COPY . /app

# 4. Command to Run: Menjalankan aplikasi Python saat container dijalankan
# Ganti "catatan_kas.py" dengan nama file Python utama Anda jika berbeda
CMD ["python", "catatan_kas.py"]