class Preist():
    def __init__(self, name, personality, level = 1):
        self.name = name
        self.personality = personality
        self.level = level
        self.movementSpeed = 2.8
        self.health = 7
        self.mana = 25
        self.attackPower = 2
        self.defence = 3
        self.healing = 12
        self.perception = 20

    def healing_hands(self, target):
        if self.mana >= 4:
            self.mana -= 4
            print(f'{self.name} has healed {target.name}')
            
            target.health += self.healing
            
            print(f'{target.name} health is now {target.health}')

    def prayer(self, target, target2 = None):
        if self.mana >= 2:
                self.mana -= 2
            
                print(f'{self.name} has boosted {target.name}')
            
                target.attackPower += 7
                target.defence += 7
            
                print(f'{target.name} attack has been boosted to {target.attackPower}')
                print(f'{target.name} deffence has been boosted to {target.defence}')

                if target2:
                    print(f'{self.name} has boosted {target2.name}')
                    
                    target2.attackPower += 7
                    target2.defence += 7
                    
                    print(f'{target2.name} attack has been boosted to {target2.attackPower}')
                    print(f'{target2.name} deffence has been boosted to {target2.defence}')

    @staticmethod
    def sayNo(name):
        print(f'Kindly go choke on a bag of dicks {name}')

    @classmethod
    def short(cls, name, personality):
        print(f'Because {name} is short, her stats have been altered')
        return cls(name, 'Fiesty')

class Warrior():
    def __init__(self, name, personality, level = 1):
        self.name = name
        self.personality = personality
        self.level = level
        self.movementSpeed = 4
        self.health = 19
        self.mana = 9
        self.attackPower = 13
        self.defence = 8
        self.perception = 4
        

    def bash(self, target):
        if self.mana >= 3:
            self.mana -= 3

            print(f'{self.name} uses bash on {target.name}')
            
            target.health -= (self.attackPower * 1.5 - target.defence)
            
            print(f'{target.name} health has been reduced to {target.health}')

    @staticmethod
    def sayNo(name):
        print(f'Kindly go choke on a bag of dicks {name}')


        

class Theif():
    def __init__(self, name, personality, level = 7):
        self.name = name
        self.personality = personality
        self.level = level
        self.movementSpeed = 6
        self.health = 30
        self.mana = 75
        self.attackPower = 9
        self.defence = 12
        self.stealth = 24

    def butt_pinch(self, target):
        if self.mana >= 7:
            self.mana -= 7
            print(f'{self.name} has pinched {target.name}\'s booty cheeks')
            target.health -= self.stealth - target.perception

            if target.personality == 'Butt enthusiast':
                print(f'Because {target.name} is a butt enthusiast, he blushes and gains back 5 health')
                target.health += 5
            
            print(f'{target.name} health is now {target.health}')
    
    @staticmethod
    def sayNo(name):
        print(f'Kindly go choke on a bag of dicks {name}')




Brett = Warrior('Brett', 'Butt enthusiast')
Rob = Warrior('Rob', 'Happy')
Theif = Theif('Theif', 'Angry')
Cheryl = Preist.short('Cheryl', 'Shy')


Brett.bash(Theif)
Theif.butt_pinch(Rob)

print(Cheryl.personality)

#Cheryl.healing_hands(Rob)
#Cheryl.prayer(Brett)
#Brett.bash(Theif)
