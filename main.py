#introduction
import savenload
import pickle
from flower import orchid
from fern import ferny
from conifer import pine
print("BOTANICAL")
print("You enter an old, almost abandonded greenhouse through its Northern entrance, but as soon as you step in, you pass out. When you wake up, the door is now blocked by a giant plant. The room you are in is covered in moss, and on the center of the floor is a small beetle.")
#super cool little beetle dude
beeta = ("")
while beeta not in ("Yes", "Y", "y", "yes"):
	beeta = input("Will you talk to the beetle?\n")
	if beeta in ("Yes", "Y", "y", "yes"):
		print("Beetle?: Hello? Who are you?")
		name = input("What's your name?\n")
		print(f"{name}: I'm {name}.")
		print("Beetle?: Yikes, that's a weird name. Well I'm Hercules, cool right?")
		print("Hercules: Anyways, have you seen that giant plant at the door? She won't move and she just so happens to be blocking the sunlight! It's annoying!")
		choose1 = input("Yes or No:\n")
		if choose1 in ("No", "N", "no", "n"):
			print("Hercules: Huh, that's weird, she's hard to miss.")
		elif choose1 in ("Yes", "Y", "y", "yes"):
			print("Hercules: Scary, right?! ")
		print("Hercules: Wait... I had an idea! Maybe you can help us! If you go look around, maybe you can find something to stop her. Ask the mist!")
#talk to the mist
def save():
	with open("savenload", "wb") as f:
		pickle.dump(orchid, f)
		pickle.dump(ferny, f)
		pickle.dump(pine, f)
		print("Your game has been saved!")
def load():
	global orchid
	global ferny
	global pine
	try:
		with open("savenload", "rb") as f:
			orchid = pickle.load(f)
			ferny = pickle.load(f)
			pine = pickle.load(f)
			print("Your game has been loaded!")
	except FileNotFoundError:
		print("This game file was not found!")
mistchoice = ("")
while mistchoice not in ("Yes", "Y", "y", "yes"):
	mistchoice = input("Will you speak to the mist? Yes or No:\n")
	if mistchoice in ("Yes", "Y", "y", "yes"):
		print(f"{name}: Um... hey...?")
#movement
finalflower = 0
completion1 = 0
completion2 = 0
completion3 = 0
move = ("")
E = 0
S = 0
W = 0
while move != "q" and finalflower != 3:
	move = input("Mist: Where would you like to move? Your options are E, S, or W. Enter q to leave. You may also save or load using s or l.\n")
#East, South, and West options
	if move == "E":
		print("You have moved East.")
		E = E+1
#The Flower Room
		if E == 4 and if completion1 == 0:
			print("Mist: You have entered the Flower Room.")
#The Orchid
			choose2 = input("Will you walk forward? Yes or No:\n")
			if choose2 in ("Yes", "Y", "y", "yes"):
				orchid.talk()
				orchid.get_item()
				orchid.use_item()
				finalflower = finalflower+1
				continue
			elif choose2 in ("No", "N", "no", "n"):
				turn1 = input(f"Would you like to turn back? Yes or No:\n")
				if turn1 in ("No", "N", "no", "n"):
					continue
	elif move == "S":
		print("You have moved South.")
		S = S+1
#The Fern Room
		if S == 2 and if completion2 == 0:
			print("Mist: You have entered the Fern Room.")
#The Fern
			choose3 = input("Will you walk forward? Yes or No:\n")
			if choose3 in ("Yes", "Y", "y", "yes"):
				ferny.talk()
				ferny.get_item()
				ferny.use_item()
				finalflower = finalflower+1
				continue
			elif choose3 in ("No", "N", "no", "n"):
				turn2 = input(f"Would you like to turn back? Yes or No:\n")
				if turn2 in ("No", "N", "no", "n"):
					continue
	elif move == "W":
		print("You have moved West.")
		W = W+1
#The Conifer Room
		if W == 1 and if completion3 == 0:
			print("Mist: You have entered the Conifer Room.")
#The Pine Tree
			choose4 = input("Will you walk forward? Yes or No:\n")
			if choose4 in ("Yes", "Y", "y", "yes"):
				pine.talk()
				pine.get_item()
				pine.use_item()
				finalflower = finalflower+1
				continue
			elif choose4 in ("No", "N", "no", "n"):
				turn3 = input(f"Would you like to turn back? Yes or No:\n")
				if turn3 in ("No", "N", "no", "n"):
					continue
	elif move == "q":
		print("Goodbye!")
	elif move == "s":
		save()
	elif move == "l":
		load()
	else:
		print("Sorry, that's not a place you can move to!")
if finalflower == 3:
	print("You walk out into the main area of the greenhouse, and Hercules is nowhere to be found. The large plant stands menacingly in front of the door, its jaws open wide.")
	finalchoice = ("")
	while finalchoice not in ("Yes", "Y", "y", "yes"):
		finalchoice = input("Are you ready to confront the plant? Yes or No:\n")
		if finalchoice in ("Yes", "Y", "y", "yes"):
			print("You walk up to the plant, trying to look as friendly as possible. One of its many mouths reaches out and snaps at you.\n")
			print(f"{name}: Hey, do you mind moving...?")
