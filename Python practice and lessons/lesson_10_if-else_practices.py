# Lesson 10 - if_else
# Date: 2026-06-26


# Exercise 1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car == 'gm':
    print(car.upper())
  else:
    print(car.title())

# Exercise 2
for car in cars:
   if car != 'gm':
     print(car.title())
   else:
     print(car.upper())

# Exercise 3
ism = "admin"
ism2 = input("login:\t")
if ism2.lower() == "admin":
  print("Xush kelibsiz, Admin.")
  ans = input("Foydalanuvchilar ro'yxatini ko'rasizmi")
  if ans.lower() == "ha":
    print("Ok, 1 min")
  else:
    print("Ok")
else:
  print(f"Xush kelibsiz, {ism2.title()}!")


# Exercise 4
son1 = int(input("Bitta son kiriting:\n>>> "))
son2 = int(input("Yana bitta son kiriting:\n>>> "))
if son2 == son1:    print("Sonlar teng")

# Exercise 5
print("Birinchi aytgan soningiz manfiy ekan !!!")   if son1 < 0 else print("Birinchi aytgan soningiz musbat ekan !!!")

# Exercise 6
son = int(input("Yana bitta son kiriting:\t"))
if son > 0:
  ildiz = son ** 0.5
  print(f"Siz kiritgan sonning ildizi {ildiz} ekan")
else: print("Musbat son kiriting")