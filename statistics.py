import db_functions as db
from tabulate import tabulate

conn, c = db.create_database("sessions")
db.create_table(conn, c, 'sessions')
# add_new_session(conn, c, session_dictionary)
values = db.get_all_sessions(c, 'sessions')
db.close_connection(conn)


print(values)
big_list_for_table = [['Game No.', 'Date', 'Mistakes No.', 'Mistakes', 'Time', 'Pi Series']]
for tuppple in values:
    list_for_table = list(tuppple)
    print(list_for_table)
    big_list_for_table.append(list_for_table)

table = big_list_for_table
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', maxcolwidths=[5, 100, 10, 30, 30, 30]))

# sqlite3 -header -csv sessions.db < select_all.sql > all_sessions.csv