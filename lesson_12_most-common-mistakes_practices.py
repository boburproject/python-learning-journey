# Lesson 12 - most common mistakes 
# Date: 2026-06-30


#### Exercise 1
# Corrected version                         
son = float(input("Juft son kiriting: ")) 
if son % 2:                               
     print("Bu son juft emas.")            
else:                                     
    print("Rahmat!")  


# First given version
# son = float(input("Juft son kiriting: ")
# if son % 2 == 0:           
# print("Bu son juft emas.') 
# else:
#     print("Rahmat!")) 



#### Exercise 2
# Corrected version                             
yosh = int(input("Yoshingiz nechida?  "))
if yosh<=4 or yosh>=60:                  
    narh = 0                             
elif yosh < 18:                          
    narh = 10000                         
else:                                    
    narh = 20000                         
print(f"Chipta narhi {narh} so'm")       


# First given version
# yosh = (input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")



#### Exercise 3
# Corrected version                               
x = float(input("Birinchi sonni kiriting: "))   
y = float(input("Ikkinchi sonni kiriting: "))   
if x==y:                                        
    print(f"{x}={y}")                           
elif x<y:                                       
    print(f"{x}<{y}")                           
else:                                           
    print(f"{x}>{y}")                           


# First given version
# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}")
# else
#     print(f"{x}>{y}")



#### Exercise 4
# Corrected version                                                   
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',             
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']       
savat = []                                                          
for n in range(5):                                                  
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))     
if savat:                                                           
    for mahsulot in savat:                                          
        if mahsulot in mahsulotlar:                                 
            print(f"Do'konimizda {mahsulot} bor")                   
        else:                                                       
            print(f"Do'konimizda {mahsulot} yo'q")                  
else:                                                                
    print("Savatingiz bo'sh")                                       


# First given version
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'


# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            



#### Exercise 5
# Corrected version                                                                     
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',                          
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']                     

savat = []                                                                        
for n in range(5):                                                                
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower().strip())   

bor_mahsulotlar = []                                                              
mavjud_emas = []                                                                  
for mahsulot in savat:                                                            
    if mahsulot in mahsulotlar:                                                   
        bor_mahsulotlar.append(mahsulot)                                          
    else:                                                                         
        mavjud_emas.append(mahsulot)                                              

if mavjud_emas:                                                                   
    print("Do'konimizda quyidagi mahsulotlar yo'q: ")                             
    for mahsulot in mavjud_emas:                                                  
        print(mahsulot)                                                           
else:                                                                             
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")                     


# First given version
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")



#### Exercise 6
# Corrected version                                         
users = ['alisher1983', 'aziza', 'yasina', 'umar']        
login = input("Yangi login tanlang:").lower().strip()     

if login in users:                                        
    print('Login band, yangi login tanalng!')             
else:                                                     
    print("Xush kelibsiz!")                               


# First given version
# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang:' )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")