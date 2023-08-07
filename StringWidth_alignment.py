#width and multiline
#data
data_nama = "lisa"
data_umur = 20
data_tinggi = 11
data_no_hp = 87832323421

#string standart
data_no_hp =f"{data_no_hp:012}" 
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi badan = {data_tinggi}, no hp = {data_no_hp}"
print(5*"="+"Data String biasa"+5*"=")
print(data_string)

#String multiline (dengan menggunakan enter, newline \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi badan = {data_tinggi}, \nno hp = {data_no_hp}"
print(5*"="+"Data String dengan enter"+5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
no hp = {data_no_hp}
"""
print(5*"="+"Data String dengan triplets"+5*"=")
print(data_string)

#mengatur lebar
data_nama = "rio"
data_tinggi = "180.4"
data_string = f"""
nama    = {data_nama:>5}
tinggi  = {data_tinggi:>5}
umur    = {data_umur:>5}
no hp   = {data_no_hp:>5}
"""
print("\n"+5*"="+"Data String pengatur lebar"+5*"=")
print(data_string)

