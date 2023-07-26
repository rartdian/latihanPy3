data = "ini adalah string" #kumpulan dari karakter
print(data)
print(type(data))

#1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."

'''
data = "menggunakan double quote"
print(data)
data = 'menggunakan single quote'
print(data)

print('"halo, apa kabar?"')
print("'halo apa kabare?'")
print("Assalamu'alaikum")

#2. menggunakan tanda \
#membuat tanda ' menjadi string
print('hati-hati dengan \'ain')

#backslah \
print("c:\\user\\system")

#tab \t
print("lisa\t\tcantik, pintar")

#backspace \b
print("lisa \bbelajar, di kamar")

#newline
print("baris pertama.\nbaris kedua.") #LF->line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR ->carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") #CRLF line feed cariage return->dipakai oleh windows

#3. String literal atau raw

#pelan-pelan
print('C:\new folder') #cetak path
#alternative dengan raw string
print(r'C:\new_folfer\dev') #yg didalam r akan dianggap dengan raw

#multiline literal string
print("""
NAma : lisa
No Absen: 3
Kelas: 2A
Web: lisa.com/profil
""")