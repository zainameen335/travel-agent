import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}


def get_destination_id(city):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

    params = {
        "name": city,
        "locale": "en-gb"
    }

    response = requests.get(url, headers=HEADERS, params=params)

    data = response.json()

    if not data:
        return None, None

    first_result = data[0]

    dest_id = first_result.get("dest_id")
    dest_type = first_result.get("dest_type")

    return dest_id, dest_type


def search_hotels(city, checkin_date, checkout_date, travelers):
    dest_id, dest_type = get_destination_id(city)

    if not dest_id:
        return []

    adults = int(travelers.split()[0])

    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    params = {
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "dest_id": dest_id,
        "dest_type": dest_type,
        "adults_number": adults,
        "room_number": 1,
        "order_by": "popularity",
        "filter_by_currency": "USD",
        "locale": "en-gb",
        "units": "metric",
        "page_number": 0,
        "include_adjacency": "true"
    }

    response = requests.get(url, headers=HEADERS, params=params)

    data = response.json()

    hotels = []

    results = data.get("result", [])

    for hotel in results[:3]:
        price = hotel.get("min_total_price", "Price unavailable")
        currency = hotel.get("currencycode", "")

        hotels.append({
            "name": hotel.get("hotel_name", "Unknown Hotel"),
            "location": city,
            "price": f"{price} {currency}"
        })

    return hotels