data_motor = [
    # Kategori Matik
    {"merek": "Honda", "nama": "Beat", "cc": 110, "transmisi": "Matik"},
    {"merek": "Honda", "nama": "Vario 150", "cc": 150, "transmisi": "Matik"},
    {"merek": "Honda", "nama": "Vario 160", "cc": 160, "transmisi": "Matik"},
    {"merek": "Honda", "nama": "PCX 160", "cc": 160, "transmisi": "Matik"},
    {"merek": "Yamaha", "nama": "Fazzio", "cc": 125, "transmisi": "Matik"},
    {"merek": "Yamaha", "nama": "Fino 125", "cc": 125, "transmisi": "Matik"},
    {"merek": "Yamaha", "nama": "Aerox 155", "cc": 155, "transmisi": "Matik"},
    {"merek": "Yamaha", "nama": "Nmax 155", "cc": 155, "transmisi": "Matik"},
    {"merek": "Yamaha", "nama": "Xmax", "cc": 250, "transmisi": "Matik"},
    {"merek": "Honda", "nama": "Forza", "cc": 250, "transmisi": "Matik"},

    # Kategori Manual
    {"merek": "Honda", "nama": "Supra X 125", "cc": 125, "transmisi": "Manual"},
    {"merek": "Honda", "nama": "Revo", "cc": 110, "transmisi": "Manual"},
    {"merek": "Honda", "nama": "Blade", "cc": 125, "transmisi": "Manual"},
    {"merek": "Yamaha", "nama": "Jupiter Z1", "cc": 115, "transmisi": "Manual"},
    {"merek": "Yamaha", "nama": "Vega", "cc": 115, "transmisi": "Manual"},

    # Kategori Kopling
    {"merek": "Honda", "nama": "CBR150R", "cc": 150, "transmisi": "Kopling"},
    {"merek": "Honda", "nama": "CBR250RR", "cc": 250, "transmisi": "Kopling"},
    {"merek": "Suzuki", "nama": "GSX R150", "cc": 150, "transmisi": "Kopling"},
    {"merek": "Yamaha", "nama": "R15", "cc": 155, "transmisi": "Kopling"},
    {"merek": "Yamaha", "nama": "R6", "cc": 600, "transmisi": "Kopling"},
    {"merek": "Kawasaki", "nama": "ZX25R", "cc": 250, "transmisi": "Kopling"},
    {"merek": "Kawasaki", "nama": "Z800", "cc": 800, "transmisi": "Kopling"},
    {"merek": "Ducati", "nama": "Panigale V4R", "cc": 1000, "transmisi": "Kopling"},
    {"merek": "Harley-Davidson", "nama": "Sportster S", "cc": 1250, "transmisi": "Kopling"},
    {"merek": "BMW", "nama": "F 900 XR", "cc": 900, "transmisi": "Kopling"}
]

def upper(teks):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""
    
    panjang_teks = 0
    ketemu_panjang = False
    while ketemu_panjang == False:
        pembanding = ""
        i = 0
        while i < panjang_teks:
            pembanding += teks[i]
            i += 1
            
        if pembanding == teks:
            ketemu_panjang = True
        else:
            panjang_teks += 1
        
    i = 0
    while i < panjang_teks:
        char_teks = teks[i]
        ditukar = False
        
        j = 0
        while j < 26:
            if huruf_kecil[j] == char_teks:
                hasil += huruf_besar[j]
                ditukar = True
            j += 1
            
        if ditukar == False:
            hasil += char_teks
            
        i += 1
        
    return hasil


def lower(teks):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""
    
    panjang_teks = 0
    ketemu_panjang = False
    while ketemu_panjang == False:
        pembanding = ""
        i = 0
        while i < panjang_teks:
            pembanding += teks[i]
            i += 1
            
        if pembanding == teks:
            ketemu_panjang = True
        else:
            panjang_teks += 1
        
    i = 0
    while i < panjang_teks:
        char_teks = teks[i]
        ditukar = False
        
        j = 0
        while j < 26:
            if huruf_besar[j] == char_teks:
                hasil += huruf_kecil[j]
                ditukar = True
            j += 1
            
        if ditukar == False:
            hasil += char_teks
            
        i += 1
        
    return hasil

# FITUR 1: Tampilkan data berdasarkan kategori transmisi
def tampilkan_berdasarkan_transmisi(jenis_transmisi):
    print(f"\n=== DAFTAR MOTOR TRANSMISI {upper(jenis_transmisi)} ===")
    print(f"{'No':<4} | {'Merek':<15} | {'Model Motor':<20} | {'Kapasitas Mesin':<10}")
    print("-" * 60)
    
    nomor = 1
    for motor in data_motor:
        if lower(motor["transmisi"]) == lower(jenis_transmisi):
            print(f"{nomor:<4} | {motor['merek']:<15} | {motor['nama']:<20} | {motor['cc']} cc")
            nomor += 1
            
    if nomor == 1:
        print("Data tidak ditemukan.")

# Menu Utama Aplikasi Rental
def menu_utama():
    while True:
        print("\n======================================")
        print("   APLIKASI MANAJEMEN RENTAL MOTOR    ")
        print("======================================")
        print("1. Lihat Motor Transmisi Matik")
        print("2. Lihat Motor Transmisi Manual")
        print("3. Lihat Motor Transmisi Kopling")
        print("4. Keluar Aplikasi")
        print("======================================")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_berdasarkan_transmisi("Matik")
        elif pilihan == "2":
            tampilkan_berdasarkan_transmisi("Manual")
        elif pilihan == "3":
            tampilkan_berdasarkan_transmisi("Kopling")
        elif pilihan == "4":
            print("\nTerima kasih! Jangan lupa selesaikan fitur lainnya ya! 😉")
            break
        else:
            print("\nPilihan tidak valid! Masukkan angka yang benar.")

# Jalankan Program
if __name__ == "__main__":
    menu_utama()