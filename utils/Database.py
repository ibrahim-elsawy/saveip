import sqlite3

class Database():
	def __init__(self, dbname) -> None: 
		self.dbname = dbname
	def insertIP(self, table_name, day, month, ip_address): 
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", (None, day, month, ip_address)) 
		conn.commit()
		conn.close()

	def getLastIP(self, table_name): 
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name}").fetchall()[-1]
		ip = r[3]
		conn.close()
		return ip

