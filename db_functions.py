import sqlite3


def create_database(database_name):
    '''
    Function to create a sqlite database connection and cursor
    '''
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    return conn, c

# Check if table already exists. Otherwise create it
def create_table(conn, c, table_name):
    '''
    Creating table 'sessions' if not existing yet.
    '''
    table_name = 'sessions'
    c.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';""")
    result = c.fetchall()
    if not result:
        print(f"The Table '{table_name}' does not exists! Let's create one ...")

        c.execute(f"""CREATE TABLE {table_name} (
                    game_no integer,
                    date text,
                    mistakes_no integer,
                    mistakes text,
                    time float,
                    pi_series text
                    )""")
        conn.commit()

def add_new_session(conn, c, session_dictionary):
    c.execute('''INSERT INTO sessions VALUES
    (:game_no, :date, :mistakes_no, :mistakes, :time, :pi_series)''', session_dictionary)
    conn.commit()


def get_all_sessions(c, table_name):
    c.execute(f'''SELECT * FROM {table_name}''')
    values = c.fetchall()
    return values

def close_connection(conn):
    conn.close()


if __name__ == '__main__':

    session_dictionary = {
    "game_no" : 5,
    "date" : 5,
    "mistakes_no" : 5,
    "mistakes" : 6,
    "time" : 5
    }

    conn, c = create_database("sessions")
    create_table(conn, c, 'sessions')
    # add_new_session(conn, c, session_dictionary)
    values = get_all_sessions(c, 'sessions')
    close_connection(conn)


    print(values)
