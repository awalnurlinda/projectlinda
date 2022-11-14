# Nama        : AWAL NUR LINDA
# NIM         : 222410102034
# Prodi       : Teknologi Informasi
# Mata Kuliah : Algoritma dan Pemrograman
# Kelas       : D

import time
import random
angka = random.randint(0, 100)

print('_ - _ - _ - _ - _ - _' ,"SELAMAT DATANG DI GAME TEBAK-TEBAKAN ANGKA", '_ - _ - _ - _ - _ - _')
time.sleep(2)

introduce = input('\nSilahkan Masukkan Username Anda : ')
print('\n                                  ''SELAMAT DATANG', introduce,)
time.sleep(2)

print('\n_ - _ - _ - _ - _ - _ - _ - _ - _ - _ - WARNING - _- _ - _ - _ - _ - _ - _ - _ - _ - _')
time.sleep(2)
print('\n          Anda Hanya Memiliki Kesempatan Untuk Menebak Angka Sebanyak 7 Kali')
time.sleep(2)
print('\n    Angka Yang Harus Anda Tebak Adalah Bilangan Bulat Yang Berkisar Antara 0 - 100')
time.sleep(2)
print('\n                         Selamat Bermain dan Semoga Beruntung')
time.sleep(2)

batas_penebakan = 7
for penebakan in range(batas_penebakan) :
  angka_tebakan = int(input(f'\n[Percobaan {penebakan + 1}] Masukkan sebuah angka : '))
  if angka_tebakan == angka :
    print('Tebakan Anda tepat, Anda menebak sebanyak',penebakan + 1,'kali')
    break
  else :
    print('Tidak tepat, angka terlalu','kecil' if angka_tebakan < angka else 'besar')
else:
  print(f'\nAnda kurang beruntung')

print('\n_ - _ - _ - _ - _ - _ - _ - _ TERIMAKASIH TELAH BERMAIN _ - _ - _ - _ - _ - _ - _ - _')
