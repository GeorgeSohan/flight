from twilio.rest import Client

# Twilio account credentials
TWILIO_SID = ""  # Twilio account SID
TWILIO_AUTH_TOKEN = ""  # Twilio auth token
TWILIO_VIRTUAL_NUMBER = ""  # Twilio virtual number
TWILIO_VERIFIED_NUMBER = ""  # Your verified phone number

class NotificationManager:

    def __init__(self):
        """
        Initialize the NotificationManager with Twilio client using provided credentials.
        """
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):

        # Send SMS message using Twilio client
        sent_message = self.client.messages.create(
            body=message,  # Message body
            from_=TWILIO_VIRTUAL_NUMBER,  # Twilio virtual number
            to=TWILIO_VERIFIED_NUMBER,  # Recipient's verified phone number
        )
        # Print the SID of the sent message
        # print(sent_message.sid)
