import requests

r = requests.get(url='https://restcountries.com/v3.1/all')
data = r.json()
countries = sorted([(country['cca2'], country['name']['common']) for country in data], key=lambda x: x[0])

valid_countries = []
for country in countries:
    r = requests.get(
        url='https://vdapi.samsung.com/tvs/tvpersonalize/api/tvapps/appserver/list',
        params={
            'country_code': country[0],
            'language_code': 'en-US',
            'offset': '0',
            'size': '1',
        }
    )
    data = r.json()
    if data.get('data', {}).get('allCount', 0) > 0:
        valid_countries.append(country)

with open('output/countries.txt', 'w') as file:
    file.write('\n'.join([f'{country[0]}, {country[1]}' for country in valid_countries]))
