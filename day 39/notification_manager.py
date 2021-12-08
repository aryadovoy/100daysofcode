from twilio.rest import Client
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s

class NotificationManager:
    
    def send_sms(text):
    
        client = Client(s.twilio_account_sid, s.twilio_auth_token)

        message = client.messages \
                        .create(
                            body=text,
                            from_='+13862844975',
                            to=s.my_num,
                        )
        print(message.status)
