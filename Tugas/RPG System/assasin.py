from character import hero

class assasin(hero): 

    def __init__(self, name, hp, role ="assasin", type="hero"):
        super().__init__(name, hp, role="assasin", type=type)

    def skill_1(self, target):
        dmg = 300
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Ashura Aura skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def skill_2(self, target):
        dmg = 350
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Mortal Coil skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def ultimate(self, target):
        dmg = 550
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Decimation Ultimate skill!")
        self.attack(target, dmg)
        target.damaged(dmg)