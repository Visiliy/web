import json

cats_dict = [{
    'name': 'Pushin',
    'age': 1,
    'meals': [
        'Purina', 'Cat Chow', 'Hills'
    ],
    'owners': [
        {
            'first_name': 'Bill',
            'last_name': 'Gates'
        },
        {
            'first_name': 'Melinda',
            'last_name': 'Gates'
        }
    ]
}]

a = [('Vasiliy', 'Shkuratov', 'Sergeevih'), ('Konstantin', 'Shkuratov', 'Sergeevih')]
asd = []
for i in a:
    s = dict()
    s['name'] = i[0]
    s['surname'] = i[1]
    s['lastname'] = i[2]
    asd.append(s)


with open('cats_3.json', 'w') as cat_file:
    json.dump(asd, cat_file)


with open('cats_3.json') as cat_file2:
    data = json.load(cat_file2)
    print(data[0]['name'])