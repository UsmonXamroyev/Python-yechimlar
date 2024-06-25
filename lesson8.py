# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 05:04:10 2024

@author: unkown
"""


    #   """  .sort() metodi ro'yhatni alifbo tartibida tartiblaydi  """   
        
        
#cars = ["malibu", "nexia", "cobalt", 'nexia3', 'Tracer', 'tico', 'matiz', "captiva", "lacetti"]
#cars.sort()
#print(cars)


      # """   Ro'yhatni teskari tartibda tartiblash uchun  reverse=True argumenti beriladi """
        

#cars = ["malibu", "nexia", "cobalt", 'nexia3', 'Tracer', 'tico', 'matiz', "captiva", "lacetti"]
#cars.sort(reverse=True)
#print(cars)


# """   .sort() metodi ro'yhadni tartiblaydi ammo asl ro'yhat ham o'zgaraddi     """   
        
 # """ sorted() funksiyasi esa asl ro'yhatga teginmagan holatda tartiblaydi  """
        
        
#cars = ["malibu", "nexia", "cobalt", 'nexia3', 'Tracer', 'tico', 'matiz', "captiva", "lacetti"]
#print(sorted(cars))
#print(cars)



#""" Ro'yhatni teskarisiga aylantirish uchun .reverse() metodidan foydalanib aylantiramiz """


#cars = ["malibu", "nexia", "cobalt", 'nexia3', 'Tracer', 'tico', 'matiz', "captiva", "lacetti"]
#cars.reverse()
#print(cars)



#"""   Ro'yhatni uzunligini ichidagi elementlari sonini aniqlash uchun len() funksiyasidan foydaanamiz """
        
#cars = ["malibu", "nexia", "cobalt", 'nexia3', 'Tracer', 'tico', 'matiz', "captiva", "lacetti"]
#print(len(cars))




# range() funksiyasi yordamida biz malum bir oraliqdagi sonlar keetma ketligini yaratishimiz mumkin
# list() funksiyasi orqali bu oraliqni jadval ko'rinishiga o'tkazamiz

#sonlar = list(range(0,10))
#print(sonlar)

#  Misol. foydalanuvchi kiritgan sonni oraliqni teng ikkiga bo'lib 1-yarmini teskari tartibda 
#  qolganini o'z holicha ko'rsatuvchi dastur tuzing


   
#i = int(input("sizga kerakli ro'yhatning quyi chegarasini kiriting\n"))
#j = int(input("sizga kerakli ro'yhatning yuqori chegarasini kiriting\n"))
#a = int((j+i)/2)
#b_yarmi = list(range(i,a+1))
#i_yarmi = list(range(a+1,j+1))

#b_yarmi.reverse()
#print('',b_yarmi,'\n\n',i_yarmi)

#sonlar = list(range(0,853,8))
#print(sonlar)


#   min() , max() hamda sum funksiyalari orqali biz eng kichik va eng katta elementlarni topishimiz mumkin

#sonlar = [3,10,15,1,0,100,20,40,30,23]
#print(min(sonlar))
#print(max(sonlar))
#print(sum(sonlar))

#countries = ['indoneziya', 'koreya', 'xitoy','rossiya', 'mongoliya', 'niderlandiya','shvetsariya','Afrika','albaniya','goolandiya','yaponiya']
#print("ro'yhat uzunligi ",len(countries))
#print('\n',sorted(countries),'\n')
#print(sorted(countries,reverse=True),'\n')
#print('\n',countries,'\n')
#countries.reverse()

#countries.sort(reverse=True)
#print(countries)

# j_sonlar = list(range(120,1202,2))     # juft sonlarni chiaradi
#print(sum(j_sonlar))
#print(max(j_sonlar)-min(j_sonlar))
#print(len(j_sonlar

# taomlar  = ['sho\'rva','sabzavot',"osh",'kabob','qaynatma','yalama']

# nonushta = taomlar[:]
# nonushta.append("non")
# nonushta.append("sariyog'")
# del(nonushta[5])
# del(nonushta[0])
# print(taomlar)
# tuple(nonushta)

# print(nonushta)
# nonushta.append('kalbosa')
# nonushta[0] = 'qaymoq va non'