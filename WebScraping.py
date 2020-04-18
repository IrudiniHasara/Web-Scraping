import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xpriy6hfjDc')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id ='seven-day-forecast-body')

items = week.find_all(class_= 'tombstone-container')

print(items[0].find(class_ = 'period-name').get_text())
print(items[0].find(class_ = 'short-desc').get_text())
print(items[0].find(class_ = 'temp').get_text())

period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_description = [item.find(class_ = 'short-desc').get_text() for item in items]
tempuratures = [item.find(class_ = 'temp').get_text() for item in items]

#print(period_names)
#print(short_description)
#print(tempuratures)

weather_stuff = pd.DataFrame(
    {
        'period' : period_names,
        'short_description' : short_description,
        'temperatures' : tempuratures
    }
)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
