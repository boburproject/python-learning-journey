# Lesson 11 - if(bir nech shartlarni bajarish)
# Date: 2026-06-27


# Exercise 1

json = int(input("Juft son kiriting:\t"))
if json % 2:
    print("Bu son juft emas")
else:
    print("Rahmat")




# Exercise 2
yosh = int(input("Yoshingiz nechchida:  "))
if 4 >= yosh or yosh > 60:
    narx = "bepul"
elif yosh <= 18:
    narx = 10_000
else:
    narx = 20_000
print(f"Sizga kirish {narx}", 
" " if yosh <= 4 else "so'm")



# Exercise 3
print("Sizdan ikkita son kiritishingizni so'raymiz:\t")
son1 = int(input("1-son:\t"))
son2 = int(input("2-son:\t"))
if son1 < son2:
    print("1-son 2-songa qaraganda kichkina ekan")
elif son2 < son1:
    print("2-son 1-songa qaraganda kichkina ekan")
else:
    print("Ikkila son ham teng ekan")



# Exercise 4 & 5
mahsulotlar = ["olcha", "banan", "sut", "non", "somsa", "malako", "bo'lichka", "daftar", "telefon", "plastik", "go'sh"]
hohishlar = []
borlar =[]
yoqlar = []
print("Sizdan 5 ta olishingiz kerak bo'lgan mahsulotlaringizni so'raymiz !!!")
for num in range(5):
    hohishlar.append(input(f"{num+1}-sini ayting:\t").lower().strip())
for hohish in hohishlar:
    if hohish in mahsulotlar:
        borlar.append(hohish)
    else:
        yoqlar.append(hohish)
if borlar:        
    if not yoqlar:
        print("Bizda siz aytgan hamma mahsulot bor ekan")
    else:
        print(f"Bizning do'konimizda {", ".join(borlar)} bor ")
if yoqlar:
    if not borlar:  print(f"Uzur lekin bizning do'konimizda siz aytgan mahsulotlaringizning birortasi ham yo'q ekan")
    else: print(f"lekin bizning do'konimizda {", ".join(yoqlar)} yo'q ekan")


# Exercise 6
ism = input("Ismingiz:\t").lower().strip()
familiya = input("Familiya:\t").lower().strip()
usernames = ["computer", "azizbek", "islomjonch", "suhrob", "anaskhon783", "boburcs", "rahmonov234"]
print(f"Agar hohlasangiz bularning birortasini tanlashingiz mumkin: {ism}0235, {familiya}9034, {ism}{familiya}3450")
newlogin = input("Log in tanlashingizni so'raymiz: ").lower().strip()
if newlogin in usernames:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {ism.title()} {familiya.title()}!")



# Exercise 7
son = int(input("Birorta butun son kiriting:  "))
for num in range(2, 11):
    if son % num == 0:
        print(num)