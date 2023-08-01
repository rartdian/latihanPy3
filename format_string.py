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

#bil desim