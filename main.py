data_motor = [
    ["Honda", "Beat", 110, "Matik"],
    ["Honda", "Vario 150", 150, "Matik"],
    ["Honda", "Vario 160", 160, "Matik"],
    ["Honda", "PCX 160", 160, "Matik"],
    ["Yamaha", "Fazzio", 125, "Matik"],
    ["Yamaha", "Fino 125", 125, "Matik"],
    ["Yamaha", "Aerox 155", 155, "Matik"],
    ["Yamaha", "Nmax 155", 155, "Matik"],
    ["Yamaha", "Xmax", 250, "Matik"],
    ["Honda", "Forza", 250, "Matik"],
    ["Honda", "Supra X 125", 125, "Manual"],
    ["Honda", "Revo", 110, "Manual"],
    ["Honda", "Blade", 125, "Manual"],
    ["Yamaha", "Jupiter Z1", 115, "Manual"],
    ["Yamaha", "Vega", 115, "Manual"],
    ["Honda", "CBR150R", 150, "Kopling"],
    ["Honda", "CBR250RR", 250, "Kopling"],
    ["Suzuki", "GSX R150", 150, "Kopling"],
    ["Yamaha", "R15", 155, "Kopling"],
    ["Yamaha", "R6", 600, "Kopling"],
    ["Kawasaki", "ZX25R", 250, "Kopling"],
    ["Kawasaki", "Z800", 800, "Kopling"],
    ["Ducati", "Panigale V4R", 1000, "Kopling"],
    ["Harley-Davidson", "Sportster S", 1250, "Kopling"],
    ["BMW", "F 900 XR", 900, "Kopling"]
]

BANYAK_DATA = 25

# Menyimpan log transaksi harian dengan format: [Nama Penyewa, Merek Motor, Model Motor, Durasi Hari, Total Biaya]
data_sewa_hari_ini = [None] * 100 
banyak_transaksi = 0

# # Kamus Data FUNGSI: upper & lower
# - huruf_kecil / huruf_besar (String): Kamus karakter untuk konversi teks manual.
# - panjang_teks (Integer): Menyimpan hasil hitung jumlah karakter secara manual.
# - hasil / pembanding (String): Wadah penampung string proses konversi teks.
# - i / j (Integer): Indeks perulangan untuk mengecek karakter per karakter.
# - berubah / selesai (Boolean): Pengendali status perulangan konversi string.
def upper(teks):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""
    panjang_teks = 0
    selesai = False

    while selesai == False:
        pembanding = ""
        i = 0
        while i < panjang_teks:
            pembanding += teks[i]
            i += 1

        if pembanding == teks:
            selesai = True
        else:
            panjang_teks += 1

    i = 0
    while i < panjang_teks:
        karakter = teks[i]
        berubah = False
        j = 0

        while j < 26:
            if huruf_kecil[j] == karakter:
                hasil += huruf_besar[j] 
                berubah = True
            j += 1

        if berubah == False:
            hasil += karakter 

        i += 1

    return hasil

def lower(teks):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""
    panjang_teks = 0
    selesai = False

    while selesai == False:
        pembanding = ""
        i = 0
        while i < panjang_teks:
            pembanding += teks[i]
            i += 1

        if pembanding == teks:
            selesai = True
        else:
            panjang_teks += 1

    i = 0
    while i < panjang_teks:
        karakter = teks[i]
        berubah = False
        j = 0

        while j < 26:
            if huruf_besar[j] == karakter:
                hasil += huruf_kecil[j] 
                berubah = True
            j += 1

        if berubah == False:
            hasil += karakter 

        i += 1

    return hasil

