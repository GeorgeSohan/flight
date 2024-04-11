from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Initialize instances of DataManager, FlightSearch, and NotificationManager
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Retrieve destination data from the data manager
sheet_data = data_manager.get_destination_data()

# Set the origin city IATA code
ORIGIN_CITY_IATA = "OTP"

# Check if the destination data has IATA codes filled in
if sheet_data[0]["iataCode"] == "":
    # If not, retrieve IATA codes for each destination and update the data manager
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Define the time range for flight search (from tomorrow to six months from today)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Iterate through each destination in the sheet data
for destination in sheet_data:
    # Check for available flights from the origin city to the destination
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # If no flight is found, continue to the next destination
    if flight is None:
        continue

    # If the price of the flight is lower than the lowest price recorded, send a notification
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Hopa! Am gasit un zbor. Costa {flight.price} EURO de la {flight.origin_city}-{flight.origin_airport}"
                    f" la {flight.destination_city}-{flight.destination_airport}, de la {flight.out_date} la {flight.return_date}."
        )
