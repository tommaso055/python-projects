import json
import requests
import random

def get_album_number(artist):
    artist_code = artists[artist]
    request = requests.get(f"https://api.deezer.com/artist/{artist_code}").json()
    album_number = request["nb_fan"]
    return album_number

artisti = "data/artists.json"

with open(artisti, "r") as f:
    artists = json.load(f)

cont = "Y"

while cont.upper() == "Y":

    two_artists = random.sample(list(artists.keys()), 2)

    guess = input(f"Chi ha più fan tra {two_artists[0]} (1) e {two_artists[1]} (2)?\n")

    album_1 = get_album_number(two_artists[0])
    album_2 = get_album_number(two_artists[1])

    ans = "1" if album_1 > album_2 else "2"

    esito = "Giusto! " if guess == ans else  "Sbagliato. "
    esito += f"{two_artists[0]} ha {album_1} fan, mentre {two_artists[1]} ha {album_2} fan. Vuoi continuare? (Y)\n"

    cont = input(esito)


