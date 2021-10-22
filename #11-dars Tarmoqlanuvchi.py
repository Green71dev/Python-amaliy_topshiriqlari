# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:37:44 2021
#11-dars Tarmoqlanuvchi(and va or)
"""

# son = int(input("Juft son kiriting: "))
# if son%2 == 0:
#     print("Raxmat!!!")
# else: print("Bu son juft emas.")

# age = int(input("Yoshengiz nechida? >>>>"))
# if age>=4 and age <18 :
#     narx = 10000
# elif age>=18 and age <60:
#     narx = 20000
# else: narx = 0      
# print(f"Chipta narxi {narx} so'm ")

# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# if son1 > son2:
#     char = ">"
# elif son1 < son2:
#     char = "<"
# else: char = "="
# print(son1,char,son2)

# mahsulotlar = ["olma","uzum","anor","tarvuz","qovun","shaftoli","kiwi","nok","olxo'ri","qulupnay"]
# savat = []
# for n in range(5):
#     mahsulot = input(f"Savatga {n+1} - mahsulotni qo'shing: ")
#     savat.append(mahsulot)
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#             print(f"Do'konimizda {mahsulot} yo'q")
        
# mahsulotlar = ["olma","uzum","anor","tarvuz","qovun","shaftoli","kiwi","nok","olxo'ri","qulupnay"]
# savat = []
# for n in range(5):
#     mahsulot = input(f"Savatga {n+1} - mahsulotni qo'shing: ")
#     savat.append(mahsulot)
# print("Do'konimizda quyidagi mahsulotlar yo'q")
# for mahsulot in savat:
#     if mahsulot not in mahsulotlar:
#         print(mahsulot)
       
# foydalanuvchilar = ["umar","xasan","xusan","akbar","oybek"]
# newfoydalanuvchi = input("Yangi login tanlang:")
# if newfoydalanuvchi in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else: print("Xush kelibsiz!")

buluvchilar = [2, 3, 4, 5, 6, 7, 8, 9, 10]
son = int(input("Istalgan butun son kiriting:"))
for buluvchi in buluvchilar:
    if son % buluvchi == 0:
        print(f"{son} soni {buluvchi} ga qoldiqsiz bo'linadi")
        

