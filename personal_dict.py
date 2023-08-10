import psycopg2
conn=psycopg2.connect(database='postgres',user='postgres', password='6978',host='localhost',port='5432')
cur=conn.cursor()

# get input from the user 
def get_input():
    inp =input('''Welcome to your personal dictionary.
if you want to open your dictionary type "open"
if you want to add a word type "add"
if you want to quit type "quit" ''')
    return inp
inp=get_input()
print(inp)