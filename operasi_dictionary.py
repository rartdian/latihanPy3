#operator dictionary

data_dict = {
'key1' : 'sepeda motor',
'key2' : 'sepeda',
'key3' : 'becak'
}

print(data_dict['key1'])

#menghitung panjang dari dictionary
LENDICT = len(data_dict)
print(f"panjang nya data dictionary : ",LENDICT)

#cek apakah ada key nya (exist) atau tidak
KEY = "key1"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di dictionary: {CHECKKEY}")

#untuk memanggil akses read dan membedakan data yg dictionary dan yg lain (contoh list),bisa menggunakan get

#menggunakan get
print(data_dict.get("key2"))
print(data_dict.get("key4"))
#print(data_dict["key0"]) akan error maka gunakan get, apabila di dict tdk ada tidak error

#contoh notif key tidak ada
print(data_dict.get("key4","key tidak ditemukan"))

#mengubah data
data_dict["key1"] = "helikopter"
print(data_dict)

#mengubah dengan lib update, jika data tidak ada maka automatis akan ditambahkan, jika ditemukan ada maka akan diubah
data_dict.update({"key4" : "Bus"})
print(data_dict)

data_dict.update({"key4" : "mobil polisi"})
print(data_dict)

#delete data dictionary
del data_dict["key4"]
print(data_dict)
