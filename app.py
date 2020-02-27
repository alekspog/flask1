from flask import Flask, render_template
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", tours=tours)


@app.route('/departure/<departure>/')
def render_departure(departure):
    departure_tours = get_departure_tours(departure)
    prices = get_tours_prices(departure_tours)
    nights = get_tours_nights(departure_tours)

    departure_info = {}
    departure_info["departure_text"] = departures[departure]
    departure_info["min_price"] = min(prices)
    departure_info["max_price"] = max(prices)
    departure_info["min_nights"] = min(nights)
    departure_info["max_nights"] = max(nights)
    return render_template("departure.html", departures=departure_info, tours=departure_tours)


@app.route('/tour/<int:id>/')
def render_tour(id):
    return render_template("tour.html", tour=tours[id], departure=departures[tours[id]["departure"]])


def get_departure_tours(departure):
    filtered_tours = []
    for index, tour in tours.items():
        if tour["departure"] == str(departure):
            tour["id"] = index
            filtered_tours.append(tour)

    # print("find tours: ", filtered_tours)
    return filtered_tours


def get_tours_nights(tours):
    nights = []
    for tour in tours:
        nights.append(tour["nights"])
    return nights


def get_tours_prices(tours):
    prices = []
    for tour in tours:
        prices.append(tour["price"])
    return prices


app.run('0.0.0.0', 8000, debug=True)
