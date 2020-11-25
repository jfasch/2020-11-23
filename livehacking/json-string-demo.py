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

json_data = json.dumps(data)

print(json_data)
