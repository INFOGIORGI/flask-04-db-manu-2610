from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("home.html", titolo="Home")

@app.route("/products")
def products():
    cursor = mysql.connection.cursor()
    sql = "SELECT * from products"
    cursor.execute(sql)
    prodotti = cursor.fetchall()

    return render_template("products.html", titolo="Prodotti", prodotti = prodotti)

@app.route("/category/<categoryID>")
def category(categoryID):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM categories WHERE categoryID = %s"
    cursor.execute(query,(categoryID,))
    dati = cursor.fetchall()

    return render_template("category.html",dati=dati)

app.run(debug=True)
