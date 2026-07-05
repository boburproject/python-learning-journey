# Lesson 07 and 08 - Lists
# Date: 2026-06-24
# 
# 
# Learned codes(list ga bog'liq bo'lgan ikkita darsdan):
# .append()
# .pop()
# .remove()
# del
# .strip()
# .lstrip()
# .rstrip()
# .insert()
# .sort()
# .reverse()
# .sorted()
# .sort(reverse=True)
# range()
# [0:0]
# [0:]
# [:0]
# [:]
# min()
# max()
# sum()
# len()
# [] ()
# list()
# tuple()
# 


#                                       AMALIYOT
# # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# Ro'yxatning uzunligini konsolga chiqaring
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# Asl ro'yxatni qaytadan konsolga chiqaring
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# Ro'yxatdagi elementlar sonini hisoblang
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.


countries = ["USA","UZB","RUSSIA","GERMAN","BRAZIL","KONGO","FRANCE","AVSTRALIA","ARGENTINA","ISPANIYA"]
print(len(countries))
print(sorted(countries))
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
num = list(range(120,1200,2))
sums = sum(num)
print(sums)
maxmin = max(num) - min(num)
print(maxmin)
print(len(num))
start = num[0:20]
finish = num[-20:]
mid = num[260:280]
print(f"Boshidan 20 tasi:\n{start}")
print(f"O'rtasidan 20 tasi:\n{mid}")
print(f"Ohiridan 20 tasi:\n{finish}")
taomlar = ["Osh", "Sho'rva", "Mastava", "Qozonkabob", "Shashlik"]
nonushta = taomlar[:]
nonushta.remove("Osh")
nonushta.remove("Qozonkabob")

nonushta.append("Bo'lichka")
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)