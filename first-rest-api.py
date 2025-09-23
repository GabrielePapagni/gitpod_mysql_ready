import mysql.connector
from flask import Flask, jsonify

# Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

# Route per la home page
@app.route("/")
def hello():
    return "Hello, World!"

# Route per ottenere tutte le unità in HTML
@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)

# Route per visualizzare solo le unità con tipo di trasporto 'Air'
@app.route("/air_transport")
def airTransport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE transport = 'Air'")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)

# Route per visualizzare solo le unità con rarità 'epic'
@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'Epic'")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)

# Route per visualizzare le unità con rarità 'Legendary'
@app.route("/legendary_units")
def legendaryUnits():
    try:
        # Query per ottenere tutte le unità con rarità 'Legendary'
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'Legendary'")
        columns = [desc[0] for desc in mycursor.description]
        myresult = mycursor.fetchall()
        
        # Creazione del risultato da restituire come JSON
        result = []
        for row in myresult:
            result.append(dict(zip(columns, row)))
        return jsonify(result)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 500

# Una route per visualizzare le unità con costo maggiore di 5
@app.route("/high_cost_units")
def highCostUnits():
    try:
        # Query per ottenere tutte le unità con un 'Cost' maggiore di 5
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost > 5")
        columns = [desc[0] for desc in mycursor.description]
        myresult = mycursor.fetchall()
        
        # Creazione del risultato da restituire come JSON
        result = []
        for row in myresult:
            result.append(dict(zip(columns, row)))
        return jsonify(result)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    app.run(debug=True)