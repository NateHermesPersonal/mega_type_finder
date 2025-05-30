import csv

def read_types_into_dict(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['slot'] == "1": # create new dictionary entry if this is the first type for that Pokemon
                data[row['pokemon_id']] = [row['type_id']]
            else: # add a second type otherwise
                data[row['pokemon_id']].append(row['type_id'])
    return data

def add_types_to_forms_sheet(file_path):
    data = []
    fieldNames = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if not fieldNames:
                fieldNames = [key for key in row.keys()]
            data.append(row)
    for row in data:
        # print(row['id'])
        id = row['pokemon_id']
        try:
            types = typeDictionary[id]
            try:
                row['type_1'] = types[0]
                row['type_2'] = types[1]
            except:
                pass
        except:
            print(f"Did not find match for {id}")

    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(data)



file_path = 'csv/pokemon_types.csv'
typeDictionary = read_types_into_dict(file_path)

print(f"Created type dictionary with {len(typeDictionary.keys())} entries")

file_path = 'csv/my_pokemon_forms.csv'
add_types_to_forms_sheet(file_path)

print(f"Updating {file_path} with Pokemon types")
