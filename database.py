import sqlite3

setup = True

def create_language_table(language):
  database.execute('''CREATE TABLE ''' + language + ''' (WORD CHAR(100) UNIQUE NOT NULL)''')

def create_word(language, value):
  print('''INSERT INTO ''' + language + '''(WORD) VALUES(''' + value + ''')''')
  # database.execute('''INSERT INTO ''' + language + ''' (WORD) VALUES (''' + value + ''')''')
  database.execute('''INSERT INTO GER VALUES (1)''')

def create_connection(word_1_id, word_2_id, lng1, lng_2):
  database.execute(
    # '''INSERT INTO CONNECT VALUES(''' + word_1_id +  ''', ''' + word_2_id + ''') (''' + lng1 + ''', ''' + lng_2 ''')'''
    '''INSERT INTO CONNECT VALUES(1, 1) (ENG, GER)'''
  )

if setup:
  database = sqlite3.connect('test.db')

  create_language_table("GER")
  create_language_table("ENG")
  create_language_table("ESP")

  database.execute('''CREATE TABLE CONNECT
    (DATE_NEXT_UP TIMESTAMP,
    GER INT NOT NULL,
    ENG INT NOT NULL,
    ESP INT,
    BOX INT NOT NULL,
    HISTORY INT
    )
  ''')

  create_word("GER", "Milch")
  create_word("ENG", "milk")
  create_word("ESP", "leche")

  create_word("GER", "Hai")
  create_word("ENG", "shark")

  create_word("GER", "Bruder")
  create_word("ESP", "hermano")

  create_connection(1, 1, "GER", "ENG")
  database.close()