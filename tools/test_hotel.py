from hotel_tool import search_hotels

hotels = search_hotels(
    city="Dubai",
    checkin_date="2026-06-01",
    checkout_date="2026-06-10",
    travelers="1 person"
)

print(hotels)