#casting : merubah 1 tipe ke tipe lain
#tipe data = int, float, str, bool
print("-----INTEGER-----")
tipe_data_int = 5
print("nilainya : ",tipe_data_int, "dengan type :", type(tipe_data_int))

#merubah tipe_data_int int ke float

tipe_data_float = float(tipe_data_int)
print("nilai float : ", tipe_data_float, "dengan type: ",type(tipe_data_float))

#merubah tipe_data_int integer ke str string
tipe_data_str = str(tipe_data_int)
print("nilainya : ",tipe_data_str, "dengan type: ",type(tipe_data_str))

#merubah tipe_data_int integer ke boolean
tipe_data_bool = bool(tipe_data_int)
print("nilainya :", tipe_data_bool, "dengan type : ", type(tipe_data_bool)) #akan false jika nilai = 0

print("-----FLOAT-----")
tipe_data_float = 1.2
#INT
tipe_data_int = int(tipe_data_float)
print(tipe_data_int, type(tipe_data_int)) #dibulatkan ke bawah
#STR
tipe_data_str = str(tipe_data_float)
print(tipe_data_str, type(tipe_data_str))
#Boolean
tipe_data_bool = bool(tipe_data_float)
print(tipe_data_bool, type(tipe_data_bool))

print("-----boolean-----")
tipe_data_bool = True
#int
tipe_data_int = int(tipe_data_bool)
print(tipe_data_int, type(tipe_data_int))

# float
tipe_data_float = float(tipe_data_bool)
print(tipe_data_float ,type(tipe_data_float))

#str
tipe_data_str = str(tipe_data_bool)
print(tipe_data_str, type(tipe_data_str))

print("-----STRING-----")
tipe_data_str = "2"
print(tipe_data_str, type(tipe_data_str))
#boolean
tipe_data_bool = bool(tipe_data_str)
print(tipe_data_bool, type(tipe_data_bool)) #string ke boolean berniali false jika kosong
coba_bool = ""
tipe_data_bool = bool(coba_bool)
print(tipe_data_bool, type(tipe_data_bool))


#int
tipe_data_int = int(tipe_data_str)#string harus number
print(tipe_data_int, type(tipe_data_int))
#float
tipe_data_float = float(tipe_data_str) #string harus number
print(tipe_data_float, type(tipe_data_float))
