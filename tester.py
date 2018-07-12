from client import PokemonApiClient

client = PokemonApiClient()
p = PokemonApiClient().getItem(1)

print(p.name + "\n" + p.category + "\n" + p.attributes + "\n" + p.shortEffect + "\n" + p.cost)

