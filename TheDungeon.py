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
		print("WELCOME TO THE DUNGEON\nv1.0\n")
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
		
		global have_gem
		global have_sword
		
		have_gem = False
		have_sword = False
		
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
		print("\nThe books are anicent tomes, most of them you are hesitant to touch lest they crumble")
		print("under your fingers. Reams of parchment look like schloraly artices lay scattarted")
		print("around, each one heavily annotated. Burnt out candles are stuck in candle holders with")
		print("mountains of wax piled beneath them. The only parts of the room not coverend in dust")
		print("cobwebs or wax are those with rat foot prints.")
		print("\nYou take a look at the piles of papers on the center of the desk. Most of them seem")
		print("to be writings on extremly high level magic. Interdimensional time travel or some such.")
		print("None of it really makes much sense to you, but you do understand one aspect. 'Travel")
		print("doors' as they are called, required keys to be opened, and the key needs to be kept")
		print("close to the door.")
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
			print("half. A putrid smell emanates from the rat, almost as if it had been dead for")
			print("weeks.")
			print("\nYou continue down the stairs.")

			return "stairs"
		elif choice == "2":
			global have_gem
			have_gem = True
			
			print("\n" + "-----" * 5)
			print("You figure this must be why the study is in a dungeon. There is some")
			print("kind of magic door way down here. You wonder if the key is still here.")
			print("\nYou search every nook and cranny of the room, and eventually you find a box, hidden")
			print("in some false bottom in one of the shelves. The box is enscribed with all manner of")
			print("glyphs that you think might have been magical warding keeping the box closed. It clearly")
			print("didn't work, because the box looks like something ripped it open with its teeth.")
			print("\nInside is a small, teardrop-shaped gem. It's got a teal tint to it and it is glowing.")
			print("This must be a key all of the writings were talking about.")
			print("\nYou take it, and head towards the other end of the corridor.")
			
			return "stairs"
		else:
			print("That is not an option here.")
			return "study"
			
		
class TheStairs(Scene):
	#Choosing to take the magic sword from the skeleton.
	def enter(self):
		print("In the darkness, you can't tell how long the corridor goes on for, and your perception")
		print("of time seems as drprived as your vision. Yet you continue to walk, along each side of")
		print("you are jail cells filled with corpses long done rotting. You keep your gaze straight")
		print("ahead, trying not to look at them, and eventually you come to the end of the corridor.")
		print("\nYou think maybe the darkness is playing tricks on your eyes when you see a staircase")
		print("once again heading down. But that is exactly what it is. Even after travelling all that")
		print("way down from the surface, whoever built this dungeon dug deeper into the earth.")
		print("\nWalking down the stairs, you go far enough to get away from the stench of death that")
		print("permeated the dungeon above. The air down here smells clearer but heavier. Looking at")
		print("walls you realize they've been charred black by a fire hot enough to melt the stone. You")
		print("come to the end of the stiarcase and at the bottom a black skeleton, more ash now than")
		print("bone. It looks as though he was once a warrior. A warrior who was fleeing for his life,")
		print("and cooked in his armor as it melted around him. The only thing untouched is the sword in")
		print("his hands.")
		print("\nWhat do you do?")
		print("\t1. Continue down the down the stair.")
		print("\t2. Take the sword.")
		
		choice = raw_input("> ")
	
		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nYou leave the body and continue down, deciding to let the man rest with the last possesion")
			print("he has left.")
			return "door"
		elif choice == "2":
			global have_sword
			have_sword = True
			
			print("\n" + "-----" * 5)
			print("\nYou pry the sword out of the bones. It feels warm and light in your hands. You give it")
			print("a few swings and are suprised by the crispness of the blade. You figure two blades are")
			print("better than one, and you decide to keep your father's sword as a backup")
			print("You continue down.")
			return "door"
		else:
			print("That is not an option here.")
			return "stairs"

			
