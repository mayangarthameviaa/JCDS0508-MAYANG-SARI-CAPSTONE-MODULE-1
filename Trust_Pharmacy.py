from tabulate import tabulate
from datetime import date

data_obat = [
    {"no": 1, "kode_obat": "OB-01", "nama": "Paracetamol", "harga": 7000, "jumlah": 100, "tgl_kadaluwarsa": date(2026, 8, 31)},
    {"no": 2, "kode_obat": "OB-02", "nama": "Lansoprazole", "harga": 15000, "jumlah": 55, "tgl_kadaluwarsa": date(2026, 12, 25)},
    {"no": 3, "kode_obat": "OB-03", "nama": "Naxprofen", "harga": 5000, "jumlah": 90, "tgl_kadaluwarsa": date(2025, 12, 30)},
    {"no": 4, "kode_obat": "OB-04", "nama": "Amoxicillin", "harga": 12500, "jumlah": 30, "tgl_kadaluwarsa": date(2025, 10, 30)},
    {"no": 5, "kode_obat": "OB-05", "nama": "Cetirizine", "harga": 8000, "jumlah": 65, "tgl_kadaluwarsa": date(2026, 7, 18)},
    {"no": 6, "kode_obat": "OB-06", "nama": "Vitamin C", "harga": 5000, "jumlah": 80, "tgl_kadaluwarsa": date(2025, 12, 30)}
]

keranjang_belanja = []

def tampilan_tabel(data):
    for index, item in enumerate(data, start=1):
        item["no"] = index
    tabel_data = [[item["no"], item["kode_obat"], item["nama"], item["harga"], item["jumlah"], item["tgl_kadaluwarsa"]] for item in data]   
    print(tabulate(tabel_data, headers=data[0].keys(), tablefmt='fancy_grid', numalign="center", stralign="center",))

def autentikasi():
    print(""" 
+-------------------------- + + + --------------------------+
|                   Welcome to Trust Pharmacy               |
|                      Your Wellnes Partner                 |
+-------------------------- + + + --------------------------+
""")          
    while True:
        choose = input("Silahkan pilih peran Anda (admin atau user): ").lower().strip()
        if choose == "admin":
            username = input("Masukkan username Admin: ")
            password = input("Masukkan password Admin: ")
            if username == "Admin1" and password == "Pass1":
                return "admin"
            else:
                print("Username atau password salah, silahkan coba lagi.")

        elif choose == "user":
            username = input("Masukkan username User: ")
            password = input("Masukkan password User: ")
            if username == "User1" and password == "Pass1":
                return "user"
            else:
                print("Username atau password salah, silahkan coba lagi")

        else:
            print("Pilihan tidak valid. Silahkan masukkan 'admin' atau 'user'. ")

def validasi_kodeobat():
    while True:
        kode_input = input("Masukkan Kode Obat (format: OB-XX): ").strip()
        if not kode_input:
            print("Input tidak boleh kosong.")
            continue
        if not kode_input.startswith("OB-") or len(kode_input) != 5:
            print("Kode obat tidak valid. Format(OB-XX): ")
            continue
        return kode_input

def validasi_nama():
    while True:
        nama_input = input("Masukkan nama obat: ").lower().strip()
        if not nama_input:
            print("Input tidak boleh kosong.")
            continue
        return nama_input
    
def validasi_nama_beli():
    while True:
        nama_input = input("Masukkan nama obat yang ingin Anda beli: ").strip()
        if not nama_input:
            print("Input tidak boleh kosong.")
            continue
        return nama_input

def validasi_harga():
    while True: 
        harga_input = input("Masukkan Harga Obat: ").strip()
        if not harga_input:
            print("Input tidak boleh kosong.")
            continue
        try:
            harga_input = int(harga_input)
            if harga_input <= 0:
                print("Harga tidak boleh 0 atau negatif!")
            else:
                return harga_input
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat tanpa koma")

def validasi_jumlah():
    while True:
            jumlah_input = input("Masukkan Jumlah Obat: ").strip()
            if not jumlah_input:
                print("Input tidak boleh kosong")
                continue
            try:
                jumlah_input = int(jumlah_input)
                if jumlah_input <0 :
                    print("Jumlah tidak boleh negatif!")
                else:
                    return jumlah_input
            except ValueError:
                print("Input tidak valid. Harap masukkan angka bilg bulat tanpa koma")
        
