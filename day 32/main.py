##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import csv
import random
import sys
import os

sys.path.append(os.getcwd()) # for secret

import secret as s


def send_email():
    connection = smtplib.SMTP_SSL('smtp.yandex.ru', port=465)
    connection.login(user=s.my_email, password=s.my_email_pass)
    with open('day 32/letter_templates/letter_{}.txt'.format(random.randrange(1, 4))) as letter:
        connection.sendmail(from_addr=s.my_email,
                            to_addrs=row[1],
                            msg='Subject:Birthday!\n\n' + \
                                str(''.join(letter.readlines())).replace('[NAME]', row[0]))
    connection.close


now_month = str(dt.datetime.now().month)
now_day = str(dt.datetime.now().day)

with open('day 32/birthdays.csv', 'r') as csvfile:
    bdays = csv.reader(csvfile, delimiter=',')
    for row in bdays:
        if row[3] == now_month and row[4] == now_day:
            send_email()
