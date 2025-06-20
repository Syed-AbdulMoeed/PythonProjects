import sqlite3
                        #':memory: to open in memory (good for testing)

def inset_movie(movie):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute("INSERT INTO movies VALUES(:title, :year, :watched)", {'title' : movie.title, 'year' : movie.year, 'watched' : 0})
    conn.commit()
    conn.close() #close the connection

def get_movie_by_name(title):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies WHERE title=?', (title,)) #needs to be a tuple when ? placeholder
    conn.close() #close the connection
    return cursor.fetchone()
    

def view_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    for movie in cursor.fetchall():
        print('Name: {} | Year: {} | {}'.format(movie[0], movie[1], 'Watched' if movie[2]==1 else 'Not Watched' ))
    conn.close()


def watch_movie(title):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET watched=1 WHERE title=:title", {'title' : title})
    conn.commit()
    conn.close()


def remove_movie(title):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE title=:title", {'title' : title})
    conn.commit()
    conn.close()


""" cursor.execute('''CREATE TABLE movies(
               title text,
               year integer,
               watched integer
               )''') """



""" cursor.execute("INSERT INTO movies VALUES(?, ?)", (movie1, y_1))
conn.commit()


cursor.execute("INSERT INTO movies VALUES(:title, :year)", {'title' : movie1, 'year' : y_1})
conn.commit() """

#cursor.execute("DELETE FROM movies WHERE title='Spider-Man'")
""" 
if __name__== '__main__':
    cursor.execute("SELECT * FROM movies")
    print(cursor.fetchall()) """




view_movies()
remove_movie('Madagascar')
view_movies()