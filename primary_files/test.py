from cs50 import SQL

db = SQL("sqlite:///students.db") # get the database in a variable called 'db'

something = db.execute("SELECT first,middle,last,birth FROM students WHERE house='Gryffindor'")

for sdict in something:
    middle = sdict['middle']

    if middle==None:
        middle = '\b'

    print(sdict['first'], middle, sdict['last']+',', 'born', sdict['birth'])