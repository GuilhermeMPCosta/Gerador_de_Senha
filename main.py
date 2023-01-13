import random

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symb = '[]{}()*#;/,-_%'

qtn=input('QUantos digitos terá na senha:')
qtnint=int(qtn)
length = qtnint

all=min+max+num+symb
caps=max+num+symb
nocaps=min+num+symb
nusy=num+symb
maxnum=max+num
minnum=min+num
maxsymb=max+symb

print("senha: " + "".join(random.sample(all,length)))
print("senha: " + "".join(random.sample(caps,length)))
print("senha: " + "".join(random.sample(nocaps,length)))
print("senha: " + "".join(random.sample(nusy,length)))
print("senha: " + "".join(random.sample(maxnum,length)))
print("senha: " + "".join(random.sample(minnum,length)))
print("senha: " + "".join(random.sample(maxsymb,length)))
