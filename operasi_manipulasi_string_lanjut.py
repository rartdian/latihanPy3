#operator dalam bentuk method
#merubah case pada string
#merubah semua ke upper case

#upper
greeting = "hallo"
print("default "+greeting)
greeting = greeting.upper()
print("Upper "+greeting)

#lower
ucapan = "Selamat Pagi"
print("aslinya "+ucapan)
ucapan = ucapan.lower()
print("lower "+ucapan)

#method is, untuk pengecekan

#contoh isupper()
ucapan = "HALLO"
ask_ucapan = ucapan.isupper()
print(ucapan+"apakah ini Upper?"+str(ask_ucapan))

ucapan = ucapan.lower()
ask_ucapan = ucapan.islower()
print(ucapan+"apakah ini lower "+ str(ask_ucapan))

#islower() untuk pengecekan apakah lower case semua?
#isalpha() untuk cek apakah huruf semua?
#isalnum() apakah huruf dan angka?
#isdecimal() apakah numerik
#isspace() apakah isinya spasi, tab dan enter (newline \n) ?
#istitle() huruf pertama setiap kata upper case

judul = "Konsisten Di Hal Prioritas"
cek_judul = judul.istitle()
print(judul+" is title? "+str(cek_judul))

#startwith() dan endwidth() ?
cek_start = "Hallo Pak,".startswith("Ha")
print("start "+str(cek_start))
cek_end = "Selamat pagi Indonesia".endswith("sia")
print("akhir end "+str(cek_end))

#join() dan split() untuk yg ingin cepat
pisah = ['saya','suka','belajar']
gabung = 'spasi'.join(pisah)
print(pisah)
print(gabung)

gabung = "rajin belajar setiap hari"
pisah = gabung.split()
print(pisah)

#alokasi karakter
print("'kiri  '")

kanan = "kanan".rjust(20) #rata kanan dengan 20 karakter
print("'"+ kanan + "'")
kiri = "kiri".ljust(20) #rata kiri dengan 20 karakter
print("'"+kiri+"'")
tengah = "tengah".center(20) #rata tengah
print("'"+tengah+"'")


print("\n")
#kebalikan dengan alokasi karakter

print('contoh strip') #menghilangkan sisa spasi atau tanda, ambil di bagian inti kata
tengah = tengah.strip()
print("'"+tengah+"'")
