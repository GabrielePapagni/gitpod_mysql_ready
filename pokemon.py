import mysql.connector
from flask import Flask, jsonify

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="PokemonDB"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/gen3")
def getAllData():
    mycursor.execute("SELECT * FROM Pokemon")
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)

@app.route("/legendary")
def getLegendary():
    sql = "SELECT * FROM Pokemon WHERE legendary = TRUE"
    mycursor.execute(sql)
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)

@app.route("/type/dark")
def getDarkType():
    sql = "SELECT * FROM Pokemon WHERE type1 = %s OR type2 = %s"
    mycursor.execute(sql, ("Dark", "Dark"))
    columns = [desc[0] for desc in mycursor.description]
    myresult = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)

@app.route("/pokemon/even")
def getEvenID():
    sql = "SELECT * FROM Pokemon WHERE id % 2 = 0"
    mycursor.execute(sql)
    columns = [desc[0] for desc in mycursor.description]
    rows = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route("/tot/greater_than/400")
def getByTotGreaterThan400():
    sql = "SELECT * FROM Pokemon WHERE total > 400"
    mycursor.execute(sql)
    columns = [desc[0] for desc in mycursor.description]
    rows = mycursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)