# # Kamus Data FUNGSI: cek_kategori_transmisi_merek & cek_kategori_transmisi_cc
# - ada_matik / ada_manual / ada_kopling (Boolean): Flag penanda tipe transmisi yang ditemukan.
# - posisi (Integer): Indeks kursor untuk menelusuri baris dataset motor.
# - transmisi_sekarang (String): Menyimpan jenis transmisi dari baris data aktif.
def cek_kategori_transmisi_merek(merek_dicari):
    ada_matik = False
    ada_manual = False
    ada_kopling = False
    posisi = 0

    while posisi < BANYAK_DATA:
        if lower(data_motor[posisi][0]) == lower(merek_dicari):
            transmisi_sekarang = lower(data_motor[posisi][3])

            if transmisi_sekarang == "matik":
                ada_matik = True
            elif transmisi_sekarang == "manual":
                ada_manual = True
            elif transmisi_sekarang == "kopling":
                ada_kopling = True
        posisi += 1

    if ada_matik and not ada_manual and not ada_kopling:
        return "Matik"
    elif ada_manual and not ada_matik and not ada_kopling:
        return "Manual"
    elif ada_kopling and not ada_matik and not ada_manual:
        return "Kopling"
    else:
        return "Matik, Manual, Kopling"

def cek_kategori_transmisi_cc(cc_dicari):
    ada_matik = False
    ada_manual = False
    ada_kopling = False
    posisi = 0

    while posisi < BANYAK_DATA:
        if data_motor[posisi][2] == cc_dicari:
            transmisi_sekarang = lower(data_motor[posisi][3])

            if transmisi_sekarang == "matik":
                ada_matik = True
            elif transmisi_sekarang == "manual":
                ada_manual = True
            elif transmisi_sekarang == "kopling":
                ada_kopling = True
        posisi += 1

    if ada_matik and not ada_manual and not ada_kopling:
        return "Matik"
    elif ada_manual and not ada_matik and not ada_kopling:
        return "Manual"
    elif ada_kopling and not ada_matik and not ada_manual:
        return "Kopling"
    else:
        return "Matik, Manual, Kopling"

# # Kamus Data FUNGSI: cetak_motor_merek_transmisi & cetak_motor_cc_transmisi
# - nomor_motor (Integer): Urutan angka numbering (1, 2, 3...) untuk tabel display.
# - posisi (Integer): Indeks kursor untuk membaca baris elemen dataset motor.
def cetak_motor_merek_transmisi(merek_dicari, transmisi_dipilih):
    print("\n=== MOTOR MEREK: " + upper(merek_dicari) + " | TRANSMISI: " + upper(transmisi_dipilih) + " ===")
    print(f"{'No':<4} | {'Model Motor':<20} | {'Kapasitas':<10}")
    print("-" * 42)

    nomor_motor = 1
    posisi = 0

    while posisi < BANYAK_DATA:
        if lower(data_motor[posisi][0]) == lower(merek_dicari) and lower(data_motor[posisi][3]) == lower(transmisi_dipilih):
            print(f"{nomor_motor:<4} | {data_motor[posisi][1]:<20} | {data_motor[posisi][2]} cc")
            nomor_motor += 1
        posisi += 1

    if nomor_motor == 1:
        print("Data tidak ditemukan untuk tipe transmisi ini.")

    input("\nTekan Enter untuk kembali...")

def cetak_motor_cc_transmisi(cc_dicari, transmisi_dipilih):
    print("\n=== MOTOR KAPASITAS: " + str(cc_dicari) + " CC | TRANSMISI: " + upper(transmisi_dipilih) + " ===")
    print(f"{'No':<4} | {'Merek':<15} | {'Model Motor':<20}")
    print("-" * 45)

    nomor_motor = 1
    posisi = 0

    while posisi < BANYAK_DATA:
        if data_motor[posisi][2] == cc_dicari and lower(data_motor[posisi][3]) == lower(transmisi_dipilih):
            print(f"{nomor_motor:<4} | {data_motor[posisi][0]:<15} | {data_motor[posisi][1]:<20}")
            nomor_motor += 1
        posisi += 1

    if nomor_motor == 1:
        print("Data tidak ditemukan untuk tipe transmisi ini.")

    input("\nTekan Enter untuk kembali...")

