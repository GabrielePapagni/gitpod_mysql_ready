import mysql.connector

# Connette al server MySQL locale usando le credenziali e seleziona il database "mydatabase"
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Crea un cursore per eseguire comandi SQL
mycursor = mydb.cursor()

# Esegue un comando SQL per creare una tabella chiamata "customers" con due colonne: "name" e "address"
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")