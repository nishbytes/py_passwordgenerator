import random


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to PY password generator")

n_l = int(input("How many letters would you like in your password :\n"))
n_s = int(input("How many symbols would you like :\n"))
n_n = int(input("How many numbers would you like :\n"))

length = n_l+n_s+n_n
z=[]

for a in range(n_l):
    z+=l[random.randint(0,len(l)-1)]
for b in range (n_n):
    z+=n[random.randint(0,len(n)-1)]
for c in range (n_s):
    z+=s[random.randint(0,len(s)-1)]



random.shuffle(z)

v=""
for a in z:
    v+=a
print(f"Here is your password : {v}")
