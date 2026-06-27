import os
import requests
from dotenv import load_dotenv
import airportsdata

load_dotenv()

DUFFEL_API_KEY = os.getenv("DUFFEL_API_KEY")

PREFERRED_AIRPORTS = {
    "sydney": "SYD",
    "london": "LHR",
    "dubai": "DXB",
    "paris": "CDG",
    "new york": "JFK",
    "toronto": "YYZ",
    "istanbul": "IST",
    "lahore": "LHE",
    "karachi": "KHI",
    "islamabad": "ISB",
}

airports = airportsdata.load("IATA")

def get_iata(place):
    place = place.strip()

    if len(place) == 3 and place.upper() in airports:
        return place.upper()

    place_lower = place.lower()
    if place_lower in PREFERRED_AIRPORTS:
        return PREFERRED_AIRPORTS[place_lower]

    for code, airport in airports.items():
        city = airport.get("city", "").lower()
        name = airport.get("name", "").lower()

        if place_lower == city or place_lower in name:
            return code

    return None


def search_flights(departure_city, destination, departure_date, travelers):
    origin = get_iata(departure_city)
    dest = get_iata(destination)

    if not origin or not dest:
        print("Could not find airport code")
        print("Departure:", departure_city)
        print("Destination:", destination)
        return []

    traveler_count = int(travelers.split()[0])

    print("ORIGIN:", origin)
    print("DEST:", dest)
    print("DATE:", departure_date)
    print("TRAVELERS:", traveler_count)

    passengers = [{"type": "adult"} for _ in range(traveler_count)]

    url = "https://api.duffel.com/air/offer_requests"

    headers = {
        "Authorization": f"Bearer {DUFFEL_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Duffel-Version": "v2",
    }

    payload = {
        "data": {
            "slices": [
                {
                    "origin": origin,
                    "destination": dest,
                    "departure_date": departure_date,
                }
            ],
            "passengers": passengers,
            "cabin_class": "economy",
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    if response.status_code not in [200, 201]:
        print(response.status_code)
        print(response.text)
        return []

    data = response.json()["data"]
    offers = data.get("offers", [])

    flights = []

    for offer in offers[:3]:
        flights.append({
            "airline": offer["owner"]["name"],
            "price": offer["total_amount"] + " " + offer["total_currency"],
            "origin": origin,
            "destination": dest,
        })

    return flights