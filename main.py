from datetime import *
import requests
from twilio.rest import Client
COMPANY_NAME = "AAPL"
today_day = datetime.now().weekday()
if today_day != 5 and today_day != 6 and today_day != 0 and today_day != 1:
    yesterday_date = datetime.now().date() - timedelta(days=1)
    day_before_yesterday_date = datetime.now().date() - timedelta(days=2)
elif today_day == 5:
    yesterday_date = datetime.now().date() - timedelta(days=2)
    day_before_yesterday_date = datetime.now().date() - timedelta(days=3)
elif today_day == 0:
    yesterday_date = datetime.now().date() - timedelta(days=3)
    day_before_yesterday_date = datetime.now().date() - timedelta(days=4)
elif today_day == 1:
    yesterday_date = datetime.now().date() - timedelta(days=1)
    day_before_yesterday_date = datetime.now().date() - timedelta(days=4)
else:
    yesterday_date = datetime.now().date() - timedelta(days=3)
    day_before_yesterday_date = datetime.now().date() - timedelta(days=4)

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": COMPANY_NAME,
    "apikey": "6AJTURJDZA3JAFMX"
}
stock_data = requests.get(url="https://www.alphavantage.co/query?", params=parameters).json()
yesterday_stock_data = stock_data['Time Series (Daily)'][str(yesterday_date)]['4. close']
day_before_yesterday_stock_data = stock_data['Time Series (Daily)'][str(day_before_yesterday_date)]['4. close']
price_difference = float(yesterday_stock_data)-float(day_before_yesterday_stock_data)
stock_percentage = int(price_difference // 100)

parameters1 = {
    "qInTitle": "apple",
    "from": day_before_yesterday_date,
    "to": yesterday_date,
    "sortby": "popularity",
    "apikey": "c9a58039e45c43b799d4d64fd4d974b1",
}
news_data = requests.get(url="https://newsapi.org/v2/everything?",params=parameters1).json()
news_title = news_data["articles"][0]["title"]
news_brief = news_data["articles"][0]["content"]
# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
account_sid = "AC2ab0b55d07f4959a9eefb943bbefc55d"
auth_token = "748ce277b3911dfa6180947788ee5438"
if stock_percentage >= 5:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
              body=f"APPLE: 🔺{stock_percentage}%\nHeadLine: {news_title}\nBrief: {news_brief}",
              from_='+13184884454',
              to='+919047989145'
              )
if stock_percentage < 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
              body=f"APPLE: 🔻{stock_percentage}%\nHeadLine: {news_title}\nBrief: {news_brief}",
              from_='+13184884454',
              to='+919047989145'
                )