def validasi_tanggal():
    while True:
        tgl_kadaluwarsa_input = input("Masukkan Tanggal Kadaluwarsa (YYYY-MM-DD): ").strip()
        if not tgl_kadaluwarsa_input:
            print("Input tidak boleh kosong.")
            continue
        try:
            return date.fromisoformat(tgl_kadaluwarsa_input) #-> konversi string to date
        except ValueError:
            print("Tanggal kadaluwarsa tidak sesuai format (YYYY-MM-DD)")

def tampilkan_keranjang():
    isi_keranjang = []
    for item in keranjang_belanja:
        total_harga = item["jumlah"] * item["harga"]
        isi_keranjang.append([item["nama"], item["jumlah"], item["harga"], total_harga])
    print(tabulate(isi_keranjang, headers=["Nama Obat", "Qty", "Harga", "Total Harga"], tablefmt='fancy_grid', numalign="center", stralign="center"))

def proses_belanja():
    total_belanja = 0
    for item in keranjang_belanja:
        total_belanja += item["jumlah"] * item["harga"]
    print(f"Total belanja Anda Rp. {total_belanja}")

    while True:
        jumlah_uang = int(input("Masukkan jumlah uang Anda: "))
        if jumlah_uang < total_belanja:
            kekurangan = total_belanja - jumlah_uang
            print(f"Uang Anda kurang sebesar Rp.{kekurangan}.")
        elif jumlah_uang > total_belanja:
            kembalian = jumlah_uang - total_belanja
            print(f"Terima kasih telah berbelanja, kembalian uang Anda Rp. {kembalian}")
            break
        else:
            print("Terima kasih telah berbelanja")
            break

def kurangi_stok():
    for item in keranjang_belanja:
        for obat in data_obat:
            if item["nama"] == obat["nama"]:
                obat["jumlah"] -= item["jumlah"]
    keranjang_belanja.clear()

def confirm_menuutama():
    while True:
        confirm = input("Apakah Anda yakin ingin kembali ke menu utama? (ya/tidak): ").lower()
        if confirm == "ya":
            return True
        elif confirm == "tidak":
            return False
        else:
            print("Input tidak valid. Silahkan masukkan 'ya' atau 'tidak' ")

# ------------------------------------ MENU 1 ------------------------------------
def tampilkan_obat():
    while True:
        print("\n-------------------  ✦ Submenu Tampilkan Obat ✦ -----------------")
        print("1. Tampilkan seluruh obat                                           ")
        print("2. Tampilkan berdasarkan kode obat                                  ")
        print("3. Tampilkan berdasarkan nama obat                                  ")
        print("4. Kembali ke menu utama                                            ")
        print("-----------------------------------------------------------------")

        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-4): ")
        if pilihan == "1":
            if data_obat:
                tampilan_tabel(data_obat)
            else:
                print("Data tidak ada.")
        
        elif pilihan in ["2", "3"]:
            if not data_obat:
                print("Data tidak ada")
                continue #-> balik ke while true

            if pilihan == "2":
                data_kode = [obat['kode_obat'] for obat in data_obat]
                kode_obat_input = validasi_kodeobat()
                found = False #-> penanda apakah obat telah ditemukan
                for obat in data_obat:
                    if obat['kode_obat'] == kode_obat_input:
                        tampilan_tabel([obat])
                        found = True
                        break
                if not found:
                    print("Kode obat tidak ditemukan. Kode yang tersedia : ", data_kode)
 
            elif pilihan == "3":
                nama_input = validasi_nama()
                found = False
                for nama in data_obat:
                    if nama['nama'].lower() == nama_input:
                        tampilan_tabel([nama])
                        found = True
                        break
                if not found:
                    print("Obat tidak ditemukan. Berikut data yang tersedia pada tabel:")
                    tampilan_tabel(data_obat)

        elif pilihan == "4":
            if confirm_menuutama():
                break
        else:
            print("Pilihan tidak valid.")

