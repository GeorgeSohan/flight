import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "" # The base URL for the Tequila API.
TEQUILA_API_KEY = "" # The API key for accessing the Tequila API.

class FlightSearch:

    def get_destination_code(self, city_name):
        # Get the IATA code for a given city name.

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Check for available flights between two cities within a specified date range.

        Returns:
            FlightData: Flight data object containing information about the cheapest flight found.
        """
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        data = response.json().get("data", [])

        if not data:
            print(f"No flights found for {destination_city_code}.")
            return None

        try:
            flight_data = FlightData(
                price=data[0]["price"],
                origin_city=data[0]["route"][0]["cityFrom"],
                origin_airport=data[0]["route"][0]["flyFrom"],
                destination_city=data[0]["route"][0]["cityTo"],
                destination_airport=data[0]["route"][0]["flyTo"],
                out_date=data[0]["route"][0]["local_departure"].split("T")[0],
                return_date=data[0]["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        except (IndexError, KeyError):
            print("Error processing flight data.")
            return None
