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
		print("\nWELCOME TO THE DUNGEON\n")
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
		
		loop = True
		choice = raw_input("> ")

		if choice == "1":
			loop = False
			print "dive into dungeon"
			return "corridor"
		elif choice == "2":
			loop = False
			print("\nYou realize you have forgotten some supplies that might be useful, and you decide to")
			print("head back into town. It would not do to dive into an unknown dungeon uprepared. While in")
			print("town see Araella, the girl you've had a crush on for quite some time.")
			return "death"
		else:
			print("That is not an option here.")
			return "start"
		
class Death(Scene):
	def enter(self):
		print "ded\n"
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
		print "test corrior"
		print("\nWhat do you do?")
		print("\t1. Go forward, through the door?")
		print("\t2. Go left, down the hall?")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print "into study"
			return "study"
		elif choice == "2":
			print "the stuff about rats"
			return "death"
		else:
			print("That is not an option here")
			return "corridor"
		
class WizardsStudy(Scene):
	def enter(self):
		print "Wizzer"
		print("\nWhat do you do?")
		print("\t1. Leave and go down the corridor?")
		print("\t2. Search the room?")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print "hallway stuff no rats"
			return "stairs"
		elif choice == "2":
			global have_gem
			have_gem = True
			
			print "grabba gem"
			
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