#Date:22.06.2026

# Exercise 1
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
randomson = int(input("Birorta son kiriting\n>>>\t"))
print(f"Kiritgan soningizning kvadrati: {randomson**2} va kubi: {randomson**3}")

# Exercise 2
# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur 
yosh = int(input("Yoshingiz nechchida:\t"))
breakpoint
t_yil = 2026 - yosh
print(f"Siz {t_yil}-yilda tug'ilgansiz")
breakpoint

# Exercise 3
# Foydalanuvchidan ikki son kiritishni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
print("Sizdan ikkita son kiritishingizni so'raymiz !!!")
son1 = int(input("1-sonni kiriting:\t"))
son2 = int(input("2-sonni kiriting:\t"))
print(son1+son2)
print(son1*son2)
if son2 > son1:
    print(son2/son1)
    print(son2 - son1)
else:
    print(son1 - son2)
    print(son1/son2)

# Actually, I haven't covered if else elif in Python classes yet, but I added it here because I know about it.