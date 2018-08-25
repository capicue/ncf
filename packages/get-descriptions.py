
import csv
import requests

file = open('results-20180210-102142.csv', 'r')
reader = csv.DictReader(file)
packages = list(reader)

def description(packageName):
    r = requests.get(f'https://pypi.python.org/pypi/{packageName}/json')
    if r.status_code == 200:
        return r.json()['info']['summary']
    else:
        return ''

def add_description(package):
    package['description'] = description(package['name'])
    return package

for package in packages:
    if not ('description' in package):
        print(package['name'])
        add_description(package)

with open('packages.csv', 'w') as csvfile:
    fieldnames = ['name', 'downloads', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for package in packages:
        writer.writerow(package)




