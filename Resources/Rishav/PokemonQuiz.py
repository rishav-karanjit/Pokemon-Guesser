import pokebase as pb

charmander = pb.pokemon('charmander')
print("Type: "+ str(charmander.types[0].type))

print("\nMoves:")
for i in range(10):
    print(charmander.moves[i].move.name)

print("Base Stat")
print(charmander.stats[0].base_stat)

print("\nArea Encountered \n")
for i in charmander.location_area_encounters:
    print(i.location_area)

print("\nability:\n")
for i in charmander.abilities:
    print(i.ability)

print("base_experience:" + str(charmander.base_experience))

print("Height: " + str(charmander.height))
print("Weight: " + str(charmander.weight))