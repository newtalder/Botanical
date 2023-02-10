name = input("What's your name?\n")
#introduction
print("You enter a greenhouse through the Northern door, but as soon as you step in you fall asleep. When you wake up, the door is now blocked by a giant, unrecognizable plant. The room you are in is covered in moss, and on the center of the floor is a small beetle.")
#super cool little beetle dude
beeta = ("")
while beeta != "Yes":
	beeta = input("Will you talk to the beetle?\n")
	if beeta == "yes":
		print("Beetle?: Hello? Who are you?")
		print(f"You: I'm {name}.")
		print("Beetle?: Yikes, that's a weird name. Well I'm Hercules, cool right?")
		print("Hercules: Anyways, have you seen that giant plant at the door? She won't move and she just so happens to be stealing all of the pollinators! Can you believe that?")
#movement
move = ("")
while move != "q":
	move = input("Where would you like to move? Your options are E, S, or W. Enter q to leave.\n")
	if move == "E":
		print("You have moved East.")
	elif move == "S":
		print("You have moved South.")
	elif move == "W":
		print("You have moved West.")
	elif move == "q":
		print("Goodbye!")
	else:
		print("Sorry, that's not a place you can move to!")