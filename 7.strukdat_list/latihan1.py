hobi = []
stop = False
i = 0
while not stop:
    hobi_baru = str(input("Masukkan hobi ke {} : """.format(i+1)))
    hobi.append(hobi_baru)
    i+=1
    tanya = input("Apakah ingin mengulang ? (y/t)")
    if tanya == "t":
        stop = True

        print("="*10)
        print("kamu memliki {} hobi".format(len(hobi)))
        for hobi in hobi:
            print(hobi)