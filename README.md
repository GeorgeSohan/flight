#Flight Deals Notifier

Flight Deals Notifier is a Python program designed to find and notify users of flight deals based on destinations stored in a Google Sheets spreadsheet.
It utilizes the Sheety API for accessing Google Sheets data, the Tequila API for flight search, and the Twilio API for sending SMS notifications.

#Features:
Retrieves destination data from a Google Sheets spreadsheet using Sheety API.
Searches for flight deals using Tequila API based on the retrieved destination data.
Notifies users of flight deals via SMS using Twilio API.

#Setup:
- Clone the repository to your local machine.
- Obtain API keys for Sheety, Tequila, and Twilio, and replace the placeholders in the code with your credentials.
- Set up a Google Sheets spreadsheet with destination data and provide the spreadsheet ID in the code.
- Update the necessary configurations in the code, such as origin city, date range, etc.
- Run the main.py script to start the program.

#Usage:
Once set up, the program will automatically retrieve destination data, search for flight deals, and notify users via SMS.
