import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kamronbek",
  database="users"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE users")


def newuser(userid):
	mycursor.execute("""CREATE TABLE IF NOT EXISTS allusers(
			ids INT,
			lastphoto INT)""")
	mycursor.execute(f'SELECT ids FROM allusers WHERE ids={userid}')
	if mycursor.fetchone() is None:

		
		mycursor.execute(f"insert into allusers(ids,lastphoto) values({userid},0)")
		
	else:
		return False

#newuser(101)		

def fetch():
	mycursor.execute('SELECT * FROM allusers')
	return mycursor.fetchall()

def fetchu(ids):
	mycursor.execute(f'SELECT * FROM allusers WHERE ids={ids}')
	return mycursor.fetchall()	


def ins(ids,last):
	
	mycursor.execute("""CREATE TABLE IF NOT EXISTS allusers(
			ids INT,
			lastphoto INT)""")
	

		
	mycursor.execute(f"update allusers set lastphoto={last} WHERE ids={ids}")	
#ins(1013574301,1)
