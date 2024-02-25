import random
simvole = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
opros = int(input('Какую длину пароля вы хотите?:'))
parole = ""
for i in range(opros):
    parole += random.choice(simvole)
print(parole)
    
