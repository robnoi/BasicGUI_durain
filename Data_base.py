
import sqlite3

conn = sqlite3.connect('product_database.sqlite3')
c = conn.cursor()

# create table
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quantity REAL,
				total REAL)""")


print('Success')

def insert_transaction(data):
	# data = {'tid': 111111','stamp':....}
	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quantity = data['quantity']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quantity,total) )
		conn.commit()
	print('Inserted!')

def view_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)

transaction = {'tid':'4204',
               'stamp':'2022-01-08',
               'product':'Durain',
               'price':100,
               'quantity':50,
               'total':5000}

#insert_transaction(transaction)
view_transaction()

