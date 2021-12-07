import sys
import os
import requests
from twilio.rest import Client

sys.path.append(os.getcwd()) # for secret

import secret as s


def send_sms(text):
        client = Client(s.twilio_account_sid, s.twilio_auth_token)

        message = client.messages \
                        .create(
                            body=text,
                            from_='+13862844975',
                            to=s.my_num,
                        )
        print(message.status)


def get_news():
    url = 'https://newsapi.org/v2/everything'

    params = {
        'q': COMPANY_NAME,
        'from': k[0],
        'sortBy': 'popularity',
        'apiKey': s.news_api_key,
    }

    response = requests.get(url, params=params).json()
    news = response['articles'][:3]
    text = [f'Headline: {i["title"]}\nBrief: {i["description"]}' for i in news]
    return text


STOCK = 'NET'
COMPANY_NAME = 'Cloudflare'

url = 'https://www.alphavantage.co/query'

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': s.alpha_api_key,
}

response = requests.get(url, params=params).json()
last_refreshed = response['Meta Data']['3. Last Refreshed']
k = list(response['Time Series (Daily)'].keys())[:2]
data = [response['Time Series (Daily)'][k[i]]['4. close'] for i in range(2)]
price_diff = float(data[0]) / float(data[1])
if price_diff > 1.05:
    for text in get_news():
        send_sms(f'{STOCK}: 🔺{int((price_diff-1)*100)}%\n' + text)
elif price_diff < 0.95:
    for text in get_news():
        send_sms(f'{STOCK}: 🔻{int((1-price_diff)*100)}%\n' + text)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
