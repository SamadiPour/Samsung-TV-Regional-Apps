import csv
import os

directory = 'output/apps/'

country_app = {}
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        with open(os.path.join(directory, filename)) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            country_name = filename.split('.')[0]
            country_app[country_name] = {app[0]: app[1] for app in csv_reader}

# Create a set of all apps and countries
countries = sorted(set(country_app.keys()))
app_names = {}
for app_dict in country_app.values():
    for app_name, app_value in app_dict.items():
        app_names.setdefault(app_name, app_value)

# Create the matrix
matrix = []
for app_id in app_names.keys():
    app_name = app_names[app_id]
    app_countries = []
    for country in countries:
        if app_id in country_app[country]:
            app_countries.append('X')
        else:
            app_countries.append('-')
    matrix.append([app_name] + app_countries)
matrix.sort(key=lambda x: x[0])

# Write the matrix to a CSV file
with open('output/matrix.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['-App/Country-'] + countries)
    writer.writerows(matrix)
