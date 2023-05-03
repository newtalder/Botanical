class Flower():
    def __init__(self):
        self.room_items = ["watering can"]
        self.inventory = []
    def talk(self):
        print(f"Orchid?: *Growwwllll*\nYou give a thumbs up, almost as to ask if it's ok.\nThe orchid shakes its sad, droopy head.")
    def get_item(self):
        flowchoi = input("You look around the room to see dead flowers of all kinds, all dried up. In the left corner of the room, there lies a watering can, would you like to pick it up?\n")
        if flowchoi in ("Yes", "Y", "y", "yes"):
            pick = input("What item would you like to 'get'?\n").lower()
            if pick in self.room_items:
                print(f"You pickup the {pick}.")
                self.inventory.append(pick)
                self.room_items.remove(pick)
            else:
                print(f"Couldn't find {pick} in room.")
        else:
            print("There's nothing to pickup here!")
    def use_item(self):
        flowechoic = input("Would you like to use something from your inventory to help the orchid?\n")
        if flowechoic in ("Yes", "Y", "y", "yes"):
            print(f"Your inventory:\n{self.inventory}")
            pick = input("What item would you like to 'use'? ").lower()
            if pick in self.inventory:
                print(self.inventory[pick])
                    self.inventory.remove(pick)
                    del self.inventory[pick]
                    self.special(pick)
                else:
                    print(f"You can't use {pick} here.")
            else:
                print(f"You don't have {pick} in your inventory.")
        else:
            print("You don't have anything in your inventory to 'use'!")
orchid = Flower()
