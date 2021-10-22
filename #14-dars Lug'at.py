# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:30:15 2021
#14-dars lug'at '
"""

# otam = {"ismi" : "Alisher", "yoshi" : 43, "muchali" : "ot"}
# onam = {"ismi" : "Dilfuza", "yoshi" : 41, "muchali" : "maymun"}
# akam = {"ismi" : "Javlon", "yoshi" : 21, "muchali" : "baliq"}
# print(f"Otamning ismi {otam['ismi']}, yoshi {otam['yoshi']} da, muchali {otam['muchali']}")
# print(f"Onamning ismi {onam['ismi']}, yoshi {onam['yoshi']} da, muchali {onam['muchali']}")
# print(f"Akamning ismi {akam['ismi']}, yoshi {akam['yoshi']} da, muchali {akam['muchali']}")

# oila = {"dadam" : "manti", "ayam" : "osh", "akam" : "sirgruch", "husan" : "shashlik", "mening" : "somsa"}
# print(f"Dadamning sivimli ta'omi {oila['dadam']} \nAyamning sivimli ta'omi {oila['ayam']} \nAkamning sivimli ta'omi {oila['akam']}")

lugat = {
    "integer":"butun",
    "float":"haqqiy",
    "string":"satr",
    "if":"shart",
    "else":"agar",
    "for":"uchun",
    "titil":"bosh harf", 
    "char":"belgi", 
    "print":"chiqarish",
    "input":"kiritish",
    "list":"Ro'yxat"  }
# print(lugat)

# soz = lugat.get(input("So'z kiriting: "),"Bunday so'z mavjud emas")
# print(soz)
soz = input("Kalit so'z kiriting: "),
if  soz in lugat:
    print(lugat["soz"])
else: print("Bunday so'z mavjut emas")



