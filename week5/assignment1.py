#base class for all the superheroes
class Superhero:
    def __init__(self, name, superpower, costume) -> None:
        self.name = name
        self.superpower = superpower
        self.costume = costume
        
    def use_power(self): # general method for all superheroes
        print(f'{self.name} uses {self.superpower}!')
        
class Batman(Superhero): #inherits from the superhero class
    def __init__(self, name, superpower, costume, gadget) -> None: # adds a gadget attribute specific to batman
        super().__init__(name,superpower,costume)
        self.gadget = gadget
        
    def use_gadget(self): # method for using the gadget
        print(f'{self.name} uses {self.gadget}!')
        
class IronMan(Superhero): # inherits from the superhero class
    def __init__(self, name, superpower, costume, suit_tech) -> None:# adds a suit_tech attribute specific to iron man
        super().__init__(name, superpower, costume)
        self.suit_tech = suit_tech
        
    def upgrade_suit(self): # method for upgrading the suit
        print(f'{self.name} upgrades {self.suit_tech} before every battle.') 
        
# creating instances of superheroes
dark_knight = Batman('Batman', 'Athletic prowess and detective skills', 'Black suit', 'Bat-mobile')
iron_man = IronMan('Iron Man', 'Technological genius', 'Red metallic suit', 'Iron suit')

#use methods
dark_knight.use_power()
dark_knight.use_gadget()
iron_man.use_power()
iron_man.upgrade_suit()