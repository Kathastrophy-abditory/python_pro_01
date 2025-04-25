import random
text = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("Generador de contraseñas")
num = int(input("Longitud de la contraseña: "))
password = ""

for i in range(num):
    password += random.choice(text)

print("Tu nueva contraseña es:", password)



