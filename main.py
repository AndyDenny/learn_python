def make_album(performer_name, album_name):
    album_info = {"performer_name" : performer_name.title() , "album_name": album_name.title()}
    return album_info

while True:
    performer_name = input("Please enter performer name: ")
    if performer_name == "q":
        break

    album_name = input("Please enter album name: ")
    if album_name == "q":
        break

    album = make_album(performer_name, album_name)
    print("performer_name: " + album['performer_name'] + ", album_name: " + album['album_name'])

