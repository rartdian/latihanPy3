a = 100
b = 40

#perkalian
hasil = a * b
print(a ,"*", b ,"=", hasil, type(hasil))
#pembagian
hasil = a /b
print(a, "/", b , "=", hasil, type(hasil)) #automatis float
#pengurangan
hasil = a - b
print(a, "-", b, "=", hasil, type(hasil))
#penjumlahan
hasil = a + b
print(a, "+", "b", "=", hasil, type(hasil))


#ada operator yg tidak ada di bahasa lain yaitu exponen ** dipangkatkan
a = 2
b = 3
hasil = a ** b
print(hasil)

#modulus , sisa bagi hasil
a = 10
b = 3
hasil = a % b
print("sisa bagi hasil 10 mod 3 adalah: ",hasil)

#kebalikan dari modulus floor division //
a = 10
b = 3
hasil = a // b
print("floor division","a",  "//", "b", "=", hasil, type(hasil)) #seperti pembagian dibulatkan ke bawah

#prioritas operasi
#urutan pengerjaan (), exponen, perkalian /, +-
#tanda kurung akan mengambil langkah pertama
a = 4
b = 5
c = 6
hasil = (a+b)*c 
print(hasil)
