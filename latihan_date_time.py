#Date and time (latihan)
import datetime as dt
print("silahkan masukkan tanggal, \nbulan dan tahun lahir\n")
tanggal = int(input("tanggal\t\t:"))
bulan = int(input("Bulan\t\t:"))
tahun = int(input("tahun\t\t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tanggal_lahir}")
