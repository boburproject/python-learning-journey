# Lesson 15 - dictionary(lug'at) 
# Date: 10/07/2026

# Exercise 1
students = {}
print('Enter 4 old students:  ')
for n in range(4):
    old = input(f"{n+1}-student:  ").lower().strip()
    students[old.title()] = 'old'
print(f'Your old students: {", ".join(students.keys())}')

print('Enter your 4 new students:  ')
for n in range(4):
    new = input(f"{n+1}) ").lower().strip()
    students[new.title()] = "new"
for student in students:
    if students[student] == 'new':
        print(f"Your new student: {student}")

print(f"\nYour all students: {", ".join(sorted(students))} \nAnd")
for key, value in sorted(students.items()):
    print(f"{key.title()} is {value}")


# Exercise 2
countries = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

country = input(" Which country do you want to know its capital: ").lower().strip()
if country in countries.keys():
    print(f"{(countries[country]).title()} is capital of {country.title()} ")
elif country in countries.values():
    print(f"This is not country")
else:
    print(f"We don't have information about {country.title()}")


# Exercise 3
foods = {'osh':15000,
         'somsa':10000,
         'bishteks':20000,
         'tabaka':25000,
         'shashlik':17000,
         'qovurdoq':30000,
         "sho'rva":40000
         }
num = int(input("How many food do you order:  "))
orders = []
for n in range(num):
    orders.append(input(f"\n{n+1}) ").lower().strip())


for food in foods:
    if food in orders:
        print(f"{food} is {foods[food]} so'm")
for order in orders:
    if order not in foods:
        print(f"We don't have {order}")

    