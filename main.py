# Kalkulator Sederhana
def kalkulator():
    print(20*"=")
    print("Kalkulator Sederhana")
    print("By Budi Agung")
    print(20*"=" + "\n")

    try:
        angka_1 = float(input("Masukkan angka Pertama : "))
    except ValueError:
        print("Input Harus Berupa Angka!")
        return
    
    operator = input("Operator (+,-,*,/) : ")

    try:
        angka_2 = float(input("Masukkan Angka Kedua : "))
    except ValueError:
        print("Input Harus Berupa Angka!")
        return

    # Percabangan
    if operator == "+":
        hasil = angka_1 + angka_2
        print(f"{angka_1} + {angka_2} = {hasil}")
    elif operator == "-":
        hasil = angka_1 - angka_2
        print(f"{angka_1} - {angka_2} = {hasil}")
    elif operator == "*":
        hasil = angka_1 * angka_2
        print(f"{angka_1} * {angka_2} = {hasil}")
    elif operator == "/":
        if angka_2 == 0:
            print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka_1 / angka_2
            print(f"{angka_1} / {angka_2} = {hasil}")
    else:
        print("Masukkan Operator Yang Benar")
        
    print()
    print("Akhir Dari Program")
    print()

def main():
    while True:
        kalkulator()
        lanjut = input("Apakah Ingin Melanjutkan Perhitungan? y/n : ").lower()
        if lanjut != 'y':
            print("Terima Kasih")
            break

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
