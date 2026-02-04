from character import hero

class mage(hero): 

    def __init__(self, name, hp, role ="mage", type="hero"):
        super().__init__(name, hp, role="mage", type=type)

    def skill_1(self, target):
        dmg = 200
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Bat Impact skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def skill_2(self, target):
        dmg = 250
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Sanguine Claws skill!")
        self.attack(target, dmg)
        target.damaged(dmg)

    def ultimate(self, target):
        dmg = 400
        print(f"🔥{target.name} takes {dmg} from {self.name}'s Bat's Feast Ultimate skill!")
        self.attack(target, dmg)
        target.damaged(dmg)