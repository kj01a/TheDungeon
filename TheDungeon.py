from sys import exit 

have_gem = False
have_sword = False
		
class Scene(object):
	def enter(self):
		pass
		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		flag = True
		current = self.scene_map.opening_game()
		
		if current == "finish":
			flag = False
			
		while flag:
			print("\n" + "-----" * 5 + "\n")
			
			next_scene_name = current.enter()
			
			if next_scene_name == "finish":
				exit(0)
			else:
				current = self.scene_map.next_scene(next_scene_name)

class TheBeginning(Scene):
	def enter(self):
		print("WELCOME TO THE DUNGEON\n")
		print("-----") * 5
		print("\nWhen you were a child you found an old map in the attic of your father's house, tucked")
		print("away in small chest that hadn't been touched in years. And you didn't think much of it")
		print("at the time. It just seemed like the plans for some old castle. Most of it was faded.")
		print("All except for the dungeon.\n")
		print("It wasn't until, years later, you were in town and overheard some travelling merchants")
		print("talking about the haunted ruins of an ancient castle not far from town. It reminded you")
		print("of that old map. You went dug it out of the attic, found your father's chainmail and")
		print ("sword, and went out to found the old ruins.\n")
		print("There wasn't anything left of the old stone building. Few walls still stood, none of")
		print("them to the height they once did. But after awhile of searching you found at least")
		print("what used to be the enterance to the dungeon.\n")
		print("You peer down into the darkness, smelling the mildew of hundred years, and chill runs")
		print("down your spine. You get goosebumps.")
		print("\nWhat do you do?")
		print("\t1. Enter the dungeon")
		print("\t2. Go back into town for more supplies?")

		choice = raw_input("> ")

		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nYou feel the fear crawl back up your thorat, but you swallow it back down. Your hands")
			print("shake, and you grasp your father's sword and your torch. You ease down onto the first")
			print("step and begin your descent into the dark.")
			return "corridor"
		elif choice == "2":
			print("\n" + "-----" * 5)
			print("\nYou realize you have forgotten some supplies that might be useful, and you decide to")
			print("head back into town. It would not do to dive into an unknown dungeon uprepared. While in")
			print("town see Araella, the girl you've had a crush on for quite some time.")
			print("\nShe smiles when she sees you. She walks over and strikes up a conversation about her")
			print("day and her work in the flower shop. Then she tells you that her and a couple of friends")
			print("are going to spend the day up the mountain, have a picnic and just hangout. She invites")
			print("you to come along, and the dungeon is forgotten for today.")
			print("\nYou hit is off! She's beautiful and funny, and you like her a lot. You're pretty sure")
			print("she feels the same way when she invites you out again tomorrow, just the two of you.")
			print("Everything seems to go naturally from there. You fall in love and get married. You have")
			print("your ups and downs, and few kids along the way. All in all a happy life. Except for the")
			print("nagging feeling you get everytime you look at your father's old map. Every once in")
			print("awhile you think maybe you'll get back down there one day and finally check it out, but")
			print("something always comes up, a sick kid, a trip Araella wants to take. You never make it,")
			print("and die of old age.")
			return "death"
		else:
			print("That is not an option here.")
			return "start"
		
class Death(Scene):
	def enter(self):
		print("You wake up on a dock. The sky above you is a shimmering white and the water sparkles")
		print("blue. There is a single ship in the harbor, and one of it's life boats is rowing")
		print("towards the dock. There is an old man with a grey beard standing on the dock in front")
		print("you. His thick bear skin cloak blows in the saltly smelling breeze.")
		print("\n'Yes', he says. 'Everyone asks the same question first, and the answer is yes.' He")
		print("claps his hand down on your shoulder. 'Did you make all of the desicions you wished")
		print("you had?' He smiles and laughs, 'If it makes you feel any better, almost no one does.'")
		print("\nThe lifeboat has made it to the dock, and the old man says, 'Well, it's time to go")
		print("all the same.' And he ushers you into the boat.")
		print("-----") * 5
		print("\n\t1. Try again?")
		print("\t2. Exit?")
		
		choice = raw_input("> ")
		
		if choice == "1":
			return "start"
		else:
			exit(0)

class CentralCorridor(Scene):
	def enter(self):
		print("When you reach the bottom of the stairs not even the light of your torch penetrates")
		print("the darkness enough to see anything. You check your map, and there are two options in")
		print("before. One you can enter the room immideately ahead of you marked 'Study,' or go")
		print("the corridor towards the prisoner cells.")
		print("\nWhat do you do?")
		print("\t1. Go forward, through the door?")
		print("\t2. Go left, down the hall?")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nYou find it odd that there would there would be a study in a dungeon, and decide to")
			print("check it out. You find your way to the doorway, and it looks like at one time the room")
			print("was magically sealed, but those spells have been blown open. The door is in splinters")
			print("on the floor.")
			print("\nYou enter the room.") 
			return "study"
		elif choice == "2":
			print("\n" + "-----" * 5)
			print("\nYou walk down the corridor. The cells are abandoned, except for the decayed remains")
			print("of the long forgotten residents of the dungeon. The smell is almost overwhelming, but")
			print("you press on.")
			print("\nYou get far enough down the hall that you can no longer see the stairs, and you start")
			print("to hear scratching on the stone in front of you. You stop, and the scratching gets")
			print("closer. And closer. And then you see two beady eyes appear just outside the light of")
			print("your torch. A rat is running toward you, almost like it is targeting you.")
			print("\nYou draw your father's sword, and swing at the rat. You miss. It jumps and sinks its")
			print("teeth into your leg. A burning sensation rips through your leg, you throw your torch to")
			print("the ground, and everything goes black.")
			print("\nYou lie on the ground fading in and out of consciousness as delirium overtakes your")
			print("your mind. Every time you try to move crippling pain rips from your twiching leg.")
			print("Eventually you give up trying to get out, and you die of thirst.")
			return "death"
		else:
			print("That is not an option here")
			return "corridor"
		
