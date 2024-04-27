#list -> array, mengakses dg menggunakan index
data_list = ['apel','mangga','pepaya']
print(data_list[0])

#perbedaan dictionary dengan list
#jika di list untuk mengakses data menggunakan indexnya
#jika di dictionary mengakses data menggunakan identifier dengan key nya

#contoh
data_dictionary = {
'key1' : 'nilaiA',
'key2' : 'nilaiB',
'list' : data_list
}

print(data_dictionary)
print(data_dictionary['key2'])
print(data_dictionary['list']) #bisa memasukkan list ke data dictionary
