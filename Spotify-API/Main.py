from requests import post, get
from dotenv import load_dotenv
import os
import base64
import json
import sys

print(sys.version)
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id+":"+client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}


def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    
    while True:
        try:
            query = f"?q={artist_name}&type=artist&limit=5"

            query_url = url + query
            result = get(query_url, headers=headers)
            json_result = json.loads(result.content)["artists"]["items"]
            return json_result
        except:
            artist_name = input("Couldn't find the artist, Please enter another name:")
    

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


def get_albums_by_artists(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?limit=5"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['items']
    return json_result


def get_recommened_artists(token, genre):
    url = f"https://api.spotify.com/v1/search?q={genre}&type=artist&limit=5"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    return json_result


def get_artist_name():
    return input("Enter Artist Name: ")


def get_choice():
    while True:
        try:
            choice = int(input("Enter Index of choice (Enter zero to search again)"))
            if 0<= choice <= 5:
                return choice
            print("Enter a digit between 0-5")
        except(ValueError):
            print("Enter a digit between 0-5")
        

def select_artist(artists):
    print("---Select an Artist---")
    for i,artist in enumerate(artists):
        print(f"{i+1}. {artist['name']} . Followers:{artist['followers']['total']}. Popularity: {artist['popularity']}")
    return get_choice()


def view_tracks(token, artist_id):
    tracks = get_songs_by_artist(token, artist_id)
    print("----Top-Tracks by Artist----")
    for i,track in enumerate(tracks):
        print(f"{1+i}.  {track['name']}")


def view_albums(token, artist_id):
    albums = get_albums_by_artists(token, artist_id)
    print("----Albums by Artist----")
    for i,album in enumerate(albums):
        print(f"{1+i}.  {album['name']}")


def view_rec_artists(token, artist_id):
    artists = get_recommened_artists(token, artist_id)
    for i,artist in enumerate(artists):
        print(f"{1+i}. {artist['name']}. Followers: {artist['followers']['total']}. Popularity: {artist['popularity']}. Genres: {artist['genres']}")


def main():
    token = get_token()
    while True:
        artist_name = get_artist_name()
        result = search_artist(token, artist_name)
        choice = select_artist(result)
        if choice != 0:
            index = choice - 1
            break
    artist = result[index]
    artist_id = result[index]["id"]
    while True:
        print(f"""-----{artist['name']}-----
            1. View Top-Tracks
            2. View Albums
            3. View Recommended Artists
            4. Exit
            
            URL:{artist['external_urls']['spotify']}
            Genres: {artist['genres']}

            """)
        choice = input("Selection: ")
        match choice:
            case '1': 
                view_tracks(token, artist_id)
            case '2': 
                view_albums(token, artist_id)
            case '3':
                if len(artist['genres']) == 0:
                    print("nahi milay ka koi, no registered genres")
                else: 
                    view_rec_artists(token, artist['genres'][0])
            case '4' :
                print('nikl yaha say')
                sys.exit()
            case _ :
                print("insaan ka bucha bunja ghuday") 


    '''
    for album in albums:
        print(album['name'])

    for song in songs:
        print(song['name'])
    '''

main()


#for i,song in enumerate(songs):
#    print(f"{i+1}. {song['name']}")