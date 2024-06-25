# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 04:09:18 2024

@author: unkown
"""

# names = ['Akrom', 'Humoyun', 'Azizbek', 'Fazliddin', 'Abdulaziz']
# for name in names:
#     print(f"Assalomu aleykum {name} sizni bugungi to'y bazmiga taklif qilaman")
# print(f"Kod {len(names)} marta takrorlandi ")


# numbers = list(range(11,100,2))
# for number in numbers:
#     print(f"{number} ning kubi {number**3}")



# films =[]
# print("Iltimos eng sevimli 5 ta kinolaringizni kiriting \n...")
# for n in range (5):
#     films.append(input(f"{n+1}-sevimli kinoingizni kiriting \n..."))

# print(films)



m = int(input("bugun nechta odam bilan suhbat qildinggiz >>>"))
humans = []
for n in range(m)    :
    humans.append(input(f"{n+1}-odam kim edi"))
print(humans)