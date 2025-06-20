#Inputs and Implementation is very crude
import datetime
import requests
import sqlite

class movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year



def get_json(url, params):
    response = requests.get(url,params=params)
    if response.status_code == 200:
        return(response.json())
    else:
        return None 



def menu():
    while True:
        print('1 - Saved Movies')
        print('2 - Search Movies')
        choice = input('Choice: ')
        if choice == '1':
            saved()
        elif choice == '2':
            search_movies()
        else:
            break


def saved():
    view_saved_all()
    print('1 - remove from watchlist')
    print('2 - Mark Watched')
    choice = input('Enter Choice: ')
    title = input('Enter Tile: ')
    match choice:
        case '1' :
            remove_movie(title)
        case '2' :
            mark_movie(title)



def view_saved_all():
    sqlite.view_movies()


def remove_movie(title):
    sqlite.remove_movie(title)


def mark_movie(title):
    sqlite.watch_movie(title)


def search_movies():
    global url
    name = input('Enter Movie Name: ')
    params['s'] = name
    response = get_json(url, params)
    if response:
        view_json(response)
    else:
        print('None Found')


def view_json(data):
    
    for i,film in enumerate(data['Search']):
        print(i, film['Title'], film['Year'], film['Type'])
        
    i = int(input('Film Details: ')) 
    id = data['Search'][i]['imdbID']
    sqlite.inset_movie(get_details(id)) 


def get_details(id):
    del params['s']
    params['i'] = id
    response = requests.get(url, params=params).json()
    print('Genre: '+response['Genre'])
    print('Actors: '+response['Actors'])
    print('Plot: '+response['Plot'])
    print('Release Date: '+response['Released'])
    save = input('1 to save: ')
    if save == '1':
        return movie(response['Title'], response['Year'])

    

def get_year():
    while True:
        try:
            year = input('Year: ')
            datetime.datetime.strptime(year, '%Y')
            return year
        except(ValueError):
            print('Enter YYYY')


params = {
    'r':'json',
    's': ''
}

saved_movies = [] #list of dict movies

api_key = ''
url = f'http://www.omdbapi.com/?apikey={api_key}&'


def main():
    
    menu()




main()