class TheDoor(Scene):
	#If you have the gem the door opens, if you don't the door does not open and you have to go back.
	def enter(self):
		print("The staircase ends at a door way. There are multiple glowing blue sigils carved into")
		print("it. You try to open the door, but it does not budge. It must be sealed by magic.")
		print("\nWhat do you do?")
		print("\t1. Examine door more closely.")
		print("\t2. Go back up the stairs.")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nYou go over the sigils, tracing your hand along each one. You find a teardrop-shaped")
			print("hole at the bottom of the door.")
			if have_gem:
				print("\n" + "-----" * 5)
				print("\nYou place the gem in the hole, and it fits perfectly. As soon as you press in you feel")
				print("pressue release and air rushes out from the other side of the door. It swings open,")
				print("almost knocking you off your feet. The wind blows out your torch and you are plunged")
				print("into complete black.")
				
				return "deep"
			else:
				print("\n" + "-----" * 5)
				print("\nYou realize must be the Travel Door, and the teardrop hole is for the key.") 
				print("\nWhat do you do?")
				print("\t1. Go back to the Study?")
				print("\t2. Go home.")
			
				choice = raw_input("> ")
			
				if choice == "1":
					return "study"
				elif choice == "2":
					print("\n" + "-----" * 5)
					print("\nYour mind races with what kind of horrors must be beyond this door. It would probably")
					print("be better if you had some kind of armor, or a sheild, or something. You don't even know")
					print("how to use a sword, not really. It was stupid to come down here so unprepared. You need")
					print("go back, get your bearings. Just get the hell out of here...")
					print("\nYou go back, decide to learn to fight abit. You tell youself you are going to go back,")
					print("and finally face what is behind that door. But you don't.")
					print("You live a happy, quiet life. You marry the girl of your dreams, you have kids and a little")
					print("farm. And you realize there is nothing wrong with that. Except every so often get this")
					print("nagging feeling in the back of your mind. A feeling that maybe there is something greater")
					print("than happiness. About once a year you go into the attic while your wife and kids are out,")
					print("and you look at your old map, dreaming of what could have been.")
					
					return "death"
				else:
					print("That is not an option here.")
					return "door"
				
		elif choice == "2":
			print("\n" + "-----" * 5)
			print("\nWhich way do you go?")
			print("\t1. Go back to the Study?")
			print("\t2. Go home.")
			
			choice = raw_input("> ")
			
			if choice == "1":
				return "study"
			elif choice == "2":
				print("\n" + "-----" * 5)
				print("\nYour mind races with what kind of horrors must be beyond this door. It would probably")
				print("be better if you had some kind of armor, or a sheild, or something. You don't even know")
				print("how to use a sword, not really. It was stupid to come down here so unprepared. You need")
				print("go back, get your bearings. Just get the hell out of here...")
				print("\nYou go back, decide to learn to fight abit. You tell youself you are going to go back,")
				print("and finally face what is behind that door. But you don't.")
				print("You live a happy, quiet life. You marry the girl of your dreams, you have kids and a little")
				print("farm. And you realize there is nothing wrong with that. Except every so often get this")
				print("nagging feeling in the back of your mind. A feeling that maybe there is something greater")
				print("than happiness. About once a year you go into the attic while your wife and kids are out,")
				print("and you look at your old map, dreaming of what could have been.")
				
				return "death"
			else:
				print("That is not an option here")
				return "door"
		else:
			print("That is not an option here.")
			return "door"
			
		
class TheDeep(Scene):
	def enter(self):
		print("In the darkness, you can make out a shape that somehow is more black than the darkness")
		print("already around you. It looks like some kind of hole. And out of the hole there is ")
		print("pouring some kind of grey mass, and it is growling.")
		print("\nThe sword in your hand comes to life. It shines a brillance, lighting up the room,")
		print("except for the hole behind this thing. It starts to take form. It morphs into what looks")
		print("like a man with grey skin, except it has grey skin and is eight feet tall with four foot")
		print("tall antlers growing from its head. When it sees you, it smiles.")
		print("\nIt's a demon. You don't know how you know that, but you do. Your breath come hard into")
		print("your lungs.")
		print("\nWhat do you do?")
		print("\t1. Run for you life!")
		print("\t2. Stand and fight!")
		
		choice = raw_input("> ")
		
		if choice == "1":
			print("\n" + "-----" * 5)
			print("\nThere is no getting out of this alive. You drop your sword and your unlit torch, and")
			print("you run for the stairs. You make it farther than the warrior before you feel the flames")
			print("licking your heals. You scream for as long as your lungs and throat exist. You whither")
			print("in pain as the last seconds of your life feel like an eterntiy. The last things your")
			print("eyes see are the flames engulfing you, and they almost look beautiful.")
			
			return "death"
		elif choice == "2":
			if have_sword:
				print("You grip your new sword as tight as you can. There wont be any running away from this.")
				print("You are already dead, so you might as well go out fighting. 'Come on, then!' you scream")
				print("at this abmomination, and it bolts at you, faster than anything should move.")
				print("\nIt feels like your hand moves on its own. The sword know where to go, you trust it, and")
				print("it strikes. It sinks deep into its chest, where its heart would be if this thing has")
				print("one. The demon's mouth grows wide in shock. It screams out like it's never felt pain")
				print("before.")
				print("\nIn its death throes it lashes out and scratches across your chest. It's not a deep wound")
				print("but it burns as if you've splashed with hot tar. The pain causes you to pass out.")
				
				return "end"
			else:
				print("\n" + "-----" * 5)
				print("\nYou draw your father's sword. You've come this far and you're not going to let some God")
				print("forsaken abomination stop you now. You charge. Deep down you find courage you never knew")
				print("you had, and you bring your sword to bear in the demon's gut. It glances off its skin")
				print("without a scratch.")
				print("\nThe demon laughs and grips your head in the palm of your head, lighting you ablaze. You")
				print("are dead before you feel anything.")
				
				return "death"			
		else:
			print("\n" + "-----" * 5)
			print("\nYou do nothing. The demon moves faster than should be possible, and before you can think")
			print("its hands are embedded in your chest cavity, and it rips apart your rib cage. You watch")
			print("you organs spill out onto the floor of the dungeon, wondering why you can't feel anything.")
			
			return "death"
		
class End(Scene):
	def enter(self):
		print("You awake. Your chest feels like it is splitting open. You open your shirt and three")
		print("cauterized slash wounds down your abdomen. You struggle to move, but eventually make it")
		print("to your feet.")
		print("\nYou make it over to the black rift. It's like it's cutting through reality itself. You")
		print("through the rift and you can see small points of light. Concentrating you can actually")
		print("make out what they are. They are other Travel Doors. It looks like there are hundreds of")
		print("them around the world, some of them opening into dungeons like this one and other just")
		print("hanging in open air.")
		print("\nThe Door in front of you begins to close. You take a deep breath and say, 'I guess I got")
		print("work to do.'")
		print("\n" + "-----" * 5 + "\n")
		
		raw_input("The End.")
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