# # Kamus Data FUNGSI: menu_opsi_transmisi_merek & menu_opsi_transmisi_cc
# - status_kategori (String): Output teks status ketersediaan tipe transmisi.
# - kembali_menu (Boolean): Pengendali loop untuk kembali ke menu filter atas.
# - menu_pilihan (String): Menampung nomor sub-menu transmisi (1-4) dari pengguna.
def menu_opsi_transmisi_merek(merek_dicari):
    status_kategori = cek_kategori_transmisi_merek(merek_dicari)
    kembali_menu = False

    while kembali_menu == False:
        print("\n======================================")
        print(" PILIH TRANSMISI MEREK " + upper(merek_dicari))
        print(" Status Kategori: " + status_kategori)
        print("======================================")
        print("1. Lihat Motor Matik")
        print("2. Lihat Motor Manual")
        print("3. Lihat Motor Kopling")
        print("4. Kembali")
        print("======================================")

        menu_pilihan = input("Pilih menu (1-4): ")

        if menu_pilihan == "1":
            cetak_motor_merek_transmisi(merek_dicari, "Matik")
        elif menu_pilihan == "2":
            cetak_motor_merek_transmisi(merek_dicari, "Manual")
        elif menu_pilihan == "3":
            cetak_motor_merek_transmisi(merek_dicari, "Kopling")
        elif menu_pilihan == "4":
            kembali_menu = True 
        else:
            print("\nPilihan tidak valid!")

def menu_opsi_transmisi_cc(cc_dicari):
    status_kategori = cek_kategori_transmisi_cc(cc_dicari)
    kembali_menu = False

    while kembali_menu == False:
        print("\n======================================")
        print(" PILIH TRANSMISI CC " + str(cc_dicari))
        print(" Status Kategori: " + status_kategori)
        print("======================================")
        print("1. Lihat Motor Matik")
        print("2. Lihat Motor Manual")
        print("3. Lihat Motor Kopling")
        print("4. Kembali")
        print("======================================")

        menu_pilihan = input("Pilih menu (1-4): ")

        if menu_pilihan == "1":
            cetak_motor_cc_transmisi(cc_dicari, "Matik")
        elif menu_pilihan == "2":
            cetak_motor_cc_transmisi(cc_dicari, "Manual")
        elif menu_pilihan == "3":
            cetak_motor_cc_transmisi(cc_dicari, "Kopling")
        elif menu_pilihan == "4":
            kembali_menu = True 
        else:
            print("\nPilihan tidak valid!")

# ==============================================================================
# # Kamus Data FUNGSI: menu_filter_merek
# - daftar_merek (List): Array sementara penampung nama merek hasil proses distingsi.
# - banyak_merek (Integer): Counter jumlah merek unik yang berhasil didata.
# - posisi / cek / nomor (Integer): Indeks iterator kendali looping pencarian data merek.
# - merek_sekarang (String): Nilai merek baris data aktif yang sedang diproses.
# - sudah_ada / kembali_menu (Boolean): Pengendali alur seleksi duplikat dan menu.
# - menu_pilihan (Integer): Angka pilihan index merek yang dipilih user.
# ==============================================================================
def menu_filter_merek():
    daftar_merek = [None] * BANYAK_DATA 
    banyak_merek = 0
    posisi = 0

    while posisi < BANYAK_DATA:
        merek_sekarang = data_motor[posisi][0]
        sudah_ada = False
        cek = 0
        while cek < banyak_merek:
            if lower(daftar_merek[cek]) == lower(merek_sekarang):
                sudah_ada = True 
            cek += 1
            
        if sudah_ada == False:
            daftar_merek[banyak_merek] = merek_sekarang 
            banyak_merek += 1
        posisi += 1

    kembali_menu = False
    while kembali_menu == False:
        print("\n======================================")
        print("       FILTER BERDASARKAN MEREK")
        print("======================================")

        nomor = 0
        while nomor < banyak_merek:
            print(str(nomor + 1) + ". " + daftar_merek[nomor])
            nomor += 1
        print(str(banyak_merek + 1) + ". Kembali ke Menu Utama")
        print("======================================")
        
        menu_pilihan = int(input("Pilih nomor merek (1-" + str(banyak_merek + 1) + "): "))
        
        if menu_pilihan > 0 and menu_pilihan <= banyak_merek:
            menu_opsi_transmisi_merek(daftar_merek[menu_pilihan - 1])
        elif menu_pilihan == banyak_merek + 1:
            kembali_menu = True
        else:
            print("\nPilihan tidak valid!")

