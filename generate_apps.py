import requests
import csv

with open('output/countries.txt', 'r') as file:
    countries = [line.split(',')[0] for line in file.read().splitlines()]

for country in countries:
    apps = []
    offset = 0
    while True:
        r = requests.get(
            url='https://vdapi.samsung.com/tvs/tvpersonalize/api/tvapps/appserver/list',
            params={
                'country_code': country,
                'language_code': 'en-US',
                'offset': offset,
                'size': '100',
                'order': 'asc',
            }
        )
        data = r.json()
        request_apps = data.get('data', {}).get('tvApp', [])
        if any(request_apps):
            apps += [
                [app['appId'], app['appName'], app['appVersionNumber'], app['appVendorName'], app['appCategoryName']]
                for app in request_apps
            ]
            if len(request_apps) < 100:
                break
            else:
                offset += 1
        else:
            break

    # write it to a file
    with open(f'output/apps/{country}.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['ID', 'Name', 'Version', 'Vendor', 'Category'])
        csv_writer.writerows(apps)