class WizardsStudy(Scene):
	def enter(self):
		print("Dusty books and baubles litter the shelves along the wall and the desk in the middle")
		print("of the room. It is defintely a study, but you still don't understand why it was put")
		print("in the dungeon. You think it might do to investigate further, if only to only to quell")
		print("the unease creeping up your spine.")
		print("\nWhat do you do?")
		print("\t1. Leave and go down the corridor?")
		print("\t2. Search the room?")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nYou are here to explore a dungeon, not read books. You walk down the corridor. The")
			print("cells are abandoned, except for the decayed remains of the long forgotten residents")
			print("of the dungeon. The smell is almost overwhelming, but you press on. You continue")
			print("until you hear what sounds like scratching on stone, and you stop. The scratching gets")
			print("closer. And closer. And then you see two beady eyes appear just outside the light of")
			print("your torch. A rat is running toward you, almost like it is targeting you.")
			print("\nYou draw your father's sword. The rat leaps at your chest, and you swing, cutting it in")
			print("half. A putrid smell emanates from the dead rat, almost as if it had been dead for")
			print("weeks.")
			print("\nYou continue down the stairs.")

			return "stairs"
		elif choice == "2":
			global have_gem
			have_gem = True
			
			print("\n" + "-----" * 5)
			print("The books are anicent tomes, most of them you are hesitant to touch lest they crumble")
			print("under your fingers. Reams of parchment look like schloraly artices lay scattarted")
			print("around, each one heavily annotated. Burnt out candles are stuck in candle holders with")
			print("mountains of wax piled beneath them. The only parts of the room not coverend in dust")
			print("cobwebs or wax are those with rat foot prints.")
			print("\nYou take a look at the piles of papers on the center of the desk. Most of them seem")
			print("to be writings on extremly high level magic. Interdimensional time travel or some such.")
			print("None of it really makes much sense to you, but you do understand one aspect. 'Travel")
			print("doors' as they are called, required keys to be opened, and the key needs to be kept")
			print("close to the door. You figure this must be why the study is in a dungeon. There is some")
			print("kind of magic door way down here. You wonder if the key is still here.")
			print("\nYou search every nook and cranny of the room, and eventually you find a box, hidden")
			print("in some false bottom in one of the shelves. The box is enscribed with all manner of")
			print("glyphs that you think might have been magical warding keeping the box closed. It clearly")
			print("didn't work, because the box looks like something ripped it open with its teeth.")
			 
			
			return "stairs"
		else:
			print("That is not an option here.")
			return "study"
			
		
class TheStairs(Scene):
	#Choosing to take the magic sword from the skeleton.
	def enter(self):
		print("sword in the hand")
		print("\nWhat do you do?")
		print("\t1. Continue down the down the stair.")
		print("\t2. Take the sword.")
		
		choice = raw_input("> ")
	
		if choice == "1":
			print("You leave the body and continue down.")
			return "door"
		elif choice == "2":
			global have_sword
			have_sword = True
			print("You pry the sword out of the bones. It feels warm and light in your hands. You give it")
			print("a few swings and are suprised by the crispness of the blade.\n")
			print("You continue down.")
			return "door"
		else:
			print("That is not an option here.")
			return "stairs"

			
class TheDoor(Scene):
	#If you have the gem the door opens, if you don't the door does not open and you have to go back.
	def enter(self):
		print "Door with the gem"
		print("\nWhat do you do?")
		print("\t1. Examine door.")
		print("\t2. Go back up the stairs.")
		
		choice = raw_input("> ")
		
		if choice == "1":
			if have_gem:
				print("put in gem! door open!")
				return "deep"
			else:
				print "must go back!"
				print("\nWhat do you do?")
				print("\t1. Go back to the Study?")
				print("\t2. Go home.")
			
				choice = raw_input("> ")
			
				if choice == "1":
					print "back to study"
					return "study"
				elif choice == "2":
					print "boring life"
					return "death"
				else:
					print("That is not an option here.")
					return "stairs"
				
		elif choice == "2":
			print "must go back!"
			print("\nWhat do you do?")
			print("\t1. Go back to the Study?")
			print("\t2. Go home.")
			
			choice = raw_input("> ")
			
			if choice == "1":
				return "study"
			elif choice == "2":
				print "boring life"
				return "death"
			else:
				print("That is not an option here")
				return "stairs"
		else:
			print("That is not an option here.")
			return "door"
			
		
class TheDeep(Scene):
	def enter(self):
		print "fighta demon"
		print("\nWhat do you do?")
		print("\t1. Run for you life!")
		print("\t2. Stand and fight!")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print "you dead"
			return "death"
		elif choice == "2" and have_sword:
			if have_sword:
				print "demon ded"
				return "end"
			else:
				print "dad sword no affect"
				return "death"			
		else:
			print "hesitate"
			return "death"
		
class End(Scene):
	def enter(self):
		print "onward to adventure!"
		raw_input("")
		exit(1)
		
class Map(object):
	
	scenes = {
		"start" : TheBeginning(), 
		"death" : Death(), 
		"corridor" : CentralCorridor(), 
		"study" : WizardsStudy(), 
		"stairs" : TheStairs(),
		"door" : TheDoor(),
		"deep" : TheDeep(), 
		"end" : End()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_game(self):
		return self.next_scene(self.start_scene)
		
a_map = Map("start")
a_game = Engine(a_map)
a_game.play()
