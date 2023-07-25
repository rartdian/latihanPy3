#operasi yg bisa dilakukan dengan singkat
#operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print("niali a= ",a)

a += 1 #artianya a = a + 1
print("nilai a +=1, nilai a menjadi, ",a)

a -= 2 #artinya a - 2
print("nilai a -= 2, nilai a menjadi, ",a)

a *= 5 # artianya a * 5
print("nilai a *= 5, nilai a menjadi, ",a)

b = 10
print("\nnilai b = ",b)

#modulus dan floor division
b %= 3
print("nilai a %= 3, nilai b menjadi, ",b)
print("floor division")
b = 10
b //= 3
print("nilai b //= 3, nilai b menjadi",b)

#pangkat atau eksponen
a = 5
print("\nnilai a =", a)
a **= 3
print("nilai a **= 3, nilai a menjadi", a)


#operator bitwise
#OR
print("\nOR")

c = True
print("\nnilai c = ", c)

c |= False
print("nilai c |= False, nilai c menjadi",c)


c = False
print("nilai c = ",c)
c |= False
print("nilai c |= False, nilai c menjadi = ",c)


print("\nAND")
c = True
print("\nnilai c adalah ",c)
c &= False
print("nilai c &= False, nilai c menjadi= ",c)

c= True
print("nilai c adalah= ",c)
c &= True
print("nilai c &= True, nilai c menjadi= ",c)

print("\nXOR")
c = True
print("\nnilai c = ",c)
c ^= False
print("nilai c ^= False, nilai c menjadi ",c)

c = True
c ^= True
print("nilai c ^= True, nilai c menjadi ",c)

#bergeser
d = 0b0100
print("\nnilai d = ",format(d,'04b'))
d >>= 2
print("nilai d>>=2, nilai d menjadi", format(d,'04b'))
d<<=1
print("nilai d<<= 1, nilai d menjadi", format(d,'04b'))
