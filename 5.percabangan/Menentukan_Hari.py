# Buatlah program yang menerima input angka 1-7, di mana:
#
# 1 berarti Senin
# 2 berarti Selasa
# 3 berarti Rabu
# 4 berarti Kamis
# 5 berarti Jumat
# 6 berarti Sabtu
# 7 berarti Minggu
# Jika pengguna memasukkan angka di luar rentang 1-7, tampilkan pesan bahwa input tidak valid.

angka = int(input("masukkan angka : "))

if angka == 1:
    print("hari = senin")
elif angka == 2:
    print("hari = selasa")
elif angka == 3:
    print("hari = rabu")
elif angka == 4:
    print("hari = kamis")
elif angka == 5:
    print("hari = jumat")
elif angka == 6:
    print("hari = sabtu")
elif angka == 7:
    print("hari = minggu")
else:
    print("angka diluar 1-7 maka tidak valid!")

