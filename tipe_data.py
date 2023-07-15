#tipe data angka satuan atau integer yg tidak ada koma

data_integer = 1 #python automatis data 1 adalah integer
print("data :", data_integer, "bertipe : ", type(data_integer)) #data : 1 bertipe :  <class 'int'>

#data float, angka dengan koma
data_float = 1.3

print("data :", data_float)
print("bertipe :", type(data_float))

#data string = kumpulan karakter
data_string = "rio"
print("data :", data_string)
print("tipe data : ",type(data_string))

#tipe data biner 0 , 1 ture / false , boolean
data_boolean = True
print("data :", data_boolean)
print("tipe data : ", type(data_boolean))

#tipe data khusus

#bliangan kompleks
#10+5i imajiner = data  komplex (5,6)

data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe data :", type(data_complex))

#karena python dibuat dengan bahasa c maka python bisa menggunakan bahasa c
#dengan cara import lib/package

from ctypes import c_double #menggunakan tipe data double jika perlu
data_c_double = c_double(11.5)
print("data :",data_c_double)
print("dengan tipe data: ",type(data_c_double))