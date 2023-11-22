import sqlite3

def createTable():
    try:
        con = sqlite3.connect('ansa.db')
        cur = con.cursor()

        # Create table
        cur.execute('''CREATE TABLE links
                    (id primary key, title, published, link)''')
        
        con.commit()
        con.close()
    except:
        print()

def insertRecord(id, title, publishedDate, link):
    con = sqlite3.connect('ansa.db')
    cur = con.cursor()

    # Insert a row of data
    cur.execute(f'INSERT INTO links VALUES (?,?,?,?)', (id,title,publishedDate,link))

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()
    
def recordExist(id):
    con = sqlite3.connect('ansa.db')
    cur = con.cursor()
    
    return cur.execute(f'SELECT * FROM links WHERE id="{id}"').fetchone()

def selectAll():
    con = sqlite3.connect('ansa.db')
    cur = con.cursor()
    
    for record in cur.execute("SELECT * FROM links"):
        print(record)
    
    con.close()