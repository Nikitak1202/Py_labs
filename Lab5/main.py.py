import requests
import json


city_name = input("Введите название города: ")
params = {
    'q':city_name,
    'appid':'11c0d3dc6093f7442898ee49d2430d20',
    'units':'metric',
    'lang':'ru'
}
res = requests.get("https://api.openweathermap.org/data/2.5/weather", params)
data = res.json()
template = 'Погода в {}: {}, влажность {}%, давление: {} милибар\n'
print(template.format(city_name, data['weather'][0]['description'], data['main']['humidity'], data['main']['pressure']))


url = 'https://api.hh.ru/salary_statistics/dictionaries/salary_industries'
res = requests.get(url)
data = res.json()

for lst in data:
    print(lst)
    print('\n')

with open('areas of activity.json', 'w', encoding='UTF-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)