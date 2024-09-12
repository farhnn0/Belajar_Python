bil1 = int(input("masukkan bilangan pertama : "))
bil2 = int(input("masukkan bilangan kedua : "))
operator =(input("Masukkan operator (+, -, *, /): "))

if operator == '+':
    hasil = bil1 + bil2
    print(hasil)
elif operator == '-':
        hasil = bil1 - bil2
        print(hasil)
elif operator == '*':
    hasil = bil1 * bil2
    print(hasil)
elif operator == '/':
    if bil2 != 0:
        hasil = bil1 / bil2
        print(hasil)
    else:
        print("error pembagian dengan 0 tidak diperbolehkan")
else:
    print("invalid!masukkan operator yang benar.")