# ------------------------------------ MENU 2 ------------------------------------
def tambah_obat():
    while True:
        print("\n-------------------  ✦ Submenu Tambah Obat ✦ -------------------")
        print("1. Tambah obat berdasarkan kode obat")
        print("2. kembali ke menu utama")
        print("-------------------------------------------------------------------")
        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-2): ")
        if pilihan == "1": 
                kode_obat_input = validasi_kodeobat()
                data_kode = [obat['kode_obat'] for obat in data_obat]
                for obat in data_obat: #--> cek jika obat sudah ada  
                    if obat["kode_obat"] == kode_obat_input:
                        print("Data sudah ada, data kode obat saat ini yaitu: ", data_kode)
                        break #--> keluar dari loop jika obat sudah ada
                else: #--> jika tidak ada index yg duplikat, lanjutkan input
                    nama_obat_input = validasi_nama()
                    for nama in data_obat:
                        if nama["nama"].lower() == nama_obat_input.lower():
                            print("Nama obat sudah ada. Masukkan nama lain")
                            break
                    else:
                        nama = nama_obat_input
                        harga = validasi_harga()
                        jumlah = validasi_jumlah()
                        tgl_kadaluwarsa = validasi_tanggal()

                        obat_baru={
                            "no" : len(data_obat)+1,
                            "kode_obat": kode_obat_input,
                            "nama": nama,
                            "harga": harga,
                            "jumlah": jumlah,
                            "tgl_kadaluwarsa": tgl_kadaluwarsa
                        }
                        print("\n Data yang akan disimpan")
                        tampilan_tabel([obat_baru])

                        confirm = input("Apakah Anda ingin menyimpan data ini (ya/tidak): ").lower()
                        if confirm == "ya":
                            data_obat.append(obat_baru)
                            tampilan_tabel(data_obat)
                            print("Data berhasil disimpan.")
                        else:
                            print("Data tidak disimpan.")
                
        elif pilihan == "2":
            if confirm_menuutama():
                break
        else:
            print("Pilihan tidak valid.")

# ------------------------------------ MENU 3 ------------------------------------
def ubah_obat():
    while True:
        print("\n-------------------  ✦ Submenu Ubah Obat ✦ -------------------")
        print("1. Ubah obat berdasarkan kode obat")
        print("2. kembali ke menu utama")
        print("-----------------------------------------------------------------")
        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-2): ")
        if pilihan == "1": 
                kode_obat_input = validasi_kodeobat()
                for obat in data_obat:
                    if obat['kode_obat'] == kode_obat_input:
                        tampilan_tabel([obat])
                        confirm = input("Apakah Anda yakin ingin mengubah data ini? (ya/tidak): ").lower()
                        if confirm == "ya":
                            kolom = input("Masukkan nama kolom yang ingin diubah: ").lower()
                            if kolom == "kode_obat":
                                print("Kode obat tidak dapat diubah")
                                break
                            if kolom == "no":
                                print("No tidak bisa diubah")
                                break
                            if kolom in obat:
                                if kolom == "jumlah":
                                    obat[kolom] = validasi_jumlah()
                                    tampilan_tabel(data_obat)
                                    print("Data berhasil diupdate.")
                                elif kolom == "harga":
                                    obat[kolom] = validasi_harga()
                                    tampilan_tabel(data_obat)
                                    print("Data berhasil diupdate.")
                                elif kolom == "tgl_kadaluwarsa":
                                    obat[kolom] = validasi_tanggal()
                                    tampilan_tabel(data_obat)
                                    print("Data berhasil diupdate.")
                                elif kolom == "nama":
                                    nama = obat["nama"]
                                    new_value = input(f"Masukkan nilai baru untuk {nama}: ").strip()
                                    for item in data_obat:
                                        if item["nama"].lower() == new_value.lower():
                                            print("Nama obat sudah ada. Silahkan masukkan nama lain")
                                            tampilan_tabel(data_obat)
                                            break
                                        else: 
                                            obat[kolom] = new_value
                                            tampilan_tabel(data_obat)
                                            print("Data berhasil diupdate.")
                                            break
                            else:
                                print("Kolom tidak ditemukan.")
                        else:
                            print("Data tidak diubah")
                        break
                else:
                    print("Data tidak ada.")
                    
        elif pilihan == "2":
            if confirm_menuutama():
                break
        else:
            print("Pilihan tidak valid.")

