import os
os.system('clear')
print '\t===== CAPTAIN021 ====='
print
print'1. perjumlahan'
print'2. pengurangan'
print'3. perkalian'
print'4. pembagian'
print'5. sisa bagi'
print'6. pemangkatan'
print
pilih = input('pilih yang mana : ')

if pilih == 1:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di jumlah : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di jumlah : ')
	total = angka_1 + angka_2
	print
	print 'Totalnya : ', total
	
elif pilih == 2:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di kurangi : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di kurangi : ')
	total = angka_1 - angka_2
	print
	print 'Totalnya : ', total
	
elif pilih == 3:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di kalikan : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di kalikan : ')
	total = angka_1 * angka_2
	print
	print 'Totalnya : ', total
	
elif pilih == 4:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di bagi : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di bagi : ')
	total = angka_1 / angka_2
	print
	print 'Totalnya : ', total
	
elif pilih == 5:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di bagi : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di bagi : ')
	total = angka_1 % angka_2
	print
	print 'Totalnya : ', total
	
elif pilih == 6:
	print
	angka_1 = input('Pilih nomor yng ke 1 yg akan di pangkat : ')
	angka_2 = input('Pilih nomor yng ke 2 yg akan di pangkat : ')
	total = angka_1 ** angka_2
	print
	print 'Totalnya : ', total

else:
	print
	print'Gw Gans thank you:v'