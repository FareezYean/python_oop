class Monster:
    def __init__(self, name: str, level: int, hp: int, mana: int):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        print(f"✨ Monster {self.name} telah di-summon!")

    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI"
            
        return f"[Monster] {self.name} | HP: {self.hp} | STATUS: {status}"

    def damaged(self, damage: int) -> bool:
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi!\n")
            return False
        return True
    
    # tipe data saat return kasih -> typedata
    def is_alive(self) -> int:
        if self.hp > 0:
            return 1
        return 0
