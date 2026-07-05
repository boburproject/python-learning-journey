# Date: 21/06/2026

# Exercise 1
kocha = input("Ko'changizning nomi\n>>>")
mahalla = input("Mahalangizning nomi\n>>>")
tuman = input ("Tumaningizning nomi\n>>>")
viloyat = input("Viloyatning nomi\n>>>")

print(kocha.title() ,"ko'chasi,", mahalla.capitalize() ,"mahallasi", tuman.title(),"tumani", viloyat.capitalize(), "viloyati") #1-oddiy versiya
print(f"{kocha.title()} ko'chasi, {mahalla.lower()} mahallasi, {tuman.capitalize()} tumani, {viloyat.upper()} viloyati") #2-professionalroq versiya
