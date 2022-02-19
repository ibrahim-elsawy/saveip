import sqlite3

DBNAME="address.db"
T1="ip"


if __name__ == '__main__': 
	conn = sqlite3.connect(DBNAME) 
	c = conn.cursor() 
	c.execute(f"CREATE TABLE {T1} (i INTEGER PRIMARY KEY AUTOINCREMENT, day INTEGER, month INTEGER, ip_address TEXT)") 
	# c.execute(f"CREATE INDEX id_comapny ON {T1} (id);")
	conn.commit() 
	conn.close()
	
