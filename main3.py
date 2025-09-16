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

# Definisce una query SQL per inserire un nuovo record nella tabella "customers"
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# Valori da inserire nella query
val = ("John", "Highway 21")
# Esegue la query con i valori specificati
mycursor.execute(sql, val)

# Conferma (committa) la modifica nel database
mydb.commit()

# Stampa il numero di record inseriti
print(mycursor.rowcount, "record inserted.")