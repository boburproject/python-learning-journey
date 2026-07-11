# Lesson 12 - dictionary(lug'at) 
# Date: 2026-07-07

# # Exercise 1
# dad = {'name':"John", 't_yil':1984, 'age':42, 'county':'uzbekistan'}
# print(f"My father's name is {dad['name'].title()}, he was born in {dad['t_yil']} now he is {dad['age']} years old \
# and he lives in {dad['county'].title()}  ")

# # Exercise 2
# fav_meals = {"dad":'osh',
#              "mother":'manti',
#              "brother":"somsa",
#              "sister":"sho'rva",
#              "l-brother":"fast food"}
# for member in fav_meals:
#     print(f"My {member}'s favourite meal is {fav_meals[member]}")


# # Exercise 3
# python = {'if':"for checking", 
#           'list':"for creating list", 
#           "print()":"For printing something from program", 
#           ".title()":"For enlarging first letter of words of sentence", 
#           ".capitalize()":"For enlarging first letter of first word of sentence", 
#           ".append()":"For adding new elements for list"}
# for word in python:
#     print(f"{word} {python[word].lower()}")

# # Exercise 4
# python = {'if':"for checking", 
#           'list':"for creating list", 
#           "print()":"For printing something from program", 
#           ".title()":"For enlarging first letter of words of sentence", 
#           ".capitalize()":"For enlarging first letter of first word of sentence", 
#           ".append()":"For adding new elements for list"}
# question = input("What do you want to learn about:  ").lower().strip()
# answer = python.get(question, "We can't answer to this qustion")
# print(answer)

# # Exercise 5
# python = {'if':"for checking", 
#           'list':"for creating list", 
#           "print()":"For printing something from program", 
#           ".title()":"For enlarging first letter of words of sentence", 
#           ".capitalize()":"For enlarging first letter of first word of sentence", 
#           ".append()":"For adding new elements for list"}
# question = input("What do you want to learn about:  ").lower().strip()
# if question in python:
#     print(python[question])
# else:
#     print("We can't answer to this question")
