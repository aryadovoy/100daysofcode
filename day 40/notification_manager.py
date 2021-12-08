import smtplib
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

    def send_email(fname, email, f, t, rf, rt, date_to, return_date, text):
        
        link = f'https://www.google.co.uk/flights?hl=en#flt={f}.{t}.{date_to}*{rf}.{rt}.{return_date}'

        connection = smtplib.SMTP_SSL('smtp.yandex.ru', port=465)
        connection.login(user=s.my_email, password=s.my_email_pass)
        connection.sendmail(from_addr=s.my_email,
                            to_addrs=email,
                            msg=(
                                f'Subject:Alert, {fname}!\n\n' + \
                                f'{text}\n' + \
                                link
                            )
                            )
        connection.close
