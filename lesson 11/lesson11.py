"""              
                 1-masala
Foydalanuvchidan juft son kiritishni so'rang.
 Agar foydalanuvchi juft son kiritsa "Rahmat!", 
 agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""
""" yechim:"""

# son = float(input("Juft son kiriting! >>>"))
# if son % 2 ==0:
#     print("Raxmat")
# else:
#     print("Bu son juft emas")
    
    
    
    
""" 
                   2-masala
Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
quyidagicha chiqaring:

Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm """

# yosh = int(input("Yoshingizni kiriting >>>"))
# if yosh < 4 or yosh > 60:
#     narx = 0
# elif yosh <18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Sizga kirish {narx} so'm")


""" 
                    3-masala
Foydalanuvchidan ikita son kiritishni so'rang, 
sonlarni solishtiring va ularning teng yoki katta/kichikligi 
haqida xabarni chiqaring   """

# print("Ikkita son kiriting")
# son1 = float(input("1-sonni kiriting >>>"))
# son2 = float(input("2-sonni kiriting >>>"))

# if son1 == son2:
#     print(f"{son1}={son2}")
# elif son1 < son2:
#     print(f"{son1}<{son2}")
# else:
#     print(f"{son1}>{son2}")
   
    
    
"""
                    4-masala
mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,
 mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
 "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring."""

# mahsulot = ["olma", "banan", "gilos", "ananas", "nok", "o'rik", "kivi", "olxo'ri", "olcha", "limon", "mandarin" ]
# savat = []

# for n in range(5):
#     m = input(f"Savatga {n+1}-mahsulotni qo'shing:")      # m foydalanuvchi kiritgan mahsulot
#     savat.append(m.lower())

# for n in savat:
#     if n in mahsulot:
#         print(f"\n{n} do'konimizda bor ✅ ")
#     else:
#         print(f"\n{n} do'konimizda yo'q ❌")

"""
            5-masala 
Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
 Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
 do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. 
 Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan 
 xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring. """

# print("Olmoqchi bo'lgan 5 ta mahsulotingizni kiriting")
# mahsulot = ["olma", "banan", "gilos", "ananas", "nok", "o'rik", "kivi", "olxo'ri", "olcha", "limon", "mandarin" ]
# bor_mahsulotlar = []
# mavjud_emas = []

# # for n in range(5):
# #     m = input(f"{n+1}-mahsulotni kiriting:")      # m foydalanuvchi kiritgan mahsulot
# #     if m in mahsulot:
# #         bor_mahsulotlar.append(m.lower())
# #     else:
# #         mavjud_emas.append(m.lower())
        
# # if len(mavjud_emas) == 0:
# #     print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor ")
# # else:
# #     print(f"Quyidagi  mahsulotlar do'konimizda yo'q ekan: {mavjud_emas}")
    
   
"""

               6-masala    
foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan
 loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
 Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda 
 "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
"""

# users = ['usmon', 'nodir', 'aziz',  'elchin', 'farhod','umar']
# login = input("Yangi login kiriting >>>")
# if login in users:
#     print("Login band,yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz {login}!")


"""
                7- masala
                
Foydalanuvchidan biror butun son kiritishni so'rang.
 Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz
 bo'linishini konsolga chiqaring. """
 
# son = input("Biror butun son kiriting >>>")
# if  float(son) != int(float(son)):
#     print("Iltimos butun son kiriting")
          
# else:
#     son = int(son)
#     for n in range(2,11):
#         if son % n ==0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
            
    





