# # Kamus Data FUNGSI: menu_filter_cc
# - daftar_cc (List): Array penampung list variasi CC motor tanpa duplikasi.
# - banyak_cc (Integer): Total kapasitas CC unik yang tersimpan.
# - posisi / cek / nomor (Integer): Pointer index kontrol looping sorting & display.
# - cc_sekarang (Integer): Kapasitas mesin motor baris aktif yang diproses.
# - sementara (Integer): Kontainer data temporer penukaran nilai (Bubble Sort).
# - sudah_ada / kembali_menu (Boolean): Pengendali status pengecekan data & loop menu.
# - menu_pilihan (Integer): Nomor kapasitas CC yang ditunjuk oleh user.
def menu_filter_cc():
    daftar_cc = [None] * BANYAK_DATA 
    banyak_cc = 0
    posisi = 0

    while posisi < BANYAK_DATA:
        cc_sekarang = data_motor[posisi][2]
        sudah_ada = False
        cek = 0
        while cek < banyak_cc:
            if daftar_cc[cek] == cc_sekarang:
                sudah_ada = True
            cek += 1
        if sudah_ada == False:
            daftar_cc[banyak_cc] = cc_sekarang
            banyak_cc += 1
        posisi += 1

    posisi = 0
    while posisi < banyak_cc:
        cek = 0
        while cek < banyak_cc - posisi - 1:
            if daftar_cc[cek] > daftar_cc[cek + 1]:
                sementara = daftar_cc[cek]
                daftar_cc[cek] = daftar_cc[cek + 1]
                daftar_cc[cek + 1] = sementara
            cek += 1
        posisi += 1

    kembali_menu = False
    while kembali_menu == False:
        print("\n======================================")
        print("        FILTER BERDASARKAN CC")
        print("======================================")
        
        nomor = 0
        while nomor < banyak_cc:
            print(str(nomor + 1) + ". Kapasitas " + str(daftar_cc[nomor]) + " cc")
            nomor += 1
        print(str(banyak_cc + 1) + ". Kembali ke Menu Utama")
        print("======================================")
        
        menu_pilihan = int(input("Pilih nomor kapasitas CC (1-" + str(banyak_cc + 1) + "): "))
        
        if menu_pilihan > 0 and menu_pilihan <= banyak_cc:
            menu_opsi_transmisi_cc(daftar_cc[menu_pilihan - 1])
        elif menu_pilihan == banyak_cc + 1:
            kembali_menu = True
        else:
            print("\nPilihan tidak valid!")

# # Kamus Data FUNGSI: cari_motor
# - keyword (String): Teks/nama model motor masukan user yang ingin dicari.
# - ditemukan (Boolean): Indikator status hasil pencarian ada atau nihil.
# - nomor (Integer): Serial item baris data hasil temuan untuk visualisasi.
# - i (Integer): Iteration index penunjuk baris database motor global.
def cari_motor():
    keyword = input("\nMasukkan nama/model motor yang dicari: ")
    ditemukan = False

    print("\n=== HASIL PENCARIAN ===")
    print(f"{'No':<4} | {'Merek':<15} | {'Model':<20} | {'CC':<8} | {'Transmisi':<10}")
    print("-" * 70)

    nomor = 1
    i = 0

    while i < BANYAK_DATA:
        if lower(keyword) in lower(data_motor[i][1]):
            print(f"{nomor:<4} | {data_motor[i][0]:<15} | {data_motor[i][1]:<20} | {data_motor[i][2]:<8} | {data_motor[i][3]:<10}")
            ditemukan = True
            nomor += 1
        i += 1

    if ditemukan == False:
        print("Motor tidak ditemukan.")

    input("\nTekan Enter untuk kembali...")

