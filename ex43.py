#The play Engine is made up of scenes.
#I'm guessing event driven functions based on character actions.
#objects that inherit Scene properties:
	#Death
	#Central corridor
	#LaserWeaponArmory
	#TheBridge
	#EscapePod
class Scene(object):
	def enter(self):
		pass
		
#This is probably the highest level object. It is the gameplay
class Engine(object):
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
		
class Death(Scene):
	def enter(self):
		pass

class CentralCorridor(Scene):
	def enter(self):
		pass
		
class LaserWeaponArmory(Scene):
	#This is the  time "enter" is defined in a Scene.
	#Why is this better and not say calling enter from a "Action" class?
	#Might have something to do with inheritance, I don't know that much about it tbh...
	def enter(self):
		pass
		
class TheBridge(Scene):
	def enter(self):
		pass
		
class EscapePod(Scene):
	def enter(self):
		pass
		
class Map(object):
	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass
		
	def opening_game(self):
		pass

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()