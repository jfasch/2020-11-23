import json


data = [
    {
        'name': 'Patrick',
        'age': 24
    },
    {
        'name': 'Gernot',
        'age': 38,
    },
]

f = open('/tmp/woswasi.json', 'x')

json.dump(data, f)
