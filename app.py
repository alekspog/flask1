from flask import Flask, render_template
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", tours=tours)


@app.route('/departure/<departure>/')
def render_departure(departure):
    return render_template("departure.html")


@app.route('/tour/<int:id>/')
def render_tour(id):
    return render_template("tour.html", tour=tours[id], departure=departures[tours[id]["departure"]])


app.run('0.0.0.0', 8000, debug=True)
