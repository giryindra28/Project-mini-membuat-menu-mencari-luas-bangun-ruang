from app import bangun_ruang, lingkaran, sub_bangunRuang

print("")
print("## Program Hitung Luas Bangun Ruang ##")
print("======================================")
print("Silahkan pilih menu dibawah ini: ")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")
print("5. Belah Ketupat")
print("6. Trapesium")
print("7. Permukaan Balok")
print("=====================")
pilihan = int(input("pilihanmu (berdasarkan nomor): "))

if pilihan == 1:
    print("")
    print("## Luas Persegi ##")
    print("==================")

    input1 = int(input("Masukan sisi 1 persegi: "))
    input2 = int(input("Masukan sisi 2 persegi: "))
    persegi = bangun_ruang(input1,input2)
    persegi.persegi()

elif pilihan == 2:
    print("")
    print("## Luas Persegi Panjang ##")
    print("==========================")

    input1 = int(input("Masukan panjang: "))
    input2 = int(input("Masukan lebar: "))
    persegi = bangun_ruang(input1,input2)
    persegi.luas_persegiPanjang()

elif pilihan == 3:
    print("")
    print("## Luas Segitiga ##")
    print("===================")

    input1 = int(input("Masukan alas: "))
    input2 = int(input("Masukan tinggi: "))
    segitiga = bangun_ruang(input1,input2)
    segitiga.luas_segitiga()

elif pilihan == 4:
    print("")
    print("## Luas Lingkaran ##")
    print("====================")

    input1 = int(input("Masukan jari-jari: "))
    lingkaran = lingkaran(input1)
    lingkaran.luas_lingkaran()

elif pilihan == 5:
    print("")
    print("## Luas Belah Ketupat  ##")
    print("=========================")

    input1 = int(input("Masukan panjang diagonal 1: "))
    input2 = int(input("Masukan panjang diagonal 2: "))
    belahKetupat = bangun_ruang(input1,input2)
    belahKetupat.belah_ketupat()

elif pilihan == 6:
    print("")
    print("## Luas Trapesium ##")
    print("====================")

    input1 = int(input("Masukan pangjang sisi sejajar atas: "))
    input2 = int(input("Masukan panjang sisi sejajar bawah: "))
    input3 = int(input("Masukan tinggi trapesium: "))
    trapesium = sub_bangunRuang(input1,input2,input3)
    trapesium.luas_trapesium()

elif pilihan == 7:
    print("")
    print("## Luas Permukaan Balok ##")
    print("==========================")

    input1 = int(input("Masukan panjang balok: "))
    input2 = int(input("Masukan lebar balok: "))
    input3 = int(input("Masukan tinggi balok: "))
    balok = sub_bangunRuang(input1,input2,input3)
    balok.luas_balok()

else:
    print("Mohon input nomor yang benar!")
    

