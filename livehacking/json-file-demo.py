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

# with: "context manager"
with open('/tmp/woswasi.json', 'x') as f:
    json.dump(data, f)
