import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

# Get a simple public IP
def  find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json')
    return ip_address['ip']

# Search on wikipedia function
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 2)
    return results

# Play video on youtube
def play_on_youtube(video):
    kit.playonyt(video)

# Search on google
def search_on_google(query):
    kit.search(query)

# Send a Whatsapp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+353{number}", message)

# Get latest news
NEWS_API_KEY = config('NEWS_KEY_API')

def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=ie&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res['articles']
    for article in articles:
        news_headlines.append(article['title'])
    return news_headlines[:5]

# Weather forecast
OPENWATHER_APP_ID = config('OPENWATHER_APP_ID')

def get_weather_report(city):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWATHER_APP_ID}&units=metric').json()
    weather = res['weather'][0]['main']
    temperature = res['main']['temp']
    feels_like = res['main']['feels_like']
    return weather, f'{temperature}°C', f'{feels_like}°C'