# # Kamus Data FUNGSI: kalkulator_sewa
# - nama_penyewa (String): Input nama identitas pelanggan yang ingin menyewa.
# - nama_motor (String): Input nama model motor spesifik yang hendak disewa.
# - ditemukan (Boolean): Penanda konfirmasi ketepatan nama motor di database.
# - harga (Integer): Besaran rate nominal rental per hari berlandaskan CC dan jenis transmisi.
# - i (Integer): Penunjuk urutan indeks pencarian data dalam loop.
# - indeks_tampil (Integer): Indeks untuk mencetak daftar motor ke layar sebelum input.
# - cc (Integer): Kapasitas mesin silinder dari motor aktif yang ditemukan di database.
# - transmisi_aktif (String): Menyimpan jenis transmisi dari motor aktif yang ditemukan.
# - hari (Integer): Jumlah kuantitas hari peminjaman motor oleh customer.
# - total (Integer): Akumulasi kalkulasi finansial (harga x hari).
# - lanjut_input (Boolean): Pengendali loop untuk menambah banyak penyewa berturut-turut.
# - konfirmasi (String): Menyimpan input keputusan user untuk lanjut sewa atau berhenti (Y/T).
# - banyak_transaksi (Global Integer): Indeks konter jumlah manifes log sewa harian.
def kalkulator_sewa():
    global banyak_transaksi
    lanjut_input = True

    while lanjut_input == True:
        # MENAMPILKAN DAFTAR MOTOR SEBELUM INPUT
        print("\n============================================================")
        print("                 DAFTAR MOTOR YANG TERSEDIA                 ")
        print("============================================================")
        print(f"{'No':<4} | {'Merek':<12} | {'Model':<18} | {'CC':<5} | {'Transmisi':<10}")
        print("-" * 60)
        indeks_tampil = 0
        while indeks_tampil < BANYAK_DATA:
            print(f"{indeks_tampil + 1:<4} | {data_motor[indeks_tampil][0]:<12} | {data_motor[indeks_tampil][1]:<18} | {data_motor[indeks_tampil][2]:<5} | {data_motor[indeks_tampil][3]:<10}")
            indeks_tampil += 1
        print("============================================================")

        nama_penyewa = input("\nMasukkan Nama Penyewa: ")
        nama_motor = input("Masukkan motor yang ingin disewa (Ketik Modelnya): ")
        ditemukan = False
        harga = 0
        i = 0

        while i < BANYAK_DATA:
            if lower(nama_motor) == lower(data_motor[i][1]):
                ditemukan = True
                cc = data_motor[i][2]
                transmisi_aktif = lower(data_motor[i][3])

                if transmisi_aktif == "matik":
                    if cc <= 125:
                        harga = 70000
                    elif cc <= 160:
                        harga = 100000
                    else:
                        harga = 250000  

                elif transmisi_aktif == "manual":
                    harga = 45000  

                elif transmisi_aktif == "kopling":
                    if cc <= 150:
                        harga = 120000
                    elif cc <= 250:
                        harga = 450000
                    elif cc <= 600:
                        harga = 2000000
                    elif cc <= 1000:
                        harga = 2000000
                    else:
                        harga = 1600000  

                print("\nMotor ditemukan!")
                print("Merek          :", data_motor[i][0])
                print("Model          :", data_motor[i][1])
                print("Harga per hari : Rp", harga)
                
                merek_terpilih = data_motor[i][0]
                model_terpilih = data_motor[i][1]
                i = BANYAK_DATA  
            else:
                i += 1

        if ditemukan == False:
            print("Motor tidak ditemukan.")
        else:
            hari = int(input("Berapa hari ingin menyewa? "))
            total = harga * hari

            print("\n=== ESTIMASI BIAYA ===")
            print("Nama Penyewa   :", nama_penyewa)
            print("Harga per hari : Rp", harga)
            print("Durasi         :", hari, "hari")
            print("Total biaya    : Rp", total)

            data_sewa_hari_ini[banyak_transaksi] = [nama_penyewa, merek_terpilih, model_terpilih, hari, total]
            banyak_transaksi += 1
            print("\n[SUKSES] Transaksi sewa berhasil dicatat!")

        konfirmasi = input("\nApakah ingin menambah data penyewa lagi? (y/t): ")
        if lower(konfirmasi) == "t":
            lanjut_input = False

