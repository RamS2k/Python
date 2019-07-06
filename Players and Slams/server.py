from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL('friendsdb')
@app.route('/')
def index():
    result = mysql.query_db("select * from players;")
    return render_template("index.html", entry = result)

if __name__=="__main__":
    app.run(debug=True)