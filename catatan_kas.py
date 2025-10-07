import time

nama = []
pin = []
password = []
saldo = []
jenis_transaksi = []
nominal_transaksi = []
keterangan_transaksi = []

while True: 
    print("\n<===== Selamat Datang di KAWI kas =====>\n 1.Daftar \n 2.Masuk \n 3.Keluar")
    pilihan = input("Masukkan Pilihan Anda : ")

    # Daftar
    if pilihan == "1":   
        print("\n<===== Daftar Akun =====>")
        nama_baru = input("Masukkan Nama Pengguna Anda : ")
        if nama_baru in nama:
            print("Nama sudah terdaftar, silakan coba lagi.")
            continue
        password_baru = input("Masukkan Password Pengguna Anda : ")
        pin_baru = input("Masukkan PIN (4 digit) : ")
        if len(pin_baru) != 4 or not pin_baru.isdigit():
            print("PIN harus terdiri dari 4 digit angka, silakan coba lagi.")
            continue
        saldo_awal = int(input("Masukkan Saldo Awal : Rp"))
        if saldo_awal < 0:
            print("Saldo awal tidak boleh negatif, silakan coba lagi.")
            continue
        nama.append(nama_baru)
        pin.append(pin_baru)
        password.append(password_baru)
        saldo.append(saldo_awal)
        jenis_transaksi.append([])
        nominal_transaksi.append([])
        keterangan_transaksi.append([])
        print("Akun berhasil dibuat!")
    # Akhir daftar

    # Masuk
    elif pilihan == "2":
        print("\n<===== Masuk Akun =====>")
        nama_masuk = input("Masukkan Nama Pengguna : ")
        if nama_masuk in nama:
            index = nama.index(nama_masuk)
            pin_masuk = input("Masukkan PIN Pengguna : ")
            max_attempts = 3
            masuk = False
            for attempts in range(1, max_attempts + 1):
                if pin_masuk == pin[index]:
                    print("PIN benar.")
                    print(f"Selamat datang, {nama_masuk}!")
                    masuk = True
                    break
                else:
                    if attempts < max_attempts:
                        print(f"PIN salah. Anda memiliki {max_attempts - attempts} kesempatan lagi.")
                        pin_masuk = input("Masukkan PIN Pengguna : ")
                        
                    else:
                        print("PIN salah. Akun Anda akan dibekukan selama 10 detik.")
                        print("\n<===== Akun Dibekukan ====>")
                        for tunggu in range(10, 0, -1):
                            print(f"Silakan tunggu {tunggu} detik.", end='\r')
                            time.sleep(1)
                        print("\nAnda dapat mencoba masuk kembali sekarang.")

            # Jika berhasil masuk
            if masuk:
                while True:
                    print("\n<===== Menu Utama =====>\n 1.Cek Saldo \n 2.Catat Pemasukan \n 3.Catat Pengeluaran \n 4.Riwayat Transaksi \n 5.Edit Riwayat \n 6.Hapus transaksi \n 7.Ubah Pin \n 8.Keluar")
                    menu = input("Masukkan Pilihan Anda : ")

                    # Lihat saldo
                    if menu == "1":
                        print("\n<==== CEK SALDO ====>")
                        print(f"Saldo Anda saat ini : Rp{saldo[index]}")
                    # Akhit lihat saldo

                    #Tambah saldo 
                    elif menu == "2":
                        try:
                            print("\n<==== CATAT PEMASUKAN ====>")
                            nominal = int(input("Masukkan nominal pemasukkan (ketik '0' untuk batal) : Rp"))
                            if nominal == 0:
                                print("Batal mencatat pemasukkan.")
                                continue
                            keterangan = input("Masukkan keterangan pemasukkan : ")
                            if keterangan.strip() == "":
                                print("Keterangan tidak boleh kosong.")
                                continue
                            if nominal > 0:
                                    saldo[index] += nominal
                                    jenis_transaksi[index].append("Pemasukan")
                                    nominal_transaksi[index].append(nominal)
                                    keterangan_transaksi[index].append(keterangan)
                                    print(f"Pemasukkan Rp{nominal} dari {keterangan} berhasil dicatatat. Saldo kas: Rp{saldo[index]}")
                            else:
                                print("Jumlah harus lebih dari 0.")
                        except ValueError:
                            print("Input tidak valid, silakan masukkan angka.")
                    # Akhir tambah saldo

                    # Tarik saldo
                    elif menu == "3":
                        try:
                            print("\n<==== CATAT PENGELUARAN ====>")
                            nominal = int(input("Masukkan nominal pengeluaran (ketik '0' untuk batal) : Rp"))
                            if nominal == 0:
                                print("Batal mencatat pengeluaran.")
                                continue
                            keterangan = input("Masukkan keterangan pengeluaran : ")
                            if keterangan.strip() == "":
                                print("Keterangan tidak boleh kosong.")
                                continue
                            if 0 < nominal <= saldo[index]:
                                    saldo[index] -= nominal
                                    jenis_transaksi[index].append("Pengeluaran")
                                    nominal_transaksi[index].append(nominal)
                                    keterangan_transaksi[index].append(keterangan)
                                    print(f"Pengeluaran Rp{nominal} untuk {keterangan} berhasil dicatat. Saldo kas: Rp{saldo[index]}")
                            else:
                                print("Jumlah penarikan tidak valid atau melebihi saldo.")
                        except ValueError:
                            print("Input tidak valid, silakan masukkan angka.")
                    # Akhir tarik saldo

                    # Riwayat transaksi
                    elif menu == "4":
                        print("\n<==== RIWAYAT TRANSAKSI ====>")
                        if not jenis_transaksi[index]:
                            print("Belum ada transaksi.")
                        else:
                            print(f"{'No.':<5}{'Jenis':<15}{'Keterangan':<30}{'Nominal':<15}")
                            print("-" * 65)
                            for i in range(len(jenis_transaksi[index])):
                                print(f"{i+1:<5}{jenis_transaksi[index][i]:<15}{keterangan_transaksi[index][i]:<30}Rp{nominal_transaksi[index][i]:<15}")
                        print(f"\nSaldo saat ini: Rp{saldo[index]}")

                    # Akhir riwayat transaksi

                    # Edit riwayat
                    elif menu == "5":
                        print("\n<==== EDIT RIWAYAT TRANSAKSI ====>")
                        if not jenis_transaksi[index]:
                            print("Belum ada transaksi untuk di edit.")
                        else:
                            print(f"{'No.':<5}{'Jenis':<15}{'Keterangan':<30}{'Nominal':<15}")
                            print("-" * 65)
                            for i in range(len(jenis_transaksi[index])):
                                print(f"{i+1:<5}{jenis_transaksi[index][i]:<15}{keterangan_transaksi[index][i]:<30}Rp{nominal_transaksi[index][i]:<15}")
                            try:
                                edit_index = int(input("Masukkan nomor transaksi yang ingin di edit (ketik '0' untuk batal): ")) - 1
                                if edit_index == -1:
                                    print("batal edit transaksi.")
                                    continue
                                if 0 <= edit_index < len(jenis_transaksi[index]):
                                    keterangan_baru = input("Masukkan keterangan baru (biarkan kosong untuk tidak mengubah): ")
                                    nominal_baru = input("Masukkan nominal baru (biarkan kosong untuk tidak mengubah): Rp")
                                    if keterangan_baru.strip():
                                        keterangan_transaksi[index][edit_index] = keterangan_baru
                                    if nominal_baru.strip():
                                        nominal_baru = int(nominal_baru)
                                        if nominal_baru <= 0:
                                            print("Nominal harus lebih dari 0.")
                                            continue
                                        if jenis_transaksi[index][edit_index] == "Pemasukan":
                                            saldo[index] += (nominal_baru - nominal_transaksi[index][edit_index])
                                        else:  # Pengeluaran
                                            if nominal_baru > saldo[index] + nominal_transaksi[index][edit_index]:
                                                print("Nominal pengeluaran baru melebihi saldo yang tersedia.")
                                                continue
                                            saldo[index] -= (nominal_baru - nominal_transaksi[index][edit_index])
                                        nominal_transaksi[index][edit_index] = nominal_baru
                                    print("Transaksi berhasil di edit.")
                                else:
                                    print("Nomor transaksi tidak valid.")
                            except ValueError:
                                print("Input tidak valid, silakan masukkan angka.")
                    # Akhir edit riwayat

                    # Hapus transaksi
                    elif menu == "6":
                        print("\n<==== HAPUS TRANSAKSI ====>")
                        if not jenis_transaksi[index]:
                            print("Belum ada transaksi untuk di hapus.")
                        else:
                            print(f"{'No.':<5}{'Jenis':<15}{'Keterangan':<30}{'Nominal':<15}")
                            print("-" * 65)
                            for i in range(len(jenis_transaksi[index])):
                                print(f"{i+1:<5}{jenis_transaksi[index][i]:<15}{keterangan_transaksi[index][i]:<30}Rp{nominal_transaksi[index][i]:<15}")
                            try:
                                hapus_index = int(input("Masukkan nomor transaksi yang ingin di hapus (ketik '0' untuk batal): ")) - 1
                                if hapus_index == -1:
                                    print("Batal hapus transaksi.")
                                    continue
                                if 0 <= hapus_index < len(jenis_transaksi[index]):
                                    if jenis_transaksi[index][hapus_index] == "Pemasukan":
                                        saldo[index] -= nominal_transaksi[index][hapus_index]
                                    else:  # Pengeluaran
                                        saldo[index] += nominal_transaksi[index][hapus_index]
                                    del jenis_transaksi[index][hapus_index]
                                    del nominal_transaksi[index][hapus_index]
                                    del keterangan_transaksi[index][hapus_index]   
                                    print("Transaksi berhasil di hapus.")
                                else:
                                    print("Nomor transaksi tidak valid.")
                            except ValueError:
                                print("Input tidak valid, silakan masukkan angka.")
                    # Akhir hapus transaksi
                    # Ganti PIN
                    elif menu == "7":
                        print("\nUntuk memastikan bahwa ini benar anda, silahkan masukkan password!")
                        verif_pass = input("Masukkan password: ")
                        if verif_pass == password[index]:
                            while True:
                                print("\n<==== UBAH PIN ====>")
                                pin_lama = input("Masukkan PIN lama (Ketik 'batal' untuk kembali): ").lower()

                                if pin_lama == "batal":
                                    print("Batal ubah PIN")
                                    break

                                ubah_pin = input("Masukkan PIN baru: ")
                                verif_ubah_pin = input("Verifikasi PIN baru: ")


                                if pin_lama != pin[index]:
                                    print("PIN lama salah!")
                                    continue

                                if ubah_pin != verif_ubah_pin:
                                    print("Verifikasi PIN baru salah")
                                    continue
                                
                                if len(ubah_pin) != 4 or not ubah_pin.isdigit():
                                    print("PIN harus terdiri dari 4 digit angka, silakan coba lagi.")
                                    continue
                                
                                pin[index] = ubah_pin
                                print("PIN berhasil di ubah!")
                                break
                        else:
                            print("Password salah")
                    # Akhir ganti PIN

                    # Keluar
                    elif menu == "8":
                        print("Keluar dari akun.")
                        break
                    # Akhir keluar
                    else:
                        print("Pilihan tidak valid, silakan coba lagi.")
        else:
            print("Nama tidak ditemukan, silakan daftar terlebih dahulu.")
# Akhir masuk

    elif pilihan == "3":
        print("Terima kasih telah menggunakan KaWi Payment. Sampai jumpa!")
        break