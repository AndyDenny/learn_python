favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

user_names = [ "Andy", "Sandy", "sarah", "Mandy", "phil", "Vendy"]

for name in user_names:
    if name.lower() in favorite_languages:
        print(name.title() + ", thank you for taking the poll")
    else:
        print(name.title() +  ", please take our poll!")