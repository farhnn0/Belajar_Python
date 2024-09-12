# Program untuk mengecek bonus dan diskon

total_belanja = int(input("Masukkan total belanja Anda: Rp"))

# Jumlah yang harus dibayar adalah berapa total belanjaannya
# Tapi kalau dapat diskon akan berkurang
bayar = total_belanja

# Jika dia belanja di atas 100rb maka berikan bonus dan diskon
if total_belanja > 100000:
    print("Selamat Anda mendapatkan piring sebanyak 1 lusin")
    print("Dan diskon 5%")

    # Hitung diskonnya
    diskon = total_belanja * 5 / 100
    bayar = total_belanja - diskon

# Cetak struk
print("Total diskon anda adalah", diskon)
print("dan Total yang harus dibayar adalah", bayar)
print("Terima kasih sudah berbelanja")
