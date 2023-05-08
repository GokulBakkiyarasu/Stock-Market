# Stock Market and News Alert System

This is a Python program that sends SMS alerts containing the daily percentage change in stock prices of a particular company and the top news headline and article on that company from the previous day using the Alphavantage and News API and the Twilio messaging service.

![1683529241354](https://user-images.githubusercontent.com/87391223/236756849-89e8daf7-f847-4242-84a4-b2b18401b7d1.jpg)


## Libraries Used
- datetime: Used to get the current date and time and manipulate the date values to get the previous day's date.
- requests: Used to send HTTP requests to the APIs to get the stock and news data.
- twilio.rest: Used to send SMS messages to a phone number.
- json: Used to parse the API response data.

## Getting Started
To use this program, you need to have an API key from Alphavantage and News API, as well as a Twilio account to send the SMS alerts. Once you have the API keys, you can replace the placeholders in the code with your keys.

### Prerequisites
- Python 3.x
- requests
- twilio
- Alphavantage API key
- News API key
- Twilio account SID and authentication token

### Installation
1. Install the required libraries:
   ```
   pip install requests twilio
   ```
2. Get an API key from Alphavantage by creating an account on their website: https://www.alphavantage.co/support/#api-key
3. Get an API key from News API by creating an account on their website: https://newsapi.org/register
4. Create a Twilio account if you don't have one already: https://www.twilio.com/try-twilio
5. Replace the placeholders in the code with your API keys and Twilio account SID and authentication token.

## Usage
To use the program, simply run the Python script. The program will send an SMS alert containing the daily percentage change in stock prices of a particular company and the top news headline and article on that company from the previous day to the phone number specified in the `to` field of the `message` object. You can customize the company name and the phone number by changing the `COMPANY_NAME` and `to` variables, respectively.

## File structure
```
├── main.py       # Main program file
```
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
