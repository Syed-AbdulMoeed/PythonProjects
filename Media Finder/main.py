#get user input
#get information release date, rating, awards, 
#append dict of params
import datetime
import requests


def get_json(url, params):
    response = requests.get(url,params=params)
    if response.status_code == 200:
        return(response.json())
    else:
        return None 



def menu():
    while True:
        print('1 - View Saved Movies')
        print('2 - Search Movies')
        choice = input('Choice: ')
        if choice == '1':
            view_saved()
        elif choice == '2':
            search_movies()
        else:
            break



def view_saved():
    with open('films.txt', 'r') as file:
        for line in file:
            print(line.strip())


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
    get_details(id)


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
        file = open('films.txt', 'a')
        file.write(response['Title']+'\n')
        file.close()

    

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