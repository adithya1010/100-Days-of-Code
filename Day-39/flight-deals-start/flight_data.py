from datetime import datetime
import requests
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_API_KEY = "7yZiSXmzM-f2GqJuGUEvyzhwg04a4_8D"


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.destination_city = destination_city
        self.price = price
        self.departure_code = origin_city
        self.origin_airport = origin_airport,
        self.departure_city = destination_city
        self.destination_airport = destination_airport,
        self.out_date = out_date
        self.return_date = return_date