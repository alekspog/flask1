from flask import Flask, render_template
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", tours=tours_list, departures=departures)


@app.route('/departure/<departure>/')
def render_departure(departure):
    departure_tours = get_departure_tours(departure)
    prices = get_tours_prices(departure_tours)
    nights = get_tours_nights(departure_tours)

    departures_info = {
         "departure_text": departures[departure],
         "min_price": min(prices),
         "max_price": max(prices),
         "min_nights": min(nights),
         "max_nights": max(nights)
    }
    return render_template("departure.html", tours=departure_tours, departures=departures,
                           departures_info=departures_info)


@app.route('/tour/<int:id>/')
def render_tour(id):
    for tour in tours_list:
        if tour['id'] == id:
            selected_tour = tour
            return render_template("tour.html", tour=selected_tour, departures=departures, departure=departures[tour["departure"]])

    return render_template("404.html", departures=departures)


def get_departure_tours(departure):
    filtered_tours = []
    for index, tour in tours.items():
        if tour["departure"] == str(departure):
            tour["id"] = index
            filtered_tours.append(tour)

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


def convert_tours_data(tours):
    converted_tours = []
    for index, tour in tours.items():
        tour["id"] = index
        converted_tours.append(tour)

    return converted_tours


tours_list = convert_tours_data(tours)
print(tours_list)


app.run('0.0.0.0', 8000, debug=True)
