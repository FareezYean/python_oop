from colorama import init, Fore, Back, Style
from mage import Mage
from warrior import Warrior
from assasin import Assasin
from monster import Monster

# reset warna di terminal
init(autoreset=True)

# fore = foreground (text)
# back = background (warna belakang)
# style = gaya (miring, tebal)
print(Fore.WHITE + Back.RED + f'== SUMMON SEMUA HERO ==')
alucard = Warrior("Alucard", 80, 100, 100)
alok = Mage("Alok", 85, 100, 100)
hayabusa = Assasin("Hayabusa", 83, 100, 100)

print('\n== SUMMON MONSTER ==')
salamander = Monster("Salamander", 100, 1000, 1000)

print('== MULAI GUILD PARTY ==')
guild_party = [
    alucard,
    alok,
    hayabusa
]
print(f"Komandan: 'Pasukan siap!'")
print(f"Total {len(guild_party)} pahlawan")

print("\n⚔️ --- RAID DIMULAI --- ⚔️\n")
# alucard.critical(salamander)
# alok.critical(salamander)
# alok.cast_spell(salamander)

# pasang cheat hp +1000
# alucard.name = "Bambang"
# ambil hp doang
# print(f"HP alucard: {alucard.get_hp()}")
# alucard.set_hp(100)

# print(alucard)
# print(alok)
# print(layla)
# print(hayabusa)

alucard.hp = 240
hayabusa.hp = 140
print(f"HP Alucard : {alucard.hp}")
print(f"HP Hayabusa : {hayabusa.hp}\n")

running = True
while running:
    print(salamander)
    print("1. Attack, 2. Heal, 3. Exit")  
    try:   
        aksi = int(input(">> Pilih Aksi :"))
    except ValueError:
        print("Input tidak valid. Masukkan angka 1-3.")
    if aksi == 1:
        dmg = 10
        for party in guild_party:
            party.attack(salamander)
            salamander.damaged(dmg)

        # cek jika hp 0 = akhir permainan
        if (salamander.hp == 0):
            print("Monster sudah mati!")
            running = False
    elif aksi == 2:
        alok.heal(10)
        # boleh yg lain heal jg ntar
        # ...
    elif aksi == 3:
        print("Game Berakhir, Bye bye!")
        running = False
    else:
        print("Input tidak valid. Masukkan angka 1-3.")