# ------------------------------------ MENU 4 ------------------------------------
def hapus_obat():
    while True:
        print("\n-------------------  ✦ Submenu Hapus Obat ✦ -------------------")
        print("1. Hapus obat berdasarkan kode obat")
        print("2. kembali ke menu utama")
        print("------------------------------------------------------------------")
        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-2): ")
        if pilihan == "1": 
                kode_obat_input = validasi_kodeobat()
                for obat in data_obat:
                    if obat['kode_obat'] == kode_obat_input:
                        tampilan_tabel([obat])
                        confirm = input("Apakah Anda yakin ingin menghapus obat ini? (ya/tidak): ").lower()
                        if confirm == 'ya':
                            data_obat.remove(obat)
                            tampilan_tabel(data_obat)
                            print("Data berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
                        break
                else:
                    print("data tidak ada.")
        elif pilihan == "2":
            if confirm_menuutama():
                break
        else: 
            print("Pilihan tidak valid")

# ------------------------------------ MENU 5 ------------------------------------
def beli_obat():
        if data_obat:
            while True:
                tampilan_tabel(data_obat)
                nama_obat_input = validasi_nama_beli()
                for obat in data_obat:
                    if obat['nama'].lower() == nama_obat_input.lower():
                        jumlah = validasi_jumlah()
                        if jumlah > obat["jumlah"]:
                            print(f"stok {nama_obat_input} tidak cukup. Stok tersedia {obat["jumlah"]}.")
                        else:
                            # keranjang_belanja.append([obat['nama'], jumlah, obat['harga']])
                            # print(f"{jumlah} {nama_obat_input} ditambahkan ke keranjang")
                            # tampilkan_keranjang()
                            keranjang_belanja.append({
                                "nama" : obat["nama"],
                                "jumlah" : jumlah,
                                "harga" : obat["harga"]
                            })
                            print(f"{jumlah} {nama_obat_input} ditambahkan ke keranjang")
                            tampilkan_keranjang()
                             
                        lanjut = input("Apakah Anda ingin membeli obat lagi? (ya/tidak): ").lower()
                        if lanjut == "tidak".lower():
                            proses_belanja()
                            kurangi_stok()
                            return #--> keluar dari fungsi jika tidak ingin membeli lagi (kembali ke menu utama)
                        elif lanjut == "ya".lower():
                            break #--> keluar dari loop ini & kembali ke while True
                else:
                    print("Nama obat tidak ditemukan")
                    return
        else: 
            print("Tidak ada obat yang tersedia untuk dibeli")

#------------------------------------ MENU 6 ------------------------------------
def keluar():
    confirm = input("Apakah Anda yakin ingin keluar dari program? (ya/tidak): ").lower()
    if confirm == "ya":
        print("Terima kasih, sampai jumpa kembali.")
        return True
    else: 
        return False 

# ------------------------ MENU UTAMA ADMIN------------------------
def menu_admin():
    while True:
        print("----------------------- ⁠⚕️  ✚ ⁠⚕️ -----------------------")
        print("                     'Trust Pharmacy'                    ")
        print("                      Admin Session                      ")
        print("----------------------- ⁠⚕️  ✚ ⚕️ -----------------------")
        print(" 1. Tampilkan Obat")
        print(" 2. Tambah Obat")
        print(" 3. Ubah Obat")
        print(" 4. Hapus Obat")
        print(" 5. Exit")
        print("-----------------------------------------------------")

        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-5): ")

        if pilihan == "1":
            tampilkan_obat()
        elif pilihan == "2":
            tambah_obat()
        elif pilihan == "3":
            ubah_obat()
        elif pilihan == "4":
            hapus_obat()
        elif pilihan == "5":
            if keluar():
                break
        else:
            print("Pilihan Anda tidak valid, silahkan coba lagi (1-6).")

# ------------------------ MENU UTAMA USER------------------------
def menu_user():
    while True:
        print("----------------------- ⁠⚕️  ✚ ⚕️  ⁠------------------------")
        print("                      Trust Pharmacy                       ")
        print("----------------------- ⁠⚕️  ✚ ⚕️  ⁠------------------------")
        print(" 1. Tampilkan Obat")
        print(" 2. Beli Obat")
        print(" 3. Exit")
        print("---------------------------------------------------------")

        pilihan = input("Silahkan pilih menu yang Anda inginkan (1-3): ")

        if pilihan == "1":
            tampilkan_obat()
        elif pilihan == "2":
            beli_obat()
        elif pilihan == "3":
            if keluar():
                break
        else:
            print("Pilihan Anda tidak valid, silahkan coba lagi (1-6).")

def main_menu():
    pengguna = autentikasi()
    if pengguna == "admin":
        menu_admin()
    else:
        menu_user()
        
main_menu()
