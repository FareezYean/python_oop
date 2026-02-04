from character import hero

class fighter(hero): 

    def __init__(self, name, hp, role ="fighter", type="hero"):
        super().__init__(name, hp, role="fighter", type=type)

    def skill_1(self, target):
        dmg = 250
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Burst Strike skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def skill_2(self, target):
        dmg = 300
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Spectre Step skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def ultimate(self, target):
        dmg = 500
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Abysm Strike Ultimate skill!")
        self.attack(target, dmg)
        target.damaged(dmg)