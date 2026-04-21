def make_album(performer_name, album_name, tracks_count = 0):
    album_info = {"performer_name" : performer_name.title() , "album_name": album_name.title()}
    if tracks_count > 0:
        album_info["tracks_count"] = tracks_count
    return album_info


album = make_album("annisokay","aurora")
print("performer_name: " + album['performer_name'] + ", album_name: " + album['album_name'])
album = make_album("nickelback","curb")
print("performer_name: " + album['performer_name'] + ", album_name: " + album['album_name'])
album = make_album("metallica","master of puppets")
print("performer_name: " + album['performer_name'] + ", album_name: " + album['album_name'])
album = make_album("nightwish","wishmaster", 14)
print("performer_name: " + album['performer_name'] + ", album_name: " + album['album_name'] + ", tracks_count: " + str(album['tracks_count']))
