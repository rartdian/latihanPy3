#operasi boolean
#not, or, and, xor


print("latihan NOT")
a = True
b = not a
print("a = true, b = not a, b = ",b)

print('latihan or') #bernilai true jika salah satu atau keduanya true. seperti pertambahan
a = True
b = False

c= a or b
d = a or a
e = b or b
f= b or a
print ('t or f =',c)
print('t or t =', d)
print('f or f=',e)
print('f or t=',f)

print('and') #bernilai true jika keduanya true, seperti perkalian 
a = True
b = False
c = a and b
d = a and a
e = b and b
f = b and a
print(a,'and',b,'=',c )
print(a,'and',a,'=',d)
print(b,'and',b,'=',e)
print(b,'and',a,'=',f)

print('XOR') #akan true jika salah satu true, sisa nya false
a = True
b = False
c = a ^ b
d = a ^ a
e = b ^ b
f = b ^ a
print(a,'XOR',b,'=',c )
print(a,'XOR',a,'=',d)
print(b,'XOR',b,'=',e)
print(b,'XOR',a,'=',f)