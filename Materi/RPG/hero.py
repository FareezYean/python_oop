# import ini untuk typehint bisa bekerja
from __future__ import annotations
from monster import Monster

class Hero:
    # self = dirinya sendiri / internal
    # __init__ = dipanggil pertama kali
    def __init__(self, name: str, level: int, hp: int, mana: int, role: str):
        # __namaAttr = maksudnya private attribute
        self.name = name
        self.level = level
        self.__hp = hp
        self.mana = mana
        self.role = role
        print(f"✨ Hero [{self.role}] {self.name} telah di-summon!")

    # mengganti print objek dari bentuk memori 0x100..
    # menjadi format string, biar lebih enak dibaca
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.__hp == 0:
            status = "💀 MATI"
            
        return f"[{self.role}] {self.name} | HP: {self.__hp} | STATUS: {status}"

    def damaged(self, damage: int):
        self.__hp -= damage
        # \n artinya newline = baris baru
        print(f"💥 {self.name} terkena {damage} damage!\n")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi!\n")
    
    def attack(self, enemy: Monster):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount: int):
        self.__hp += amount
        print(f"💊 {self.name} mendapat heal +{amount}!\n")
        
    def critical(self, target: Monster):        
        print(f"👹 {self.name} menggunakan skill 0 DMG!")

    # getter: mengambil attribute yg private dari luar class
    #def get_hp(self):
        #return self.__hp
    
    # setter: memperbarui attribute yg private dari luar class
    #def set_hp(self, add_hp):
        # tambahan validasi jgn smpe lewat max 100 hp
        #self.__hp += add_hp

    # @property = setter & getter modern
    @property
    def hp(self):
        return self.__hp
    
    # setter @namaProperty, setter
    @hp.setter
    def hp(self, value):
        if value < 0: # validasi hp minus
            value = 0

        self.__hp = value