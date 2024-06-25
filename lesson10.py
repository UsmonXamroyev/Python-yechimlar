# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:50:15 2024

@author: unkown
"""


"""
 1.  Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
     ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
     GM uchun ikkala harfni katta qiling.
"""

# cars = ['toyota', 'mayazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#        print(car.upper())
#     else:
#         print(car.title())


"""
2.    Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. """


# cars = ['toyota', 'mayazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())



"""
3.   Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. 
Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, 
{foydalanuvchi_ismi}!
"  matnini konsolga chiqaring.
"""

# ism = input(f"Assalomu aleykum, Iltimos loginni kirirting>>>")
# if ism.lower() == 'admin':
#     print("""Xush kelibsiz, Admin. 
# Foydalanuvchi ro'yhatini ko'rasizmi?""")
# else:
#     print(f"Xush kelibsiz, {ism.title()}")



"""
4.  Foydalanuvchidan 2 ta son kiritishni so'rang. 
    Agar ikki son bir-biriga teng bo'lsa,
    "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
"""
# a = float(input(f"1-sonni kiriting\n>>>"))
# b = float(input(f"2-sonni kiriting\n>>>"))
# if a == b :
#     print("sonlar teng")


"""
Foydalanuvchidan istalgan son kiritishni so'rang. 
Agar son manfiy bo'lsa konsolga "Manfiy son",
 agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
"""
# a = float(input(f"Istalgan sonni kiriting>>>"))
# if a < 0:
#     print("siz kiritgan son manfiy")
# elif a == 0:
#     print("siz kiritgan son na musbat na manfiy")
# else:
#     print("musbat son ekan")
 
    
""" Foydalanuvchidan son kiritishni so'rang, 
 agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
 Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
""" 
# a = float(input(f"Musbat son kiriting\n>>>"))
# if a > 0:
#     print(f"sonning ildizi {(a)**(1/2)}")
# else:
#     print("Siz kiritgan son musbat emas,Iltimos musbat son kiriting")


