#format string
#contoh generic

#string
nama = "lisa"
format_str = f"hai {nama}" #f itu untuk format
print(format_str)

#Boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

#number
numb = 20.3
format_str = f"number = {numb}"
print(format_str)

#bil bulat
numb = 122
format_str = f"bilangan bulat = {numb:d}"
print(format_str)

#bil dengan ordo ribuan
number = 9000000000
format_str = f"juta = Rp. {number:,},-"
print(format_str)

#bil desimal
number = 20.543299999
format_str = f"desimal = {number:.3f}" #ambil 3 angka dibelakang koma f=float
print(format_str)

#menampilkan leading zero
number = 2101.290920
format_str = f"desimal = {number:010.3f}"
print(format_str)

#menampilkan tanda + atau -
nilai_minus = -10
nilai_plus = +10.2323
format_minus = f"minus = {nilai_minus:+d}"
format_plus = f"plus = {nilai_plus:+.2f}"
print(format_minus)
print(format_plus)

#format persen
presentase = 0.045
format_persen = f"presen = {presentase:.2%}"
print(format_persen)



#melakukan operasi aritmatika di dalam placeholder
harga = 100000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

#format angka lain (binary, octal, hexadecimal)

nilai = 128
format_binary = f"binary = {bin(nilai)}"
format_octal = f"octal = {oct(nilai)}"
format_hex = f"hex = {hex(nilai)}"

print(format_binary)
print(format_octal)
print(format_hex)
