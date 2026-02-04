class hero:
    def __init__(self, name, hp, role, type):
        self.name = name
        self.hp = hp
        self.role = role
        self.type = type

        if type == "hero":
            self.max_hp = 1500
            print(f"[{self.role}] | {self.name} joinned the game!")

        elif type == "boss":
            self.max_hp = 3000
            print(f"Monster type : [{self.type}] | {self.name}'s has appeared!")

        elif type == "normal":
            self.max_hp = 2000
            print(f"Monster type : [{self.type}] | {self.name}'s has appeared!")

        else:
            raise ValueError("Type unknown!")

    def __str__(self):
        status = "🟢Life"
        if self.type == "boss" and self.hp <= self.max_hp / 2:
            dmg = +100
            status = "Rage Mode🩸"
            return f"[{self.name}] | HP: {self.hp} | Status:{status}"
    
        if self.hp == 0:
            status = "💀Death"
            return f"[{self.name}] has died and cannot attack again"
        return f"[{self.name}] | HP: {self.hp} | Status:{status}"
    
    def basic_attack(self, enemy, dmg=None):
        if dmg is None:
            if self.type == "hero":
                dmg = 100
            elif self.type == "boss":
                dmg = 300
            elif self.type == "normal":
                dmg = 150
            else:
                dmg = 0
        print(f"⚔️{self.name} attack the {enemy.name} with {dmg} damage!")

    def attack(self, enemy, dmg=None):
        self.basic_attack(enemy, dmg)

    def damaged(self, damage):
        self.hp -= damage
        print(f"💥{self.name} take {damage} damage!.")
        if self.hp <= 0:
            print(f"❌{self.name} already died.")
