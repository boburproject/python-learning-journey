# Lesson 09 - For Loops
# Date: 2026-06-25


# Exercise 1
ismlar = ["Islomjon","Zohirshoh","Bobur","Javohir","Muhammad"]
for ism in ismlar:
  print(f"Salom {ism} bugun choyxona borasanmi?")

print(f"Ko'd jami {len(ismlar)} martta takrorlandi.")

# Exercise 2
for toq in range(11,100,2):
  print(f"\n{toq} sonning kubi:")
  print(f"{toq**3}")

# Exercise 3
kinolar = []
print("5 ta eng yahshi ko'rgan kinoyingizni ayting:")
for son in range(5):
  kinolar.append(input(f"{son+1}-si:\t"))
print(kinolar)

# Exercise 4
odamlar = []
raqam = int(input("Hurmarli janob, bugun nechta odam bilan ko'rishdingiz:\t"))
for harb in range(raqam):
  odamlar.append(input(f"{harb+1} chi uchgashgan odamingiz kim bo'ldi:\t").title())
print(odamlar)