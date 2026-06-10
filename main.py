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

jumlah_data = 25

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


def cek_kategori_transmisi_merek(merek_dicari):
    ada_matik = False
    ada_manual = False
    ada_kopling = False

    posisi = 0

    while posisi < jumlah_data:
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

    while posisi < jumlah_data:

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
def cetak_motor_merek_transmisi(merek_dicari, transmisi_dipilih):
    print("\n=== MOTOR MEREK: " + upper(merek_dicari) + " | TRANSMISI: " + upper(transmisi_dipilih) + " ===")
    print(f"{'No':<4} | {'Model Motor':<20} | {'Kapasitas':<10}")
    print("-" * 42)

    nomor_motor = 1
    posisi = 0

    while posisi < jumlah_data:
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

    while posisi < jumlah_data:
        if data_motor[posisi][2] == cc_dicari and lower(data_motor[posisi][3]) == lower(transmisi_dipilih):
            print(f"{nomor_motor:<4} | {data_motor[posisi][0]:<15} | {data_motor[posisi][1]:<20}")
            nomor_motor += 1

        posisi += 1

    if nomor_motor == 1:
        print("Data tidak ditemukan untuk tipe transmisi ini.")

    input("\nTekan Enter untuk kembali...")


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
def menu_filter_merek():

    daftar_merek = [None] * jumlah_data
    banyak_merek = 0
    posisi = 0

    while posisi < jumlah_data:
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

def menu_filter_cc():

    daftar_cc = [None] * jumlah_data
    banyak_cc = 0
    posisi = 0
    while posisi < jumlah_data:
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
def menu_utama():
    aplikasi_selesai = False

    while aplikasi_selesai == False:
        print("\n======================================")
        print("    APLIKASI MANAJEMEN RENTAL MOTOR")
        print("======================================")
        print("1. Filter Berdasarkan Daftar Merek")
        print("2. Filter Berdasarkan Daftar CC")
        print("3. Keluar Aplikasi")
        print("======================================")

        menu_pilihan = input("Pilih menu utama (1-3): ")
        if menu_pilihan == "1":
            menu_filter_merek()
        elif menu_pilihan == "2":
            menu_filter_cc()
        elif menu_pilihan == "3":
            print("\nTerima kasih! Sampai jumpa kembali. 😉")
            aplikasi_selesai = True
        else:
            print("\nPilihan tidak valid! Masukkan angka yang benar.")

if __name__ == "__main__":
    menu_utama()