cities_info = {
    "city" : {
        "country": "countryName",
        "population": "123123",
        "fact" : "smallest population",
    },
    "city2": {
        "country": "countryName2",
        "population": "5675677653",
        "fact": "very unique name"
    },
    "city3": {
        "country": "countryName3",
        "population": "89988678",
        "fact": "biggest rivers"
    },

}
for city, info in cities_info.items():
    print(city + ": country - " + info["country"] + ", population - " + info["population"] + ", fact - " + info["fact"])
