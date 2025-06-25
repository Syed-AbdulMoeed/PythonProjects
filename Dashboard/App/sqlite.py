import sqlite3


def delete_all():
    conn= sqlite3.connect('database.db')
    c = sqlite3.Cursor(conn)
    with conn:
        c.execute('DELETE FROM posts ')
    conn.commit()
    conn.close()


def insert_into(username, comment):
    conn = sqlite3.connect('database.db')
    c = sqlite3.Cursor(conn)
    with conn:
        c.execute('INSERT INTO posts VALUES(:username, :comment)',{'username' : username, 'comment' : comment})
    conn.commit()
    conn.close()


def get_data():
    conn = sqlite3.connect('database.db')
    c = sqlite3.Cursor(conn)
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    conn.close()
    return posts

#c.execute("""CREATE TABLE posts(
#          username text,
#          comment text)  
#          """)

#c.execute("""INSERT INTO posts VALUES('Potato', 'I love cats')""")

#c.execute(""" SELECT * FROM posts """)
#print(c.fetchall())
#conn.close()