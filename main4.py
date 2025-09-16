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

# Esegue una query SQL per selezionare tutti i record dalla tabella "customers"
mycursor.execute("SELECT * FROM customers")

# Recupera tutti i risultati della query
myresult = mycursor.fetchall()

# Cicla su ogni record e lo stampa
for x in myresult:
  print(x)