# # Kamus Data FUNGSI: akhir_hari
# - total_pendapatan (Integer): Akumulasi dari seluruh omzet biaya sewa masuk hari ini.
# - i (Integer): Iterator indeks penelusur daftar manifes transaksi sewa harian.
# - sewa (List): Menyimpan sub-list data satu transaksi aktif saat dibongkar.
def akhir_hari():
    print("\n=========================================================================")
    print("                     LAPORAN REKAPITULASI AKHIR HARI                     ")
    print("=========================================================================")
    print(f"{'No':<4} | {'Nama Penyewa':<15} | {'Motor yang Disewa':<25} | {'Durasi':<7} | {'Total Biaya':<12}")
    print("-" * 73)

    total_pendapatan = 0
    i = 0

    while i < banyak_transaksi:
        sewa = data_sewa_hari_ini[i]
        # Menggabungkan Merek + Model untuk tampilan ringkas (Contoh: Honda Beat)
        motor_teks = sewa[1] + " " + sewa[2]
        
        print(f"{i + 1:<4} | {sewa[0]:<15} | {motor_teks:<25} | {sewa[3]:<2} hari | Rp{sewa[4]:<10}")
        total_pendapatan += sewa[4]
        i += 1

    if banyak_transaksi == 0:
        print(" Belum ada transaksi penyewaan yang tercatat untuk hari ini.")
        
    print("-" * 73)
    print(f" TOTAL PENYEWA AKTIF HARI INI : {banyak_transaksi} Orang")
    print(f" TOTAL OMZET PENDAPATAN HARI INI : Rp {total_pendapatan}")
    print("=========================================================================")
    
    input("\nTekan Enter untuk kembali...")

# # Kamus Data/VARIABEL GLOBAL UTAMA:
# 1. data_motor (List of Lists): Matriks dataset utama berisi [Merek, Model, CC, Transmisi].
# 2. BANYAK_DATA (Integer): Batas acuan total baris data untuk perulangan di seluruh program.
# 3. data_sewa_hari_ini (List of Lists): Kumpulan log riwayat sewa motor harian dari multi-user.
# 4. banyak_transaksi (Integer): Counter jumlah orang/transaksi sewa yang sukses tersimpan.
# 5. aplikasi_selesai (Boolean): Pengendali utama siklus hidup jalannya program utama.
# 6. menu_pilihan (String): Menyimpan angka input respons pemilihan menu (1-5) dari user.
def menu_utama():
    aplikasi_selesai = False

    while aplikasi_selesai == False:
        print("\n======================================")
        print("    APLIKASI MANAJEMEN RENTAL MOTOR")
        print("======================================")
        print("1. Filter Berdasarkan Daftar Merek")
        print("2. Filter Berdasarkan Daftar CC")
        print("3. Cari Motor")
        print("4. Input Sewa Motor Baru")
        print("5. Laporan Akhir Hari")
        print("6. Keluar Aplikasi")
        print("======================================")

        menu_pilihan = input("Pilih menu utama (1-6): ")
        
        if menu_pilihan == "1":
            menu_filter_merek()
        elif menu_pilihan == "2":
            menu_filter_cc()
        elif menu_pilihan == "3":
            cari_motor()
        elif menu_pilihan == "4":
            kalkulator_sewa()
        elif menu_pilihan == "5":
            akhir_hari()
        elif menu_pilihan == "6":
            print("\nTerima kasih! Sampai jumpa kembali. 😉")
            aplikasi_selesai = True 
        else:
            print("\nPilihan tidak valid! Masukkan angka yang benar.")

if __name__ == "__main__":
    menu_utama()