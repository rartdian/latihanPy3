#Operator bitwise adalah operasi biner atau binary
#bitwise -> operasi kepada masing-masing bit, contoh angka 2 di bitwise kan or dengan angka 1

#perbedaan boolean dengan bitwize
#jika boolean memakai OR, XOR, AND , NOT
#sedangkan bitwize memakai | , ^ , & , ~

#contoh
#int 2 -> 00000010 artinya index dipangkatkan
#         76543210
#               2^1 = 2

#jika int = 1
#         00000001
#                2^0 = 1 #berapapun nilainya jika dipangkatkan 0 adalah 1

#int = 9
#         00001001
  #            2^3    2^0 = 9
#----------------------> dijumlahkan (2*2*2) + 1 = 9


a = 9
b = 5

#bitwise OR (|)
c= a | b

print('bitwise OR')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('------------------------------------ OR |')
print('nilai :',c,',binary:',format(c,'08b'))

#bitwise AND (&)
c = a & b

print('bitwise AND')
print('nilai :',a,',binary:',format(a,'08b'))
print('nilai :',b,',binary:',format(b,'08b'))
print('---------------------------------- AND &')
print('nilai :',c,',binary: ',format(c,'08b'))

#bitwise XOR (^)
c = a ^ b

print('bitwise XOR')
print('nilai :',a,',binary: ',format(a,'08b'))
print('nilai :',b,',binary: ',format(b,'08b'))
print('---------------------------------- XOR ^')
print('nilai :',c,',binary: ',format(c,'08b'))

#bitwise NOT (~)

c = ~a
print('bitwise NOT')
print('nilai :',a,',binary : ',format(a,'08b'))

print('---------------------------------- NOT ~')
print('nilai :',c,',binary : ',format(c,'08b')) #kenapa hasilnya not 9 adalah -10, karena not dimuali dari -1
#untuk menangani not ada tri yaitu dengan di XOR kan maka didapat hasil not 9
d = 0b00001001 #nilai 9
e = 0b11111111 #trik untuk hasil not yg benar
f = e ^ d
print('---------------------------------- XOR ^')
#print('nilai :', e^d) 00001001 ,
print('nilai :', f ,'binary : ',format(f,'08b')) #not c = f
#karena di py tdk mempunyai unsigned, semuany signed ada tanda ny + -


#shiting

#shift right (>>)
a = 100
shift_right = a >> 1
print('biner 100 :',format(a,'08b'))
print('shift right 1 :',format(shift_right,'08b'))

#shift left (<<)
b = 3
shift_left = b << 2
print('biner dari 3 adalah :',format(b,'08b'))
print('shift left << 3 maka:',format(shift_left,'08b'))