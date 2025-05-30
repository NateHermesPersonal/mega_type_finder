import csv

def read_types_into_dict(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['slot'] == "1":
                data[row['pokemon_id']] = [row['type_id']]
            else:
                data[row['pokemon_id']].append(row['type_id'])
    return data

file_path = 'csv/pokemon_types.csv'
typeDictionary = read_types_into_dict(file_path)

print(f"Created type dictionary with {len(typeDictionary.keys())} entries")