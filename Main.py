#menggunakan library waktu untuk menghitung lama program dijalankan
import time #lib atau package time
start_time = time.time()


print("hello world")

#python itu dari sourcecode main.py diterjemahkan python ke terminal untuk dijalankan
#langsung di run tanpa harus compile,run atau compile python berdasarkan urutan atas ke bawah

#berbeda dengan cpp dengan compile dari source code ke compile lalu .exe dijalankan di terminal

a = 12 #assignment = menaruh ke memory
print(a)

#bisa compile python ke bytecode atau posisi sama dengan .exe dan lebih efisien 
#dari source code ke python langsung ditampilkan


#membuktikan compile lebih cepat daripada interpreted
#cara compile Main.py   python -m py_compile Main.py

#akhir pada time
print(time.time() - start_time, "detik")