from character import hero
from assasin   import assasin
from fighter   import fighter
from mage      import mage

cecilion   = mage    ("Cecilion", 1000, "mage", "hero")
dyrroth    = fighter ("Dyrroth", 1200, "fighter", "hero")
martis     = assasin ("Martis", 1500, "assasin", "hero")
slime      = hero    ("Slime", 2000, "slime", "normal")
lord       = hero    ("Lord", 3000, "lord", "boss")

print("================================================")
print("--- BATTLE 1 ---")
print("Dungeon Level 1 : Slime Area")

print("Slime : Gloop gloop!")
print("Martis : Semuanya, bersiaplah!")

cecilion.basic_attack(slime)
dyrroth.basic_attack(slime)
martis.basic_attack(slime)
slime.damaged(300)

slime.basic_attack(cecilion)
slime.basic_attack(dyrroth)
slime.basic_attack(martis)
cecilion.damaged(150)
dyrroth.damaged(150)
martis.damaged(150)

print(slime)
print(cecilion)
print(dyrroth)
print(martis)

print("Martis : Akan sulit jika kita menyerang seperti ini terus!.")
print("Dyrroth : Akan kubunuh!")

dyrroth.skill_1(slime)
dyrroth.skill_2(slime)
dyrroth.ultimate(slime)
dyrroth.skill_1(slime)
dyrroth.skill_2(slime)
dyrroth.basic_attack(slime)
slime.damaged(100)
print(slime)

print("Slime : Gloop... gloop...")
print("Martis : Dyrroth, Jangan lakukan hal itu lagi!")
print("Dyrroth : HAH!, aku sudah mengalahkannya bukan ?!")
print("Martis : Kau terlalu boros tenaga diawal")
print("Martis : Musuh kita adalah Lord, bukan Slime!")
print("Cecilion : Sudahlah, Ayo kita lanjutkan perjalanan kita.")
print("==========================================================")

print("--- BATTLE 2 ---")
print("Dungeon Level 2 : Lord Area")
print("Lord : Selamat datang di Kerajaanku!")
print("Lord : Banyak yang sudah berusaha mengalahkanku, tapi semuanya gagal!")
print("Dyrroth : Kami hanya perlu bukti nyatanya!")

cecilion.skill_1(lord)
dyrroth.skill_1(lord)
martis.skill_1(lord)
print(lord)

print("Lord : Hahaha! Kalian Kira itu cukup?")
print("Lord : ( Memegang pedang besarnya dan menghilang sekejap )")

lord.basic_attack(cecilion)
lord.basic_attack(dyrroth)
lord.basic_attack(martis)
cecilion.damaged(300)
dyrroth.damaged(300)
martis.damaged(300)
print(cecilion)
print(dyrroth)
print(martis)

print("Dyrroth : Tcih, Cepet bet!")
print("Lord : Hahaha, Kalianlah yang terlalu lambat!")
print("Martis : Kita serang bersamaan!")
print("Cecilion, Martis : Setuju!")

cecilion.ultimate(lord)
martis.skill_1(lord)
cecilion.skill_1(lord)
dyrroth.ultimate(lord)
print(lord)

print("Lord : Tidak mungkin! Aku kalah!")

cecilion.skill_2(lord)
martis.skill_1(lord)
dyrroth.skill_2(lord)
print(lord)

print("Lord : Arghhh!!!")
print("Lord : Aku Kalah... Kalian memang layak menjadi pemenang...")
print("Dyrroth : Hahaha, Lihatlah siapa yang mengalahkanmu!")

print("============================================================")







