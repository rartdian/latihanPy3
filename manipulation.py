#operasi dan manupulasi string

#1. menyambung string(concatenate)
nama_pertama = "lisa"
nama_tengah = "tisha"
nama_akhir = "azzahra"

nama_lengkap = nama_pertama+" "+nama_tengah+" "+nama_akhir
print(nama_lengkap)

#2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang string nama lengkap adalah="+str(panjang)+"str")

#3.operator untuk string
#cek apakah ada komponen pada sebuah string
a = "a"
status = a in nama_lengkap
print(" apakah karakter a ada ?"+str(status))

A = "A"
status = A in nama_lengkap
print("apakah karakter A ada ?"+ str(status))

s = "s"
status = s is not nama_lengkap
print("apakah s tidak ada di "+nama_lengkap+"? "+str(status))


#mengulang string
print("wk"*19)
print(100*"ok")

#indexing

print("index ke-0: "+nama_lengkap[0])#dimulai dari 0
print("index ke-6 : "+nama_lengkap[6])#index ke 6
print("index ke-(-1) : "+nama_lengkap[-1])#indexing dari belakang
print("index ke-[6,8] : "+nama_lengkap[6:8]) #dimulai dari 6 sampai sebelum8
print("index ke-[0,2,4,6,8]"+nama_lengkap[0:10:2]) #diambil index 0,2,4,6,8

#item paling kecil
print("alphabet terkecil adalah: "+ min(nama_lengkap))
#item paling besar
print("alphabet terbesar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII number dari spasi : "+str(ascii_code))
data = 117
print("character dari acii code 117 : "+ chr(data))

 
#4. operator dalam bentuk method
data = "selamat pagi dunia"
jumlah = data.count("a")
print("jumlah a di "+ data + " : "+str(jumlah))