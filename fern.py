class Fern():
    def __init__(self):
        self.room_items = ["gardening scissors"]
        self.usable_items = {"gardening scissors"}
        self.inventory = []
    def talk(self):
        print("You see a fern that is so full that it sags, it does not turn to look at you. Maybe lighten it's load?")
    def get_item(self):
        ferchoi = input("You are surrounded by overgrown leaves and weeds crawling up the walls, one of the stray vines holds a pair of gardening scissors, would you like to pick it up?\n")
        if ferchoi in ("Yes", "Y", "y", "yes"):
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
        fernchoic = input("Would you like to use something from your inventory to lighten the fern?\n")
        if fernchoic in ("Yes", "Y", "y", "yes"):
            if self.inventory:
                print(f"Your inventory:\n{self.inventory}")
                pick = input("What item would you like to 'use'? ").lower()
                if pick in self.usable_items:
                    print("You used the", pick)
                    self.inventory.remove(pick)
                    self.usable_items.remove(pick)
                    print("The fern feels free and lighter, and wiggles around to show off it's newfound space. The fern is now willing to help with the final plant.")
                else:
                    print(f"You don't have {pick} in your inventory.")
            else:
                print("You don't have anything in your inventory to 'use'!")
ferny = Fern()