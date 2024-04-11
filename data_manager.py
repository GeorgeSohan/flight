import requests

SHEETY_PRICES_ENDPOINT = ""  # Replace with the actual SHEETY prices endpoint URL


class DataManager:
    """
    Class to manage data related operations.
    """

    def __init__(self):
        """
        Initialize DataManager object.
        """
        self.destination_data = {}

    def get_destination_data(self):
        """
        Retrieve destination data from the SHEETY prices endpoint.

        Returns:
            dict: Destination data retrieved from the SHEETY prices endpoint.
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
        Update destination codes in the SHEETY prices endpoint.

        This method iterates over the destination data and updates the IATA codes for each city.

        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
