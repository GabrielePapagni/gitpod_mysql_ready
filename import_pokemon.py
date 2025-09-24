import mysql.connector
import pandas as pd

# Connessione al database MySQL (modifica i dati di accesso se serve)
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123"
)

mycursor = mydb.cursor()

# Creo il database se non esiste
mycursor.execute("CREATE DATABASE IF NOT EXISTS PokemonDB")
mycursor.execute("USE PokemonDB")

# Creo la tabella Pokemon (se non esiste già)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Pokemon (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    type1 VARCHAR(50),
    type2 VARCHAR(50) DEFAULT NULL,
    total INT,
    hp INT,
    attack INT,
    defense INT,
    sp_atk INT,
    sp_def INT,
    speed INT,
    generation INT,
    legendary BOOLEAN
)
""")

# Leggo il CSV con pandas
df = pd.read_csv('Pokemon.csv')  # modifica il path se serve

# Sostituisco eventuali NaN in type2 con None (per i NULL in SQL)
df['Type 2'] = df['Type 2'].where(pd.notnull(df['Type 2']), None)

# Sostituisco il campo Legendary da stringa a booleano
df['Legendary'] = df['Legendary'].astype(bool)

# Elimino tutti i dati presenti nella tabella per evitare duplicati
mycursor.execute("DELETE FROM Pokemon")
mydb.commit()

# Inserisco i dati nel database
sql = """
INSERT INTO Pokemon (id, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    data = (
        int(row['#']),
        row['Name'],
        row['Type 1'],
        row['Type 2'],
        int(row['Total']),
        int(row['HP']),
        int(row['Attack']),
        int(row['Defense']),
        int(row['Sp. Atk']),
        int(row['Sp. Def']),
        int(row['Speed']),
        int(row['Generation']),
        row['Legendary']
    )
    mycursor.execute(sql, data)

mydb.commit()

print("Dati inseriti correttamente!")

# Controllo dei dati inseriti
mycursor.execute("SELECT COUNT(*) FROM Pokemon")
count = mycursor.fetchone()[0]
print(f"Totale record inseriti: {count}")

# Chiudo la connessione
mycursor.close()
mydb.close()