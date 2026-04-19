people = {
    "jd" : {
    "first": "John",
    "last": "Doe",
    "location": "New York"
    },
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    }
}

for person, info in people.items():
    print(info['first'].title() + " " + info['last'].title() + " " + info['location'].title())