
import requests	
import json

class PokemonApiClient:
	baseURL = "http://pokeapi.co/api/v2/"
	def __init__(self):
		
		pass

	def getPokemon(self, nameorID):
		source = requests.get(self.baseURL+"pokemon/"+str(nameorID)).text
		j = json.loads(source)

		types = ""
		moves = ""
		name = j["forms"][0]["name"]

		numoftypes = len(j["types"])
		for i in range(0, numoftypes):
			types = types + j["types"][i]["type"]["name"] + ", "
		types = types[:-2]

		numofmoves = len(j["moves"])
		for i in range(0, numofmoves):
			moves = moves + j["moves"][i]["move"]["name"] + ", "
		moves = moves[:-2]

		pokemon = Pokemon(name, types, moves)
		return pokemon

	def getBerry(self, nameorID):
		source = requests.get(self.baseURL+"berry/"+str(nameorID)).text
		j = json.loads(source)

		flavors = ""
		name = j["name"]
		size = j["size"]

		numofflavors = len(j["flavors"])
		for i in range(0, numofflavors):
			flavors = flavors + j["flavors"][i]["flavor"]["name"] + ", "
		flavors = flavors[:-2]

		berry = Berry(name, flavors, size)
		return berry

	def getItem(self, nameorID):
		source = requests.get(self.baseURL+"item/"+str(nameorID)).text
		j = json.loads(source)

		attributes = ""
		name = j["name"]
		category = j["category"]["name"]
		cost = j["cost"]
		effect = j["effect_entries"][0]["effect"]
		shortEffect = j["effect_entries"][0]["short_effect"]

		numofattributes = len(j["attributes"])
		for i in range(0, numofattributes):
			attributes = attributes + j["attributes"][i]["name"] + ", "
		attributes = attributes[:-2]

		item = Item(name, category, cost, attributes, effect, shortEffect)
		return item




	

class Pokemon:

	def __init__(self, name, types, moves):
		self.name = name
		self.types = types
		self.moves = moves
		pass

class Berry:

	def __init__(self, name, flavors, size):
		self.name = name
		self.flavors = flavors
		self.size = size

class Item:

	def __init__(self, name, category, cost, attributes, effect, shortEffect):
		self.name = name
		self.category = category
		self.cost = str(cost)
		self.attributes = attributes
		self.effect = effect
		self.shortEffect = shortEffect




				
