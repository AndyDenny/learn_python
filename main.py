pets = {
    "holly" : {
        "type": "dog",
        "name": "holly",
        "owner": "John Doe"
    },
    "dolly" : {
        "type": "sheep",
        "name": "dolly",
        "owner": "nasa"
    },
    "barbados" : {
        "type": "hamster",
        "name": "barbados",
        "owner": "michael jackson"
    }
}

for name, info in pets.items():
    print(info['type'].title() + " - " + info['name'].title() + " by " + info['owner'].title())