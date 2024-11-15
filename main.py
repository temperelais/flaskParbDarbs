from flask import Flask, render_template
from dati import iegut_lietotajus

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    lietotaji = iegut_lietotajus()




if __name__ == "__main__":
    app.run(port = 5000)
