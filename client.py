import requests	
import json

class PokemonApiClient:
	baseURL = "http://pokeapi.co/api/v2/"
	def __init__(self, nameorID):
		self.name = ""
		self.types = ""
		self.moves = ""
		source = requests.get(self.baseURL+"pokemon/"+str(nameorID)).text
		j = json.loads(source)

		self.name = j["forms"][0]["name"]

		numoftypes = len(j["types"])
		for i in range(0, numoftypes):
			self.types = self.types + j["types"][i]["type"]["name"] + ", "
		self.types = self.types[:-2]

		numofmoves = len(j["moves"])
		for i in range(0, numofmoves):
			self.moves = self.moves + j["moves"][i]["move"]["name"] + ", "
		self.moves = self.moves[:-2]


				
