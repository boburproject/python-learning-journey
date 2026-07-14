# Lesson 16 - nesting 
# Date: 14/07/2026

# Exercise 1
stive = {'name':'Steve Jobs',
        't_yil':1955,
        'v_yil':2011,
        't_place':'USA'
        }
bill = {'name':'Bill Gates',
        't_yil':1955,
        'v_yil':'alive',
        't_place':'USA'
        }
ilon = {'name':'Elon Musk',
        't_yil':1971,
        'v_yil':'alive',
        't_place':'Africa'
        }
mark = {'name':"Mark Sukerberg",
        't_yil':1984,
        'v_yil':'alive',
        't_place':'USA'
        }
celebrities = [stive, bill, ilon, mark]
for celebrity in celebrities:
    print(f"{celebrity['name']} was born in {celebrity['t_yil']} in {celebrity['t_place']} and {celebrity['name']}", end=' ' )
    print(f"is alive now") if celebrity['v_yil'] == 'alive' else print(f"was died in {celebrity['v_yil']}")


# Exercise 2
stive = {'name':'Steve Jobs',
        't_yil':1955,
        'v_yil':2011,
        't_place':'USA'
        }
bill = {'name':'Bill Gates',
        't_yil':1955,
        'v_yil':'alive',
        't_place':'USA'
        }
ilon = {'name':'Elon Musk',
        't_yil':1971,
        'v_yil':'alive',
        't_place':'Africa'
        }
mark = {'name':"Mark Sukerberg",
        't_yil':1984,
        'v_yil':'alive',
        't_place':'USA'
        }
celebrities = [stive, bill, ilon, mark]

stive['inventions'] = ['apple', 'mac', 'iPad', 'iPhone', 'iPod']
bill['inventions'] = ['MS-DOS', 'Windows OS', 'Microsoft office', 'Internet explorer']
ilon['inventions'] = ['x.com', 'Falcon rockets', 'tesla cars', 'starlink']
mark['inventions'] = ['facebook', 'meta', 'whatsapp', 'social ecosystem']

for celebrity in celebrities:
    print(f"Inventor: {celebrity['name']}")
    print(f"Inventions: {(", ".join(celebrity['inventions'])).title()}\n")


# Exercise 3
people = {"bro":[],
          "mother":[],
          "friend":[]
          }
for person in people:
    print(f"Hi {person}, tell me your 3 favourite movies:")
    for n in range(3):
        people[person].append(input(f"{n+1}) "))

for person, movie in people.items():
    print(f"{person}'s favourite movies are {", ".join(movie[:-1])} and {movie[-1]}")


# Exercise 4
countries = {"O'zbekiston":{'capital':'Tashkent',
                            'area':448_900,
                            'population':'37.5 million',
                            'currency':'UZS'
                            },
            'Russia':{'capital':'Moscow',
                      'area':17_098_246,
                      'population':'144 million',
                      'currency':'RUB'
                            },
            'USA':{'capital':'Washington',
                   'area':9_833_517,
                   'population':'345 million',
                   'currency':'USD'
                   }
            }
for country, info in countries.items():
    print(f"Capital of {country} is {info['capital']}", end=' and ')
    print(f"its area is {info['area']}", end='. ')
    print(f"Population of {country} is {info['population']}", end=' and ')
    print(f"its currency is {info['currency']}")


# Exercise 5
countries = {"O'zbekiston":{'capital':'Tashkent',
                            'area':448_900,
                            'population':'37.5 million',
                            'currency':'UZS'
                            },
            'Russia':{'capital':'Moscow',
                      'area':17_098_246,
                      'population':'144 million',
                      'currency':'RUB'
                            },
            'USA':{'capital':'Washington',
                   'area':9_833_517,
                   'population':'345 million',
                   'currency':'USD'
                   }
            }
question = input('Search: ').title().strip()
for country, info in countries.items():
    if question == country:
        print(f"Capital of {country} is {info['capital']}", end=' and ')
        print(f"its area is {info['area']}", end='. ')
        print(f"Population of {country} is {info['population']}", end=' and ')
        print(f"its currency is {info['currency']}")

if question not in countries.keys():
    print(f"We don't have information about {question}")