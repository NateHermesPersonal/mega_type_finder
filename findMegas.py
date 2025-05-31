import csv

typeDictionary = {}
selectedPokemonByType = {}
megaPokemon = {}
megaPokemonBoost = {}

def build_type_dictionary(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if int(row['id']) < 19: # don't care about stellar or any special types
                typeDictionary[row['id']] = row['identifier']
                megaPokemon[row['id']] = []
                selectedPokemonByType[row['id']] = []

def parse_spreadsheet(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dictionary = 0
            identifier = row['identifier']
            if row['selected'] == '1':
                dictionary = selectedPokemonByType
            elif row['is_mega'] == '1':
                dictionary = megaPokemon
            if dictionary != 0:
                dictionary[row['type_1']].append(identifier)
                if row['type_2'] != '0':
                    dictionary[row['type_2']].append(identifier)

def print_pokemon():
    sortedSelectedPokemonByType = dict(sorted(selectedPokemonByType.items(), key=lambda item: len(item[1]), reverse=True))
    for type in sortedSelectedPokemonByType.keys():
        listLength = len(sortedSelectedPokemonByType[type])
        if listLength > 0:
            print(f"Type {typeDictionary[type]} has {listLength} spawn(s): {', '.join(sortedSelectedPokemonByType[type])}")
            for pokemon in megaPokemon[type]:
                if pokemon not in megaPokemonBoost:
                    megaPokemonBoost[pokemon] = []
                    for spawn in sortedSelectedPokemonByType[type]:
                        if spawn not in megaPokemonBoost[pokemon]:
                            megaPokemonBoost[pokemon].append(spawn)
    sortedMegaPokemonBoost = dict(sorted(megaPokemonBoost.items(), key=lambda item: len(item[1]), reverse=True))
    print("")
    for mega in sortedMegaPokemonBoost.keys():
        boostList = sortedMegaPokemonBoost[mega]
        print(f"{mega} boosts {len(boostList)} Pokemon spawn(s): {', '.join(boostList)}")


build_type_dictionary('csv/types.csv')
parse_spreadsheet('csv/my_pokemon_forms.csv')
print_pokemon()
# print(megaPokemon)
# sorted_dict = dict(sorted(megaPokemon.items(), key=lambda item: len(item[1]), reverse=True))
# print(sorted_dict)
print("\nFound Megas which boost spawns")