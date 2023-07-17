#operasi untuk membandingkan nilai,
#setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

# lebih besar
a = 8
b = 9
c = a > 7
print("apakah a > 7 = ",c)

#lebih kecil
a = 2
b = 7
c = b<3
print("b = 7 , apakah b < 3 = ",c)

#lebih besar atau sama dengan
a = 5
b = 4
c = 5 >= a
print(a, " >= 5 = ",c)  

#sama dengan = dengan sama dengan sama dengan == adalah berbeda
#jika sama dengan = adalah assignment disimpan ke memory
#sedangkan sama dengan sama dengan == adalah membandingkan nilai terakhir true/false

# tidak sama dengan !=
a = 3
b = 2
c = a != 2
print("a = 3, b = 2, a tidak sama dengan 2= ",c)

#operasi komparasi diatas dapat bekerja pada syntax literal
#artinya pada baris x saja

#contoh
a == 9
 # a adalah bernilai yg disimpan pada memory,bisa dipanggil pada line selanjutnya
 # 9 adalah literal tidak disimpan ke memory, bekerja pada baris saja


#objek identity

 #is membandingkan nilai yg khusus ada di memory/objek 

a = 3 #is adalah assignment membuat object 
b = 3
c = a is b
print("lokasi hex memory a =",hex(id(a)))
print("lokasi hex memory b=", hex(id(b)))
print("a=3, b=3, a is b =", c)
#jika diperhatikan lokasi a dan b sama,karena python terlalu pintar untuk efisiensi memory

#is not , sama seperti tidak samadengan

a = 3
b = 3
c = a is not b
print("a=3,b=3, a isnot b = ",c)