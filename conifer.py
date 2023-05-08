class Conifer():
    def __init__(self):
        self.room_items = ["pinecone"]
        self.usable_items = {"pinecone"}
        self.inventory = []
    def talk(self):
        print(f"Pine Tree?: ....hi\nYou give a thumbs up, almost as to ask if it's ok.\nPine Tree?: Just lonely is all.")
    def get_item(self):
        ferchoi = input("This room is not like the rest, it is almost completely empty besides the lone tree. Not far from it though, lays a stray pinecone. Would you like to pick it up?\n")
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
        fernchoic = input("Would you like to use something from your inventory to help give the tree some company?\n")
        if fernchoic in ("Yes", "Y", "y", "yes"):
            if self.inventory:
                print(f"Your inventory:\n{self.inventory}")
                pick = input("What item would you like to 'use'? ").lower()
                if pick in self.usable_items:
                    print("You used the", pick)
                    self.inventory.remove(pick)
                    self.usable_items.remove(pick)
                    print("The pinecone snuggles up close to the pine tree, and you see them embrace each other. The pine tree is now willing to help with the final plant.")
                else:
                    print(f"You don't have {pick} in your inventory.")
            else:
                print("You don't have anything in your inventory to 'use'!")
pine = Conifer()