import sqlite3
from flask import Flask, render_template, request, redirect
from dati import pievienot_lietotaju
from dati import lietotaju_tabulas_izveide
from dati import zinojumu_tabulas_izveide
from dati import iegut_lietotajvardus
from dati import pievienot_zinojumu
from dati import iegut_zinojumus

lietotaju_tabulas_izveide()# deklarēta tabula, ja tā neeksistē
zinojumu_tabulas_izveide()

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        vards = request.form['name'].capitalize()
        uzvards = request.form['surname'].capitalize()
        lietotajvards = request.form['username']
        if vards and uzvards and lietotajvards:
            pievienot_lietotaju(vards, uzvards, lietotajvards)

    return render_template("index.html")

@app.route("/statements")
def statements():
    lietotajvardi = iegut_lietotajvardus()
    zinojumi = iegut_zinojumus()
    return render_template("statements.html", lietotajvardi = lietotajvardi, zinojumi = zinojumi)

@app.route("/statements/izveleties", methods=["POST"])
def izveleties():
    lietotajvards = request.form['lietotajvards']
    zinojums = request.form['zinojums']
    pievienot_zinojumu(lietotajvards, zinojums)
    return redirect("/statements")

if __name__ == "__main__":
    app.run(port = 5000)
