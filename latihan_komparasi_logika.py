#program membuat area rentang dari angka
#+++3-------10+++
inputUser = float(input("masukkan angka < 3 atau 10>"))
print(inputUser)
hasil1 = inputUser < 3
hasil2 = inputUser>10
hasil3 = hasil1 or hasil2
print(hasil1,"\n","or",hasil2,"\n", hasil3)

#memeriksa angka lebih dari 10
lebihdari = inputUser > 10
print("lebih dari 10 = ", lebihdari)

#cek kebenaran
iscorrect = hasil3 or lebihdari
print("angka yg anda masukkan = ", iscorrect)

#contoh kasus irisan
#----3+++++10-----
inputUser = float(input("masukkan nilai diantara 3 dan 10 = "))

#----3++++
lebihdari = inputUser > 3
print("lebih dari 3 = ",lebihdari)

#+++++10----
kurangdari = inputUser < 10
print('kurang dari 10 = ',kurangdari)

iscorrect = lebihdari and kurangdari
print('nilai anda diantara 3 dan 10 = ', iscorrect)