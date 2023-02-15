#introduction
print("BOTANICAL")
print("You enter an old, almost abandonded greenhouse through its Northern entrance, but as soon as you step in, you pass out. When you wake up, the door is now blocked by a giant plant. The room you are in is covered in moss, and on the center of the floor is a small beetle.")
#super cool little beetle dude
beeta = ("")
while beeta != "Yes":
	beeta = input("Will you talk to the beetle?\n")
	if beeta == "Yes":
		print("Beetle?: Hello? Who are you?")
		name = input("What's your name?\n")
		print(f"{name}: I'm {name}.")
		print("Beetle?: Yikes, that's a weird name. Well I'm Hercules, cool right?")
		print("Hercules: Anyways, have you seen that giant plant at the door? She won't move and she just so happens to be stealing all of the pollinators! It's annoying!")
		choose1 = input("Yes or No:\n")
		if choose1 == "No":
			print("Hercules: Huh, that's weird, she's hard to miss.")
		elif choose1 == "Yes":
			print("Hercules: Scary, right?! ")
		print("Hercules: Wait... I had an idea! Maybe you can help us! If you go into the 3 other rooms, maybe you can find something to stop her. Ask the mist!")
#talk to the mist
		mistchoice = ("")
		while mistchoice != "Yes":
			mistchoice = input("Will you speak to the mist? Yes or No:\n")
			if mistchoice == "Yes":
				print(f"{name}: Um... hi mist...")
#movement
move = ("")
E = 0
S = 0
W = 0
while move != "q":
	move = input("Mist: Where would you like to move? Your options are E, S, or W. Enter q to leave.\n")
#East, South, and West options
	if move == "E":
		print("You have moved East.")
		E = E+1
#The Flower Room
		if E == 4:
			print("Mist: You have entered the Flower Room.")
#The Orchid
			choose2 = input("Will you walk forward? Yes or No:\n")
			if choose2 == "Yes":
				print("Orchid?: *Growwwllll*")
				print(f"{name}: Hello? Are you ok?")
				print("The orchid shakes its sad, droopy head.")
			break
	elif move == "S":
		print("You have moved South.")
		S = S+1
#The Fern Room
		if S == 2:
			print("Mist: You have entered the Fern Room.")
			break
	elif move == "W":
		print("You have moved West.")
		W = W+1
#The Conifer Room
		if W == 1:
			print("Mist: You have entered the Conifer Room.")
			break
	elif move == "q":
		print("Goodbye!")
	else:
		print("Sorry, that's not a place you can move to!")