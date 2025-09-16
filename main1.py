import mysql.connector

# Connette al server MySQL locale con le credenziali fornite
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)

# Crea un cursore per eseguire comandi SQL
mycursor = mydb.cursor()

# Esegue un comando SQL per creare un nuovo database chiamato "mydatabase"
mycursor.execute("CREATE DATABASE mydatabase")