#Date and time (latihan)
import datetime as dt
print("silahkan masukkan tanggal, \nbulan dan tahun lahir\n")
tanggal = int(input("tanggal\t\t:"))
bulan = int(input("Bulan\t\t:"))
tahun = int(input("tahun\t\t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tanggal_lahir}")

hari_sekarang = dt.date.today()
print(f"Hari ini tanggal: {hari_sekarang}")
umur_day = hari_sekarang - tanggal_lahir
umur_year = umur_day.days // 365
umur_month_sisa = (umur_day.days % 365 ) // 30
umur_day_sisa = (umur_day.days - tanggal_lahir)

print(f"hari nya adalah: {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_year} tahun,{umur_month_sisa} bulan, {umur_day_sisa} hari")

#perbedaan mod dg floor division?
a = 5
b = 2
floordiv = a // b #seharusnya 2.5 namun di cut dengan fungsi floor division jadi hasilnya adalah 2
print(floordiv)

