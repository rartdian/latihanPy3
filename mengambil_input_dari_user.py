#input user
nilai = input("masukkan nilai: ")
print("nilainya adalah: ", nilai, type(nilai))
#data yg diinput adalah string
#jika yg diinginkan adalah data integer maka casting saja

nilai_int = int(nilai)
print(nilai_int, type(nilai_int))

#atau

data_number = float(input("masukkkan number desimal float : "))
print(data_number, type(data_number))

#boolean
data_bool = bool(input("masukkan T/F: "))
print(data_bool, type(data_bool)) #karena boolean bernilai false jika kosong,
#maka input kita casting ke int terlebih dahulu lalu casting ke boolean.

#contoh

input_int = int(input("masukkan 1/0: "))
data_bool = bool(input_int)
print(data_bool, type(data_bool))