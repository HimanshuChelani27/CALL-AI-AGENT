import os
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

# Get the list of your phone numbers
phone_numbers = client.incoming_phone_numbers.list()

# Find the phone number you want to use (replace with your Twilio number)
twilio_number = "+16629204237"  # The "from" number in your original code

for number in phone_numbers:
    if number.phone_number == twilio_number:
        # Update the webhook URL for incoming calls
        number.update(
            voice_url="https://569e-114-143-207-106.ngrok-free.app/incoming-call",
            voice_method="POST"
        )
        print(f"Updated {twilio_number} to use your webhook URL")
        break
