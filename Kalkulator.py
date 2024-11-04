import pyfiglet

judul = pyfiglet.figlet_format('KALKULATOR SEDERHANA')
print(judul)

#inputan user
def kalkulator():
    print('pilih operasi :')
    print('1. Tambah (+)')
    print('2. Kurang (-)')
    print('3. Kali (*)')
    print('4. Bagi (/)')

#user memilih inputan
operasi = input('Masukkan operasi (+), (-), (*), (/) :')

angka1 = int(input('Masukkan angka pertama :'))
angka2 = int(input('Masukkan angka kedua   :'))

#algoritma

if operasi == '+':
    hasil = angka1 + angka2
    print('hasilnya               :', hasil)

elif operasi == '-':
    hasil = angka1 - angka2
    print('hasilnya               :', hasil)

elif operasi == '*':
    hasil = angka1 * angka2
    print('hasilnya               :', hasil)

elif operasi == '/':
    if angka2 == 0:
        print('Error: Tidak bisa dibagi dengan 0')

    else:
        hasil = angka1 / angka2
        print('hasilnya               :', hasil)

else:
    print('Perhitungan tidak valid')






